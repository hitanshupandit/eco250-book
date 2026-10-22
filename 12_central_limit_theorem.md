# Chapter 12 — The Central Limit Theorem

> **The question:** Chapter 11 gave you the centre and the spread of $\bar{X}$. What
> about its *shape*?

## Why shape is the missing piece

You know $E(\bar{X}) = \mu$ and $\mathrm{SD}(\bar{X}) = \sigma/\sqrt{n}$. Both came
out of the rules for expectation and variance in Chapter 7, and both hold for any
population whatsoever.

But a centre and a spread are not enough to compute a probability. To say anything
like "there is a 5% chance $\bar{X}$ exceeds 19" you need the whole distribution —
you need to know which curve to find an area under.

The Central Limit Theorem supplies it, and it supplies it on terms that are almost
too generous to believe.

## The statement

> For a random sample of size $n$ drawn from **any** population with mean $\mu$ and
> finite standard deviation $\sigma$, the sampling distribution of $\bar{X}$ becomes
> approximately normal as $n$ grows:
>
> $$\bar{X} \ \dot\sim\ N\!\left(\mu,\ \frac{\sigma^2}{n}\right)
> \qquad\text{equivalently}\qquad
> Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \ \dot\sim\ N(0, 1)$$

Read the word **any** again. Not "any symmetric population", not "any population
without outliers". Skewed, bimodal, uniform, discrete — it does not matter. Average
enough draws and the average is normal.

That is a genuinely strange result, and it is the reason the normal distribution
occupies the place it does in statistics. The normal is not common in nature because
of some mysterious preference. It is common because **so many of the quantities we
measure are secretly averages or sums**, and sums of independent things go normal
whatever they are sums of.

## Seeing it happen

Take something that is plainly not normal.

A gym weight stack wears unevenly: the middle plates are rubbed shiny and the top
and bottom ones stay dusty. Nobody collected that data — hundreds of people
independently chose a weight and the metal kept score. The distribution of those
choices is lopsided, with a long tail towards the heavy end.

Now change one thing. Suppose every person does **six sets** and we record *each
person's own average*. One number per person. Plot those.

| | every set everyone did | one average per person |
|---|---|---|
| $n$ | 1 | 6 |
| standard deviation | 24.1 lb | 9.7 lb |
| shape | skewed right | symmetric |

Three things happened, and each is one of the results you now have.

**The spread shrank**, from 24.1 to 9.7. That is $\sigma/\sqrt{n}$ with $n = 6$:
$24.1/\sqrt{6} = 9.8$. The standard error, measured rather than predicted.

**The centre did not move.** $E(\bar{X}) = \mu$.

**The shape changed.** The left panel is skewed. The right panel, built from exactly
the same choices, is not. Nobody made the population normal — we took averages, and
averages go normal.

There is a matching result for skewness that is worth knowing because it tells you
*how fast*:

$$\text{skewness of } \bar{X} \;=\; \frac{\text{skewness of the population}}{\sqrt{n}}$$

The asymmetry does not merely fade, it fades at the same $\sqrt{n}$ rate as the
spread.

## How large does $n$ have to be?

You will see "$n \geq 30$" quoted as a rule. It is a rule of thumb and not a law, and
the honest answer is **it depends on how skewed the population is**.

Here is the evidence, from a deliberately nasty population — strongly left-skewed,
with skewness $-2.11$. For each sample size, 1,000 simulated samples, and we count
how many sample means fall below, inside and above the interval the normal
approximation predicts should hold 95% of the time:

| $n$ | skewness of $\bar{X}$ | below | inside | above |
|---|---|---|---|---|
| 4 | $-1.05$ | 0.047 | 0.953 | **0.000** |
| 9 | $-0.63$ | 0.049 | 0.942 | 0.009 |
| 36 | $-0.29$ | 0.030 | 0.955 | 0.015 |
| 100 | $-0.34$ | 0.034 | 0.937 | 0.029 |

The skewness column follows the $\sqrt{n}$ prediction closely: $-2.11/\sqrt{4} =
-1.06$ against a simulated $-1.05$.

But look at the row for $n = 4$, because it contains a trap.

**The "inside" share is 0.953 — almost exactly the 0.95 promised.** On that evidence
the normal approximation looks perfect. It is not. The two tails are 0.047 and
**0.000** against 0.025 each. The left tail is nearly double what it should be and
the right tail is *empty*, and the two errors cancel in the total.

So a two-sided 95% statement survives at $n = 4$ by sheer luck. Any **one-tailed**
probability is badly wrong — $\mathrm{P}(\bar{X} < 1.5)$ would be understated, and an
upper-tail probability overstated.

