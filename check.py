#!/usr/bin/env python3
"""Structural checks for the Fold corpus.

Run from the repository root:

    python check.py

Checks, in order:

1. exactly nine HTML models;
2. the paper is six pages;
3. every Markdown note is listed in the README contents;
4. every relative link and backticked filename resolves;
5. every Markdown table has a consistent column count;
6. the docs and Python lints in `fold_lint.py`;
7. the zone map quoted in the README matches the one computed from the notes.

Exit status is 1 if any check fails.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML_EXPECTED = 9
PDF_PAGES_EXPECTED = 6

failures: list[str] = []
notes: list[str] = []


def fail(message: str) -> None:
    failures.append(message)


def ok(message: str) -> None:
    notes.append(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------- HTML count

html_files = sorted(ROOT.glob("*.html"))
if len(html_files) != HTML_EXPECTED:
    fail(f"HTML models: expected {HTML_EXPECTED}, found {len(html_files)}")
else:
    ok(f"HTML models: {len(html_files)}")


# ---------------------------------------------------------------- PDF pages

def pdf_page_count(path: Path) -> int | None:
    try:
        from pypdf import PdfReader  # type: ignore

        return len(PdfReader(str(path)).pages)
    except Exception:
        pass
    try:
        from PyPDF2 import PdfReader  # type: ignore

        return len(PdfReader(str(path)).pages)
    except Exception:
        pass
    try:
        raw = path.read_bytes()
    except OSError:
        return None
    pages = len(re.findall(rb"/Type\s*/Page(?![s])", raw))
    return pages or None


pdf = ROOT / "the-fold.pdf"
if not pdf.exists():
    fail("the-fold.pdf: missing")
else:
    pages = pdf_page_count(pdf)
    if pages is None:
        fail("the-fold.pdf: could not determine page count")
    elif pages != PDF_PAGES_EXPECTED:
        fail(f"the-fold.pdf: expected {PDF_PAGES_EXPECTED} pages, found {pages}")
    else:
        ok(f"paper: {pages} pages")


# ---------------------------------------------------------------- README index

readme = ROOT / "README.md"
readme_text = read_text(readme) if readme.exists() else ""
md_files = sorted(p for p in ROOT.glob("*.md") if p.name != "README.md")

for path in md_files:
    if f"`{path.name}`" not in readme_text:
        fail(f"README contents: `{path.name}` is not listed")

ok(f"Markdown notes: {len(md_files)} checked against the README")


# ---------------------------------------------------------------- links

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
BACKTICK_RE = re.compile(r"`([A-Za-z0-9._-]+\.(?:md|html|pdf|tex))`")


def check_links(path: Path) -> None:
    text = read_text(path)
    for raw in LINK_RE.findall(text):
        target = raw.strip().strip("<>").split("#", 1)[0].split(" ", 1)[0]
        if not target or "://" in target or target.startswith(("mailto:", "#")):
            continue
        if not target.lower().endswith((".md", ".html", ".pdf", ".tex")):
            continue
        if not (path.parent / target).exists():
            fail(f"{path.name}: link target not found: {target}")
    for name in BACKTICK_RE.findall(text):
        if not (path.parent / name).exists():
            fail(f"{path.name}: backticked file not found: {name}")


for path in [readme, *md_files]:
    check_links(path)

ok("links: checked")


# ---------------------------------------------------------------- tables

FENCE = re.compile(r"^\s*(```|~~~)")


def split_cells(line: str) -> list[str]:
    text = line.strip()
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|"):
        text = text[:-1]
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", text)]


def is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def check_tables(path: Path) -> None:
    lines = read_text(path).splitlines()
    in_fence = False
    block: list[tuple[int, str]] = []
    start = 0

    def flush() -> None:
        nonlocal block
        if not block:
            return
        header = split_cells(block[0][1])
        if len(block) < 2 or not is_separator(split_cells(block[1][1])):
            fail(f"{path.name}:{block[0][0]}: table has no separator row")
            block = []
            return
        for lineno, line in block[2:]:
            row = split_cells(line)
            if len(row) != len(header):
                fail(
                    f"{path.name}:{lineno}: table row has {len(row)} cells, "
                    f"header has {len(header)}"
                )
        block = []

    for index, line in enumerate(lines, start=1):
        if FENCE.match(line):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.lstrip().startswith("|"):
            if not block:
                start = index
            block.append((index, line))
        else:
            flush()
    flush()


for path in [readme, *md_files]:
    check_tables(path)

ok("tables: checked")


# ---------------------------------------------------------------- lints

try:
    import fold_lint

    lint_findings = fold_lint.run_docs(fold_lint.default_docs())
    lint_findings += fold_lint.run_approx(fold_lint.default_approx())
    lint_errors = [f for f in lint_findings if f.severity == "error"]
    for finding in lint_errors:
        fail(
            f"lint {finding.path}:{finding.line}: "
            f"[{finding.code}] {finding.message}"
        )
    ok(
        f"lint: {len(lint_errors)} error(s), "
        f"{len(lint_findings) - len(lint_errors)} warning(s)"
    )
except Exception as exc:  # a broken linter should still report
    fail(f"lint: could not run fold_lint: {exc}")


# ------------------------------------------------------- README zone map

ZONE_ROW_RE = re.compile(
    r"^\s*(exact|reformulation|rhyme|false friend|the absence|"
    r"without tables|no prose label|total|legend[^\d]*)\s+(\d+)"
)


def quoted_zone_map() -> tuple[dict[str, int], dict[str, int]]:
    """Read the two blocks quoted in the README's Checks section."""
    table: dict[str, int] = {}
    prose: dict[str, int] = {}
    inside = False
    in_prose = False
    for line in read_text(readme).splitlines():
        if line.lstrip().startswith("```"):
            inside = not inside
            continue
        if not inside:
            continue
        if "prose attributions" in line:
            in_prose = True
            continue
        match = ZONE_ROW_RE.match(line)
        if not match:
            continue
        key = "legend" if match.group(1).startswith("legend") else match.group(1).strip()
        (prose if in_prose else table)[key] = int(match.group(2))
    return table, prose


