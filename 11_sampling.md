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

---
