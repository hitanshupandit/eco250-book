# Chapter 5 — Probability: the four rules

> **The question:** how do you put a number on "how likely"?

## Why this chapter exists

Chapters 1 to 4 described data you have. Everything from here on describes data you
*might* get — and the bridge is probability.

The connection is the one from Chapter 1: your sample arrived by a random process. To
say anything careful about how far $\bar{x}$ might sit from $\mu$, you need a language
for randomness. This chapter is that language, and it is only four rules.

## The vocabulary, quickly

An **experiment** is any process with an uncertain outcome. The **sample space** is the
set of all possible outcomes. An **event** is a collection of outcomes you care about.

Roll a die: the sample space is $\{1,2,3,4,5,6\}$, and "even" is the event
$\{2,4,6\}$.

Probabilities obey two rules so basic they are easy to forget: every probability lies
between 0 and 1, and the probabilities of all outcomes in the sample space sum to
exactly 1. If your answer is 1.4 or $-0.2$, stop.

## Rule 1 — the complement

$$\mathrm{P}(A^c) = 1 - \mathrm{P}(A)$$

The cheapest trick available, and the one students under-use.

Whenever a question says **"at least one"**, try the complement first. "At least one"
covers many separate cases; "none" is a single case. Computing one thing and
subtracting from 1 beats computing eight things and adding.

## Rule 2 — addition

$$\mathrm{P}(A \cup B) = \mathrm{P}(A) + \mathrm{P}(B) - \mathrm{P}(A \cap B)$$

$A \cup B$ is "$A$ or $B$ or both". You subtract the overlap because adding the two
probabilities counts anything in both twice.

When $A$ and $B$ cannot happen together — **mutually exclusive** — the overlap is empty
and the rule simplifies to $\mathrm{P}(A) + \mathrm{P}(B)$. But check that it really is
empty rather than assuming.

## Rule 3 — conditional probability

$$\mathrm{P}(A \mid B) = \frac{\mathrm{P}(A \cap B)}{\mathrm{P}(B)}$$

Read it as: **you have been told $B$ happened, so shrink the world down to $B$ and
measure $A$ inside it.**

That phrase — shrink the world — is the only intuition you need. The denominator is the
new world; the numerator is the part of it where $A$ also holds. It is why conditional
probabilities are so easy to read off a table, as the worked example shows.

## Rule 4 — multiplication

$$\mathrm{P}(A \cap B) = \mathrm{P}(B)\,\mathrm{P}(A \mid B)$$

This is Rule 3 rearranged, and it holds always.

It collapses to the familiar $\mathrm{P}(A)\mathrm{P}(B)$ **only when $A$ and $B$ are
independent** — which Chapter 6 takes up properly. Multiplying probabilities without
checking independence is the most common error in this material.

## Mutually exclusive is not independent

These two get confused constantly, and they are close to opposites.

| | Mutually exclusive | Independent |
|---|---|---|
| Means | cannot both happen | knowing one tells you nothing about the other |
| $\mathrm{P}(A \cap B)$ | $0$ | $\mathrm{P}(A)\mathrm{P}(B)$ |
| $\mathrm{P}(A \mid B)$ | $0$ | $\mathrm{P}(A)$ |

If $A$ and $B$ are mutually exclusive and $B$ happens, you know for certain $A$ did
not. That is the strongest possible dependence. **Mutually exclusive events with
non-zero probabilities are never independent.**

## Worked example

A credit union classifies 400 loan applications by outcome and by borrower type:

| | First-time | Repeat | Total |
|---|---|---|---|
| **Approved** | 180 | 120 | 300 |
| **Declined** | 70 | 30 | 100 |
| **Total** | 250 | 150 | 400 |

**(a) What is the probability an application was approved?**

**(b) Approved *and* from a repeat borrower?**

**(c) Approved *or* from a repeat borrower?**

**(d) Approved, *given* it came from a repeat borrower?**

### Solution

**(a)** The approved row total over the grand total:

$$\mathrm{P}(A) = \frac{300}{400} = 0.75$$

**(b)** The single cell where both hold:

$$\mathrm{P}(A \cap R) = \frac{120}{400} = 0.30$$

**(c)** Addition rule, subtracting the overlap:

$$\mathrm{P}(A \cup R) = \frac{300}{400} + \frac{150}{400} - \frac{120}{400}
= 0.75 + 0.375 - 0.30 = 0.825$$

**(d)** Shrink the world to repeat borrowers — the 150 in that column — and ask how
many were approved:

$$\mathrm{P}(A \mid R) = \frac{120}{150} = 0.80$$

Notice you can read (d) straight off the table without the formula. That is the whole
point of "shrink the world": the denominator becomes the column total instead of 400.

**A bonus observation.** $\mathrm{P}(A) = 0.75$ but $\mathrm{P}(A \mid R) = 0.80$.
Knowing the applicant is a repeat borrower *changes* the probability of approval, so
these two events are **not independent** — which is Chapter 6's test, arriving early.

## Reading a table

Contingency tables are where most probability questions on an exam live, so get the
pattern fixed:

| You want | Denominator |
|---|---|
| a **joint** probability, $\mathrm{P}(A \cap B)$ | the grand total |
| a **marginal** probability, $\mathrm{P}(A)$ | the grand total |
| a **conditional** probability, $\mathrm{P}(A\mid B)$ | the **row or column** total for $B$ |

