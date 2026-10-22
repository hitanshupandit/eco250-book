# Chapter 6 — Conditional probability, independence, and Bayes

> **The question:** something happened. What does it tell you about why?

## Turning a conditional round

Chapter 5 gave you $\mathrm{P}(A \mid B)$. This chapter is about the fact that
$\mathrm{P}(A \mid B)$ and $\mathrm{P}(B \mid A)$ are **different numbers**, and about
how to get from one to the other.

That sounds like a technicality. It is the single most consequential idea in the first
half of this course, and the place where trained professionals get things wrong in
print.

Consider: the probability that someone is a professional pianist given that they can
read music is small. The probability that they can read music given that they are a
professional pianist is 1. Same two events, opposite conditioning, wildly different
answers.

## Independence, properly

$A$ and $B$ are **independent** when

$$\mathrm{P}(A \mid B) = \mathrm{P}(A)$$

Knowing $B$ happened tells you nothing about $A$. Equivalently — multiply both sides by
$\mathrm{P}(B)$ —

$$\mathrm{P}(A \cap B) = \mathrm{P}(A)\,\mathrm{P}(B)$$

Either form is a valid test, so use whichever the question makes easy. If you are given
a table, the first is usually quicker; if you are given probabilities, the second.

**Independence is a claim that needs justifying.** On an exam you may only multiply
when independence is stated, or genuinely arguable. "Two different people drawn at
random" is an argument. "Two days at the same shop" usually is not — weather, payday
and season link them.

## Total probability

When the thing you care about can be reached by several routes, add the routes.

If $B_1, B_2, \ldots, B_k$ are mutually exclusive and together cover everything, then
for any event $D$:

$$\mathrm{P}(D) = \mathrm{P}(D \mid B_1)\mathrm{P}(B_1) + \mathrm{P}(D \mid B_2)\mathrm{P}(B_2)
+ \cdots + \mathrm{P}(D \mid B_k)\mathrm{P}(B_k)$$

Each term is one route: the chance of taking that route, times the chance of $D$ once
you are on it. It is a weighted average of the conditional probabilities, weighted by
how often each case arises.

## Bayes' theorem

$$\mathrm{P}(B_i \mid D) = \frac{\mathrm{P}(D \mid B_i)\,\mathrm{P}(B_i)}{\mathrm{P}(D)}$$

Look at the denominator. **It is exactly the total probability** you just computed.

Which gives you the procedure, and it never varies:

> **Compute $\mathrm{P}(D)$ first. Every time.**

Students who get stuck on Bayes problems are almost always students who tried to skip
that step. Build the weighted sum, then divide the one route you care about by it.

The three pieces have names worth knowing: $\mathrm{P}(B_i)$ is the **prior** — what
you believed before the evidence; $\mathrm{P}(D \mid B_i)$ is the **likelihood** — how
well that case explains the evidence; and $\mathrm{P}(B_i \mid D)$ is the
**posterior** — what you believe after.

## Worked example — where did the defect come from?

A plant buys one component from two suppliers.

| | Share of parts | Defect rate |
|---|---|---|
| Supplier X | 0.70 | 0.02 |
| Supplier Y | 0.30 | 0.05 |

**(a) What proportion of all parts are defective?**

**(b) A part fails inspection. What is the probability it came from Y?**

Before computing (b), guess. Most parts come from X, so surely a defective part
probably came from X too?

### Solution

**(a)** Total probability — add the two routes to a defect:

$$\mathrm{P}(D) = (0.70)(0.02) + (0.30)(0.05) = 0.014 + 0.015 = 0.0290$$

**(b)** Bayes — the route through Y, divided by all routes:

$$\mathrm{P}(Y \mid D) = \frac{(0.30)(0.05)}{0.0290} = \frac{0.015}{0.0290} = 0.5172$$

**Y supplies under a third of the parts and is the more likely source of a defective
one.**

Why the intuition failed: it was answering a different question. "Where do parts come
from?" has the answer X. "Where do *defective* parts come from?" weights each supplier
by its defect rate as well as its share, and Y's rate is two and a half times X's —
enough to overturn the share.

