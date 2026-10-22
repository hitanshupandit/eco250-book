# Statistics for Economists

**A reading companion for Econ 250 — Bates College**

Hitanshu Pandit · Department of Economics

---

This is the course written down, in the order we teach it. It is not a reference
work and it does not try to be complete the way a textbook is complete. It covers
what we cover, in our sequence, with our examples.

The assigned textbooks for Econ 250 are **Keller, *Statistics for Management and
Economics*** and **OpenIntro Statistics**. This repository is not a replacement for
either — it is the course's teaching notes written up, so students can read the
material in the order it is actually taught, work the practice problems, and drill
the per-module multiple-choice banks.

## Contents

### Part I — Describing data

- [1. What statistics is for](01_what_statistics_is_for.md)
- [2. Centre: mean, median, mode](02_centre.md)
- 3. Spread, standard deviation, and standardising *(in progress)*
- 4. Two variables: covariance and correlation *(in progress)*

### Part II — Chance

- 5. Probability: the four rules *(in progress)*
- 6. Conditional probability, independence, Bayes *(in progress)*
- 7. Random variables, expectation, variance *(in progress)*

### Part III — Distributions

- 8. Counting successes: the binomial *(in progress)*
- 9. Continuous distributions: uniform, normal, exponential *(in progress)*
- 10. Three distributions built out of normals: t, chi-squared, F *(in progress)*

### Part IV — From sample to population

- 11. Sampling: designs, and the two kinds of error *(in progress)*
- 12. The sampling distribution and the Central Limit Theorem *(in progress)*
- 13. Estimation and confidence intervals *(in progress)*
- 14. Hypothesis testing, and what a p-value is *(in progress)*

### Part V — Comparisons and relationships

- 15. Comparing two means *(in progress)*
- 16. Comparing several means: ANOVA *(in progress)*
- 17. Categorical data: proportions and chi-squared tests *(in progress)*
- 18. Regression *(in progress)*

### Practice

- [Twenty practice problems, with solutions](90_practice_problems.md) — covers
  descriptive statistics through hypothesis testing

## How to read it

Read with a pen. Every worked example is laid out the way I want an answer written
on a problem set, so cover the solution and try it first. Reading a worked example
and producing one are different skills, and only the second is any use when there is
a clock running.

The examples repeat on purpose. The same five numbers appear in Chapters 2 and 3,
the same two suppliers in Chapters 5 and 6. You are meant to notice that a new tool
is answering a different question about data you already understand.

Stata appears only as it was taught. If you see a command you have not run in a lab,
that is a mistake and I would like to know.

## A note on accuracy

Every number in the worked examples is computed by the scripts in this repository,
not typed in by hand, and the Stata figures were produced by running the code. If a
number here disagrees with a number on a lecture slide, **the book is wrong** —
please open an issue or tell me in class.

## Building it

    python3 build.py          # assembles the chapters into ECO250.md
    python3 make_practice.py  # regenerates the practice problems and solutions

## Sources

The course was built against Keller's *Statistics for Management and Economics*,
with OpenIntro Statistics as a second opinion on study design, and two lecture
series — Professor Leonard's on descriptive statistics, Steve Brunton's on
probability — behind several of the explanations.

**The writing here is original.** Those sources shaped what is covered and in what
order; none of them is quoted. Where a particular framing is theirs, the text says
so, in case you want to go and find the original.

## Licence

© 2026 Hitanshu Pandit. Released under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — you may
share and adapt this for non-commercial purposes with attribution.
