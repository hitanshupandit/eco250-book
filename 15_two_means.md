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

<!-- more-practice:start -->

## More practice

Twelve more. Question 4 is the one to get right first — every other question in this
chapter is downstream of deciding whether the design is paired or independent.

1. Two plants are compared. Plant A: $n_1 = 18$, $\bar{x}_1 = 64$, $s_1 = 9$.
   Plant B: $n_2 = 22$, $\bar{x}_2 = 58$, $s_2 = 11$. Assume equal variances.
   (a) Find $s_p^2$ and $s_p$.
   (b) Find the standard error of the difference.
   (c) Find $t$ and state $\nu$.
   (d) Test at $\alpha = 0.05$, two-tailed.
   (e) Find the p-value.

2. For the data in question 1, build a 95% confidence interval for
   $\mu_1 - \mu_2$.
   (a) Give the interval.
   (b) Confirm it agrees with your test, and say which of the two is more informative.

3. Seven trainees are tested before and after a course. The improvements are
   $2,\ 5,\ 3,\ 6,\ 4,\ 7,\ 5$.
   (a) Find $\bar{d}$ and $s_d$.
   (b) Find the standard error and $t$, with $\nu$.
   (c) Test at $\alpha = 0.05$ against a one-sided alternative that the course helps.
   (d) Find the p-value.

4. For each, state whether the design is independent or matched pairs.
   (a) Forty men and forty-five women at a firm, comparing salaries.
   (b) Twenty patients' blood pressure before and after a drug.
   (c) Fifteen fields split in half, one half treated with fertiliser.
   (d) Reaction times of each subject's left and right hand.
   (e) Exam marks of this year's class and last year's class.
   (f) Twenty-five pairs of twins, one of each pair in a programme.
   (g) The same thirty shops' sales in January and in July.
   (h) Thirty randomly assigned to treatment and thirty to control.

5. Compare question 1 (40 observations, not significant) with question 3 (7 pairs,
   significant). Explain how the smaller study produced the stronger result.

6. Why is the variance of $\bar{X}_1 - \bar{X}_2$ a **sum** of the two variances
   rather than a difference? Answer from the formula for the variance of a difference.

7. When would you use the unequal-variance (Welch) version rather than the pooled one?
   (a) Give the rule of thumb.
   (b) Say what goes wrong if you pool when you should not.
   (c) Why is Welch not simply the default?

8. State the degrees of freedom for (a) a pooled two-sample $t$ with $n_1 = 12$ and
   $n_2 = 15$, (b) a matched-pairs $t$ on 12 pairs, (c) a one-sample $t$ with
   $n = 27$. Note which two coincide and say why that is a coincidence.

9. A researcher has 20 subjects measured before and after a treatment, and runs an
   independent-samples test on the two columns of 20.
   (a) What has gone wrong?
   (b) Which direction does the error push the $t$ statistic, and why?
   (c) What would you expect to happen to the p-value?

10. A 95% interval for $\mu_1 - \mu_2$ is $(-1.8,\ 7.4)$.
    (a) What do you conclude at $\alpha = 0.05$?
    (b) A colleague writes "the two groups are the same". Correct them.

11. Using the data in question 1, test the one-sided alternative $\mu_1 > \mu_2$ at
    $\alpha = 0.05$.
    (a) What changes, and what is the conclusion?
    (b) Under what circumstances would this have been the legitimate test to run?

12. Write the sentence you would put in a report for question 3, in language a
    training manager would act on. It should contain the effect size, not just the
    verdict.

### Answers to the extra problems

1. (a) $s_p^2 = \dfrac{17(81) + 21(121)}{38} = \dfrac{1377 + 2541}{38} = 103.1053$,
   so $s_p = 10.1541$.
   (b) SE $= 10.1541\sqrt{\tfrac{1}{18} + \tfrac{1}{22}} =
   10.1541(0.3178) = 3.2272$.
   (c) $t = (64 - 58)/3.2272 = 1.8592$ with $\nu = 18 + 22 - 2 = 38$.
   (d) $t_{0.025,38} = 2.0244$. Since $1.8592 < 2.0244$, **do not reject** — there is
   insufficient evidence of a difference in mean output.
   (e) $p = 0.0707$.

2. (a) $6 \pm 2.0244(3.2272) = 6 \pm 6.5331 = (-0.5331,\ 12.5331)$.
   (b) The interval **contains zero**, so it does not reject $H_0: \mu_1 = \mu_2$ —
   the same verdict as the test, as it must be. The **interval is more informative**:
   it says the gap could plausibly be anywhere from Plant B being half a unit ahead to
   Plant A being twelve and a half ahead. "Not significant" sounds like "no
   difference"; the interval shows that a large difference is entirely consistent with
   this data, and that the study was simply too small to settle the matter.

3. (a) $\bar{d} = 32/7 = 4.5714$. The deviations square to
   $\sum d^2 - (\sum d)^2/n = 164 - 146.2857 = 17.7143$, so
   $s_d^2 = 17.7143/6 = 2.9524$ and $s_d = 1.7183$.
   (b) SE $= 1.7183/\sqrt{7} = 0.6494$, so $t = 4.5714/0.6494 = 7.0391$ with
   $\nu = 6$.
   (c) One-tailed, so the critical value is $t_{0.05,6} = 1.9432$. Since
   $7.0383 > 1.9432$, **reject** — the course improves scores.
   (d) $p = 0.0002$.

