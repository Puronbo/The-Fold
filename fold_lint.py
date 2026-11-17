#!/usr/bin/env python3
"""Two lints for the Fold corpus, together.

Run from the repository root:

    python fold_lint.py            # docs + approx over the repository
    python fold_lint.py docs       # zone labels in the Markdown notes
    python fold_lint.py approx     # tolerance-as-equality bugs in Python
    python fold_lint.py zones      # the corpus's zone distribution
    python fold_lint.py selftest   # the linter checked against fixtures

The two checks are the corpus's two transferable habits:

docs
    Every table with a `zone` column must use the four-zone vocabulary
    (`exact`, `reformulation`, `rhyme`, `false friend`), a `rhyme` row
    must not contain a proof claim, and a prose sentence that says
    "false friend" must name the claim.

approx
    Several Python bugs are the same non-transitivity failure the corpus
    records for tolerance: a class whose `__eq__` is approximate but whose
    `__hash__` is exact, and a `cmp_to_key` comparator that uses a
    tolerance.  Both are found by inspecting the AST, not by running code.

zones
    A map, not a gate.  It counts three different acts apart: a claim in
    a zone table, an inline label, and the legend that defines the
    vocabulary (a definition is not a claim).  It counts the prose
    attributions -- "the quotient statement is exact", "that remains a
    rhyme" -- because that is how most of the corpus labels, and it counts
    the status markers that mark a claim by contrast without naming a zone
    -- "a reading, not a derivation" -- because that is the same discipline
    one step short of a label.  A file with none of the three has nothing
    to put on the scale, and the map says so rather than inventing a label.

Exit status is 1 if any error is found (or any warning under --strict).
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXTURES = ROOT / "tools" / "fixtures"

ZONE_RE = re.compile(r"^(exact|reformulation|rhyme|false friend)\b", re.I)
# The corpus uses one fifth label once, for the hard problem: the map can
# name the edge but not cross it.  It is accepted, and it is not a rhyme.
ZONE_EXTENSIONS = {"the absence"}
ZONE_SCAN_RE = re.compile(
    r"(?:^|;\s*)(exact|reformulation|rhyme|false friend)\b", re.I
)
INLINE_ZONE_RE = re.compile(
    r"^\s*[-*]\s+\*\*(exact|reformulation|rhyme|false friend)\*\*", re.I
)
PROSE_ZONE_RE = re.compile(
    r"\b(?:is|are|was|were|remains?|stays?|becomes?|seems?)\s+(?:now\s+)?"
    r"(?:an?\s+)?(exact|reformulation|rhyme|false\s+friend)\b",
    re.I,
)
# The definite form names a false friend without an article: "… is the false
# friend".  It is allowed only for false friend, because "is the exact
# opposite" is a noun phrase and "is the absence of X" is ordinary English,
# not a label.
DEFINITE_ZONE_RE = re.compile(
    r"\b(?:is|are|was|were|remains?|stays?)\s+(?:now\s+)?the\s+"
    r"(false\s+friend)\b",
    re.I,
)
# The corpus marks a claim's status without naming a zone, most often by
# contrast: "a rhyme, not a proof", "a reading, not a derivation", "an input,
# not a result", "a statement about the lattice, not about the probe".  These
# are not labels -- they do not say which of the four the claim is in -- but
# they are the same discipline, and a note that uses them is not unlabelled.
STATUS_RE = re.compile(
    r",\s*not\s+(?:an?\s+|the\s+)?"
    r"(?:proof|derivation|reduction|theorem|route|identity|law|mechanism|"
    r"result|input|definition|reading|model|prediction|same\s+fold|"
    r"same\s+object|Fold's\s+object)\b"
    r"|,\s*not\s+about\b",
    re.I,
)
PROOF_RE = re.compile(
    r"\b(prove|proves|proved|proving|proof|therefore|hence|thus|q\.e\.d\.)\b", re.I
)
NEG_RE = re.compile(
    r"\b(not|no|cannot|never|neither|nor|without|nothing|error|mistake|fallacy|wrong|avoid)\b"
    r"|n't",
    re.I,
)
FALSE_FRIEND_RE = re.compile(r"false\s+friend", re.I)
QUOTE_RE = re.compile(r"[\"\u201c\u201d\u2018\u2019`]|[\u2014\u2013:]")


@dataclass(frozen=True)
class Finding:
    severity: str  # "error" | "warning"
    code: str
    path: str
    line: int
    message: str


def safe(text: str, limit: int = 60) -> str:
    """ASCII-only, bounded, so the Windows console can print it."""
    clipped = text.replace("\n", " ").strip()
    if len(clipped) > limit:
        clipped = clipped[: limit - 3] + "..."
    return clipped.encode("ascii", "replace").decode("ascii")


# --------------------------------------------------------------------- Markdown

def split_cells(line: str) -> list[str]:
    text = line.strip()
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|"):
        text = text[:-1]
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", text)]


def is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def blocks(text: str):
    """Yield ("table" | "prose", first_line, [(lineno, line), ...])."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            fence = stripped[:3]
            i += 1
            while i < len(lines) and not lines[i].lstrip().startswith(fence):
                i += 1
            i += 1
            continue
        if not stripped:
            i += 1
            continue
        if stripped.startswith("|"):
            start = i + 1
            rows: list[tuple[int, str]] = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append((i + 1, lines[i]))
                i += 1
            yield ("table", start, rows)
            continue
        start = i + 1
        prose: list[tuple[int, str]] = []
        while (
            i < len(lines)
            and lines[i].strip()
            and not lines[i].lstrip().startswith("|")
            and not lines[i].lstrip().startswith(("```", "~~~"))
        ):
            prose.append((i + 1, lines[i]))
            i += 1
        yield ("prose", start, prose)