## A harder case worth seeing

A screening test is 99% sensitive (it catches 99% of those who have the condition) and
95% specific (it correctly clears 95% of those who do not). The condition affects 1% of
the population. You test positive. What is the probability you have it?

Most people say about 95%. Work it:

$$\mathrm{P}(+) = \underbrace{(0.01)(0.99)}_{\text{sick and positive}}
+ \underbrace{(0.99)(0.05)}_{\text{healthy and false positive}}
= 0.0099 + 0.0495 = 0.0594$$

$$\mathrm{P}(\text{sick} \mid +) = \frac{0.0099}{0.0594} = 0.1667$$

**About 17%.** Five positives in six are false.

The reason is in the denominator. The healthy group is 99 times larger, so even a small
false-positive rate on a huge group produces more positives than a high true-positive
rate on a tiny one. The test is good; the **base rate** is doing the work.

This is the most important thing in the chapter. A small $\mathrm{P}(D \mid B)$ applied
to a large group can swamp a large $\mathrm{P}(D \mid B)$ applied to a small one.

## The probability tree

For two or three cases, a tree is faster and less error-prone than the formula.

Draw one branch per case, labelled with its prior. From each, draw a branch for the
evidence, labelled with the likelihood. **Multiply along each path** to get the joint
probability of that path. The total probability is the sum of the paths where the
evidence occurred; the posterior is one path divided by that sum.

For the supplier problem the four paths multiply to $0.686$, $0.014$, $0.285$ and
$0.015$. They sum to 1, which is your check, and the two defect paths give the $0.029$
above.

## In Stata

*The snippets below assume the header and preamble from [Chapter 1](01_what_statistics_is_for.md) — `clear all`, the log, and a `cd` to your own folder.*

Bayes is pencil work, but you can confirm an answer by simulation, which is a genuinely
good way to convince yourself:

```stata
clear
set seed 250
set obs 1000000

* 70% of parts come from X, the rest from Y
generate byte fromY = runiform() < 0.30

* defect rates differ by supplier
generate byte defect = runiform() < cond(fromY, 0.05, 0.02)

summarize defect
summarize fromY if defect == 1
```

The first `summarize` estimates $\mathrm{P}(D)$ and should land near 0.029. The second
restricts to defective parts and reports the fraction from Y — near 0.5172.

That second line is "shrink the world" written as code: `if defect == 1` *is* the
conditioning.

## In Python — check Bayes by simulation

Bayes is pencil work, but simulating it is the fastest way to convince yourself the
answer is right — and "shrink the world" becomes a line of code.

```python
import numpy as np
rng = np.random.default_rng(250)
n = 1_000_000

from_Y = rng.random(n) < 0.30                            # 30% come from Y
defect = rng.random(n) < np.where(from_Y, 0.05, 0.02)    # rates differ by supplier

print(defect.mean())            # 0.0290  -- P(D), matching the exact answer
print(from_Y[defect].mean())    # 0.5183  -- P(Y | D), exact value 0.5172
```

The second line is the whole idea. `from_Y[defect]` keeps **only the defective parts**
and then asks what fraction came from Y. That subsetting *is* the conditioning — you
have shrunk the world to $D$ and measured $Y$ inside it.

The simulated 0.5183 differs from the exact 0.5172 in the third decimal. That is
simulation noise, not an error: with a million draws the standard error on a
proportion near 0.5 is about 0.0005, so a gap of 0.001 is ordinary.

### The base-rate case

Worth running, because the result is hard to believe until you have counted it:

```python
prev, sens, spec = 0.01, 0.99, 0.95
sick = rng.random(n) < prev
pos  = rng.random(n) < np.where(sick, sens, 1 - spec)

print(pos.mean())          # 0.0594  -- how many test positive at all
print(sick[pos].mean())    # 0.1667  -- how many of those are actually sick
```

About one positive in six is real. Change `prev` to 0.10 and re-run: the same test now
gives a predictive value near 0.69. **The test did not change — the base rate did.**