By $n = 36$ both tails are within noise of 0.025. So for a population this skewed,
**roughly 36 or more**, and more again if a one-tailed probability is what you
actually care about.

> Thirty is a rule of thumb, not a law. For a badly skewed population it is about the
> minimum; for a symmetric one you can often get away with far less.

## The binomial, as a special case

You already met a version of this in Chapter 8 without it being called the CLT.

A binomial count is a sum: $X = $ the number of successes in $n$ independent trials
is $n$ Bernoulli variables added up. Sums of independent things go normal. So:

$$X \sim \text{Bin}(n, p) \quad\Longrightarrow\quad
X \ \dot\sim\ N\big(np,\ np(1-p)\big) \text{ for large } n$$

Standardise a binomial at $p = 0.3$ and plot it for $n = 5$, then 20, then 60, and
the lumpy, lopsided set of bars at $n = 5$ has nearly settled onto a bell by 20 and
is indistinguishable from one by 60.

The usual working condition is $np \geq 5$ **and** $n(1-p) \geq 5$. Both are needed:
at $n = 60$ and $p = 0.01$ you have $np = 0.6$, and the distribution is piled against
zero with nowhere to be symmetric.

## A worked example

Daily sales per outlet for a coffee chain have $\mu = 18$ (hundred cups) and
$\sigma = 6$. The distribution of individual outlets is right-skewed. A random sample
of $n = 36$ outlets is drawn.

**(a) What is the distribution of $\bar{X}$?**

**(b) Find $\mathrm{P}(\bar{X} > 19)$.**

**(c) Can you find the probability that a *single* outlet sells more than 19?**

### Solution

**(a)** By the CLT, $\bar{X}$ is approximately normal with
$E(\bar{X}) = 18$ and $\mathrm{SD}(\bar{X}) = 6/\sqrt{36} = 1$.

**(b)** Standardise:

$$z = \frac{19 - 18}{1} = 1.00
\qquad\Longrightarrow\qquad
\mathrm{P}(\bar{X} > 19) = \mathrm{P}(Z > 1) = 1 - 0.8413 = 0.1587$$

**(c)** **No.** The population is right-skewed and the CLT says nothing about
individual observations — it is a statement about averages. To find a probability
for one outlet you would need the actual shape of the population, which you have not
been given.

That distinction is the one students most often lose marks on. $\bar{X}$ being
well-behaved does not make $X$ well-behaved.

## In Stata

The simulation is the demonstration. Draw many samples, keep each mean, look at what
you get:

```stata
use "DATA/Gen_y.dta", clear
tempfile pop
quietly save `pop', replace

clear
set obs 1000
set seed 66454
generate double sample_mean = .

forvalues i = 1/1000 {
    preserve
        use `pop', clear
        bsample 4
        quietly summarize Gen_y
        local m = r(mean)
    restore
    quietly replace sample_mean = `m' in `i'
}

summarize sample_mean, detail
histogram sample_mean, normal
```

Change `bsample 4` to 9, 36, 100 and watch the skewness in `summarize, detail` fall
and the histogram straighten. That is the table above, produced in front of you.

For the theoretical probability once you trust the approximation:

```stata
display "P(xbar > 19) = " 1 - normal((19 - 18)/(6/sqrt(36)))
```

## In Python — change $n$ yourself

Stata showed you the simulation. Python shows you the *picture*, and the point of
this one is that **you change the number and watch what happens.**

![The CLT as n increases](figures/clt_convergence.png)

The population on the left is deliberately nasty — strongly right-skewed with a lump
near zero, nothing bell-like about it. Read the two numbers in each title as $n$ grows:

| $n$ | SD of $\bar{X}$ | skewness |
|---|---|---|
| 1 | 8.36 | $+3.76$ |
| 5 | 3.67 | $+1.59$ |
| 30 | 1.49 | $+0.65$ |
| 100 | 0.82 | $+0.37$ |

The spread falls like $\sigma/\sqrt{n}$ and the skewness falls like
$\text{skew}/\sqrt{n}$, exactly as the chapter claims — and by $n = 100$ the red normal
curve sits on the histogram.

Here is the code that drew it. **Change the first line** and run it again:

```python
N_VALUES = [1, 5, 30, 100]      # <-- change these and re-run
REPS     = 20000                # how many sample means to simulate

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(250)

def draw(size):
    """A deliberately ugly population: mostly short values, a long right tail."""
    a = rng.exponential(2.0, size)
    b = rng.exponential(12.0, size)
    return np.where(rng.random(size) < 0.30, b, a)

pop = draw(200_000)
mu, sigma = pop.mean(), pop.std()

