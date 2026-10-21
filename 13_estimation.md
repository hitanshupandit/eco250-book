# Chapter 13 — Estimation and confidence intervals

> **The question:** you have a sample mean. Somebody asks what $\mu$ is. What do you
> actually say?

## Two kinds of answer

**A point estimate** is one number. "The mean commute is about 28.4 minutes."
$\bar{x}$ is the point estimator of $\mu$, $s^2$ of $\sigma^2$, $\hat{p}$ of $p$.

**An interval estimate** is a range with a claim attached. "The mean commute is
between 26.4 and 30.4 minutes, and I am 95% confident of that."

## Why a point estimate on its own is worthless

$\bar{X}$ is continuous, so

$$\mathrm{P}(\bar{X} = \mu) = 0$$

The probability that your sample mean lands exactly on $\mu$ is zero. The statement
"$\mu$ is 28.4" is, strictly, certainly wrong.

That is the pedantic objection. The practical one is worse: a point estimate with no
$\pm$ hides the thing the reader most needs, which is **how much it would have moved
had you drawn a different sample**. A study of 10 people and a study of 10,000 can
produce the same $\bar{x}$. They do not deserve the same confidence, and only an
interval says so.

> An estimate without a margin is a number pretending to be a measurement.

## Building the interval

Start from Chapter 12. The CLT says

$$Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \ \dot\sim\ N(0,1)$$

and the standard normal puts 95% of its area between $-1.96$ and $+1.96$:

$$\mathrm{P}\!\left(-1.96 < \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} < 1.96\right) = 0.95$$

Now just do algebra on the inequality inside. Multiply through by $\sigma/\sqrt{n}$,
subtract $\bar{X}$, multiply by $-1$ (which flips both inequalities), and read it
backwards:

$$\mathrm{P}\!\left(\bar{X} - 1.96\frac{\sigma}{\sqrt{n}} \;<\; \mu \;<\;
\bar{X} + 1.96\frac{\sigma}{\sqrt{n}}\right) = 0.95$$

Nothing statistical happened in that step. It is rearrangement. But the rearranged
version has $\mu$ in the middle, which is the form we can use.

## Anatomy

$$\bar{x} \;\pm\; \underbrace{z_{\alpha/2}}_{\text{how confident}}
\times \underbrace{\frac{\sigma}{\sqrt{n}}}_{\text{how noisy}}$$

or in words:

$$\textbf{point estimate} \;\pm\; (\textbf{critical value}) \times (\textbf{standard error})$$

**That shape never changes.** Every interval in the rest of this course is these
three pieces; only the pieces get swapped. Learn the shape and the later chapters
cost you almost nothing.

The critical values you need:

| confidence | $\alpha$ | $z_{\alpha/2}$ |
|---|---|---|
| 90% | 0.10 | 1.645 |
| 95% | 0.05 | 1.960 |
| 99% | 0.01 | 2.575 |

More confidence means a **wider** interval. There is no free lunch here: you buy
certainty with vagueness. A 100% confidence interval is $(-\infty, \infty)$ and it is
perfectly correct and perfectly useless.

## What "95% confident" means

This is the sentence students get wrong most often, and it is worth being exact.

> **The interval is random. $\mu$ is not.**

**Correct:** if you repeated the whole exercise many times — new sample, new interval
each time — then 95% of the intervals you constructed would contain $\mu$. This
particular one either does or does not, and you will never find out which.

**Wrong:** "there is a 95% probability that $\mu$ lies between 26.4 and 30.4."
$\mu$ is a fixed number. It is not wandering in and out of your interval. Once the
interval is computed, every quantity in that sentence is fixed and no probability
remains.

The confidence is a property of **the procedure**, not of the one interval in front
of you. It is a claim about your method's track record.

This is not pedantry, and you can measure it. Simulate 1,000 samples of $n = 36$ from
a normal population and build an interval from each: **955 of the 1,000 contain
$\mu$**. The procedure promised 95% and delivered 95.5%. The 45 that missed are not
errors — they are the price of admission, and they are exactly what the 5% refers to.