## What goes wrong

**Skipping $\mathrm{P}(D)$.** Compute the denominator first and the rest is division.

**Inverting the conditional.** $\mathrm{P}(\text{positive} \mid \text{sick})$ is 0.99;
$\mathrm{P}(\text{sick} \mid \text{positive})$ is 0.17. Writing one when you mean the
other is the error this chapter exists to prevent.

**Ignoring the base rate.** The priors are not decoration — in the screening example
they change the answer by a factor of five.

**Assuming independence to make the arithmetic easier.** Check it.

**Forgetting the cases must cover everything.** Total probability needs the $B_i$ to be
mutually exclusive *and* exhaustive. If the shares do not sum to 1, something is
missing.

## Exercises

1. A firm's output comes from three lines: A makes 50% with a 3% defect rate, B makes
   30% with 5%, and C makes 20% with 8%.
   (a) What proportion of output is defective?
   (b) A defective item is found. Which line most probably made it?
   (c) Line C makes the least. Explain in one sentence why it is still a strong
   suspect.

2. $\mathrm{P}(A) = 0.4$, $\mathrm{P}(B) = 0.5$, $\mathrm{P}(A \cap B) = 0.2$. Are $A$
   and $B$ independent? Show both tests.

3. A test for a rare condition is 98% sensitive and 97% specific. The condition affects
   2 people in 1,000.
   (a) Of 100,000 people tested, roughly how many test positive?
   (b) Of those, roughly how many actually have the condition?
   (c) Comment on using this test for population-wide screening.

4. Explain, to someone who has not taken this course, why
   $\mathrm{P}(A \mid B) \neq \mathrm{P}(B \mid A)$. Use an example of your own.

5. Two events have $\mathrm{P}(A) = 0.3$ and $\mathrm{P}(B \mid A) = 0.6$. Find
   $\mathrm{P}(A \cap B)$. Can you find $\mathrm{P}(B)$ from what you are given?

### Answers

1. (a) $(0.50)(0.03) + (0.30)(0.05) + (0.20)(0.08) = 0.015 + 0.015 + 0.016 = 0.046$.
   (b) **Line C**: $0.016/0.046 = 0.3478$, against $0.015/0.046 = 0.3261$ for each of A
   and B. C is the most probable source despite making the least.
   (c) Because its defect rate is high enough to more than offset its small share —
   what matters is share **times** rate, not share alone.

2. **Not independent.** Test 1: $\mathrm{P}(A \mid B) = 0.2/0.5 = 0.4$ — which equals
   $\mathrm{P}(A) = 0.4$, so this test says independent. Test 2:
   $\mathrm{P}(A)\mathrm{P}(B) = 0.4 \times 0.5 = 0.20$, which matches the given joint
   probability. Both tests agree: they **are** independent. (If the two tests ever
   disagree, you have made an arithmetic error — they are algebraically the same
   condition.)

3. (a) Sick: 200 people, of whom 98% test positive → 196. Healthy: 99,800, of whom 3%
   falsely test positive → 2,994. Total positives ≈ **3,190**.
   (b) About **196**, so $196/3190 = 0.0614$ — roughly **6%**.
   (c) As a screen it generates about fifteen false positives for every true one. That
   is not a reason to reject the test, but it is a decisive reason not to treat a
   positive as a diagnosis: it must be followed by a second, more specific test.

4. Any correct example. One form: the probability that it is raining given that the
   ground is wet is moderate — sprinklers, street cleaning, a burst pipe. The
   probability that the ground is wet given that it is raining is nearly 1. The two
   questions point in opposite directions, and the sizes of the two groups — rainy days
   versus wet-ground occasions — are what make the answers differ.

5. $\mathrm{P}(A \cap B) = \mathrm{P}(A)\mathrm{P}(B \mid A) = (0.3)(0.6) = 0.18$.
   **No**, you cannot find $\mathrm{P}(B)$: that would need $\mathrm{P}(B \mid A^c)$ as
   well, to complete the total-probability sum.

---
