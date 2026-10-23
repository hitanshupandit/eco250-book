"""Extra practice for chapters 15-18. Imported by make_more_practice.py."""

import numpy as np
from scipy import stats

BLOCKS = {}

# ---------------------------------------------------------------- chapter 15

_sp2 = (17 * 81 + 21 * 121) / 38
_sp = float(np.sqrt(_sp2))
_se15 = float(_sp * np.sqrt(1 / 18 + 1 / 22))
_t15 = 6 / _se15
_c15 = float(stats.t.ppf(0.975, 38))

_d15 = np.array([2, 5, 3, 6, 4, 7, 5], dtype=float)
_dbar = float(_d15.mean())
_sd15 = float(_d15.std(ddof=1))
_sed15 = _sd15 / np.sqrt(7)

BLOCKS["15_two_means.md"] = (r"""
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
""", [
    ("q1a sp2", 103.1053, float(_sp2)),
    ("q1a sp", 10.1541, _sp),
    ("q1b root", 0.3178, float(np.sqrt(1 / 18 + 1 / 22))),
    ("q1b SE", 3.2272, _se15),
    ("q1c t", 1.8592, float(_t15)),
    ("q1d crit", 2.0244, _c15),
    ("q1e p", 0.0707, float(2 * stats.t.sf(_t15, 38))),
    ("q2a ME", 6.5331, float(_c15 * _se15)),
    ("q2a lo", -0.5331, float(6 - _c15 * _se15)),
    ("q2a hi", 12.5331, float(6 + _c15 * _se15)),
    ("q3a dbar", 4.5714, _dbar),
    ("q3a sumsq", 164, float((_d15 ** 2).sum())),
    ("q3a correction", 146.2857, float(_d15.sum() ** 2 / 7)),
    ("q3a SS", 17.7143, float(((_d15 - _dbar) ** 2).sum())),
    ("q3a sd2", 2.9524, float(_d15.var(ddof=1))),
    ("q3a sd", 1.7183, _sd15),
    ("q3b SE", 0.6494, float(_sed15)),
    ("q3b t", 7.0391, float(_dbar / _sed15)),
    ("q3c crit", 1.9432, float(stats.t.ppf(0.95, 6))),
    ("q3d p", 0.0002, float(stats.t.sf(_dbar / _sed15, 6))),
    ("q7a ratio", 1.4938, 121 / 81),
    ("q11a crit", 1.6860, float(stats.t.ppf(0.95, 38))),
    ("q11a p", 0.0354, float(stats.t.sf(_t15, 38))),
])

# ---------------------------------------------------------------- chapter 16

_F16 = 96 / 16