Repeat that on a **skewed** population at the same $n$ and only **919** contain $\mu$.
The interval under-covers, because at $n = 36$ a skewed population has not finished
converging and the $t$ interval is slightly too narrow. Raise $n$ to 200 and it
improves to 939. That is Chapter 12's "it depends on the shape", shown in the one
place where it costs you something.

## When $\sigma$ is unknown — which is always

In the derivation above, $\sigma$ was handed to us. It never is. You have $s$,
computed from the same sample, and substituting it costs you something:

$$\bar{x} \;\pm\; t_{\alpha/2,\,n-1}\,\frac{s}{\sqrt{n}}$$

The critical value becomes $t$ with $\nu = n - 1$ degrees of freedom — that same
$n - 1$ from Chapter 3.

Why? Because $s$ is itself a random variable. With $\sigma$ you have a fixed
denominator; with $s$ you have one that jumps around from sample to sample, and when
it comes out small the whole ratio blows up. The $t$ distribution's fatter tails are
the distribution being honest about that.

Since $t_{\alpha/2} > z_{\alpha/2}$ always, **the $t$ interval is always wider**. That
extra width is the price of not knowing $\sigma$, and it shrinks fast as $n$ grows:

| $n$ | $t_{0.025,\,n-1}$ | against $z = 1.96$ |
|---|---|---|
| 16 | 2.1314 | 8.7% wider |
| 36 | 2.0301 | 3.6% wider |
| 121 | 1.9799 | 1.0% wider |

## Worked example — a commute

A random sample of $n = 36$ staff reports a mean one-way commute of
$\bar{x} = 28.4$ minutes.

**(a) Suppose past years establish $\sigma = 6$ minutes. Build a 95% interval.**

**(b) Now suppose $\sigma$ is unknown and this sample gave $s = 6$. Rebuild it.**

**(c) Which is wider, and why should it be?**

### Solution

The standard error first, since both parts need it:

$$\frac{6}{\sqrt{36}} = \frac{6}{6} = 1 \text{ minute}$$

**(a)** With $\sigma$ known, use $z_{0.025} = 1.96$:

$$28.4 \pm 1.96(1) \;\Longrightarrow\; (26.44,\ 30.36)$$

**(b)** With $\sigma$ estimated, use $t_{0.025,\,35} = 2.0301$:

$$28.4 \pm 2.0301(1) \;\Longrightarrow\; (26.37,\ 30.43)$$

**(c)** The $t$ interval, by about 0.07 of a minute at each end. You estimated
$\sigma$ from the same 36 people, so you know less — and the interval is honest about
it.

## Margin of error, and the three ways to shrink it

$$E = z_{\alpha/2}\,\frac{\sigma}{\sqrt{n}}$$

the half-width of the interval. There are exactly three levers.

**Raise $n$.** The only honest one — but $\sqrt{n}$ means four times the data for
half the margin.

**Accept less confidence.** 90% instead of 95% narrows it immediately. You are simply
agreeing to be wrong more often.

**Reduce $\sigma$.** Not a statistical move. It means measuring more carefully, or
studying a more homogeneous population.

Nothing else works. Every "tighter interval" you read about came from one of these
three, and it is worth asking which.

## Choosing $n$ before you collect anything

Turn the margin-of-error formula round:

$$n = \left(\frac{z_{\alpha/2}\,\sigma}{E}\right)^{\!2}$$

For the commute study, suppose we want the estimate good to $\pm 1$ minute at 95%,
with $\sigma \approx 6$:

$$n = \left(\frac{1.96 \times 6}{1}\right)^{\!2} = 138.29 \;\Longrightarrow\; n = 139$$

**Always round up.** 138.29 people cannot be surveyed, and rounding down misses the
target.

And note the arithmetic: 36 observations gave us a margin of about 2 minutes. Getting
to 1 minute costs 139. That is the $\sqrt{n}$ tax from Chapter 11, in the form you
will actually meet it.

## In Stata

```stata
use "DATA/cps_small.dta", clear
ci means wage
```

```
    Variable |  Obs   Mean    Std. err.   [95% conf. interval]
        wage | 1,000  10.21302  .1975361   9.825387   10.60065
```

Read it across: $n$, the point estimate, the **standard error** ($s/\sqrt{n}$, not
$s$), and the interval.

The confidence level is a dial:

```stata
ci means wage, level(90)
ci means wage, level(99)
```

which give widths of 0.650, 0.775 and 1.020 for 90%, 95% and 99% on the same data.
Same $\bar{x}$, same standard error — only the critical value moves.

And `ci means` is not doing anything you cannot do by hand:

```stata
quietly summarize wage
display "lower = " r(mean) - invttail(r(N)-1, 0.025)*r(sd)/sqrt(r(N))
display "upper = " r(mean) + invttail(r(N)-1, 0.025)*r(sd)/sqrt(r(N))
```

These match `ci means` to the last decimal it prints. There is no magic in the
command — it is the formula above, typed once by StataCorp.

For sample size, there is no special command; it is arithmetic:

```stata
display "n = " ceil((invnormal(0.975)*6/1)^2)
```

## What goes wrong

**"There is a 95% probability that $\mu$ is in this interval."** The most-penalised
sentence in the course. $\mu$ is fixed; the interval is what was random.

**Using $z$ when $\sigma$ was estimated.** If you computed $s$ from the data, it is
$t$ with $n-1$ degrees of freedom. At large $n$ the difference is cosmetic, but the
reasoning is what is being marked.

**Using $s$ instead of $s/\sqrt{n}$.** The interval comes out $\sqrt{n}$ times too
wide, and absurdly so for large samples.

**Rounding $n$ down.** Round up, always. 138.29 means 139.

**Reporting a point estimate alone.** Say the margin. If you do not know it, you do
not know your estimate.

## Exercises

1. A sample of $n = 64$ has $\bar{x} = 120$ and $s = 16$.
   (a) Compute the standard error.
   (b) Build a 95% confidence interval for $\mu$.
   (c) Build a 99% interval and state how much wider it is.

2. A sample of $n = 25$ has $\bar{x} = 48$ and $s = 10$. Build a 95% interval.
   (Use $t_{0.025,\,24} = 2.0639$.)

3. Explain the difference between these two sentences, and say which is correct:
   (a) "95% of the time, $\mu$ falls inside this interval."
   (b) "95% of intervals built this way contain $\mu$."

4. A researcher wants to estimate a population mean to within 3 units at 95%
   confidence, believing $\sigma \approx 20$.
   (a) How many observations are needed?
   (b) How many to get within 1.5 units?
   (c) What does the comparison illustrate?

5. Two studies estimate the same quantity. Study A reports $12.4 \pm 0.3$; Study B
   reports $12.4 \pm 2.9$. Both used 95% confidence. Give two distinct reasons B's
   interval might be so much wider.

### Answers

1. (a) $16/\sqrt{64} = 2$.
   (b) $\nu = 63$, so $t_{0.025} \approx 1.998$: $120 \pm 1.998(2) = (116.00,
   124.00)$.
   (c) $t_{0.005,\,63} \approx 2.656$: $120 \pm 5.31 = (114.69, 125.31)$ — a half-width
   of 5.31 against 4.00, about 33% wider. Higher confidence, vaguer statement.

2. $10/\sqrt{25} = 2$, so $48 \pm 2.0639(2) = 48 \pm 4.128 = (43.87,\ 52.13)$.

3. **(b) is correct.** Sentence (a) treats $\mu$ as the thing that moves, which it is
   not — it is a fixed unknown constant. The randomness lives in the sample, hence in
   the interval. Confidence describes the long-run performance of the procedure.

4. (a) $n = (1.96 \times 20 / 3)^2 = 170.7$, so **171**.
   (b) $n = (1.96 \times 20 / 1.5)^2 = 683.0$, so **684**.
   (c) Halving the margin roughly quadruples the sample. Precision costs at a rate of
   $\sqrt{n}$, so each further improvement is more expensive than the last.

5. Any two of: **(i)** B had a much smaller sample — the margin goes as
   $1/\sqrt{n}$, so a margin nearly ten times larger suggests a sample on the order of
   a hundred times smaller; **(ii)** B's population is far more variable, so $\sigma$
   or $s$ is larger; **(iii)** B measured less precisely, inflating $s$ through
   measurement error. Note that both studies agree on the point estimate — it is the
   precision, not the finding, that differs.

---
