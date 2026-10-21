# ECO 250 — the book

A reading companion for Econ 250, written to the order we actually teach the course
rather than to any textbook's table of contents.

## Why it exists

Students have no assigned textbook. Keller is the reference the course was built
against and the video series are good, but neither is something a student can be
told to read: Keller is long and ordered differently from our lectures, and a
transcript is not prose. So the course needs one document that runs start to
finish in our sequence.

## Sources, and what we take from each

| Source | What it gives us |
|---|---|
| Keller, *Statistics for Management and Economics* 12e | the topic list and the level; which cases are standard |
| OpenIntro Statistics 4e | an alternative ordering, and the modern treatment of study design |
| Professor Leonard's lectures | the descriptive-statistics framing and the four sampling designs |
| Brunton's probability lectures | the limit arguments — binomial to normal, sums of squares to chi-squared |
| This course's own notes and decks | most of the prose, already written and already checked |

**Everything in the book is written from scratch.** The sources above are
copyrighted; we use them to decide *what* to cover and in *what order*, never for
sentences. Where a framing came from a particular source and is worth attributing
out loud in class — the stratosphere mnemonic, the normal as a limit — the chapter
says so.

## Rules the book follows

1. **Every number is computed, not typed.** Worked examples carry the figures that
   appear on the slides, which were produced by the generators in `build/` and
   verified in Stata 17.
2. **It matches what students were actually shown.** Same examples, same notation,
   same order as the decks. A student who attended should recognise every page.
3. **No textbook references.** No "see Keller 8.4", no "Table 1 of Appendix B".
   If a table is needed, it is printed.
4. **Stata appears as it was taught.** Only commands used in a lab, in the style of
   the lab do-files.
5. **Written in the first person**, like the lecture notes — not as a reference work.

## Table of contents

### Part I — Describing data

| # | Chapter | Built from |
|---|---|---|
| 1 | What statistics is for | L1, syllabus week 1 |
| 2 | Centre: mean, median, mode | L2, Recap §1 |
| 3 | Spread, standard deviation, and standardising | L2, Recap §1 |
| 4 | Two variables: covariance and correlation | L3, Recap §4 |

### Part II — Chance

| # | Chapter | Built from |
|---|---|---|
| 5 | Probability: the four rules | L4, Recap §3 |
| 6 | Conditional probability, independence, Bayes | L4, Recap §3 |
| 7 | Random variables, expectation, variance | L5, L6, Recap §4 |

### Part III — Distributions

| # | Chapter | Built from |
|---|---|---|
| 8 | Counting successes: the binomial | L6, Lab 5 |
| 9 | Continuous distributions: uniform, normal, exponential | L6, Lab 5 |
| 10 | Three distributions built out of normals: t, chi-squared, F | L6/L7, teaching notes |

### Part IV — From sample to population

| # | Chapter | Built from |
|---|---|---|
| 11 | Sampling: designs, and the two kinds of error | L7, Recap §2 |
| 12 | The sampling distribution and the Central Limit Theorem | L7, CLT appendix, Lab 6 |
| 13 | Estimation and confidence intervals | L8, Lab 7 |
| 14 | Hypothesis testing, and what a p-value is | L8, Lab 7, `Lab_sess7_pvalue.do` |

### Part V — Comparisons and relationships

| # | Chapter | Built from |
|---|---|---|
| 15 | Comparing two means | L9 |
| 16 | Comparing several means: ANOVA | L11 |
| 17 | Categorical data: proportions and chi-squared tests | L12 |
| 18 | Regression | L10, L12 |

### Back matter

- Appendix A — the normal, t, chi-squared and F tables, printed
- Appendix B — every Stata command used in the course, with the lab it came from
- Appendix C — a proof of the Central Limit Theorem (already written)

## Chapter template

Each chapter runs in this order:

1. **The question the chapter answers**, in one sentence.
2. **The idea**, in prose, before any formula.
3. **The formulas**, with what each symbol is.
4. **A worked example**, with the answer set out the way we want it written.
5. **In Stata** — the commands, as taught.
6. **What goes wrong** — the mistakes that cost marks.
7. **Exercises**, answers at the back of the chapter.

## Build

    python3 book/build.py

Concatenates the chapters in order into `book/ECO250.md`, inserts a table of
contents, and reports word counts and any chapter missing a section from the
template. Markdown only for now; there is no pandoc on this machine, so a PDF
would need either pandoc installed or a converter written.

## Status

| Chapter | State |
|---|---|
| Front matter, index | published |
| 1, 2 | published |
| 11, 12, 13, 14 | published — written first, as the Checkpoint 2 material |
| Practice problems (20) | published |
| 3–10, 15–18 | not started |

## Publishing model

Slides go to Lyceum as now. The book replaces the student-facing teaching notes
and is linked from the course website, one chapter at a time as we reach each
topic.

GitHub Pages serves every chapter at a stable URL — `…/14_hypothesis_testing.html`
— which does not change when later chapters are added, so a link posted in week 8
still works in week 14.

**The instructor teaching notes are a separate thing and stay private.** Those carry
timing, board plans and what to expect students to get wrong. The book is the
student version and must never pick up any of that; `build.py` has no check for it,
so the discipline is manual.