BLOCKS["16_anova.md"] = (r"""
## More practice

Eight more. The arithmetic is mechanical; what is tested is whether you can say what
the $F$ statistic is a ratio *of*, and what rejecting it does and does not tell you.

1. Three teaching methods are compared with six students each. The group means are
   22, 26 and 30, and SSW $= 240$.
   (a) Find the grand mean and SSB.
   (b) State $\nu_1$, $\nu_2$ and SST.
   (c) Find MSB, MSW and $F$.
   (d) Test at $\alpha = 0.05$, given $F_{0.05,2,15} = 3.6823$.
   (e) Find the p-value.

2. Explain why running three separate $t$ tests on the three pairs would be wrong.
   (a) How many pairwise tests are there with three groups? With five?
   (b) With three groups and $\alpha = 0.05$ each, find the probability of at least one
   false positive, assuming independence.
   (c) Repeat for five groups.

3. Complete this ANOVA table.

   | Source | SS | df | MS | $F$ |
   |---|---|---|---|---|
   | Between | 120 | 3 | ? | ? |
   | Within | 280 | 36 | ? | |
   | Total | ? | ? | | |

4. In question 3, how many groups were there and how many observations in total?

5. An $F$ statistic comes out as 0.84.
   (a) Can you reject $H_0$? Answer without a table.
   (b) What does an $F$ below 1 tell you about the two sources of variation?

6. State the three assumptions behind one-way ANOVA, and for each say how you would
   check it.

7. A researcher rejects $H_0$ in a four-group ANOVA and concludes "all four means
   differ from each other."
   (a) What is wrong?
   (b) What does rejection actually establish?
   (c) What would you do next?

8. Explain why the $F$ test is always **upper-tailed**, when the $t$ test for two
   means is usually two-tailed. Your answer should mention what large and small values
   of $F$ each imply.

### Answers to the extra problems

1. (a) Grand mean $= (22 + 26 + 30)/3 = 26.0000$, since the groups are equal in size.
   SSB $= 6(22-26)^2 + 6(26-26)^2 + 6(30-26)^2 = 96 + 0 + 96 = 192$.
   (b) $k = 3$ so $\nu_1 = 2$; $N = 18$ so $\nu_2 = 15$. SST $= 192 + 240 = 432$.
   (c) MSB $= 192/2 = 96.0000$; MSW $= 240/15 = 16.0000$; $F = 96/16 = 6.0000$.
   (d) $6.0000 > 3.6823$, so **reject $H_0$** — the three method means are not all
   equal.
   (e) $p = 0.0122$.

2. Because the error rate compounds. Each test carries its own 5% chance of a false
   positive, and the chance that *at least one* of several tests misfires is much
   larger than 5%. ANOVA asks the question once, at 5%, which is why it exists.
   (a) $\binom{3}{2} = 3$ with three groups; $\binom{5}{2} = 10$ with five.
   (b) $1 - 0.95^3 = 1 - 0.8574 = 0.1426$.
   (c) $1 - 0.95^{10} = 1 - 0.5987 = 0.4013$ — a better than two-in-five chance of
   declaring a difference that is not there, from a procedure each of whose steps was
   run "at 5%".

3. MSB $= 120/3 = 40.0000$. MSW $= 280/36 = 7.7778$.
   $F = 40/7.7778 = 5.1429$. SST $= 120 + 280 = 400$ with
   $3 + 36 = 39$ degrees of freedom. The row of totals is a free arithmetic check: if
   SSB and SSW do not add to SST, something has gone wrong upstream.

4. $\nu_1 = k - 1 = 3$, so $k = 4$ groups. $\nu_2 = N - k = 36$, so
   $N = 36 + 4 = 40$ observations — and the total degrees of freedom, 39, is
   $N - 1$ as it should be.

5. (a) **No**, and you do not need a table. $F$ is a ratio of two estimates of the same
   variance, so under $H_0$ it should hover around 1; every critical value for $F$ is
   greater than 1, so any $F$ below 1 is automatically in the non-rejection region.
   (b) That the between-group variation is *smaller* than the within-group variation —
   the group means are closer together than random assignment alone would typically
   produce. It is not evidence of anything beyond "no detectable difference", though a
   persistently tiny $F$ across studies can hint that the grouping is capturing
   something that was controlled rather than randomised.

6. **Independence** of observations, within and between groups: check from the design,
   not the data. **Normality** within each group: check with histograms or normal plots
   per group, though with reasonable group sizes the CLT makes ANOVA fairly tolerant.
   **Equal variances** across groups: compare the group standard deviations, and as a
   rough field check the largest should be no more than about twice the smallest. This
   last one matters most, because MSW pools the groups' variances and pooling is only
   meaningful if there is a common variance to pool.

7. (a) ANOVA tests a single composite null, $H_0: \mu_1 = \mu_2 = \mu_3 = \mu_4$.
   Rejecting it says that claim is false — which it would be if just one mean differed
   and the other three were identical.
   (b) Only that **not all** the means are equal. It identifies no particular pair and
   gives no ranking.
   (c) Follow up with post-hoc pairwise comparisons that adjust for multiple testing,
   or — better in most applied work — report the group means with their confidence
   intervals and let the reader see which gaps are large and which are not.

8. Because $F$ is a ratio of between-group to within-group variance, and only one
   direction is evidence against $H_0$. A **large** $F$ means the group means are
   spread out by more than within-group noise can account for, which is exactly what
   "the means differ" looks like. A **small** $F$ means the group means are unusually
   close together, which is not evidence that they differ — it is, if anything, the
   opposite. There is nothing in the lower tail worth rejecting for, so the whole
   $\alpha$ goes in the upper one. The two-tailed $t$ is different because a difference
   of means can be negative, and a negative difference is still a difference; squaring
   things into a variance ratio throws that sign away.
""", [
    ("q1a grand", 26.0000, float(np.mean([22, 26, 30]))),
    ("q1a SSB", 192, 6 * (16 + 0 + 16)),
    ("q1b SST", 432, 192 + 240),
    ("q1c MSB", 96.0000, 192 / 2),
    ("q1c MSW", 16.0000, 240 / 15),
    ("q1c F", 6.0000, float(_F16)),
    ("q1d crit", 3.6823, float(stats.f.ppf(0.95, 2, 15))),
    ("q1e p", 0.0122, float(stats.f.sf(_F16, 2, 15))),
    ("q2b survive", 0.8574, 0.95 ** 3),
    ("q2b", 0.1426, 1 - 0.95 ** 3),
    ("q2c survive", 0.5987, 0.95 ** 10),
    ("q2c", 0.4013, 1 - 0.95 ** 10),
    ("q3 MSB", 40.0000, 120 / 3),
    ("q3 MSW", 7.7778, 280 / 36),
    ("q3 F", 5.1429, (120 / 3) / (280 / 36)),
])