def check_docs_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8")
    for kind, _start, block in blocks(text):
        if kind == "table":
            header = split_cells(block[0][1])
            lowered = [cell.lower() for cell in header]
            if "zone" not in lowered:
                continue
            zone_index = lowered.index("zone")
            for lineno, row_line in block[2:]:
                cells = split_cells(row_line)
                if len(cells) != len(header):
                    continue  # check.py already reports column mismatches
                cell = cells[zone_index]
                if cell.strip().lower() in ZONE_EXTENSIONS:
                    continue
                match = ZONE_RE.match(cell)
                if not match:
                    findings.append(
                        Finding(
                            "error",
                            "Z1",
                            path.name,
                            lineno,
                            f"zone label must start with exact/reformulation/rhyme/"
                            f"false friend: '{safe(cell, 40)}'",
                        )
                    )
                    continue
                base = match.group(1).lower()
                statement = " ".join(c for j, c in enumerate(cells) if j != zone_index)
                if base == "rhyme" and PROOF_RE.search(statement) and not NEG_RE.search(statement):
                    findings.append(
                        Finding(
                            "error",
                            "Z4",
                            path.name,
                            lineno,
                            "rhyme row contains a proof claim without a negation",
                        )
                    )
                if base == "false friend" and not statement.strip():
                    findings.append(
                        Finding(
                            "warning",
                            "Z2",
                            path.name,
                            lineno,
                            "false-friend row does not name the claim",
                        )
                    )
            continue

        if all(line.lstrip().startswith("#") for _, line in block):
            continue

        paragraph = " ".join(line for _, line in block)
        if FALSE_FRIEND_RE.search(paragraph) and not QUOTE_RE.search(paragraph):
            findings.append(
                Finding(
                    "warning",
                    "Z2",
                    path.name,
                    block[0][0],
                    "false friend is not named in quotes or after a colon",
                )
            )
        for sentence in re.split(r"(?<=[.!?])\s+", paragraph):
            if (
                re.search(r"\brhyme\b", sentence, re.I)
                and PROOF_RE.search(sentence)
                and not NEG_RE.search(sentence)
            ):
                findings.append(
                    Finding(
                        "error",
                        "Z3",
                        path.name,
                        block[0][0],
                        "sentence uses 'rhyme' and a proof word without a negation",
                    )
                )
    return findings


