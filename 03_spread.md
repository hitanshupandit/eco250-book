# Chapter 3 — Spread, standard deviation, and standardising

> **The question:** two data sets have the same mean. How else do they differ?

## Why the centre is not enough

Two factories both average 50 units a day. One produces between 48 and 52; the other
swings between 10 and 90. Same mean, and you would run them very differently.

Centre is the first of the five questions from Chapter 2. This chapter is the second
and the fourth — variation, and outliers — and it ends with the move that the rest of
the course is built on.

## Three measures, in order of usefulness

**The range** is maximum minus minimum. It uses two numbers and throws away everything
in between, so a single freak value controls it entirely. Report it as a quick sanity
check, never as your answer.

**The interquartile range** is $Q_3 - Q_1$, the width of the middle half. It ignores the
extremes by construction, which makes it the spread to pair with a median.

**The variance and standard deviation** use every observation, and they are what the
rest of the course needs.

$$s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}
\qquad\qquad
\sigma^2 = \frac{\sum (x_i - \mu)^2}{N}$$

$$s = \sqrt{s^2}$$

### Reading the formula

Work from the inside out and it stops looking arbitrary.

$x_i - \bar{x}$ is how far one observation sits from the middle. You cannot simply
average these, because $\sum(x_i - \bar{x}) = 0$ always — that is what "balance point"
means, and the positives cancel the negatives exactly.

So **square them**. Squaring kills the signs and, usefully, penalises distant points
more than near ones. Add the squares, divide to get an average, and you have the
variance.

The variance is in **squared units** — squared dollars, squared minutes — which nobody
has an intuition for. So take the square root, and the **standard deviation** is back
in the units you started with. That is the number to report.

## Why $n-1$

The question that comes up every year.

You are measuring deviations from $\bar{x}$, not from $\mu$. And $\bar{x}$ sits in the
dead centre of *your particular* sample by construction. So your deviations are, on
average, slightly too small — they are measured from the most favourable point
available rather than from the truth.

Dividing by $n-1$ instead of $n$ inflates them by exactly the right amount to correct
for it.

The other way to say the same thing: once you know $\bar{x}$ and any $n-1$ of the
values, the last one is forced. Only $n-1$ of the deviations were ever free to vary.
That count has a name — **degrees of freedom** — and it reappears in Chapters 10, 13
and 14 as the parameter of the $t$ distribution. It is the same $n-1$ every time.

For a *population* you divide by $N$, because there is nothing to correct for. You have
everybody.

## Worked example

The five values from Chapter 2: $\{3,\ 7,\ 7,\ 9,\ 14\}$, with $\bar{x} = 8$.

| $x$ | 3 | 7 | 7 | 9 | 14 |
|---|---|---|---|---|---|
| $x - \bar{x}$ | $-5$ | $-1$ | $-1$ | $1$ | $6$ |
| $(x-\bar{x})^2$ | 25 | 1 | 1 | 1 | 36 |

The deviations sum to zero, as they must — a free check on your arithmetic. The squares
sum to **64**, so

$$s^2 = \frac{64}{5-1} = 16 \qquad s = \sqrt{16} = 4$$

Build that table every time. It is the same table that produces covariance in Chapter 4,
and being fast at it is most of the battle on a timed paper.

## Comparing spreads across different things

A standard deviation of 9 is large for shoe sizes and tiny for house prices, so raw
standard deviations cannot be compared across variables with different means. The
**coefficient of variation** fixes that:

$$\text{CV} = \frac{s}{\bar{x}}$$

A bank's Branch A has a mean wait of 42 seconds with $s = 6$; Branch B averages 78
seconds with $s = 9$.

$$\text{CV}_A = \frac{6}{42} = 14.29\% \qquad \text{CV}_B = \frac{9}{78} = 11.54\%$$

Branch B has the larger standard deviation and is the **more consistent** of the two
relative to its own average. A manager comparing raw standard deviations would get this
exactly backwards.

## Standardising

$$z = \frac{x - \mu}{\sigma}
\qquad\text{or, from a sample,}\qquad
z = \frac{x - \bar{x}}{s}$$

**"How many standard deviations from the middle is this?"**

Three things about it.

It **strips the units**. A $z$ of 1.5 means the same thing for dollars, kilograms and
test scores, which is what makes comparison across different variables possible at all.