# ---------------------------------------------------------------- chapter 17

_phat = 108 / 300
_sep17 = float(np.sqrt(_phat * (1 - _phat) / 300))
_obs = np.array([42, 55, 61, 42], dtype=float)
_gof = float((((_obs - 50) ** 2) / 50).sum())
_tab = np.array([[30, 45, 25], [50, 35, 65]], dtype=float)
_chi17, _p17, _dof17, _exp17 = stats.chi2_contingency(_tab, correction=False)

BLOCKS["17_categorical.md"] = (r"""
## More practice

Eight more. Watch the degrees of freedom in questions 2 and 3 — they are the single
commonest slip in this chapter, and a correct $\chi^2$ compared against the wrong row
of the table scores nothing.

1. In a survey of 300 customers, 108 say they would recommend the product.
   (a) Find $\hat{p}$ and its standard error.
   (b) Build a 95% confidence interval.
   (c) Check the condition for the approximation.
   (d) Why is the critical value $z$ and not $t$, when the standard error was
   estimated from the data?

2. A firm expects its four regional offices to handle equal shares of enquiries. Out
   of 200 enquiries the counts are 42, 55, 61 and 42.
   (a) State the hypotheses and the expected counts.
   (b) Compute $\chi^2$ and state the degrees of freedom.
   (c) Test at $\alpha = 0.05$, given $\chi^2_{0.05,3} = 7.8147$.
   (d) Find the p-value.

3. Two hundred and fifty applicants are classified by outcome and by which of three
   channels they applied through:

   | | A | B | C | Total |
   |---|---|---|---|---|
   | **Accepted** | 30 | 45 | 25 | 100 |
   | **Rejected** | 50 | 35 | 65 | 150 |
   | **Total** | 80 | 80 | 90 | 250 |

   (a) Compute all six expected counts.
   (b) Compute $\chi^2$ and state the degrees of freedom.
   (c) Test at $\alpha = 0.05$, given $\chi^2_{0.05,2} = 5.9915$.
   (d) State the conclusion in words.

4. State the degrees of freedom for a test of independence on a table that is
   (a) $2 \times 2$, (b) $4 \times 5$, (c) $2 \times 6$, (d) $3 \times 3$. Then say why
   a $2 \times 2$ table has 1 and not 3.

5. A researcher's $2 \times 2$ table has one cell with an observed count of 2 and an
   expected count of 8.
   (a) Is the condition satisfied?
   (b) Which of the two numbers does the condition apply to, and why does that make
   sense?

6. A student converts a table of counts into row percentages, then feeds the
   percentages into $\chi^2 = \sum (O-E)^2/E$.
   (a) What goes wrong?
   (b) Why does the statistic depend on the counts rather than only the proportions?

7. Explain why the chi-squared test is always upper-tailed, and what an unusually
   *small* $\chi^2$ would suggest.

8. A test of independence between an applicant's channel and their outcome rejects
   $H_0$. A manager concludes "channel C is causing rejections."
   (a) What does the test establish?
   (b) Give two explanations consistent with the result that are not causal.

### Answers to the extra problems

1. (a) $\hat{p} = 108/300 = 0.3600$ and
   SE $= \sqrt{0.36(0.64)/300} = \sqrt{0.000768} = 0.0277$.
   (b) $0.36 \pm 1.96(0.0277) = 0.36 \pm 0.0543 = (0.3057,\ 0.4143)$.
   (c) $n\hat{p} = 108$ and $n(1-\hat{p}) = 192$, both far above 5. Valid.
   (d) Because the $t$ distribution arises from a very specific construction — a
   standard normal over the square root of an independent scaled chi-squared, which is
   what you get when $s$ and $\bar{x}$ are computed from normal data. For a proportion
   there is no separate $s$: the standard error is a function of $\hat{p}$ itself, so
   the ratio is not a $t$ variable. "Estimated denominator means $t$" is a useful
   habit and not a rule, and this is the counterexample.

2. (a) $H_0$: the four offices handle equal shares, so each expected count is
   $200/4 = 50$. $H_a$: the shares are not all equal.
   (b) $\chi^2 = \dfrac{64 + 25 + 121 + 64}{50} = \dfrac{274}{50} = 5.4800$ with
   $\nu = k - 1 = 3$.
   (c) $5.4800 < 7.8147$, so **do not reject** — the observed split is consistent with
   equal shares.
   (d) $p = 0.1398$.

3. (a) Each is row total times column total over 250:
   Accepted — $32.0000$, $32.0000$, $36.0000$; Rejected — $48.0000$, $48.0000$,
   $54.0000$. They reproduce the margins, which is the check.
   (b) $\chi^2 = \dfrac{4}{32} + \dfrac{169}{32} + \dfrac{121}{36} + \dfrac{4}{48}
   + \dfrac{169}{48} + \dfrac{121}{54} = 14.6128$ with
   $\nu = (2-1)(3-1) = 2$.
   (c) $14.6128 > 5.9915$, so **reject $H_0$** ($p = 0.0007$).
   (d) Outcome and channel are not independent. Channel B's applicants are accepted far
   more often than its share of applications would suggest — 45 accepted against an
   expected 32 — while channel C's are accepted far less, 25 against an expected 36.

4. (a) 1. (b) 12. (c) 5. (d) 4. A $2 \times 2$ table has 1 rather than 3 because the
   row and column totals are fixed by the data itself, not supplied from outside: once
   you know the margins and any **one** cell, the other three are forced by
   subtraction. Only one number in the table is free to vary, so there is one degree of
   freedom. Counting four cells and subtracting one is the wrong arithmetic and happens
   to give 3.

5. (a) **Yes.** The condition is that every *expected* count be at least 5, and 8
   clears it.
   (b) It applies to the **expected** count. That makes sense because $E$ is the
   denominator in each term of $\chi^2 = \sum (O-E)^2/E$ — a tiny expectation makes the
   term explode and destroys the chi-squared approximation, regardless of what was
   observed. A cell can observe zero and be perfectly well behaved provided enough was
   expected there.

6. (a) The test statistic changes, usually becoming far too small. Converting 60 out of
   100 into "60%" and 600 out of 1,000 into "60%" makes two completely different bodies
   of evidence look identical, and $\chi^2$ computed on percentages effectively asserts
   $n = 100$ for every row.
   (b) Because the strength of evidence depends on how much data there is, not only on
   the pattern. A 10-point gap in proportions from 40 observations is noise; the same
   gap from 4,000 is decisive. Proportions describe the pattern, counts carry the
   sample size, and $\chi^2$ needs both — which is exactly why it is built from counts.

7. The statistic is a sum of squared discrepancies, so it is zero when observation
   matches expectation exactly and grows as they diverge — in either direction, since
   the squaring removes the sign. Only *large* values are evidence against $H_0$, so
   all of $\alpha$ goes in the upper tail. An unusually **small** $\chi^2$ means the
   data fit the expectation more closely than chance would normally allow, which is not
   evidence for $H_0$ so much as grounds for suspecting the data were not generated the
   way they were described — the classic reason to be sceptical of results that are
   *too* good.

8. (a) Only **association**: the distribution of outcomes differs across channels by
   more than chance would explain. It identifies no cause and no direction.
   (b) (i) **Selection** — stronger applicants may choose channel B, so the channel is
   marking a difference in applicants rather than creating one. (ii) **A confounder** —
   channels may differ in what roles they advertise, in which case both channel and
   outcome are driven by the type of position. A third: the channels may be used at
   different times of year, with different acceptance rates for unrelated reasons.
""", [
    ("q1a phat", 0.3600, float(_phat)),
    ("q1a inner", 0.000768, float(_phat * (1 - _phat) / 300)),
    ("q1a SE", 0.0277, _sep17),
    ("q1b ME", 0.0543, float(1.96 * _sep17)),
    ("q1b lo", 0.3057, float(_phat - 1.96 * _sep17)),
    ("q1b hi", 0.4143, float(_phat + 1.96 * _sep17)),
    ("q2b chi2", 5.4800, _gof),
    ("q2c crit", 7.8147, float(stats.chi2.ppf(0.95, 3))),
    ("q2d p", 0.1398, float(stats.chi2.sf(_gof, 3))),
    ("q3a e11", 32.0000, float(_exp17[0, 0])),
    ("q3a e13", 36.0000, float(_exp17[0, 2])),
    ("q3a e21", 48.0000, float(_exp17[1, 0])),
    ("q3a e23", 54.0000, float(_exp17[1, 2])),
    ("q3b chi2", 14.6128, float(_chi17)),
    ("q3c crit", 5.9915, float(stats.chi2.ppf(0.95, 2))),
    ("q3c p", 0.0007, float(_p17)),
])

