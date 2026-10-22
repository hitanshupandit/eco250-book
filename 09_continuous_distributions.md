# Chapter 9 — Continuous distributions: uniform, normal, exponential

> **The question:** what changes when the variable can take any value in an interval?

## Probability becomes area

For a discrete variable you add probabilities. For a continuous one you cannot, and the
reason is worth seeing rather than memorising.

Ask for the probability that a delivery takes exactly 3 minutes. Not 3.0001, not
2.9999 — exactly 3, to infinite precision. There are infinitely many values it could
take, so any single one gets probability

$$\mathrm{P}(X = a) = 0$$

That is not a technicality to wave past. It has three consequences you will use.

**Only intervals carry probability.** $\mathrm{P}(2 < X < 4)$ is a sensible question;
$\mathrm{P}(X = 3)$ is not.

**Probability is area.** The curve is a **probability density function**, and
$\mathrm{P}(a < X < b)$ is the area under it between $a$ and $b$. Total area is 1.

**Strict and weak inequalities are the same.** $\mathrm{P}(X < a) = \mathrm{P}(X \le a)$,
because the endpoint contributes nothing. This is **false for discrete variables**, and
confusing the two cases is a standard exam trap.

One more thing: a density is not a probability, and its **height can exceed 1**. A
uniform distribution on $[0, 0.5]$ has height 2 everywhere. What cannot exceed 1 is the
area.

## The uniform distribution

The simplest case: every value in $[a, b]$ is equally likely. The density is a flat
line of height $1/(b-a)$, and probabilities are rectangles.

$$\mathrm{P}(c < X < d) = \frac{d - c}{b - a}
\qquad
\mu = \frac{a+b}{2}
\qquad
\sigma = \frac{b-a}{\sqrt{12}}$$

**Example.** Delivery times are uniform between 10 and 50 minutes.

$$\mu = \frac{10+50}{2} = 30
\qquad
\sigma = \frac{40}{\sqrt{12}} = 11.547
\qquad
\mathrm{P}(X < 25) = \frac{25-10}{40} = 0.375$$

No tables, no standardising — just the fraction of the interval you want. The uniform
is genuinely as simple as it looks, which is why it gets one page.

## The normal distribution

$$X \sim N(\mu, \sigma^2)$$

The bell. Symmetric about $\mu$, with $\sigma$ controlling how wide. Two parameters and
you have the whole curve.

It matters for two quite different reasons. Many measured quantities happen to be
roughly bell-shaped — and, far more importantly, Chapter 12 will show that **sample
means are normal whatever the population looks like**. Most of the normal's work in
this course is done on behalf of $\bar{X}$, not on behalf of raw data.

### Standardising, and the table

There are infinitely many normal curves, one for each $(\mu, \sigma)$, and nobody
tabulates them all. Instead, convert to the one that is tabulated:

$$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$

Chapter 3's $z$-score, doing a new job. Subtracting $\mu$ centres the curve on zero;
dividing by $\sigma$ sets its width to 1.

**Always sketch first.** Draw the bell, mark $\mu$, mark your value, shade what the
question asks for. Then compute. It takes five seconds and it prevents the most common
error in this chapter, which is finding the area on the wrong side.

### Worked example

Placement test scores are normal with $\mu = 72$ and $\sigma = 8$.

**(a) What proportion score above 80?**

$$z = \frac{80-72}{8} = 1.00
\qquad
\mathrm{P}(X > 80) = \mathrm{P}(Z > 1) = 1 - 0.8413 = 0.1587$$

**(b) What proportion score between 64 and 80?**

Those are $z = -1$ and $z = +1$:

$$\mathrm{P}(-1 < Z < 1) = 0.8413 - 0.1587 = 0.6827$$

The familiar 68% from the empirical rule, now derived rather than quoted.

**(c) Above what score do the top 10% fall?**

This is the table read **backwards** — you are given an area and want a value. The top
10% begins at $z = 1.2816$, so

$$x = \mu + z\sigma = 72 + 1.2816(8) = 82.25$$

Both directions matter and the second is the one students practise less. Given a
probability, find $z$ first, then unstandardise with $x = \mu + z\sigma$.