@dataclass(frozen=True)
class ZoneMap:
    """A file's labels: table claims, the legend, and prose attributions."""

    claims: Counter[str]
    legend: Counter[str]
    prose: Counter[str]
    marks: int = 0


def paragraph_sentences(text: str) -> list[tuple[int, str, str]]:
    """Yield (line, sentence, masked sentence) over prose, skipping code and headings.

    The corpus wraps prose inside sentences, so a paragraph is read whole and
    each sentence is mapped back to the line it starts on.  Scanning line by
    line would split a quotation or a clause in two and misread both.
    """
    out: list[tuple[int, str, str]] = []
    for kind, _start, block in blocks(text):
        if kind != "prose":
            continue
        kept = [(n, line) for n, line in block if not line.lstrip().startswith("#")]
        if not kept:
            continue
        paragraph = ""
        starts: list[tuple[int, int]] = []
        for lineno, line in kept:
            starts.append((len(paragraph), lineno))
            paragraph += line.strip() + " "
        masked = mask_spans(paragraph)
        bounds = list(re.finditer(r"(?<=[.!?])\s+", masked))
        spans = [0, *(m.end() for m in bounds)]
        ends = [*(m.start() for m in bounds), len(masked)]
        for base, stop in zip(spans, ends):
            sentence = masked[base:stop]
            if not sentence.strip():
                continue
            lineno = kept[0][0]
            for start, candidate in starts:
                if start <= base:
                    lineno = candidate
            out.append((lineno, paragraph[base:stop].strip(), sentence))
    return out


def mask_spans(sentence: str) -> str:
    """Blank out code spans and quotations, keeping offsets.

    The map counts attributions the corpus makes, not ones it quotes.  A code
    span holds a formula; a quotation holds a phrase being named -- including
    the illustrative ``is exact`` in the README's own documentation.
    """
    masked = re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), sentence)
    masked = re.sub(
        r"\"[^\"]*\"|\u201c[^\u201d]*\u201d", lambda m: " " * len(m.group(0)), masked
    )
    return masked


def prose_attributions(text: str) -> list[tuple[int, str, str]]:
    """Find sentences that assign a zone in prose: "X is exact", "Y is a rhyme".

    Only the predicative form counts, because it is the form the corpus uses
    to label a claim.  The maxims ("a rhyme written as a proof") are not
    attributions, and a negated attribution ("this is not exact") is a
    rejection, not a label.  The negation is read in the clause the verb sits
    in, so "does not make it an adjunction; that remains a rhyme" still
    counts the rhyme.
    """
    hits: list[tuple[int, str, str]] = []
    for lineno, shown, sentence in paragraph_sentences(text):
        for pattern in (PROSE_ZONE_RE, DEFINITE_ZONE_RE):
            for match in pattern.finditer(sentence):
                clause = re.split(r"[;,]", sentence[: match.start()])[-1]
                if re.search(r"\b(not|never|no longer|hardly|scarcely)\b|n't", clause, re.I):
                    continue
                label = match.group(1).lower()
                if "friend" in label:
                    label = "false friend"
                hits.append((lineno, label, shown))
    return hits


def status_markers(text: str) -> list[tuple[int, str]]:
    """Find claims marked by contrast rather than by a zone name.

    "a rhyme, not a proof" is a label; "a reading, not a derivation" and "a
    statement about the lattice, not about the probe" are not, because they
    do not say which of the four zones the claim sits in.  They are still the
    same discipline, and a note that uses them is not silent.
    """
    hits: list[tuple[int, str]] = []
    for lineno, shown, sentence in paragraph_sentences(text):
        if STATUS_RE.search(sentence):
            hits.append((lineno, shown))
    return hits


