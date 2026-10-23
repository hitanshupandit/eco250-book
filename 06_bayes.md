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

<!-- more-practice:start -->

## More practice

Ten more. The screening-test problem appears three times with different base rates,
on purpose: the arithmetic is identical and the conclusion changes completely, and
that is the only thing about Bayes worth remembering.

1. A disease affects 2% of a population. A test returns positive for 95% of people
   who have it, and for 10% of people who do not.
   (a) Find $\mathrm{P}(\text{positive})$.
   (b) Find $\mathrm{P}(\text{disease} \mid \text{positive})$.
   (c) Explain to a patient, in one sentence, why a positive result from a "95%
   accurate" test still leaves them probably healthy.

2. Repeat 1(b) for a population in which the disease affects **20%**, with the same
   test. Compare the two answers and say what changed.

3. Using the figures in question 1, find
   $\mathrm{P}(\text{no disease} \mid \text{negative})$, and comment on why this test
   is much more useful for ruling out than for ruling in.

4. A firm buys components from two suppliers: 60% from A, which has a 2% defect rate,
   and 40% from B, which has a 5% rate.
   (a) Find the overall defect rate.
   (b) A defective component arrives. Find the probability it came from A.
   (c) A manager says "B is the problem, since B's rate is higher". Comment, using
   your answer to (b).

5. Three machines produce output: M1 makes 50% with a 1% defect rate, M2 makes 30%
   with 2%, M3 makes 20% with 4%.
   (a) Find the overall defect rate.
   (b) Given a defective item, find the probability it came from each machine.
   (c) Check that your three answers sum to 1, and say why they must.

6. Explain, using the law of total probability, why the overall defect rate in
   question 5 is not the average of 1%, 2% and 4%.

7. A spam filter flags 90% of spam and 3% of legitimate email. Sixty per cent of
   incoming email is spam.
   (a) Find the probability a flagged message is actually spam.
   (b) Find the probability a message that got through is actually spam.

8. In a courtroom, a forensic match occurs in 1 in 10,000 innocent people, and the
   defendant matched. The prosecutor says "so there is a 1 in 10,000 chance the
   defendant is innocent."
   (a) What quantity has the prosecutor actually been given?
   (b) What quantity did they claim?
   (c) If the match was found by searching a database of 50,000 people, roughly how
   many innocent matches would you expect?

9. Two events have $\mathrm{P}(A) = 0.3$ and $\mathrm{P}(B \mid A) = 0.3$. Are they
   independent? What extra information would you need to be sure?

10. Write down Bayes' theorem, then say in one sentence what each of the three
    quantities in it is called and what question each one answers.

### Answers to the extra problems

1. (a) $\mathrm{P}(+) = 0.02(0.95) + 0.98(0.10) = 0.019 + 0.098 = 0.1170$.
   (b) $\mathrm{P}(D \mid +) = 0.019/0.117 = 0.1624$.
   (c) Because the disease is rare: out of 1,000 people only 20 have it and 19 of
   those test positive, but 98 of the 980 healthy people also test positive — so 98 of
   the 117 positives are false alarms, simply because there are so many more healthy
   people for the test to be wrong about.

2. $\mathrm{P}(+) = 0.20(0.95) + 0.80(0.10) = 0.19 + 0.08 = 0.2700$, so
   $\mathrm{P}(D \mid +) = 0.19/0.27 = 0.7037$. **The test did not change — only the
   base rate did**, and the answer went from 16% to 70%. The same evidence supports a
   completely different conclusion depending on how common the condition is, which is
   why the prevalence is not an optional extra in a diagnostic question.

3. $\mathrm{P}(-) = 1 - 0.117 = 0.8830$, and
   $\mathrm{P}(D \cap -) = 0.02(0.05) = 0.0010$, so
   $\mathrm{P}(D \mid -) = 0.001/0.883 = 0.0011$ and
   $\mathrm{P}(\text{no } D \mid -) = 0.9989$. A negative result is almost conclusive
   while a positive one is weak evidence. The asymmetry comes from the base rate: when
   a condition is rare, "you do not have it" is a claim that was very probably true
   before the test and the test only reinforces it.