Everything else is reading the right cell.

## In Stata

*The snippets below assume the header and preamble from [Chapter 1](01_what_statistics_is_for.md) — `clear all`, the log, and a `cd` to your own folder.*

Probability is mostly pencil work, but a contingency table is one command:

```stata
use "DATA/cps_small.dta", clear
tabulate female black
tabulate female black, cell
tabulate female black, row
```

Plain `tabulate` gives the counts. `, cell` turns every cell into a proportion of the
grand total — those are your **joint** probabilities. `, row` makes each row sum to 1 —
those are **conditional** probabilities given the row variable.

Running all three on the same table is the fastest way to see that joint, marginal and
conditional are three different divisions of the same counts.

## In Python

### The rules, drawn

![Venn diagrams for the probability rules](figures/venn_probability.png)

The left panel is the addition rule and why it has a minus sign: shading both circles
covers the lens **twice**, so you subtract it once to put it right. The middle panel
is the intersection alone. The right panel is conditioning, which the next chapter
takes up — $B$ becomes the whole world and $A$ is measured inside it.

### Contingency tables

```python
import pandas as pd

d = pd.read_stata("DATA/cps_small.dta")

pd.crosstab(d.female, d.black)                      # counts
pd.crosstab(d.female, d.black, normalize="all")     # JOINT probabilities
pd.crosstab(d.female, d.black, normalize="index")   # CONDITIONAL, given the row
pd.crosstab(d.female, d.black, margins=True)        # with the totals
```

Those three `normalize` options are exactly the three divisions from the chapter.
`"all"` divides by the grand total; `"index"` divides by the row total, which *is*
conditioning on the row. Running all three on one table is the quickest way to see
that joint, marginal and conditional are three ways of dividing the same counts.

### Stata to Python

| Stata | Python |
|---|---|
| `tabulate x y` | `pd.crosstab(d.x, d.y)` |
| `tabulate x y, cell` | `pd.crosstab(d.x, d.y, normalize="all")` |
| `tabulate x y, row` | `pd.crosstab(d.x, d.y, normalize="index")` |
| `count if x == 1` | `(d.x == 1).sum()` |

## What goes wrong

**Multiplying without independence.** $\mathrm{P}(A \cap B) = \mathrm{P}(A)\mathrm{P}(B)$
needs justification every single time.

**Forgetting to subtract the overlap** in the addition rule.

**Confusing $\mathrm{P}(A \mid B)$ with $\mathrm{P}(B \mid A)$.** These are different
numbers and the difference matters enormously — Chapter 6 is largely about it.

**Treating mutually exclusive as independent.** They are near-opposites.

**Probabilities outside $[0,1]$.** Always sanity-check the final number.

## Exercises

1. $\mathrm{P}(A) = 0.55$, $\mathrm{P}(B) = 0.40$, $\mathrm{P}(A \cap B) = 0.22$.
   (a) Find $\mathrm{P}(A \cup B)$.
   (b) Find the probability neither occurs.
   (c) Find $\mathrm{P}(A \mid B)$.
   (d) Are $A$ and $B$ independent?

2. A machine produces items independently, each defective with probability 0.04. Six
   are drawn. Find the probability that at least one is defective, and say why the
   complement is the sensible route.

3. Of 500 commuters, 300 take the bus, 150 cycle, and 40 do both at different times.
   Find the probability a randomly chosen commuter does neither.

4. Explain, in your own words and without formulas, why two mutually exclusive events
   with non-zero probability cannot be independent.

5. A table shows $\mathrm{P}(A) = 0.6$, $\mathrm{P}(B) = 0.5$ and
   $\mathrm{P}(A \cap B) = 0.30$. A classmate concludes the events must be mutually
   exclusive. What has gone wrong, and what are they actually?

### Answers

1. (a) $0.55 + 0.40 - 0.22 = 0.73$.
   (b) $1 - 0.73 = 0.27$.
   (c) $0.22/0.40 = 0.55$.
   (d) **Yes.** $\mathrm{P}(A \mid B) = 0.55 = \mathrm{P}(A)$. Equivalently
   $0.55 \times 0.40 = 0.22$, which matches the given joint probability.

2. $\mathrm{P}(\text{none defective}) = 0.96^6 = 0.7828$, so
   $\mathrm{P}(\text{at least one}) = 1 - 0.7828 = 0.2172$. Directly, "at least one"
   would need the six separate cases $X = 1$ through $X = 6$ added together. The
   complement is one calculation instead of six.

3. $\mathrm{P}(\text{bus or cycle}) = (300 + 150 - 40)/500 = 410/500 = 0.82$, so neither
   is $1 - 0.82 = 0.18$.

4. If they are mutually exclusive and you learn that one happened, you immediately know
   the other did not — its probability drops to zero. Learning something that changes
   the other's probability that drastically is the opposite of "tells you nothing",
   which is what independence requires.

5. They have confused the two ideas. $\mathrm{P}(A \cap B) = 0.30$ is **not zero**, so
   the events plainly *can* occur together and are not mutually exclusive. In fact
   $0.6 \times 0.5 = 0.30$ exactly, so they are **independent**.

---