def legend_runs(items: list[tuple[int, str]]) -> set[int]:
    """Line numbers that belong to a legend.

    A legend is a run of consecutive inline zone lines whose labels are all
    distinct and number at least three: it defines the vocabulary instead of
    labelling a claim.  A single inline label on a claim is not a legend.
    """
    in_legend: set[int] = set()
    run: list[tuple[int, str]] = []

    def flush() -> None:
        if len(run) >= 3 and len({label for _, label in run}) == len(run):
            in_legend.update(lineno for lineno, _ in run)

    for item in items:
        if run and item[0] != run[-1][0] + 1:
            flush()
            run = []
        run.append(item)
    flush()
    return in_legend


def zone_counts(paths: list[Path]) -> dict[str, ZoneMap]:
    """Count zone labels in each file's zone tables and inline zone lists."""
    result: dict[str, ZoneMap] = {}
    for path in paths:
        claims: Counter[str] = Counter()
        legend: Counter[str] = Counter()
        text = path.read_text(encoding="utf-8")
        for kind, _start, block in blocks(text):
            if kind != "table":
                continue
            header = split_cells(block[0][1])
            lowered = [cell.lower() for cell in header]
            if "zone" not in lowered:
                continue
            zone_index = lowered.index("zone")
            for _lineno, row_line in block[2:]:
                cells = split_cells(row_line)
                if len(cells) != len(header):
                    continue
                cell = cells[zone_index]
                extension = cell.strip().lower()
                if extension in ZONE_EXTENSIONS:
                    claims[extension] += 1
                for label in ZONE_SCAN_RE.findall(cell):
                    claims[label.lower()] += 1

        inline: list[tuple[int, str]] = []
        in_fence = False
        for lineno, line in enumerate(text.splitlines(), start=1):
            stripped = line.lstrip()
            if stripped.startswith(("```", "~~~")):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            match = INLINE_ZONE_RE.match(line)
            if match:
                inline.append((lineno, match.group(1).lower()))
        legend_lines = legend_runs(inline)
        for lineno, label in inline:
            (legend if lineno in legend_lines else claims)[label] += 1

        result[path.name] = ZoneMap(
            claims=claims,
            legend=legend,
            prose=Counter(label for _, label, _ in prose_attributions(text)),
            marks=len(status_markers(text)),
        )
    return result


# ------------------------------------------------------------------------- Python

def call_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def is_abs_sub(node: ast.AST) -> bool:
    return (
        isinstance(node, ast.Call)
        and call_name(node.func) in {"abs", "fabs"}
        and len(node.args) == 1
        and isinstance(node.args[0], ast.BinOp)
        and isinstance(node.args[0].op, ast.Sub)
    )


UNKNOWN = object()


def isclose_zero_tolerance(node: ast.Call) -> bool:
    """True only when both tolerances are known literals and both are zero.

    An argument that is not a literal -- `abs_tol=5e-16 if f32 else 1e-7` --
    is unknown, not absent.  Treating it as absent would read the default
    (zero for abs_tol) and invent an exact comparison the source does not
    make, which is the same mistake the rule exists to catch.
    """
    if call_name(node.func) != "isclose":
        return False
    values: dict[str, object] = {}
    for keyword in node.keywords:
        if keyword.arg is None:
            continue
        try:
            values[keyword.arg] = ast.literal_eval(keyword.value)
        except (ValueError, SyntaxError):
            values[keyword.arg] = UNKNOWN
    rel = values.get("rel_tol", 1e-9)
    absolute = values.get("abs_tol", 0.0)
    return rel == 0 and absolute == 0


def uses_tolerance(node: ast.AST) -> bool:
    for inner in ast.walk(node):
        if isinstance(inner, ast.Call):
            name = call_name(inner.func)
            if name in {"isclose", "allclose"}:
                return True
        if isinstance(inner, ast.Compare):
            ordered = any(
                isinstance(op, (ast.Lt, ast.LtE, ast.Gt, ast.GtE)) for op in inner.ops
            )
            if not ordered:
                continue
            for operand in [inner.left, *inner.comparators]:
                if is_abs_sub(operand):
                    return True
                if isinstance(operand, ast.Name) and re.search(
                    r"(tol|eps|epsilon)$", operand.id.lower()
                ):
                    return True
    return False