## The exponential distribution

Waiting time until the next event, when events arrive at a constant average rate. Calls
to a switchboard, time between machine breakdowns, time until a component fails.

If the mean waiting time is $\mu$, then

$$\mathrm{P}(X > x) = e^{-x/\mu}
\qquad
\mathrm{P}(X < x) = 1 - e^{-x/\mu}
\qquad
\sigma = \mu$$

That last identity is not a misprint: for an exponential, **the standard deviation
equals the mean**. It is a strongly right-skewed distribution — many short waits, a few
very long ones.

**Example.** Time between arrivals at a service desk averages 4 minutes.

$$\mathrm{P}(X > 6) = e^{-6/4} = e^{-1.5} = 0.2231
\qquad
\mathrm{P}(X < 2) = 1 - e^{-2/4} = 1 - 0.6065 = 0.3935$$

No table needed — just the exponential function.

## Which one, when

| Distribution | Reach for it when |
|---|---|
| **Uniform** | every value in a range is equally likely |
| **Normal** | symmetric and bell-shaped — and for sample means, always |
| **Exponential** | waiting time until the next event |

## In Stata

*The snippets below assume the header and preamble from [Chapter 1](01_what_statistics_is_for.md) — `clear all`, the log, and a `cd` to your own folder.*

The two normal functions, and the fact that they invert each other:

```stata
* value -> probability.  normal(z) gives the area to the LEFT.
display "P(X>80)    = " 1 - normal((80-72)/8)
display "P(64<X<80) = " normal((80-72)/8) - normal((64-72)/8)

* probability -> value.  invnormal() takes the area to the left.
display "z for top 10% = " invnormal(0.90)
display "the score     = " 72 + invnormal(0.90)*8
```

`normal()` and `invnormal()` are inverses, which is worth confirming once:

```stata
display normal(invnormal(0.90))
```

For the exponential, no special function is needed:

```stata
display "P(X>6) = " exp(-6/4)
display "P(X<2) = " 1 - exp(-2/4)
```

And to generate continuous data to experiment on:

```stata
clear
set seed 250
set obs 10000
generate double y = rnormal(72, 8)
generate double u = runiform(10, 50)
summarize y u
histogram y, normal
```

## In Python — what the normal actually is

The formula for the normal density is unpleasant and you are never asked to use it.
What you do need is a feel for **what the two parameters do** and **what the areas
look like**, and a picture settles both in seconds.

![What the normal distribution is](figures/normal_anatomy.png)

The left panel is the whole definition. $\mu$ **slides** the curve left or right
without changing its shape; $\sigma$ **widens or narrows** it without moving its
centre. Those are the only two things you can change, which is why naming $\mu$ and
$\sigma$ names the entire distribution.

The right panel is the empirical rule drawn as areas rather than quoted as a rule:
**68.3%** within one standard deviation, **95.4%** within two, **99.7%** within three.

Change the parameters and re-run:

```python
MU, SIGMA = 72, 8        # <-- change these

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

xs = np.linspace(MU - 4*SIGMA, MU + 4*SIGMA, 600)
plt.plot(xs, stats.norm.pdf(xs, MU, SIGMA), color="#8b1a1a", lw=1.8)

for k in (1, 2, 3):                       # shade one, two, three sigma
    m = (xs >= MU - k*SIGMA) & (xs <= MU + k*SIGMA)
    plt.fill_between(xs[m], stats.norm.pdf(xs[m], MU, SIGMA),
                     color="#8b1a1a", alpha=0.12, linewidth=0)
    pct = stats.norm.cdf(k) - stats.norm.cdf(-k)
    print(f"within {k} sigma: {pct:.4f}")

plt.yticks([]); plt.show()
```

Notice the printed percentages **do not change** when you change `MU` and `SIGMA`.
That is the point of standardising: every normal is the same curve in different units.

### The two directions, in Python

Chapter 9's worked example, done both ways. `sf` is the *survival function* — the area
to the right — so you never have to subtract from 1:

```python
mu, sigma = 72, 8

# value -> probability
print(stats.norm.sf(80, mu, sigma))                  # P(X > 80)   = 0.1587
print(stats.norm.cdf(80, mu, sigma)
      - stats.norm.cdf(64, mu, sigma))               # P(64<X<80)  = 0.6827

# probability -> value
print(stats.norm.ppf(0.90, mu, sigma))               # top 10% start at 82.25
```

`ppf` is the inverse — Stata's `invnormal()`. The two are exact inverses, which is worth
confirming once: `stats.norm.cdf(stats.norm.ppf(0.9))` returns `0.9`.

### Stata to Python

| Stata | Python |
|---|---|
| `normal(z)` | `stats.norm.cdf(z)` |
| `1 - normal(z)` | `stats.norm.sf(z)` |
| `invnormal(p)` | `stats.norm.ppf(p)` |
| `display exp(-6/4)` | `stats.expon.sf(6, scale=4)` |
| `runiform(10, 50)` | `rng.uniform(10, 50, size)` |
| `rnormal(72, 8)` | `rng.normal(72, 8, size)` |

Python is **not taught and not examined** in this course — your problem sets are done in
Stata. It is here because seeing the same operation written twice is a cheap way to
notice which part is the statistics and which part is the software.

## What goes wrong

**Looking for $\mathrm{P}(X = a)$ on a continuous variable.** It is zero. The question
must mean an interval.

**Finding the area on the wrong side.** `normal()` and most printed tables give the area
to the **left**. For an upper tail, subtract from 1. Sketching prevents this.

**Forgetting to unstandardise.** When the question asks for a *score* and you have found
$z = 1.2816$, you are not finished: $x = \mu + z\sigma$.

**Using $\sigma^2$ where $\sigma$ belongs.** $N(72, 64)$ and $N(72, 8)$ describe the
same distribution under different conventions — check whether you have been given the
variance or the standard deviation.

**Treating a density height as a probability.** It can exceed 1; only area cannot.

## Exercises

1. $X \sim N(100, 15^2)$.
   (a) Find $\mathrm{P}(X > 120)$.
   (b) Find $\mathrm{P}(85 < X < 130)$.
   (c) Below what value do the bottom 5% fall?

2. Waiting times at a counter are uniform between 0 and 12 minutes.
   (a) Find the mean and standard deviation.
   (b) Find $\mathrm{P}(X > 9)$.
   (c) Find $\mathrm{P}(3 < X < 7)$.

3. The time between breakdowns of a machine is exponential with a mean of 20 days.
   (a) Find the probability it runs more than 30 days without breaking down.
   (b) Find the probability it breaks down within the first week.
   (c) What is the standard deviation?

4. A classmate writes $\mathrm{P}(X = 50) = 0.04$ for a continuous variable. Explain
   what has gone wrong and what they probably meant.

5. Scores are normal with $\mu = 500$ and $\sigma = 100$. A scholarship goes to the top
   2.5%. What is the cut-off, and what $z$ did you use?

### Answers

1. (a) $z = (120-100)/15 = 1.3333$, so $\mathrm{P} = 1 - 0.9088 = 0.0912$.
   (b) $z = -1$ and $z = 2$, so $0.9772 - 0.1587 = 0.8186$.
   (c) $z = -1.6449$, so $x = 100 - 1.6449(15) = 75.33$.

2. (a) $\mu = 6$; $\sigma = 12/\sqrt{12} = 3.4641$.
   (b) $(12-9)/12 = 0.25$.
   (c) $(7-3)/12 = 0.3333$.

3. (a) $e^{-30/20} = e^{-1.5} = 0.2231$.
   (b) $1 - e^{-7/20} = 1 - 0.7047 = 0.2953$.
   (c) 20 days — for an exponential, the standard deviation equals the mean.

4. For a continuous variable the probability of any exact value is zero, so
   $\mathrm{P}(X=50)$ cannot be 0.04. They have most likely computed the **density** at
   50, which is a height and not a probability, or they meant an interval around 50
   such as $\mathrm{P}(49.5 < X < 50.5)$.

5. The top 2.5% starts at $z = 1.96$, so the cut-off is $500 + 1.96(100) = 696$.

---
