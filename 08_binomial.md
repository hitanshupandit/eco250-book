# Chapter 8 — Counting successes: the binomial

> **The question:** you run the same trial $n$ times. How many will succeed?

## The first named distribution

Chapter 7 gave you machinery for *any* discrete random variable — but it needed a table
of probabilities handed to you. This chapter is the first case where you can **build**
the table from a description of the situation.

That is the trade a named distribution offers: accept a few assumptions about how the
data arose, and every probability follows from a formula. No table required.

## The four conditions

It is only binomial if **all four** hold. Checking them is worth marks on its own, and
it is the honest reason half of real-world "binomial" problems are not.

1. **A fixed number of trials, $n$**, decided before you start.
2. **Two outcomes per trial** — success or failure. (What you call a "success" is your
   choice; it need not be good.)
3. **The same $p$ on every trial.**
4. **The trials are independent.**

Condition 3 is the one that quietly fails most often. Drawing without replacement from
a small population changes $p$ as you go — take two cards from a deck and the second
draw's probabilities depend on the first. The usual rule of thumb is that sampling
without replacement is close enough to binomial when the sample is under about 5% of
the population.

### Bernoulli

Satisfy conditions 2, 3 and 4 with $n = 1$ and you have a **Bernoulli trial** — a
single success-or-failure experiment.

The binomial is just $n$ Bernoullis added together. That is the quickest way to see why
$E(X) = np$: it is $n$ copies of $p$. It is also why Chapter 12's claim that the
binomial goes normal is not a separate fact — it is the Central Limit Theorem applied
to a sum.

## The formula

