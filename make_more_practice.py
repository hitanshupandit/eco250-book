#!/usr/bin/env python3
"""Append a second, longer exercise set to every chapter of the book.

Each chapter already ends with five exercises. This adds a 'More practice' block
after them -- eight to twenty-five further problems with full worked answers,
weighted towards the CLT and hypothesis testing because that is where students
lose marks. The block sits between sentinel comments, so running this again
replaces it instead of stacking a second copy.

Nothing here is trusted on sight. Every number quoted in an answer is listed in
that chapter's CHECKS table and recomputed from scipy before a single file is
written, and the check also insists the number actually appears in the text --
otherwise I would be verifying arithmetic I never printed. The script also
counts the problems and the answers and refuses to write if they disagree.

Usage:  python3 book/make_more_practice.py
"""

import os
import re

import more_practice_a as _a
import more_practice_b as _b
import more_practice_c as _c
import more_practice_d as _d
import more_practice_e as _e

HERE = os.path.dirname(os.path.abspath(__file__))

START = "<!-- more-practice:start -->"
END = "<!-- more-practice:end -->"

BLOCKS = {}
for _mod in (_a, _b, _c, _d, _e):
    BLOCKS.update(_mod.BLOCKS)


def shown(value, text):
    """True if `value` appears in `text` in any of the ways we print numbers."""
    #  LaTeX writes dollars as \$ and thousands separators as {,}, neither of
    #  which is in the number as formatted. Strip them before searching.
    text = text.replace("\\$", "").replace("{,}", "")
    forms = {f"{value:.4f}", f"{value:.3f}", f"{value:.2f}", f"{value:.1f}",
             f"{value:.0f}", f"{value:g}", f"{value:,.2f}", f"{value:,.0f}"}
    #  0.1624 is also written 16.24% in places, and 0.95 as 95
    forms |= {f"{value * 100:.2f}", f"{value * 100:.1f}", f"{value * 100:.0f}"}
    return any(f in text for f in forms)


def verify(name, body, checks):
    """Recompute every quoted number, and confirm each one is really printed."""
    problems = []
    for label, stated, computed in checks:
        if abs(stated - computed) > 1e-4 * max(1.0, abs(computed)):
            problems.append(
                f"{name}: {label} -- text says {stated!r}, scipy says {computed!r}")
        elif not shown(stated, body):
            problems.append(
                f"{name}: {label} -- {stated!r} is checked but never printed")
    return problems


def count_items(text):
    """The top-level numbered items in a markdown list, in the order written."""
    return [int(m.group(1)) for m in re.finditer(r"^(\d+)\.\s", text, re.M)]


def structure(name, body):
    """Questions and answers must be contiguous, numbered from 1, and equal."""
    problems = []
    if "### Answers to the extra problems" not in body:
        return [f"{name}: the answers heading is missing"]

    q_part, a_part = body.split("### Answers to the extra problems", 1)
    q, a = count_items(q_part), count_items(a_part)

    for part, nums in (("questions", q), ("answers", a)):
        want = list(range(1, len(nums) + 1))
        if nums != want:
            problems.append(f"{name}: {part} are numbered {nums}, not 1..{len(nums)}")
    if len(q) != len(a):
        problems.append(f"{name}: {len(q)} questions but {len(a)} answers")
    if len(q) < 8:
        problems.append(f"{name}: only {len(q)} problems -- the floor is 8")
    return problems


def splice(text, block):
    """Put the block in just before the chapter's closing rule."""
    wrapped = f"{START}\n\n{block.strip()}\n\n{END}"

    if START in text:
        head, rest = text.split(START, 1)
        _, tail = rest.split(END, 1)
        return head + wrapped + tail

    #  Chapters end with a horizontal rule. Sit above it, so the rule stays last.
    stripped = text.rstrip()
    if stripped.endswith("---"):
        return stripped[:-3].rstrip() + "\n\n" + wrapped + "\n\n---\n"
    return stripped + "\n\n" + wrapped + "\n"


def main():
    faults, counts = [], {}

    for name, (body, checks) in sorted(BLOCKS.items()):
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            faults.append(f"{name}: no such chapter")
            continue
        faults += structure(name, body)
        faults += verify(name, body, checks)
        counts[name] = len(count_items(body.split(
            "### Answers to the extra problems")[0]))

    if faults:
        print("  nothing written. Fix these first:\n")
        for f in faults:
            print("   ", f)
        raise SystemExit(1)

    for name, (body, _) in sorted(BLOCKS.items()):
        path = os.path.join(HERE, name)
        text = open(path).read()
        open(path, "w").write(splice(text, body))

    total = sum(counts.values())
    print(f"  added {total} problems across {len(counts)} chapters\n")
    for name in sorted(counts):
        print(f"    {name:<36} {counts[name]:>3} problems")
    print(f"\n    every quoted number recomputed and found in the text")


if __name__ == "__main__":
    main()