# ---------------------------------------------------------------- chapter 18

_x18 = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
_y18 = np.array([14, 21, 18, 23, 27, 26, 35, 36], dtype=float)
_fit = stats.linregress(_x18, _y18)
_sse18 = float(((_y18 - (_fit.intercept + _fit.slope * _x18)) ** 2).sum())
_sst18 = float(((_y18 - _y18.mean()) ** 2).sum())

BLOCKS["18_regression.md"] = (r"""
## More practice

Eight more. Question 1 is a full fit by hand — slow, and worth doing once, because
every quantity in a regression output is built from the two sums you compute there.

1. Advertising spend $x$ (thousands) and sales $y$ (thousands of units):

   | $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
   |---|---|---|---|---|---|---|---|---|
   | $y$ | 14 | 21 | 18 | 23 | 27 | 26 | 35 | 36 |

   (a) Find $\bar{x}$, $\bar{y}$, $\sum(x-\bar{x})(y-\bar{y})$ and
   $\sum(x-\bar{x})^2$.
   (b) Find $b_1$ and $b_0$, and write the fitted line.
   (c) Interpret the slope in the units of the problem.
   (d) Verify that the line passes through $(\bar{x}, \bar{y})$.

2. For the same data:
   (a) Find SST, SSE and SSR.
   (b) Find $R^2$ and interpret it.
   (c) Find $r$, and say how you know its sign.

3. Still with the same data, SE$(b_1) = 0.3883$.
   (a) Find $t$ and state $\nu$.
   (b) Test $H_0: \beta_1 = 0$ at $\alpha = 0.05$, given $t_{0.025,6} = 2.4469$.
   (c) State what rejection means in the language of the problem.

4. Using the fitted line from question 1:
   (a) Predict sales at $x = 5$.
   (b) Predict sales at $x = 20$.
   (c) Which prediction would you report, and why?

5. A different regression gives SST $= 800$ and SSE $= 200$.
   (a) Find SSR and $R^2$.
   (b) Find $|r|$.
   (c) Can you determine the sign of $r$ from these figures? Explain.

6. A fitted line is $\hat{y} = 80 - 2.5x$, from data where $x$ ran from 10 to 40.
   (a) Interpret the slope.
   (b) Interpret the intercept, or explain why you would not.
   (c) What is $\hat{y}$ at $x = 32$, and is that a defensible prediction?

7. Two residual plots are described. In the first, the residuals form a shapeless band
   around zero. In the second, they fan out steadily as $\hat{y}$ increases.
   (a) Which assumption does the second violate?
   (b) Would $R^2$ have revealed it?
   (c) Why is the plot not optional?

8. A paper reports a slope of 1.4 on years of schooling in a wage regression, with
   $p < 0.001$ and $R^2 = 0.18$.
   (a) Does the small p-value establish that schooling raises wages?
   (b) What does $R^2 = 0.18$ tell you?
   (c) Are (a) and (b) in tension? Explain.

### Answers to the extra problems

1. (a) $\bar{x} = 4.5000$ and $\bar{y} = 25.0000$. The $x$ deviations are
   $-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5$ and the $y$ deviations are
   $-11, -4, -7, -2, 2, 1, 10, 11$. The cross-products sum to $126$ and the squared $x$
   deviations sum to $42$.
   (b) $b_1 = 126/42 = 3.0000$ and $b_0 = 25 - 3(4.5) = 11.5000$, so
   $\hat{y} = 11.5 + 3x$.
   (c) Each additional **thousand dollars** of advertising is associated with about
   **3,000 more units** sold. "Associated with", not "causes" — the data is
   observational.
   (d) $11.5 + 3(4.5) = 25.0000 = \bar{y}$. The least-squares line always passes
   through the point of means, which is a free check on $b_0$.

2. (a) SST $=$ the squared $y$ deviations $= 416$. SSE $= 38.0000$. SSR $= 416 - 38 =
   378$ — or, equivalently, $b_1^2 \sum(x-\bar{x})^2 = 9(42) = 378$.
   (b) $R^2 = 378/416 = 0.9087$. The line accounts for **90.9%** of the variation in
   sales.
   (c) $r = \sqrt{0.9087} = 0.9532$, **positive**, because the slope is positive.
   $R^2$ on its own cannot give you the sign — the square root is taken with the sign
   of $b_1$.

3. (a) $t = 3.0/0.3883 = 7.7256$ with $\nu = n - 2 = 6$.
   (b) $7.7256 > 2.4469$, so **reject $H_0$**. ($p = 0.0002$.)
   (c) The relationship between advertising and sales is not plausibly zero: a slope
   this far from zero would arise by chance in well under one study in a thousand if
   advertising had no association with sales at all. It does **not** establish that
   advertising causes sales, and it says nothing about whether a slope of 3 is
   commercially worth having — that depends on the cost of the advertising.

4. (a) $11.5 + 3(5) = 26.5000$ thousand units.
   (b) $11.5 + 3(20) = 71.5000$ thousand units.
   (c) Only **(a)**. $x = 5$ sits in the middle of the observed range of 1 to 8;
   $x = 20$ is two and a half times the largest value ever seen. The straight line is
   evidence only across the range where there is data, and extrapolating assumes
   linearity continues into territory that was never tested. Advertising returns in
   particular almost certainly flatten, so 71.5 is not a cautious estimate — it is a
   guess dressed as arithmetic.

5. (a) SSR $= 800 - 200 = 600$, so $R^2 = 600/800 = 0.7500$.
   (b) $|r| = \sqrt{0.75} = 0.8660$.
   (c) **No.** $R^2$ is a squared quantity and discards the sign. You need the sign of
   $b_1$ or of the covariance; a relationship explaining 75% of the variation could be
   strongly rising or strongly falling.

6. (a) Each one-unit increase in $x$ is associated with a decrease of **2.5** in
   $\hat{y}$.
   (b) **I would not interpret it.** $x = 0$ lies well outside the observed range of 10
   to 40, so 80 is the fitted value at a point the data says nothing about. Report it
   because the line requires it; interpret it only when $x = 0$ is genuinely in range
   and meaningful.
   (c) $80 - 2.5(32) = 0.0000$. That is **inside** the range of $x$, so the prediction
   is defensible as arithmetic — but a predicted value of exactly zero at the upper end
   of the data is worth a second look, since it suggests the relationship may bend
   rather than continuing straight to zero and beyond. The residual plot would tell
   you.

7. (a) **Constant variance** of the residuals. A fan shape means the spread of the
   errors grows with the fitted value, so the single $s$ that the standard errors are
   built from describes neither end of the data.
   (b) **No.** $R^2$ measures how much variation the line explains and is completely
   silent on whether the residuals are well behaved. A fanning pattern can sit under a
   high $R^2$, and the coefficient estimates will be fine while their standard errors —
   and therefore every p-value and interval — are wrong.
   (c) Because the two most consequential failures, non-linearity and
   non-constant variance, are both invisible in the output table and both obvious in
   the plot. It takes one line of code and it is the only part of the diagnostics that
   cannot be skipped.

8. (a) **No.** It establishes that the slope is very unlikely to be zero. Schooling may
   raise wages; higher-ability people may acquire more of both; family background may
   drive both. Identifying the causal effect requires a design, not a smaller p-value,
   and this is the problem the rest of econometrics exists to address.
   (b) That schooling accounts for 18% of the variation in wages, leaving 82% to
   everything else — experience, occupation, location, luck. That is a perfectly
   ordinary figure for a cross-section of individuals.
   (c) **Not at all**, and the pair is worth understanding together. $p < 0.001$ is a
   statement about whether the slope is distinguishable from zero, which with a large
   sample it easily can be; $R^2 = 0.18$ is a statement about how much of the outcome
   the model predicts. A variable can matter reliably and still explain only a modest
   share of the variation, because the thing being explained has many causes. Confusing
   the two is how a well-identified small effect gets dismissed and a large $R^2$ from
   an uninformative model gets believed.
""", [
    ("q1a xbar", 4.5000, float(_x18.mean())),
    ("q1a ybar", 25.0000, float(_y18.mean())),
    ("q1a Sxy", 126, float(((_x18 - _x18.mean()) * (_y18 - _y18.mean())).sum())),
    ("q1a Sxx", 42, float(((_x18 - _x18.mean()) ** 2).sum())),
    ("q1b b1", 3.0000, float(_fit.slope)),
    ("q1b b0", 11.5000, float(_fit.intercept)),
    ("q1d check", 25.0000, float(_fit.intercept + _fit.slope * 4.5)),
    ("q2a SST", 416, _sst18),
    ("q2a SSE", 38.0000, _sse18),
    ("q2a SSR", 378, _sst18 - _sse18),
    ("q2b R2", 0.9087, float(_fit.rvalue ** 2)),
    ("q2c r", 0.9532, float(_fit.rvalue)),
    ("q3 SE", 0.3883, float(_fit.stderr)),
    ("q3a t", 7.7256, float(_fit.slope / _fit.stderr)),
    ("q3b crit", 2.4469, float(stats.t.ppf(0.975, 6))),
    ("q3b p", 0.0002, float(_fit.pvalue)),
    ("q4a", 26.5000, float(_fit.intercept + _fit.slope * 5)),
    ("q4b", 71.5000, float(_fit.intercept + _fit.slope * 20)),
    ("q5a R2", 0.7500, 600 / 800),
    ("q5b r", 0.8660, float(np.sqrt(0.75))),
    ("q6c", 0.0000, 80 - 2.5 * 32),
])