fig, axes = plt.subplots(1, len(N_VALUES), figsize=(3.1*len(N_VALUES), 2.7))
for ax, n in zip(np.atleast_1d(axes), N_VALUES):
    means = draw(REPS*n).reshape(REPS, n).mean(axis=1)

    ax.hist(means, bins=60, density=True, color="#999999", edgecolor="white")
    xs = np.linspace(means.min(), means.max(), 300)
    ax.plot(xs, stats.norm.pdf(xs, mu, sigma/np.sqrt(n)), color="#8b1a1a", lw=1.6)

    ax.set_title(f"n = {n}\nSD {means.std():.2f}   skew {stats.skew(means):+.2f}")
    ax.set_yticks([])
plt.tight_layout(); plt.show()
```

**Things worth trying.**

Set `N_VALUES = [1, 2, 3, 4]` and watch how slowly it starts — a population this skewed
is nowhere near normal at $n = 4$, which is the honest answer to "is 30 enough?"

Replace `draw` with `rng.normal(100, 15, size)`. Now even $n = 1$ is a perfect bell,
because the population was already normal and averaging had nothing to fix.

Replace it with `rng.uniform(0, 1, size)` — flat, not remotely bell-shaped. It converges
in a handful of draws, far faster than the skewed case. **How fast the CLT works depends
on how far the population starts from normal**, and this is the cheapest way to see it.

Set `REPS = 200` instead of 20,000. The bell gets lumpy — a reminder that you are
looking at a simulation, not the theorem itself.

## What goes wrong

**Applying the CLT to one observation.** The most common error in this chapter. The
theorem is about $\bar{X}$. A skewed population stays skewed no matter how many
samples you take from it.

**Believing $n = 30$ is a threshold.** It is a convention. For a symmetric population
$n = 10$ may be ample; for the population in the table above, 30 is roughly the
floor, and not enough for a one-tailed statement.

**Trusting a two-sided result as evidence the approximation works.** The $n = 4$ row
shows why: errors in the two tails can cancel and leave the total looking perfect.
Check the tails separately.

**Thinking the CLT makes the population normal.** It does not change the population
at all. Standardising does not either — Chapter 3 made that point, and it is the same
point. The CLT is a statement about what happens when you *average*.

**Forgetting the standard error.** Using $\sigma$ in place of $\sigma/\sqrt{n}$ when
standardising $\bar{X}$ produces a $z$ that is $\sqrt{n}$ times too small.

## Exercises

1. A population has $\mu = 50$, $\sigma = 15$, and is heavily right-skewed. A sample
   of 100 is drawn.
   (a) What is the approximate distribution of $\bar{X}$?
   (b) Find $\mathrm{P}(\bar{X} < 47)$.
   (c) Find $\mathrm{P}(X < 47)$ for a single observation, or explain why you cannot.

2. Explain why the normal distribution turns up so often in practice. Your answer
   should use the word "sum" or "average".

3. A binomial has $n = 40$ and $p = 0.08$. Is the normal approximation appropriate?
   Show the check.

4. In the skewed-population table, the "inside" share at $n = 4$ is 0.953, almost
   exactly the nominal 0.95. Explain why this is not evidence that the approximation
   works at $n = 4$.

5. A quantity is the sum of 200 small independent effects, none of them normal and
   none dominant. What can you say about its distribution, and which theorem licenses
   it?

### Answers

1. (a) Approximately $N(50, 15^2/100)$, i.e. mean 50 with standard error
   $15/\sqrt{100} = 1.5$.
   (b) $z = (47 - 50)/1.5 = -2.00$, so $\mathrm{P}(\bar{X} < 47) = 0.0228$.
   (c) **You cannot.** The population is right-skewed, and the CLT applies only to
   $\bar{X}$. Without the population's actual distribution there is no way to get a
   probability for a single observation.

2. Because so many measured quantities are themselves sums or averages of many small
   independent contributions — a person's height, a firm's monthly revenue, a
   measurement error. The CLT says such sums approach normality whatever the
   individual pieces look like, so the bell appears everywhere without anyone
   arranging it.

3. $np = 40(0.08) = 3.2$, which is **below 5**, so the approximation is not
   appropriate. ($n(1-p) = 36.8$ passes, but both conditions must hold.) Use the
   binomial directly.

4. Because the two tails err in opposite directions and cancel. They are 0.047 and
   0.000 against 0.025 each — the left tail is nearly double and the right is empty.
   The total hides two large, offsetting failures, and any one-tailed statement built
   on that approximation would be badly wrong.

5. It will be approximately normal, by the Central Limit Theorem. The conditions that
   matter are in the question: the effects are independent, there are many of them,
   and none dominates — so no single component's shape can impose itself on the
   total.

---
