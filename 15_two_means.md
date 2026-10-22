# Chapter 15 — Comparing two means

> **The question:** two groups, two averages. Is the gap real?

## The same machinery, one parameter further

Chapter 14 tested a mean against a claimed number. This chapter tests a mean against
*another mean*, and almost nothing new is required — the test statistic is still

$$\frac{\text{what I got} - \text{what I expected}}{\text{how much it typically wobbles}}$$

What changes is that "what I got" is now a **difference**, $\bar{x}_1 - \bar{x}_2$, and
the denominator has to describe how much a *difference* wobbles.

Under $H_0$ the two population means are equal, so the expected difference is zero.
That is why the numerator is usually just $\bar{x}_1 - \bar{x}_2$ with nothing
subtracted.

## First, decide which design you have

This is the decision that matters, and getting it wrong invalidates everything after.

**Independent samples.** Two separate groups of people or items, with no pairing
between them. Thirty workers at one plant and thirty-five at another.

**Matched pairs.** *The same* subject measured twice, or subjects deliberately paired.
Before and after a training course; left hand and right hand; twins.

If each observation in group 1 has a natural partner in group 2, it is paired. If the
two groups could have different sizes without anything breaking, they are independent.

The two designs use different formulas, and the paired design is usually far more
powerful — because pairing removes the variation *between* subjects, leaving only the
variation in the thing you care about.

## Independent samples

The variance of a difference adds, from Chapter 7:

$$V(\bar{X}_1 - \bar{X}_2) = \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}$$

Note the **plus**. Subtracting the means does not subtract the uncertainties — two
noisy estimates make a noisier difference.

When the two population variances can be assumed equal, pool them:

$$s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}$$

$$t = \frac{\bar{x}_1 - \bar{x}_2}{s_p\sqrt{\dfrac{1}{n_1} + \dfrac{1}{n_2}}}
\qquad \nu = n_1 + n_2 - 2$$

The pooled variance is a weighted average of the two sample variances, weighted by
degrees of freedom. The larger sample has more say, which is as it should be.

### Worked example

Plant A: $n_1 = 30$ workers, mean output $\bar{x}_1 = 78$, $s_1 = 9$.
Plant B: $n_2 = 35$ workers, mean output $\bar{x}_2 = 72$, $s_2 = 11$.

**Is there a difference in mean output, at $\alpha = 0.05$?**

$H_0: \mu_1 = \mu_2$ against $H_a: \mu_1 \neq \mu_2$. Two-tailed — the question says
"a difference", with no direction.

$$s_p^2 = \frac{29(81) + 34(121)}{63} = \frac{2349 + 4114}{63} = 102.5873
\qquad s_p = 10.1285$$

$$\text{SE} = 10.1285\sqrt{\tfrac{1}{30} + \tfrac{1}{35}} = 2.5200$$

$$t = \frac{78 - 72}{2.5200} = 2.3809 \qquad \nu = 63$$

The critical value is $t_{0.025,63} = 1.9983$. Since $2.3809 > 1.9983$, **reject
$H_0$** — $p = 0.0203$.

**The interval tells you more.** A 95% confidence interval for $\mu_1 - \mu_2$:

$$6 \pm 1.9983(2.5200) = (0.9641,\ 11.0359)$$

It excludes zero, which is the same verdict. But it also says the gap could plausibly
be as small as **1 unit** or as large as **11** — so while the difference is real, its
size is poorly pinned down. A test alone would have hidden that.

## Matched pairs

Here the trick is to stop thinking about two samples at all. Compute the difference
for each pair, and you have **one** sample of differences. Then run the one-sample
test from Chapter 14 on it.

$$t = \frac{\bar{d}}{s_d/\sqrt{n}} \qquad \nu = n - 1$$

### Worked example

Eight trainees are tested before and after a course. The improvements are

$$4,\quad 6,\quad 2,\quad 8,\quad 5,\quad 3,\quad 7,\quad 5$$

$\bar{d} = 5.0$ and $s_d = 2.0$, so

$$\text{SE} = \frac{2}{\sqrt{8}} = 0.7071
\qquad t = \frac{5.0}{0.7071} = 7.0711 \qquad \nu = 7$$

That is enormous — $p = 0.0002$. **Reject $H_0$**: the course improves scores.

Notice how small the sample is. Eight pairs produced a far more decisive result than
65 workers did in the independent case, because pairing stripped out the differences
between trainees and left only the thing being measured.

## In Stata

*The snippets below assume the header and preamble from
[Chapter 1](01_what_statistics_is_for.md).*