4. (a) Independent. (b) **Paired**. (c) **Paired** — the two halves of one field share
   its soil, weather and drainage. (d) **Paired**. (e) Independent. (f) **Paired** —
   twins are deliberately matched. (g) **Paired** — the same shops twice.
   (h) Independent. The test: if each observation in group 1 has a specific partner in
   group 2, it is paired; if the two groups could have had different sizes without
   anything breaking, they are independent.

5. Pairing removed the between-subject variation. In question 1 the denominator
   contains $s_p = 10.1541$, which is mostly differences *between workers* — a source
   of noise that has nothing to do with the question. In question 3 each trainee is
   compared with themselves, so that variation subtracts out and the denominator
   contains only $s_d = 1.7183$, the variation in the *improvement*. A standard
   deviation six times smaller more than compensates for having a fifth as many
   observations. The lesson is that design beats sample size: 7 well-paired
   observations here outperform 40 unpaired ones.

6. Because $V(X - Y) = V(X) + V(Y) - 2\text{COV}(X,Y)$, and with independent samples
   the covariance is zero, leaving $V(X) + V(Y)$. Uncertainty does not cancel when you
   subtract: two noisy estimates make a noisier difference, and the minus sign in the
   numerator has no effect on the denominator. (Note that a *paired* design is exactly
   the case where the covariance is **not** zero and is positive, so the $-2\text{COV}$
   term bites and the variance of the difference falls — which is question 5 written
   algebraically.)

7. (a) Pool only if the two sample variances are of similar size; the common rule of
   thumb is that the larger $s^2$ should be no more than about four times the smaller.
   Here $121/81 = 1.4938$, comfortably within that.
   (b) Pooling averages the two variances, so if they genuinely differ the pooled value
   overstates the uncertainty for the group with the smaller variance and understates
   it for the other. The resulting $t$ has neither the right value nor the right
   distribution, and the error is worst when the sample sizes are also unequal — the
   smaller sample's variance gets too little weight precisely when it matters most.
   (c) Welch is close to the default in modern practice, and Stata's `unequal` option
   is cheap to use. It is taught second because the pooled version makes the structure
   visible — you can see the weighted average of variances and the $n_1 + n_2 - 2$
   degrees of freedom — whereas Welch's fractional degrees of freedom are impossible to
   compute by hand and teach nothing.

8. (a) $12 + 15 - 2 = 25$. (b) $12 - 1 = 11$. (c) $27 - 1 = 26$. None of these
   coincide — but note how close (a) and (c) are, with 27 observations in each case.
   The difference is that the two-sample test estimated **two** means from the data and
   so pays twice; the one-sample test estimated one.

9. (a) The pairing has been discarded. The test now treats the 20 "before" and 20
   "after" values as two unrelated groups of people, when in fact each after-value
   belongs with a specific before-value.
   (b) **Downward**, usually sharply. The denominator becomes a pooled standard
   deviation reflecting differences between subjects, which is typically far larger
   than the standard deviation of the within-subject changes. The numerator is
   unchanged — $\bar{x}_1 - \bar{x}_2$ equals $\bar{d}$ — so a bigger denominator means
   a smaller $t$.
   (c) It will be much larger, and a real effect may well come out "not significant".
   This is the error the chapter exists to prevent, and it is expensive because it
   produces a null result that looks perfectly respectable.

10. (a) The interval contains zero, so **do not reject** at the 5% level.
    (b) "The two groups are the same" overstates it. The interval says the difference
    could be anything from $-1.8$ to $7.4$, which includes values that would matter a
    great deal in practice. The correct statement is that this study cannot distinguish
    the two means — absence of evidence, not evidence of absence, and the width of the
    interval is the measure of how little was learned.

11. (a) Only the critical value: it becomes $t_{0.05,38} = 1.6860$, with all 5% in the
    upper tail. Since $1.8592 > 1.6860$, you would now **reject**, and the one-tailed
    p-value is 0.0354.
    (b) Only if the direction had been specified **before** seeing the data, on
    substantive grounds — for instance if Plant A had new equipment and the whole point
    of the study was to test whether it raised output. If the direction was chosen after
    noticing that $\bar{x}_1 > \bar{x}_2$, the stated 5% is really 10% and the
    rejection is not credible. Note how much hangs on this: the identical data give
    opposite verdicts, and nothing in the output distinguishes the honest version from
    the other one.

12. One acceptable answer: "Across seven trainees, scores rose by an average of 4.57
    points after the course, and the improvement was consistent — every trainee
    improved, by between 2 and 7 points. An improvement this consistent would arise by
    chance about twice in ten thousand such studies, so the course is doing something.
    The caution is the sample: seven trainees is enough to establish that the effect is
    real and not enough to pin down its size for the wider intake."

<!-- more-practice:end -->

---