try:
    import fold_lint as _zones

    docs = _zones.default_docs()
    maps = _zones.zone_counts(docs)
    table_totals: dict[str, int] = {}
    prose_totals: dict[str, int] = {}
    legend_total = 0
    tagged = 0
    prose_files = 0
    for zmap in maps.values():
        tagged += 1 if zmap.claims else 0
        prose_files += 1 if zmap.prose else 0
        legend_total += sum(zmap.legend.values())
        for zone, count in zmap.claims.items():
            table_totals[zone] = table_totals.get(zone, 0) + count
        for zone, count in zmap.prose.items():
            prose_totals[zone] = prose_totals.get(zone, 0) + count

    expected_table = dict(table_totals)
    expected_table["without tables"] = len(docs) - tagged
    expected_table["legend"] = legend_total
    expected_prose = dict(prose_totals)
    expected_prose["total"] = sum(prose_totals.values())
    expected_prose["no prose label"] = len(docs) - prose_files

    quoted_table, quoted_prose = quoted_zone_map()
    before = len(failures)
    for label, expected, quoted in (
        ("table", expected_table, quoted_table),
        ("prose", expected_prose, quoted_prose),
    ):
        if not quoted:
            fail(f"README zone map: no {label} block found in the Checks section")
            continue
        for key in sorted(set(expected) | set(quoted)):
            if expected.get(key) != quoted.get(key):
                fail(
                    f"README zone map: {label} '{key}' says {quoted.get(key)}, "
                    f"computed {expected.get(key)}"
                )
    if len(failures) == before:
        ok("README zone map: quoted counts match")
except Exception as exc:
    fail(f"README zone map: could not check: {exc}")


# ---------------------------------------------------------------- report

for message in notes:
    print(f"  ok   {message}")
for message in failures:
    print(f"  FAIL {message}")

if failures:
    print(f"\n{len(failures)} failure(s)")
    sys.exit(1)
print("\nall checks passed")