```stata
use "DATA/cps_small.dta", clear

* independent samples, pooled
ttest wage, by(female)

* independent samples, not assuming equal variances
ttest wage, by(female) unequal

* from summary statistics, with no data
ttesti 30 78 9 35 72 11
```

For matched pairs the syntax differs — you give two variables rather than a grouping:

```stata
ttest before == after
```

Stata's output row labelled `diff` is a confidence interval for the difference. If it
excludes zero you reject, by exactly the equivalence from Chapter 14.

## In Python

```python
from scipy import stats

# independent, pooled
stats.ttest_ind(group1, group2)                      # equal_var=True by default

# independent, Welch (does not assume equal variances)
stats.ttest_ind(group1, group2, equal_var=False)

# matched pairs
stats.ttest_rel(before, after)

# from summary statistics
stats.ttest_ind_from_stats(78, 9, 30, 72, 11, 35)    # t = 2.3809
```

`ttest_rel` is the paired version, and using `ttest_ind` on paired data is the error
this chapter exists to prevent — it throws away the pairing and usually fails to find
a real effect.

## What goes wrong

**Treating paired data as independent.** The commonest and most expensive error here.
It discards the very structure that makes the design powerful.

**Subtracting the variances.** $V(X - Y) = V(X) + V(Y) - 2\text{COV}$, and for
independent samples the covariance is zero — so the variances **add**. Uncertainty
never cancels.

**Using the wrong degrees of freedom.** $n_1 + n_2 - 2$ for pooled independent samples;
$n - 1$ for paired, where $n$ is the number of *pairs*.

**Pooling when the variances are clearly unequal.** If one sample variance is several
times the other, use the unequal-variance version.

**Reporting only the test.** The interval for the difference tells you the plausible
*size* of the gap, which is usually what somebody actually wants.

## Exercises

1. Group 1: $n = 20$, $\bar{x} = 55$, $s = 8$. Group 2: $n = 25$, $\bar{x} = 49$,
   $s = 10$.
   (a) Compute $s_p^2$ and the standard error of the difference.
   (b) Compute $t$ and state the degrees of freedom.
   (c) Test at $\alpha = 0.05$, given $t_{0.025,43} = 2.0167$.

2. Six people are weighed before and after a diet. The losses in kg are
   $3, 5, 2, 4, 6, 4$.
   (a) Find $\bar{d}$ and $s_d$.
   (b) Test whether the diet produces a loss, at $\alpha = 0.05$, one-tailed, given
   $t_{0.05,5} = 2.0150$.

3. For each, say whether the design is independent or paired.
   (a) Test scores of 30 students taught by method A and 30 by method B.
   (b) Blood pressure of 25 patients before and after a drug.
   (c) Yields from 15 fields split in half, one half treated.
   (d) Salaries of 40 men and 45 women at a firm.

4. Explain why a paired design usually detects a smaller effect than an independent
   design with the same number of observations.

5. A 95% confidence interval for $\mu_1 - \mu_2$ is $(-2.4,\ 8.6)$. What do you
   conclude at $\alpha = 0.05$, and why?

### Answers

1. (a) $s_p^2 = [19(64) + 24(100)]/43 = (1216 + 2400)/43 = 84.093$, so
   $s_p = 9.1702$ and SE $= 9.1702\sqrt{1/20 + 1/25} = 9.1703(0.3) = 2.7511$.
   (b) $t = (55-49)/2.7511 = 2.1810$, $\nu = 43$.
   (c) $2.1810 > 2.0167$, so **reject** — the means differ.

2. (a) $\bar{d} = 24/6 = 4.0$; deviations $-1, 1, -2, 0, 2, 0$ give
   $\sum d^2 = 10$, so $s_d^2 = 2.0$ and $s_d = 1.4142$.
   (b) SE $= 1.4142/\sqrt{6} = 0.5774$, so $t = 4.0/0.5774 = 6.9282$ with $\nu = 5$.
   Since $6.9282 > 2.0150$, **reject** — the diet produces a loss.

3. (a) Independent. (b) **Paired** — same patients twice. (c) **Paired** — the two
   halves of one field are matched. (d) Independent.

4. Pairing removes the variation *between* subjects. In an independent design that
   person-to-person variation sits in the denominator as noise; in a paired design it
   cancels when you subtract, leaving only the variation in the effect itself. A
   smaller denominator means a larger $t$ for the same real effect.

5. **Do not reject.** The interval contains zero, so "no difference" remains plausible,
   and a two-tailed test at $\alpha = 0.05$ rejects exactly when the 95% interval
   excludes the claimed value — here, zero.

---
