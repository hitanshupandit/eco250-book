# Chapter 11 — Sampling: why your answer moves

> **The question:** two honest researchers do the same study and get different
> numbers. Which one is wrong?

## Neither of them

That is the whole chapter, and it is worth stating before any formula.

Chapter 1 set up the gap: you measure a sample, you care about a population.
Chapters 2 to 10 filled in the tools — how to describe the sample, how to reason
about chance, how to put a shape on a population. This chapter joins the two ends,
and it does it with one idea that most students take longer to accept than they
expect:

> **A statistic is itself a random variable.**

Draw a sample, compute $\bar{x}$. Draw a different sample from the same population,
compute $\bar{x}$ again. The two numbers differ. Nobody made an arithmetic mistake
and no equipment malfunctioned — the samples were different, so the numbers are
different.

Which means $\bar{x}$ has a distribution. It has a centre, it has a spread, it has a
shape. That distribution is called the **sampling distribution of the mean**, and
once you can describe it, everything in Chapters 13 and 14 follows almost
mechanically.

## Sampling error

Define

$$\text{sampling error} = \bar{x} - \mu$$

It is the gap between what you computed and what you wanted. Three things about it.

It is **not a mistake**. Chapter 1 contrasted it with non-sampling error, which *is*
a mistake — a mistyped value, a leading question. Sampling error is what remains
when you have done everything right.

It is **random**, not systematic. Sometimes positive, sometimes negative, with no
tendency either way.

And it **shrinks with $n$** — at a rate we are about to pin down exactly.

## Building a sampling distribution, once, by hand

The only honest way to believe any of this is to construct one. So take a population
small enough to write down completely:

$$\{2,\ 4,\ 6,\ 8\}$$

This is a *population*, not a sample, so we divide by $N$ and not by $N - 1$:

$$\mu = \frac{2+4+6+8}{4} = 5, \qquad
\sigma^2 = \frac{(2-5)^2 + (4-5)^2 + (6-5)^2 + (8-5)^2}{4} = \frac{20}{4} = 5$$

so $\sigma = \sqrt{5} = 2.2361$.

Now take every possible sample of size $n = 2$, drawing **with replacement** so the
draws are independent. There are $4 \times 4 = 16$ of them. Here is what their means
come to:

| $\bar{x}$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| how many of the 16 | 1 | 2 | 3 | 4 | 3 | 2 | 1 |
| probability | 1/16 | 2/16 | 3/16 | 4/16 | 3/16 | 2/16 | 1/16 |

That table **is** the sampling distribution of $\bar{X}$ for $n = 2$. It is an
ordinary probability distribution of an ordinary random variable, and you already
know how to find its mean and variance from Chapter 7.

**Its centre.** Treating it as a discrete random variable:

$$E(\bar{X}) = 2\left(\tfrac{1}{16}\right) + 3\left(\tfrac{2}{16}\right) + \cdots
+ 8\left(\tfrac{1}{16}\right) = 5$$

Exactly $\mu$. Not approximately — exactly.

**Its spread.**

$$V(\bar{X}) = \sum (\bar{x} - 5)^2 \mathrm{P}(\bar{x}) = 2.5
\qquad\Longrightarrow\qquad
\mathrm{SD}(\bar{X}) = \sqrt{2.5} = 1.5811$$

And now look at that number next to the population's:

$$\frac{\sigma}{\sqrt{n}} = \frac{2.2361}{\sqrt{2}} = 1.5811$$

The same. Which is not a coincidence, and is the single most useful fact in the
course.

## The two results

For a simple random sample of size $n$ from a population with mean $\mu$ and
standard deviation $\sigma$:

$$\boxed{\;E(\bar{X}) = \mu \qquad\qquad \mathrm{SD}(\bar{X}) = \frac{\sigma}{\sqrt{n}}\;}$$

**The first says $\bar{X}$ is unbiased.** It is not systematically too big or too
small. It misses, but it does not lean.

**The second has a name**: $\sigma/\sqrt{n}$ is the **standard error of the mean**.
It is not the standard deviation of the data — it is the standard deviation of
$\bar{x}$ *across repeated samples*. Confusing the two is the most expensive mistake
in this half of the course, and the Stata section below is largely about not making
it.

### The $\sqrt{n}$, and why precision is expensive

The $n$ is under a square root, and that has a consequence people find
disappointing:

| $n$ | standard error when $\sigma = 6$ |
|---|---|
| 36 | 1.000 |
| 144 | 0.500 |
| 576 | 0.250 |

**To halve the standard error you must quadruple the sample.** Not double it. Going
from 36 observations to 144 buys you a factor of two; getting another factor of two
costs you 432 more.

This is why survey costs explode when someone asks for a more precise estimate, and
why Chapter 13 can tell you exactly how many observations a target precision
requires.

## A worked example

A coffee chain knows that daily sales per outlet have mean $\mu = 18$ (hundred cups)
and standard deviation $\sigma = 6$. A random sample of $n = 36$ outlets is drawn.

**(a) Find the standard error of $\bar{X}$.**

**(b) Within what range would you expect the middle 95% of sample means to fall?**

**(c) Why can you answer (b) without being told the shape of the population?**

### Solution

**(a)**

$$\mathrm{SD}(\bar{X}) = \frac{\sigma}{\sqrt{n}} = \frac{6}{\sqrt{36}} = \frac{6}{6} = 1$$

**(b)** Taking the sampling distribution as approximately normal — which is what
Chapter 12 justifies — the middle 95% lies within 1.96 standard errors of the centre:

$$18 \pm 1.96(1) = (16.04,\ 19.96)$$

**(c)** Because of the Central Limit Theorem, which is the next chapter. The results
$E(\bar{X}) = \mu$ and $\mathrm{SD}(\bar{X}) = \sigma/\sqrt{n}$ hold for *any*
population shape whatsoever — they are consequences of the rules for expectation and
variance from Chapter 7, nothing more. Only the claim that the shape is **normal**
needs the CLT, and at $n = 36$ it is usually safe.

Notice what we have **not** claimed: nothing here says a single outlet's sales lie
between 16.04 and 19.96. That statement would need the population itself to be
normal. This is a statement about *averages of 36 outlets*, which is a far
better-behaved quantity.

## When the draws are not independent

Everything above assumes a simple random sample — independent draws. Large real
surveys are often not built that way, and the consequence is worth seeing.

The American Community Survey does not sample people. It samples **households**, and
interviews everyone in them. We tested this in lab on 13,275 people from Maine, where
the population standard deviation of age is 23.82:

| design | people per sample | SD of the 1,000 sample means |
|---|---|---|
| 100 people, drawn independently | 100.0 | 2.427 |
| 48 households | 99.9 | 3.364 |

Both samples contain about a hundred people. The household design has **39% more
sampling error**.

The reason is that $\sigma/\sqrt{n}$ counts *independent pieces of information*, and
people in the same household are not independent — partners are close in age, and a
household of students or of retirees pulls a sample's ages together. Forty-eight
households carry less information than a hundred unrelated people.

So the formula $\sigma/\sqrt{n}$, applied with $n$ = number of people, **understates**
the true standard error for household survey data. Anyone reporting a margin of error
from a clustered survey without adjusting for the design is quoting a number that is
too small.

## In Stata

*The snippets below assume the header and preamble from [Chapter 1](01_what_statistics_is_for.md) — `clear all`, the log, and a `cd` to your own folder.*

The distinction that matters:

```stata
use "DATA/cps_small.dta", clear
summarize wage
ci means wage
```

`summarize` reports `Std. dev.` — that is $s$, the spread of individual wages,
$6.2466$.

`ci means` reports `Std. err.` — that is $s/\sqrt{n}$, the spread of $\bar{x}$,
$0.1975$.

They differ by a factor of $\sqrt{1000} = 31.6$, and they answer different questions.
**How much do wages vary?** is the first. **How precisely do I know the average
wage?** is the second.

To watch a sampling distribution being built rather than take my word for it:

```stata
use "DATA/Gen_w.dta", clear
tempfile pop
quietly save `pop', replace

clear
set obs 1000
set seed 66454
generate double sample_mean = .

forvalues i = 1/1000 {
    preserve
        use `pop', clear
        bsample 36
        quietly summarize Gen_w
        local m = r(mean)
    restore
    quietly replace sample_mean = `m' in `i'
}

summarize sample_mean
histogram sample_mean, normal
```

The standard deviation that `summarize` reports at the end is the standard error,
measured rather than predicted. Compare it with $\sigma/\sqrt{36}$ and it will agree.

## In Python

Build a sampling distribution the same way the lab did, but in three lines:

```python
import numpy as np, pandas as pd
rng = np.random.default_rng(250)

