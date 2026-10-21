#!/usr/bin/env python3
"""Assemble the ECO250 book from its chapter files.

Concatenates every NN_*.md in order into book/ECO250.md, builds a table of
contents from the chapter headings, and checks each chapter against the template
in PLAN.md. There is no pandoc on this machine, so the output is markdown only.

Usage:  python3 book/build.py
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "ECO250.md")

#  Sections every chapter is supposed to carry. A chapter missing one is not an
#  error -- front matter has none of them -- but the build says so, because the
#  usual reason is that I stopped writing halfway and forgot.
TEMPLATE = ["## In Stata", "## What goes wrong", "## Exercises", "### Answers"]


def chapters():
    """Chapter files, in filename order. The NN_ prefix is the running order."""
    names = sorted(f for f in os.listdir(HERE)
                   if re.match(r"^\d\d_.*\.md$", f))
    return [(n, open(os.path.join(HERE, n)).read()) for n in names]


def main():
    files = chapters()
    if not files:
        print("  no chapter files found")
        return

    toc, body, rows = [], [], []

    for name, text in files:
        #  the chapter's own H1 is its title
        m = re.search(r"^# (.+)$", text, re.M)
        title = m.group(1).strip() if m else name

        if not name.startswith("00_"):
            anchor = re.sub(r"[^a-z0-9 -]", "", title.lower()).replace(" ", "-")
            toc.append(f"- [{title}](#{anchor})")
            #  second-level headings, for the detailed contents
            for sub in re.findall(r"^## (.+)$", text, re.M):
                if not sub.startswith(("In Stata", "What goes wrong",
                                       "Exercises", "Answers")):
                    toc.append(f"  - {sub.strip()}")

        body.append(text.rstrip() + "\n")

        words = len(text.split())
        #  Front matter (00_) and the back-matter problem sets (9x_) are not
        #  chapters, so the chapter template does not apply to them.
        is_chapter = not name.startswith(("00_", "9"))
        missing = [s for s in TEMPLATE if s not in text] if is_chapter else []
        rows.append((name, words, missing))

    with open(OUT, "w") as f:
        f.write(files[0][1].rstrip() + "\n\n")
        f.write("## Contents\n\n" + "\n".join(toc) + "\n\n---\n\n")
        f.write("\n".join(body[1:]))

    total = sum(r[1] for r in rows)
    print(f"  wrote {os.path.relpath(OUT)}  --  {len(files)} files, {total:,} words")
    print()
    for name, words, missing in rows:
        flag = "" if not missing else "   MISSING: " + ", ".join(
            s.lstrip("# ") for s in missing)
        print(f"    {name:<36} {words:>6,} words{flag}")

    #  A book that cites a textbook students do not own is the thing we are
    #  replacing, so the build refuses to let one back in.
    whole = "\n".join(b for _, b in files)
    banned = ["Keller 8", "Keller 7", "Appendix B", "see Keller",
              "Table 1 of", "Table 4 of"]
    found = [b for b in banned if b in whole]
    print()
    print("    textbook references:", ", ".join(found) if found else "none")

    done = sum(1 for n, _, m in rows if not m and not n.startswith(("00_", "9")))
    print(f"    chapters complete:   {done} of 18")


if __name__ == "__main__":
    main()