It **does not change the shape**. Standardise a skewed variable and you get a skewed
variable with mean 0 and standard deviation 1. Standardising is not a way of making
something normal, and the Stata section below demonstrates it.

And **every test statistic in this course is a $z$ in disguise**:

$$\frac{\text{what I got} - \text{what I expected}}{\text{how much it typically wobbles}}$$

Chapter 14 will put $\bar{x}$ on top and a standard error underneath, but the shape is
this one.

## The empirical rule

For data that *is* roughly bell-shaped — and only then — the standard deviation has a
direct reading:

| within | of the mean |
|---|---|
| $\mu \pm 1\sigma$ | about **68%** of observations |
| $\mu \pm 2\sigma$ | about **95%** |
| $\mu \pm 3\sigma$ | about **99.7%** |

The exact figures are 68.27%, 95.45% and 99.73%. This is where "a $z$ beyond 2 is
unusual" comes from, and it is worth memorising because it lets you sanity-check an
answer without a table.

## In Stata

```stata
use "DATA/cps_small.dta", clear
summarize wage
summarize wage, detail
```

`summarize` gives the standard deviation. `summarize, detail` adds the percentiles —
$Q_1$ is the 25th, $Q_3$ the 75th, so the IQR is the difference — plus skewness and the
five largest and smallest values, which is the fastest outlier check available.

To standardise a variable:

```stata
egen double zwage = std(wage)
summarize zwage
histogram zwage, normal
```

`egen std()` subtracts the mean and divides by the standard deviation. `summarize` will
confirm the new mean is 0 and the new standard deviation is 1 — and the histogram will
show you that the shape has not changed at all. Wage was right-skewed before
standardising and is right-skewed after.

## What goes wrong

**Dividing by $n$ when you have a sample.** Use $n-1$ unless the data really is the
whole population.

**Forgetting to square-root.** The variance is not the standard deviation, and an
answer in squared minutes is almost always a missing square root.

**Comparing standard deviations across different variables.** Use the coefficient of
variation, as the branch example shows.

**Applying the empirical rule to skewed data.** The 68–95–99.7 figures assume a bell.
For a skewed variable they can be badly wrong.

**Thinking standardising normalises.** It centres and rescales. It does not reshape.

## Exercises

1. For $\{4,\ 8,\ 9,\ 11,\ 13,\ 15\}$ compute the range, the mean, the sample variance
   and the sample standard deviation.

2. A data set has $\bar{x} = 60$ and $s = 5$. Convert each to a $z$-score: 52, 60, 73.

3. Two investments: Fund A returns a mean of 8% with $s = 3$; Fund B returns a mean of
   22% with $s = 7$. Which is riskier? Defend your answer with a number.

4. A sample of deviations from the mean is reported as $-3, -1, 0, 2, 3$. Something is
   wrong. What, and how do you know without any other information?

5. Scores are bell-shaped with $\mu = 500$, $\sigma = 100$.
   (a) Roughly what proportion lie between 400 and 600?
   (b) Between 300 and 700?
   (c) A score of 780 — is it unusual? Answer with a $z$-score and one sentence.

### Answers

1. Range $= 15 - 4 = 11$. Sum is 60, so $\bar{x} = 10$. Deviations $-6, -2, -1, 1, 3, 5$
   square to $36, 4, 1, 1, 9, 25$, summing to 76. So $s^2 = 76/5 = 15.2$ and
   $s = 3.8987$.

2. $z = (52-60)/5 = -1.60$; $z = (60-60)/5 = 0$; $z = (73-60)/5 = +2.60$. The last is
   unusual — beyond two standard deviations.

3. By standard deviation, B. By **coefficient of variation**, A is riskier:
   $3/8 = 37.5\%$ against $7/22 = 31.8\%$. Per unit of return, Fund A's outcome varies
   more. Either answer is defensible provided you say which measure you used and why —
   but the CV is the one that compares like with like.

4. The deviations sum to $+1$, not 0. Deviations from the mean must sum to exactly zero,
   so either a value or the mean has been computed wrongly. You need nothing else to
   know that.

5. (a) 400 and 600 are $\mu \pm 1\sigma$, so about **68%**.
   (b) $\mu \pm 2\sigma$, so about **95%**.
   (c) $z = (780-500)/100 = 2.80$. Yes — nearly three standard deviations above the
   mean, which the empirical rule puts in the outer 0.3% or so.

---