def check_approx_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc:
        return [Finding("error", "P0", path.name, exc.lineno or 0, "could not parse")]

    definitions = {
        node.name: node
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            methods = {
                item.name: item
                for item in node.body
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
            }
            eq = methods.get("__eq__")
            hash_method = methods.get("__hash__")
            hash_assigned = False
            hash_none = False
            for item in node.body:
                if isinstance(item, ast.Assign):
                    for target in item.targets:
                        if isinstance(target, ast.Name) and target.id == "__hash__":
                            hash_assigned = True
                            if (
                                isinstance(item.value, ast.Constant)
                                and item.value.value is None
                            ):
                                hash_none = True
            if eq is not None and uses_tolerance(eq):
                decorated = any(
                    call_name(decorator) == "total_ordering"
                    for decorator in node.decorator_list
                )
                if decorated:
                    findings.append(
                        Finding(
                            "warning",
                            "A4",
                            path.name,
                            eq.lineno,
                            f"{node.name}: @total_ordering with an approximate __eq__; "
                            "the derived comparisons are not transitive",
                        )
                    )
                if hash_method is not None or (hash_assigned and not hash_none):
                    findings.append(
                        Finding(
                            "error",
                            "A1",
                            path.name,
                            eq.lineno,
                            f"{node.name}: approximate __eq__ with an explicit __hash__; "
                            "equal-by-tolerance objects can hash apart",
                        )
                    )
                elif not hash_none:
                    findings.append(
                        Finding(
                            "warning",
                            "A1b",
                            path.name,
                            eq.lineno,
                            f"{node.name}: approximate __eq__ is not transitive; "
                            "instances are unhashable but still not a quotient",
                        )
                    )

        if isinstance(node, ast.Call) and call_name(node.func) == "cmp_to_key" and node.args:
            argument = node.args[0]
            if isinstance(argument, ast.Lambda):
                target: ast.AST | None = argument
            else:
                name = getattr(argument, "id", None)
                target = definitions.get(name) if name else None
            if target is not None and uses_tolerance(target):
                findings.append(
                    Finding(
                        "error",
                        "A2",
                        path.name,
                        node.lineno,
                        "cmp_to_key comparator uses a tolerance; the order is not transitive",
                    )
                )

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isclose_zero_tolerance(node):
            findings.append(
                Finding(
                    "warning",
                    "A3",
                    path.name,
                    node.lineno,
                    "isclose with rel_tol=0 and abs_tol=0 is exact equality; use ==",
                )
            )

    return findings


# -------------------------------------------------------------------------- CLI

def collect(paths: list[str], suffix: str, recursive: bool = False) -> list[Path]:
    found: list[Path] = []
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            pattern = f"**/*{suffix}" if recursive else f"*{suffix}"
            found.extend(sorted(path.glob(pattern)))
        elif path.is_file():
            found.append(path)
        else:
            found.extend(sorted(ROOT.glob(f"*{suffix}")))
    return found


def default_docs() -> list[Path]:
    return sorted(ROOT.glob("*.md"))


def default_approx() -> list[Path]:
    return sorted(ROOT.glob("*.py"))


def run_docs(paths: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in paths:
        findings.extend(check_docs_file(path))
    return findings


def run_approx(paths: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in paths:
        findings.extend(check_approx_file(path))
    return findings


def report(name: str, files: int, findings: list[Finding]) -> None:
    errors = sum(1 for f in findings if f.severity == "error")
    warnings = len(findings) - errors
    status = "ok  " if errors == 0 else "FAIL"
    print(f"  {status} {name}: {files} files, {errors} errors, {warnings} warnings")
    for finding in findings:
        print(
            f"       {finding.path}:{finding.line}: {finding.severity} "
            f"[{finding.code}] {finding.message}"
        )


def selftest() -> int:
    expected = {
        "docs_bad.md": {"Z1", "Z2", "Z3", "Z4"},
        "docs_good.md": set(),
        "approx_bad.py": {"A1", "A1b", "A2", "A3", "A4"},
        "approx_good.py": set(),
    }
    failures: list[str] = []
    for name, codes in expected.items():
        path = FIXTURES / name
        if not path.exists():
            failures.append(f"missing fixture: {name}")
            continue
        if name.endswith(".md"):
            findings = check_docs_file(path)
        else:
            findings = check_approx_file(path)
        seen = {f.code for f in findings if f.severity == "error"}
        warnings = {f.code for f in findings if f.severity == "warning"}
        all_codes = seen | warnings
        if name.endswith("_good.md") or name.endswith("_good.py"):
            if findings:
                failures.append(f"{name}: expected no findings, got {sorted(all_codes)}")
        else:
            missing = codes - all_codes
            if missing:
                failures.append(f"{name}: missing {sorted(missing)}")
    if failures:
        print("  FAIL selftest")
        for message in failures:
            print(f"       {message}")
        return 1
    zmap = zone_counts([FIXTURES / "docs_good.md"]).get(
        "docs_good.md", ZoneMap(Counter(), Counter(), Counter())
    )
    expected_counts = {"exact": 1, "rhyme": 1, "reformulation": 1}
    if {zone: zmap.claims.get(zone, 0) for zone in expected_counts} != expected_counts:
        print(f"  FAIL selftest: zones fixture gave {dict(zmap.claims)}")
        return 1
    if {zone: zmap.prose.get(zone, 0) for zone in ("exact", "rhyme")} != {
        "exact": 1,
        "rhyme": 1,
    }:
        print(f"  FAIL selftest: prose fixture gave {dict(zmap.prose)}")
        return 1
    if zmap.prose.get("reformulation"):
        print(f"  FAIL selftest: legend line counted as prose: {dict(zmap.prose)}")
        return 1
    if zmap.marks != 1:
        print(f"  FAIL selftest: marker fixture gave {zmap.marks} marks")
        return 1
    if sum(zmap.legend.values()) != 0:
        print(f"  FAIL selftest: one-line legend counted as legend: {dict(zmap.legend)}")
        return 1
    legend_file = zone_counts([FIXTURES / "docs_legend.md"]).get(
        "docs_legend.md", ZoneMap(Counter(), Counter(), Counter())
    )
    if sum(legend_file.legend.values()) != 4 or sum(legend_file.claims.values()) != 0:
        print(
            f"  FAIL selftest: legend fixture gave "
            f"claims {dict(legend_file.claims)}, legend {dict(legend_file.legend)}"
        )
        return 1
    if sum(legend_file.prose.values()) != 0:
        print(f"  FAIL selftest: legend fixture gave prose {dict(legend_file.prose)}")
        return 1
    if legend_file.marks != 0:
        print(f"  FAIL selftest: legend fixture gave {legend_file.marks} marks")
        return 1
    print(f"  ok   selftest: {len(expected) + 1} fixtures, 9 rules")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="The Fold's two lints.")
    parser.add_argument(
        "command",
        nargs="?",
        default="all",
        choices=["all", "docs", "approx", "zones", "selftest"],
    )
    parser.add_argument("paths", nargs="*", help="files or directories (default: repo root)")
    parser.add_argument("--json", action="store_true", help="machine-readable findings")
    parser.add_argument("--strict", action="store_true", help="warnings fail the run")
    parser.add_argument("--per-file", action="store_true", help="zones: show one line per file")
    parser.add_argument(
        "--show", action="store_true", help="zones: print each prose attribution"
    )
    parser.add_argument(
        "--recursive", action="store_true", help="walk directories for the suffix"
    )
    args = parser.parse_args(argv)

    if args.command == "selftest":
        return selftest()

    if args.command == "zones":
        docs = collect(args.paths, ".md") if args.paths else default_docs()
        per_file = zone_counts(docs)
        if args.json:
            print(
                json.dumps(
                    {
                        name: {
                            "claims": dict(zmap.claims),
                            "legend": dict(zmap.legend),
                            "prose": dict(zmap.prose),
                            "marks": zmap.marks,
                        }
                        for name, zmap in per_file.items()
                    },
                    indent=2,
                )
            )
            return 0
        order = ["exact", "reformulation", "rhyme", "false friend", "the absence"]
        totals: Counter[str] = Counter()
        legend: Counter[str] = Counter()
        prose: Counter[str] = Counter()
        for zmap in per_file.values():
            totals.update(zmap.claims)
            legend.update(zmap.legend)
            prose.update(zmap.prose)
        width = max(len(zone) for zone in order)
        tagged = sum(1 for zmap in per_file.values() if zmap.claims)
        print(f"  zone map: {tagged} files with zone tables of {len(docs)}")
        for zone in order:
            print(f"       {zone:<{width}}  {totals.get(zone, 0):4d}")
        print(f"       {'without tables':<{width}}  {len(docs) - tagged:4d}")
        legend_total = sum(legend.values())
        if legend_total:
            print(
                f"       {'legend (definitions, not claims)':<{width}}  {legend_total:4d}"
            )

        prose_files = sum(1 for zmap in per_file.values() if zmap.prose)
        prose_total = sum(prose.values())
        if prose_total:
            print(f"\n  prose attributions: {prose_files} files of {len(docs)}")
            for zone in order:
                if prose.get(zone):
                    print(f"       {zone:<{width}}  {prose.get(zone, 0):4d}")
            print(f"       {'total':<{width}}  {prose_total:4d}")

        mark_files = sum(1 for zmap in per_file.values() if zmap.marks)
        mark_total = sum(zmap.marks for zmap in per_file.values())
        if mark_total:
            print(
                f"\n  status markers (marked by contrast, zone not named): "
                f"{mark_files} files of {len(docs)}"
            )
            print(f"       {'total':<{width}}  {mark_total:4d}")

        silent = [
            name
            for name, zmap in per_file.items()
            if not (zmap.claims or zmap.prose or zmap.marks)
        ]
        if silent and not args.show:
            print(f"       {'no zone language':<{width}}  {len(silent):4d}  {', '.join(silent)}")

        if args.per_file:
            for name, zmap in per_file.items():
                if not (zmap.claims or zmap.prose or zmap.marks):
                    continue
                parts = [
                    f"table {sum(zmap.claims.values())}" if zmap.claims else "",
                    f"prose {sum(zmap.prose.values())}" if zmap.prose else "",
                    f"marks {zmap.marks}" if zmap.marks else "",
                ]
                summary = ", ".join(part for part in parts if part)
                print(f"       {name}: {summary}")
        if args.show:
            for path in docs:
                text = path.read_text(encoding="utf-8")
                for lineno, label, sentence in prose_attributions(text):
                    print(f"       {path.name}:{lineno} [{label}] {safe(sentence, 96)}")
                for lineno, sentence in status_markers(text):
                    print(f"       {path.name}:{lineno} [mark] {safe(sentence, 96)}")
        return 0

    findings: list[Finding] = []
    if args.command in {"all", "docs"}:
        docs = (
            collect(args.paths, ".md", args.recursive) if args.paths else default_docs()
        )
        doc_findings = run_docs(docs)
        findings.extend(doc_findings)
        if not args.json:
            report("docs", len(docs), doc_findings)
    if args.command in {"all", "approx"}:
        approx = (
            collect(args.paths, ".py", args.recursive) if args.paths else default_approx()
        )
        approx_findings = run_approx(approx)
        findings.extend(approx_findings)
        if not args.json:
            report("approx", len(approx), approx_findings)

    errors = sum(1 for f in findings if f.severity == "error")
    warnings = len(findings) - errors
    if args.json:
        print(json.dumps([f.__dict__ for f in findings], indent=2))
    if errors or (args.strict and warnings):
        if not args.json:
            print(f"\n{errors} error(s), {warnings} warning(s)")
        return 1
    if not args.json:
        print("\nall lint checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