$$\mathrm{P}(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
\qquad\text{where}\qquad
\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

Read it in three pieces, because then you never have to memorise it.

$p^k$ — the probability of $k$ successes, if they all happened first.

$(1-p)^{n-k}$ — the probability that the remaining $n - k$ trials all fail.

$\binom{n}{k}$ — **the number of different orders** in which those $k$ successes could
have occurred. Three successes in ten trials could be the first three, or the last
three, or scattered; each arrangement has the same probability, and the coefficient
counts them.

And the summary measures:

$$E(X) = np \qquad\qquad V(X) = np(1-p) \qquad\qquad \sigma = \sqrt{np(1-p)}$$

## Worked example

Thirty per cent of items coming off a production line need rework. Ten items are drawn
independently.

**(a) Check the four conditions.**

**(b) Find $\mathrm{P}(X = 3)$.**

**(c) Find $\mathrm{P}(X \leq 2)$.**

**(d) Find $E(X)$ and $\sigma$.**

### Solution

**(a)** $n = 10$ is fixed; each item either needs rework or does not; $p = 0.30$ is
constant; the items are drawn independently. All four hold, so $X \sim \text{Bin}(10,
0.3)$.

**(b)**

$$\mathrm{P}(X=3) = \binom{10}{3}(0.3)^3(0.7)^7
= 120 \times 0.027 \times 0.0823543 = 0.2668$$

**(c)** "At most 2" means $X = 0$, 1 or 2, so three terms added:

$$\mathrm{P}(X \le 2) = \binom{10}{0}(0.7)^{10} + \binom{10}{1}(0.3)(0.7)^{9}
+ \binom{10}{2}(0.3)^2(0.7)^{8} = 0.3828$$

**(d)**

$$E(X) = 10(0.3) = 3.0
\qquad
\sigma = \sqrt{10(0.3)(0.7)} = \sqrt{2.1} = 1.4491$$

Sit with (b) and (d) together for a moment. The expected value is exactly 3, and the
probability of getting exactly 3 is only **0.2668** — it happens about a quarter of the
time. Chapter 7's point, made concrete: the expected value is where the distribution
balances, not a value you should expect.

## The complement, again

"At least one" questions are binomial questions in disguise, and the complement trick
from Chapter 5 is always the fast route.

A firm sends out 8 invoices, each independently queried with probability 0.15.

Directly, "at least one query" is $X = 1, 2, \ldots, 8$ — eight binomial terms. Via the
complement, it is one:

$$\mathrm{P}(X \ge 1) = 1 - \mathrm{P}(X = 0) = 1 - (0.85)^8 = 1 - 0.2725 = 0.7275$$

One calculation instead of eight. Look for "at least one" and reach for this
immediately.

## In Stata

*The snippets below assume the header and preamble from [Chapter 1](01_what_statistics_is_for.md) — `clear all`, the log, and a `cd` to your own folder.*

Two functions, and the distinction between them is the usual cumulative-versus-exact
trap:

```stata
* P(X = 3) exactly, for n = 10, p = 0.3
display "P(X=3)  = " comb(10,3)*0.3^3*0.7^7

* the cumulative function: P(X <= k)
display "P(X<=2) = " binomial(10, 2, 0.3)

* the upper tail: P(X >= k)
display "P(X>=1) = " binomialtail(8, 1, 0.15)
```

`binomial(n, k, p)` gives $\mathrm{P}(X \le k)$ — **at most** $k$. `binomialtail(n, k, p)`
gives $\mathrm{P}(X \ge k)$ — **at least** $k$. Note they are not complements of each
other, because both include $k$.

For an exact single probability, either compute it with `comb()` as above, or subtract:
`binomial(10,3,0.3) - binomial(10,2,0.3)`.

To generate binomial data and check the theory empirically:

```stata
clear
set seed 250
set obs 10000
generate byte x = rbinomial(10, 0.3)
summarize x
tabulate x
```

The mean should land near 3 and the standard deviation near 1.4491.

## In Python

```python
from scipy import stats

stats.binom.pmf(3, 10, 0.3)      # 0.2668  P(X = 3)      exactly
stats.binom.cdf(2, 10, 0.3)      # 0.3828  P(X <= 2)     at most
1 - stats.binom.cdf(0, 8, 0.15)  # 0.7275  P(X >= 1)     at least one
stats.binom.stats(10, 0.3)       # (3.0, 2.1)  mean and VARIANCE, not sd
```

Watch the last one: `stats.binom.stats` returns the **variance**, so take a square
root for the standard deviation — $\sqrt{2.1} = 1.4491$.

`pmf` is exact, `cdf` is cumulative. Those are the "exactly" and "at most" of the
chapter, and mixing them up is the commonest error here.

### Watching it become normal

![A standardised binomial becoming the normal](figures/binomial_to_normal.png)

Each panel is an exact binomial at $p = 0.3$, standardised, with the standard normal
drawn over it. At $n = 5$ the bars are visibly lumpy and lopsided; by $n = 20$ they
have nearly settled; by $n = 60$ you cannot separate them by eye.

```python
import numpy as np, matplotlib.pyplot as plt

p, n = 0.3, 60
k = np.arange(n + 1)
mu, sd = n*p, np.sqrt(n*p*(1-p))

plt.bar((k - mu)/sd, stats.binom.pmf(k, n, p)*sd, width=1/sd, color="#999999")
xs = np.linspace(-4, 4, 300)
plt.plot(xs, stats.norm.pdf(xs), color="#8b1a1a", lw=1.6)
plt.show()
```

**Change `n` and re-run.** Then set `p = 0.03` and watch it fail — at $np = 1.8$ the
distribution is piled against zero with no room to be symmetric, which is the
$np \geq 5$ condition made visible.

## What goes wrong

**Not checking the four conditions.** Especially constant $p$ — sampling without
replacement from a small population breaks it.

**Confusing $\mathrm{P}(X = k)$ with $\mathrm{P}(X \le k)$.** "Exactly", "at most" and
"at least" are three different calculations, and the wording is the only clue.

**Dropping the binomial coefficient.** Without $\binom{n}{k}$ you have computed the
probability of one specific ordering, not of $k$ successes.

**Using $\sigma = np(1-p)$.** That is the **variance**. The standard deviation is its
square root.

**Doing "at least one" the long way.** Use the complement.

**Mixing up $k$ and $n-k$** in the exponents. The power on $p$ is the number of
successes.

## Exercises

1. $X \sim \text{Bin}(12, 0.25)$.
   (a) Find $\mathrm{P}(X = 3)$.
   (b) Find $E(X)$ and $\sigma$.
   (c) Is $\mathrm{P}(X = 3)$ the most likely single outcome? Explain without computing
   every probability.

2. A multiple-choice quiz has 20 questions, each with four options. A student guesses
   every one.
   (a) What are $n$ and $p$?
   (b) How many would you expect them to get right?
   (c) Find the standard deviation.

3. A machine produces items with a 4% defect rate. Six are drawn independently. Find
   the probability that at least one is defective.

4. For each, say whether the binomial applies, and if not which condition fails.
   (a) Number of heads in 50 flips of a fair coin.
   (b) Number of aces in 5 cards dealt from a 52-card deck.
   (c) Number of customers arriving at a shop between 9 and 10 am.
   (d) Number of left-handed people in a random sample of 200 from a city.

5. $X \sim \text{Bin}(n, 0.5)$ has standard deviation 3. Find $n$.

### Answers

1. (a) $\binom{12}{3}(0.25)^3(0.75)^9 = 220 \times 0.015625 \times 0.0750847 = 0.2581$.
   (b) $E(X) = 12(0.25) = 3$ and $\sigma = \sqrt{12(0.25)(0.75)} = \sqrt{2.25} = 1.5$.
   (c) Yes. The distribution peaks at or next to $np = 3$, and since $np$ is a whole
   number here the mode is exactly 3.

2. (a) $n = 20$, $p = 0.25$.
   (b) $E(X) = 20(0.25) = 5$.
   (c) $\sigma = \sqrt{20(0.25)(0.75)} = \sqrt{3.75} = 1.9365$.

3. $\mathrm{P}(X \ge 1) = 1 - (0.96)^6 = 1 - 0.7828 = 0.2172$.

4. (a) **Yes** — all four hold.
   (b) **No.** Cards are dealt without replacement, so $p$ changes between draws, and 5
   of 52 is nearly 10% of the population, too large for the approximation.
   (c) **No.** There is no fixed number of trials — $n$ is not decided in advance. This
   is a counting-over-time problem, which needs a different distribution.
   (d) **Yes**, effectively. Strictly it is without replacement, but 200 from a city is
   a tiny fraction of the population, so $p$ is constant to any accuracy that matters.

5. $\sigma^2 = n(0.5)(0.5) = 0.25n = 9$, so $n = 36$.

---