4. (a) $0.60(0.02) + 0.40(0.05) = 0.012 + 0.020 = 0.0320$, so 3.2%.
   (b) $0.012/0.032 = 0.3750$.
   (c) The manager is right that B's *rate* is worse, but 37.5% of all defects still
   come from A, because A supplies half again as many components. Whether to act on
   the rate or on the count depends on the decision: renegotiating a contract is about
   the rate, while staffing an inspection line is about the count.

5. (a) $0.50(0.01) + 0.30(0.02) + 0.20(0.04) = 0.005 + 0.006 + 0.008 = 0.0190$.
   (b) $\mathrm{P}(M1 \mid D) = 0.005/0.019 = 0.2632$;
   $\mathrm{P}(M2 \mid D) = 0.006/0.019 = 0.3158$;
   $\mathrm{P}(M3 \mid D) = 0.008/0.019 = 0.4211$.
   (c) They sum to 1 because the three machines are exhaustive and mutually exclusive
   — every defective item came from exactly one of them, so the posterior probability
   has to be distributed entirely among the three. It is a free check on the
   arithmetic and catches a dropped term immediately.

6. Because the three rates apply to three groups of different sizes, and the law of
   total probability weights each conditional probability by the probability of the
   branch it sits on. The unweighted average of 1%, 2% and 4% is 2.3333%, which would
   be correct only if each machine made a third of the output. M1 is the cleanest
   machine and makes half of everything, so it pulls the true figure down to 1.9%.

7. (a) $\mathrm{P}(\text{flagged}) = 0.60(0.90) + 0.40(0.03) = 0.54 + 0.012 = 0.5520$,
   so $\mathrm{P}(\text{spam} \mid \text{flagged}) = 0.54/0.552 = 0.9783$.
   (b) $\mathrm{P}(\text{through}) = 0.60(0.10) + 0.40(0.97) = 0.06 + 0.388 = 0.4480$,
   so $\mathrm{P}(\text{spam} \mid \text{through}) = 0.06/0.448 = 0.1339$. The filter
   is trustworthy when it flags and leaves about one message in seven of the survivors
   as spam.

8. (a) $\mathrm{P}(\text{match} \mid \text{innocent}) = 0.0001$ — the probability of
   the evidence given innocence.
   (b) $\mathrm{P}(\text{innocent} \mid \text{match})$ — the probability of innocence
   given the evidence. These are not the same quantity, and converting one into the
   other requires a prior probability that the defendant was involved at all. This is
   the **prosecutor's fallacy**, and it is question 2 of this set wearing a wig.
   (c) About $50{,}000 \times 0.0001 = 5$ innocent matches. Finding a match by
   trawling a database is very different evidence from testing a suspect identified
   some other way, and the number 1 in 10,000 does not distinguish them.

9. **Yes**, as far as this goes: $\mathrm{P}(B \mid A) = 0.3$ tells you the
   conditional probability of $B$, and independence requires that to equal
   $\mathrm{P}(B)$. You would need $\mathrm{P}(B)$ to confirm it. The fact that
   $\mathrm{P}(B \mid A)$ happens to equal $\mathrm{P}(A)$ is a coincidence of the
   numbers and is irrelevant — a trap worth noticing.

10. $\mathrm{P}(A \mid B) = \dfrac{\mathrm{P}(B \mid A)\mathrm{P}(A)}{\mathrm{P}(B)}$.
    $\mathrm{P}(A)$ is the **prior** — what you believed before seeing the evidence.
    $\mathrm{P}(B \mid A)$ is the **likelihood** — how probable this evidence would be
    if $A$ were true. $\mathrm{P}(A \mid B)$ is the **posterior** — what you should
    believe now. The denominator is just the total probability of the evidence,
    computed across all the ways it could have arisen, and it is what makes the
    posteriors sum to one.

<!-- more-practice:end -->

---