d = pd.read_stata("DATA/cps_small.dta")
w = d["wage"].astype(float).to_numpy()

means = np.array([rng.choice(w, 36, replace=True).mean() for _ in range(2000)])

print(means.std(ddof=1))        # the standard error, MEASURED
print(w.std(ddof=1)/np.sqrt(36))  # the standard error, PREDICTED
```

Those two numbers agree to within simulation noise, which is the chapter's central
claim checked rather than asserted. `rng.choice(..., replace=True)` is Stata's
`bsample`.

```python
import matplotlib.pyplot as plt
plt.hist(w, bins=60, alpha=0.5, density=True, label="individual wages")
plt.hist(means, bins=40, alpha=0.8, density=True, label="means of 36")
plt.legend(); plt.show()
```

Two histograms on one axis makes the point no table can: the sample means are centred
in the same place and are **dramatically narrower**. That narrowing is $\sigma/\sqrt{n}$.

**Change 36 to 144 and re-run.** The second histogram halves in width — not quarters —
because the standard error goes as $\sqrt{n}$.

## What goes wrong

**Confusing $s$ with $s/\sqrt{n}$.** Reading `Std. dev.` where you want `Std. err.`
is the single most common error in submitted work. One describes the data, the other
describes your estimate.

**Thinking $\mu$ moves.** It does not. $\mu$ is a fixed number you do not know.
$\bar{x}$ is what moves. Sentences like "the population mean could be anywhere in
this range" are sloppy in a way that causes real trouble in Chapter 13.

**Treating $\sigma/\sqrt{n}$ as a law of nature.** It assumes independent draws. For
clustered or stratified designs it is wrong, and for clustered designs it is wrong in
the dangerous direction — too small.

**Dividing by $N-1$ for a population.** In the $\{2,4,6,8\}$ example we divided by
$N$, because those four values *are* the population. The $n-1$ correction exists to
compensate for estimating the mean from a sample. There is nothing to compensate for
when you have everybody.

**Applying a statement about $\bar{X}$ to a single observation.** "95% of sample
means fall between 16.04 and 19.96" says nothing about any individual outlet.

## Exercises

1. A population has $\mu = 70$ and $\sigma = 12$. A random sample of 9 is drawn.
   (a) Find $E(\bar{X})$ and $\mathrm{SD}(\bar{X})$.
   (b) How large would $n$ have to be for the standard error to equal 2?

2. For the population $\{1,\ 3,\ 5\}$:
   (a) Find $\mu$ and $\sigma$.
   (b) List all 9 samples of size 2 drawn with replacement and their means.
   (c) Verify that $E(\bar{X}) = \mu$ and that $\mathrm{SD}(\bar{X}) = \sigma/\sqrt{2}$.

3. A researcher reports that in her sample of 400, the standard deviation of income
   is \$18,000 and therefore "the average is accurate to within about \$18,000".
   What has she confused, and what is the right figure?

4. Explain in your own words why quadrupling the sample size only halves the standard
   error.

5. A polling firm samples 1,200 voters by selecting 300 households and interviewing
   all adults in each. It reports a margin of error based on $n = 1{,}200$. Is that
   margin too large, too small, or about right? Explain.

### Answers

1. (a) $E(\bar{X}) = 70$ and $\mathrm{SD}(\bar{X}) = 12/\sqrt{9} = 4$.
   (b) Set $12/\sqrt{n} = 2$, so $\sqrt{n} = 6$ and $n = 36$.

2. (a) $\mu = 3$; $\sigma^2 = [(1-3)^2 + (3-3)^2 + (5-3)^2]/3 = 8/3 = 2.6667$, so
   $\sigma = 1.6330$.
   (b) The nine means are 1, 2, 3, 2, 3, 4, 3, 4, 5 — that is, $\bar{x} = 1, 2, 3, 4,
   5$ with probabilities $1/9, 2/9, 3/9, 2/9, 1/9$.
   (c) $E(\bar{X}) = (1 + 4 + 9 + 8 + 5)/9 = 3 = \mu$. And
   $V(\bar{X}) = 4/3$, so $\mathrm{SD}(\bar{X}) = 1.1547 = 1.6330/\sqrt{2}$.

3. She has used $s$ where she wanted $s/\sqrt{n}$. The standard error is
   $18{,}000/\sqrt{400} = \$900$, which is twenty times smaller. \$18,000 describes
   how much *incomes* vary, not how precisely she knows the average.

4. The standard error depends on $\sqrt{n}$, not $n$. Averaging cancels out
   independent errors, but each new observation contributes less than the one before
   — the tenth observation improves a mean of nine far more than the thousandth
   improves a mean of 999. Precision accumulates, but with diminishing returns, and
   the exponent $\tfrac{1}{2}$ is the exact rate.

5. **Too small.** Adults in the same household are not independent draws — they share
   location, income bracket, and often political views. The effective sample size is
   well below 1,200, so the true standard error is larger than
   $\sigma/\sqrt{1200}$ and the reported margin is optimistic.

<!-- more-practice:start -->

## More practice

Fifteen more. Everything in the second half of the course is built on the standard
error, so the arithmetic in questions 1 to 6 needs to become automatic — you should
be able to write down $\sigma/\sqrt{n}$ without pausing.

1. A population has $\mu = 80$ and $\sigma = 12$. Samples of $n = 36$ are drawn.
   (a) Find $E(\bar{X})$ and the standard error.
   (b) What is the shape of the sampling distribution, and what are you assuming?

2. For the same population, find the standard error when (a) $n = 9$, (b) $n = 36$,
   (c) $n = 144$.

3. Look at your three answers to question 2. What has to happen to $n$ to halve the
   standard error, and what does that imply about the cost of precision?

4. Still with $\mu = 80$, $\sigma = 12$, $n = 36$:
   (a) Find $\mathrm{P}(\bar{X} > 83)$.
   (b) Find $\mathrm{P}(\bar{X} < 76)$.
   (c) Find $\mathrm{P}(77 < \bar{X} < 83)$.

5. A researcher wants the standard error to be 1.5 with $\sigma = 12$. What sample
   size is needed?

6. A sample of 36 gives $\bar{x} = 83$, and the population mean really is 80. Is the
   researcher's estimate wrong? Answer carefully.

7. Explain what it means to say $E(\bar{X}) = \mu$, and why this is a statement about
   a *procedure* rather than about any one sample.

8. A population consists of the four values $2,\ 4,\ 6,\ 8$. All samples of size 2
   are drawn **with** replacement.
   (a) How many such samples are there?
   (b) Find the mean of the population and its standard deviation (as a population).
   (c) Without enumerating all of them, state what the mean of the 16 sample means
   must be, and what their standard deviation must be.

9. A sample of 50 is drawn from a population of 500, with $\sigma = 12$.
   (a) Find the standard error ignoring the finite population.
   (b) Apply the finite population correction and recompute.
   (c) Does the correction matter here? Use the 5% rule to justify your answer.

10. In a population 40% of people hold a particular view. A sample of 100 is drawn.
    (a) Find the standard error of the sample proportion.
    (b) Find $\mathrm{P}(\hat{p} > 0.50)$.
    (c) Check that the normal approximation is legitimate.

11. Why does the standard error have $\sqrt{n}$ in it rather than $n$? Answer using the
    fact that variances add.

12. Two researchers study the same population. One takes a single sample of 400; the
    other takes four samples of 100 and averages the four sample means. Compare the
    precision of the two answers.

13. A student says: "the standard deviation and the standard error are the same thing,
    one is just for samples." Correct them in two sentences.

14. A sampling distribution is sometimes called a "distribution of a statistic". Explain
    what is random in it, given that the population is fixed and not random at all.

15. The standard error $\sigma/\sqrt{n}$ requires $\sigma$, which nobody knows. State
    what you do instead, and what that substitution costs you.

### Answers to the extra problems

1. (a) $E(\bar{X}) = \mu = 80$, and SE $= 12/\sqrt{36} = 2.0000$.
   (b) Approximately normal. The assumption is either that the population is normal,
   or — by the CLT — that $n = 36$ is large enough, which for a population that is not
   wildly skewed it is.

2. (a) $12/3 = 4.0000$. (b) $12/6 = 2.0000$. (c) $12/12 = 1.0000$.

3. $n$ must be **quadrupled**. Going from 9 to 36 halved it, and 36 to 144 halved it
   again. Precision is bought at a quadratic price: the second decimal place costs a
   hundred times what the first did, which is why survey budgets stop where they do
   and why no amount of money makes a sample mean exact.

4. (a) $z = (83-80)/2 = 1.50$, so $\mathrm{P} = 0.0668$.
   (b) $z = (76-80)/2 = -2.00$, so $\mathrm{P} = 0.0228$.
   (c) $z = \pm 1.50$, so $\mathrm{P} = 0.8664$.

5. $n = (\sigma/\text{SE})^2 = (12/1.5)^2 = 8^2 = 64$.

6. **No.** The estimate is 3 above the parameter, but that is sampling error, not a
   mistake — any sample of 36 would land somewhere near 80 without landing on it, and
   a gap of 1.5 standard errors is entirely ordinary. An estimate is "wrong" only if
   the procedure that produced it is biased, and this one is not: $E(\bar{X}) = 80$.
   Distinguishing an unlucky draw from a bad method is most of what the rest of the
   course does.

7. It means that if you drew every possible sample of size $n$ and averaged all the
   resulting $\bar{x}$ values, you would get exactly $\mu$. It says nothing about the
   sample in front of you, which will generally miss. The claim is about the long-run
   behaviour of the *method* — it is unbiased, aiming at the right target — and a
   single draw can no more confirm it than a single coin toss confirms a coin is fair.

8. (a) $4^2 = 16$.
   (b) $\mu = 5.0000$; the deviations are $-3, -1, 1, 3$, squaring to 20, so
   $\sigma^2 = 20/4 = 5.0000$ and $\sigma = 2.2361$.
   (c) The mean of the 16 sample means must be $\mu = 5$, since $E(\bar{X}) = \mu$.
   Their standard deviation must be $\sigma/\sqrt{2} = 2.2361/1.4142 = 1.5811$. You do
   not need the enumeration — the two results in this chapter tell you both answers in
   advance, and the enumeration in the chapter was there to show you they are true,
   not because it is how the work is done.

9. (a) $12/\sqrt{50} = 1.6971$.
   (b) The correction factor is
   $\sqrt{(N-n)/(N-1)} = \sqrt{450/499} = 0.9496$, so the corrected standard error is
   $1.6971 \times 0.9496 = 1.6116$.
   (c) **Yes, mildly.** The sample is $50/500 = 10\%$ of the population, above the 5%
   threshold, so the uncorrected figure overstates the uncertainty — by about 5% here.
   The intuition: once you have measured a tenth of a finite population you genuinely
   know more than the formula for an infinite one credits you with, and in the extreme
   case $n = N$ the correction goes to zero, as it should.

10. (a) $\sqrt{0.4(0.6)/100} = \sqrt{0.0024} = 0.0490$.
    (b) $z = (0.50 - 0.40)/0.0490 = 2.0412$, so $\mathrm{P} = 0.0206$.
    (c) $np = 40$ and $n(1-p) = 60$, both far above 5. Legitimate.

11. The variance of a sum of $n$ independent draws is $n\sigma^2$, because variances
    add. The sample mean divides that sum by $n$, and dividing a random variable by
    $n$ divides its *variance* by $n^2$ — so $V(\bar{X}) = n\sigma^2/n^2 =
    \sigma^2/n$. The standard error is the square root of that, which is
    $\sigma/\sqrt{n}$. The square root is not a modelling choice; it is what taking the
    square root of a variance does.

12. They are **identical in precision**. The average of four sample means of 100 is
    the mean of all 400 observations, so both have standard error
    $\sigma/\sqrt{400} = \sigma/20$. What the second researcher gains is something
    else: four separate estimates whose spread is itself a check on whether the
    sampling is behaving as the theory says.

13. The standard deviation describes how much the individual observations vary; the
    standard error describes how much a *statistic* computed from them varies from
    sample to sample. They are different quantities measured on the same scale — a
    population can have $\sigma = 12$ while the mean of 144 observations from it
    varies by only 1.

14. What is random is the **sampling** — which units happened to be drawn. The
    population is a fixed set of numbers and $\mu$ is a fixed constant, but $\bar{x}$
    changes from draw to draw because the draws change, and the sampling distribution
    catalogues how it changes. Nothing about the world is random here; the randomness
    was introduced deliberately, by you, when you chose the sample at random, and that
    is precisely what makes the uncertainty calculable.

15. You substitute the sample standard deviation $s$ for $\sigma$, giving the estimated
    standard error $s/\sqrt{n}$. The cost is that $s$ is itself a statistic with its own
    sampling variability, so you no longer have a standard normal — you have a $t$
    distribution with $n-1$ degrees of freedom, which is wider. That is the entire
    reason Chapter 10 bothered to introduce the $t$ at all.

<!-- more-practice:end -->

---
