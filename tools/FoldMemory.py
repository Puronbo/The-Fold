"""FoldMemory: append-only, auditable memory for Fold experiments.

Memory entries are immutable events. Corrections append a superseding event;
they never rewrite prior evidence. A SHA-256 chain detects accidental edits,
reordering, truncation (when the expected head is retained), and corruption.

This is a local prototype, not secure storage against an attacker who can
rewrite both the ledger and its trusted head. It is not an AGI memory system.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable


GENESIS = "0" * 64


def _canonical(value: dict[str, Any]) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


@dataclass(frozen=True)
class MemoryEvent:
    sequence: int
    event_type: str
    subject: str
    content: str
    source: str
    task: str
    confidence: float
    tags: tuple[str, ...]
    supersedes: int | None
    previous_digest: str
    digest: str

    def payload(self) -> dict[str, Any]:
        data = asdict(self)
        data.pop("digest")
        return data


class FoldMemory:
    """Append-only JSONL event ledger with explicit provenance and corrections."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.touch()

    def _read(self) -> list[MemoryEvent]:
        events: list[MemoryEvent] = []
        for line_number, line in enumerate(
            self.path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if not line.strip():
                continue
            try:
                raw = json.loads(line)
                raw["tags"] = tuple(raw["tags"])
                event = MemoryEvent(**raw)
            except (json.JSONDecodeError, TypeError, KeyError) as exc:
                raise ValueError(f"invalid memory event at line {line_number}") from exc
            events.append(event)
        return events

    def verify(self, expected_head: str | None = None) -> bool:
        previous = GENESIS
        events = self._read()
        for expected_sequence, event in enumerate(events, start=1):
            if event.sequence != expected_sequence:
                return False
            if event.previous_digest != previous:
                return False
            calculated = hashlib.sha256(_canonical(event.payload())).hexdigest()
            if calculated != event.digest:
                return False
            previous = event.digest
        if expected_head is not None and previous != expected_head:
            return False
        return True

    @property
    def head(self) -> str:
        events = self._read()
        return events[-1].digest if events else GENESIS

    def append(
        self,
        event_type: str,
        subject: str,
        content: str,
        *,
        source: str,
        task: str,
        confidence: float = 1.0,
        tags: Iterable[str] = (),
        supersedes: int | None = None,
    ) -> MemoryEvent:
        if not all((event_type, subject, content, source, task)):
            raise ValueError("event type, subject, content, source, and task are required")
        if not 0.0 <= confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        events = self._read()
        if not self.verify():
            raise ValueError("refusing to append to an invalid memory chain")
        if supersedes is not None:
            if supersedes < 1 or supersedes > len(events):
                raise ValueError("supersedes must identify an existing event")
            target = events[supersedes - 1]
            if target.subject != subject:
                raise ValueError("a correction must retain the original subject")
        payload = {
            "sequence": len(events) + 1,
            "event_type": event_type,
            "subject": subject,
            "content": content,
            "source": source,
            "task": task,
            "confidence": float(confidence),
            "tags": tuple(sorted(set(tags))),
            "supersedes": supersedes,
            "previous_digest": events[-1].digest if events else GENESIS,
        }
        digest = hashlib.sha256(_canonical(payload)).hexdigest()
        event = MemoryEvent(**payload, digest=digest)
        with self.path.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(asdict(event), sort_keys=True, ensure_ascii=False))
            stream.write("\n")
        return event

    def remember(self, subject: str, content: str, **metadata: Any) -> MemoryEvent:
        return self.append("observation", subject, content, **metadata)

    def correct(
        self, sequence: int, content: str, *, source: str, reason: str,
        confidence: float = 1.0,
    ) -> MemoryEvent:
        events = self._read()
        if sequence < 1 or sequence > len(events):
            raise ValueError("unknown event sequence")
        original = events[sequence - 1]
        return self.append(
            "correction", original.subject, content, source=source,
            task=original.task, confidence=confidence,
            tags=(*original.tags, "correction", reason), supersedes=sequence,
        )

    def recall(
        self, *, task: str | None = None, tag: str | None = None,
        subject: str | None = None, include_superseded: bool = False,
    ) -> tuple[MemoryEvent, ...]:
        events = self._read()
        superseded = {
            event.supersedes for event in events if event.supersedes is not None
        }
        result = []
        for event in events:
            if not include_superseded and event.sequence in superseded:
                continue
            if task is not None and event.task != task:
                continue
            if tag is not None and tag not in event.tags:
                continue
            if subject is not None and event.subject != subject:
                continue
            result.append(event)
        return tuple(result)


def _self_test() -> None:
    import tempfile

    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "fold-memory.jsonl"
        memory = FoldMemory(path)
        first = memory.remember(
            "concept:round-object", "Two observations share round shape.",
            source="dataset:demo-v1", task="object-classification",
            confidence=0.8, tags=("shape", "candidate"),
        )
        second = memory.remember(
            "counterexample:colour", "Same shape does not imply same colour.",
            source="test:colour-counterexample", task="object-classification",
            confidence=1.0, tags=("counterexample", "colour"),
        )
        checks = []
        checks.append(("empty ledger starts at genesis", first.previous_digest == GENESIS))
        checks.append(("events have increasing sequence numbers",
                       (first.sequence, second.sequence) == (1, 2)))
        checks.append(("hash chain verifies", memory.verify()))
        checks.append(("task recall returns matching events",
                       len(memory.recall(task="object-classification")) == 2))
        checks.append(("tag recall filters evidence",
                       len(memory.recall(tag="counterexample")) == 1))
        correction = memory.correct(
            1, "The observations share shape, but identity is unproven.",
            source="review:human", reason="scope-correction", confidence=0.95,
        )
        checks.append(("correction appends instead of overwriting",
                       correction.sequence == 3 and len(memory._read()) == 3))
        checks.append(("latest recall hides superseded claim",
                       len(memory.recall(subject="concept:round-object")) == 1
                       and memory.recall(subject="concept:round-object")[0].sequence == 3))
        checks.append(("audit mode retains superseded claim",
                       len(memory.recall(subject="concept:round-object",
                                         include_superseded=True)) == 2))
        checks.append(("correction preserves subject and task",
                       correction.subject == first.subject
                       and correction.task == first.task))
        checks.append(("chain remains valid after correction", memory.verify()))
        checks.append(("trusted head detects truncation",
                       not FoldMemory(path).verify(expected_head=second.digest)))

        # Tamper with one event and ensure the digest check rejects it.
        lines = path.read_text(encoding="utf-8").splitlines()
        altered = json.loads(lines[0])
        altered["content"] = "silently altered"
        lines[0] = json.dumps(altered)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        checks.append(("tampering is detected", not memory.verify()))

        for name, passed in checks:
            print(f"{'PASS' if passed else 'FAIL'}  {name}")
        print(f"{sum(p for _, p in checks)}/{len(checks)} checks passed")
        if not all(p for _, p in checks):
            raise SystemExit("FoldMemory regression failure")


if __name__ == "__main__":
    _self_test()
