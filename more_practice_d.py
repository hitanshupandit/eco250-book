"""Extra practice for chapter 14 -- hypothesis testing.

Twenty-five problems, the largest set in the book. Hypothesis testing is where
the marks are lost: not in the arithmetic, which is one subtraction and one
division, but in the set-up, the tail, and the sentence at the end.
"""

import numpy as np
from scipy import stats

BLOCKS = {}

_t35 = float(stats.t.ppf(0.975, 35))
_t15_90 = float(stats.t.ppf(0.95, 15))
_t15_95 = float(stats.t.ppf(0.975, 15))
_t48 = float(stats.t.ppf(0.975, 48))
_crit_pow = 100 + stats.norm.ppf(0.95) * 3
_power25 = float(stats.norm.sf((_crit_pow - 106) / 3))
_crit_pow100 = 100 + stats.norm.ppf(0.95) * 1.5
_power100 = float(stats.norm.sf((_crit_pow100 - 106) / 1.5))

BLOCKS["14_hypothesis_testing.md"] = (r"""
## More practice

Twenty-five more — the biggest set in the book, because this is the chapter the
exam leans on hardest and because almost none of the marks are in the arithmetic.
Questions 1 to 4 are set-up only, with no numbers at all; do them first, because a
test with the wrong $H_a$ is worth nothing however neatly the rest is computed.

1. For each, state $H_0$ and $H_a$, and name the tail.
   (a) A manufacturer claims its cereal boxes average 500 g; an inspector suspects
   they are underfilled.
   (b) A training programme is meant to change productivity, and management wants to
   know whether it has.
   (c) A supplier guarantees that mean impurity is at most 3 parts per million; you
   are the buyer.
   (d) Historically mean class size was 18; the dean asks whether it has changed.
   (e) A drug company claims a mean recovery time below 7 days; a regulator checks.
   (f) A machine is calibrated to 250 ml and drifts in either direction.
   (g) An economist believes a minimum wage rise raised mean hours worked.
   (h) A bank claims mean wait time is under 4 minutes; a journalist investigates.

2. In each of these set-ups, something is wrong. Identify it.
   (a) $H_0: \bar{x} = 50$ against $H_a: \bar{x} \neq 50$.
   (b) $H_0: \mu > 100$ against $H_a: \mu < 100$.
   (c) $H_0: \mu = 20$ against $H_a: \mu = 25$.
   (d) "We will test whether $\mu > 30$, and if the sample mean comes out below 30 we
   will test whether $\mu < 30$ instead."

3. Why does the equals sign always go in $H_0$? Answer by saying what would go wrong
   in the calculation if it did not.

4. A researcher collects the data, sees that $\bar{x}$ is above $\mu_0$, and then
   decides to run a one-tailed test in the upper direction.
   (a) What is the stated significance level?
   (b) What is the actual one?
   (c) Why does this matter more than it sounds like it should?

5. A machine should fill to 500 g. A sample of $n = 64$ gives $\bar{x} = 497.5$, and
   $\sigma = 8$ is known from long experience.
   (a) State the hypotheses.
   (b) Find the standard error and the test statistic.
   (c) Find the two-tailed p-value.
   (d) Conclude at $\alpha = 0.05$ and at $\alpha = 0.01$, and comment on the pair of
   answers.

6. A tutoring programme claims to raise scores above the historical mean of 100. A
   sample of $n = 16$ students gives $\bar{x} = 104$ and $s = 12$.
   (a) State the hypotheses and the tail.
   (b) Find the standard error, the test statistic and the degrees of freedom.
   (c) Compare with the critical value and conclude at $\alpha = 0.05$.
   (d) Find the p-value.

7. Repeat question 6 as a **two-tailed** test.
   (a) What is the new critical value, and what is the new p-value?
   (b) The data have not changed. Explain why the conclusion could, in principle,
   change.

8. A bottling line is set to 500 ml. A sample of $n = 49$ gives $\bar{x} = 498.2$ and
   $s = 4.9$.
   (a) Test at $\alpha = 0.05$, two-tailed, reporting $t$, $\nu$ and the critical
   value.
   (b) Find the p-value.
   (c) State the conclusion in a sentence a plant manager would act on.

9. For the commute data of Chapter 13 — $n = 36$, $\bar{x} = 28.4$, $s = 6$ — test
   $H_0: \mu = 30$ against a two-sided alternative at $\alpha = 0.05$.
   (a) Find $t$ and conclude.
   (b) The 95% confidence interval is $(26.3699,\ 30.4301)$. Confirm it agrees, and
   state the general rule.

10. Using the same commute data, test $H_0: \mu = 31$ instead.
    (a) Find $t$ and conclude.
    (b) Does this agree with the interval? Explain how one interval answers infinitely
    many tests at once.

11. Which of these is the correct definition of a p-value?
    (a) The probability that $H_0$ is true.
    (b) The probability that $H_0$ is false.
    (c) The probability of observing data at least as extreme as this, if $H_0$ is
    true.
    (d) The probability of making a Type I error.
    (e) The probability the result is due to chance.
    For each wrong one, say specifically what is wrong with it.

12. A test returns $p = 0.03$.
    (a) Conclude at $\alpha = 0.05$.
    (b) Conclude at $\alpha = 0.01$.
    (c) Explain why the same data give two different conclusions without either being
    a mistake.

13. In a quality-control setting, $H_0$ is "the batch meets specification".
    (a) Describe the Type I error in plain words and say who it costs.
    (b) Describe the Type II error and say who it costs.
    (c) Which would you rather make if the product is a brake component? A packet of
    crisps?

14. $H_0: \mu = 100$ is tested against $H_a: \mu > 100$ at $\alpha = 0.05$ with
    $n = 25$ and $\sigma = 15$.
    (a) Find the critical value of $\bar{X}$ — the value above which you reject.
    (b) Suppose the truth is $\mu = 106$. Find the power of the test.
    (c) Find $\beta$.

15. Repeat 14(b) with $n = 100$.
    (a) What is the power now?
    (b) State the general relationship between $n$ and power, and why it matters when
    a study reports "no significant effect".

16. Explain the trade-off between $\alpha$ and $\beta$. Why can you not simply set
    $\alpha = 0.001$ and be safe?

17. A sample of $n = 5{,}000$ gives $\bar{x} = 100.3$ where $H_0: \mu = 100$, with
    $\sigma = 5$.
    (a) Find $z$ and the two-tailed p-value.
    (b) Now find the same for $n = 25$ with the identical $\bar{x}$.
    (c) The effect is three-tenths of a unit in both cases. What should be reported
    alongside the p-value, and why?

18. A research group runs 20 independent tests at $\alpha = 0.05$, on data where every
    null hypothesis is in fact true.
    (a) How many "significant" results do they expect?
    (b) Find the probability they get at least one.
    (c) What does this imply about a paper that reports the one significant result out
    of twenty tests run?

19. Each of these sentences is wrong. Rewrite it.
    (a) "We accept the null hypothesis."
    (b) "$p = 0.20$, so there is no effect."
    (c) "$p = 0.001$, so the effect is large."
    (d) "The result is significant, so it is important."
    (e) "We reject $H_0$, so $H_a$ is true."

20. A test does not reject $H_0$. List three distinct reasons this could happen, only
    one of which is "$H_0$ is true".

21. A test statistic is $z = 1.85$.
    (a) Find the one-tailed p-value.
    (b) Find the two-tailed p-value.
    (c) At $\alpha = 0.05$, which tail choice changes the conclusion?

22. A student computes $t = -2.45$ with $\nu = 20$ for a left-tailed test, looks up
    $t_{0.05,20} = 1.7247$, and writes "$-2.45 < 1.7247$, so do not reject."
    Identify the error and give the correct conclusion.

23. List the assumptions behind the one-sample $t$ test, and for each say how you
    would check it and what you would do if it failed.

24. Write out the eight steps of a hypothesis test from memory, then use them to test
    the following: a college claims its graduates earn a mean starting salary of
    \$52,000. A sample of 36 graduates gives $\bar{x} = \$49{,}800$ with
    $s = \$7{,}200$. Test at $\alpha = 0.05$ against a two-sided alternative.

25. Two economists analyse the same dataset. One reports "$p = 0.049$, significant";
    the other reports "$p = 0.051$, not significant". Write a paragraph on what, if
    anything, separates these two findings.

### Answers to the extra problems

1. (a) $H_0: \mu = 500$, $H_a: \mu < 500$ — **left**. The inspector needs evidence of
   underfilling. (b) $H_0: \mu = \mu_0$, $H_a: \mu \neq \mu_0$ — **two-tailed**;
   "whether it has changed" names no direction. (c) $H_0: \mu = 3$,
   $H_a: \mu > 3$ — **right**; the buyer needs evidence the guarantee is breached.
   (d) $H_0: \mu = 18$, $H_a: \mu \neq 18$ — **two-tailed**. (e) $H_0: \mu = 7$,
   $H_a: \mu < 7$ — **left**; the regulator is checking the company's claim, and the
   claim is the thing requiring evidence. (f) $H_0: \mu = 250$,
   $H_a: \mu \neq 250$ — **two-tailed**; drift either way is a fault.
   (g) $H_0: \mu = \mu_0$, $H_a: \mu > \mu_0$ — **right**. (h) $H_0: \mu = 4$,
   $H_a: \mu < 4$ — **left**.

2. (a) The hypotheses are about $\bar{x}$, a **statistic**. Hypotheses are always
   about parameters; you know $\bar{x}$ exactly, so there is nothing to test.
   (b) $H_0$ has **no equals sign**, so there is no single value from which to compute
   a sampling distribution. Write $H_0: \mu = 100$ against $H_a: \mu < 100$.
   (c) The two hypotheses are **not exhaustive** — they say nothing about $\mu = 22$.
   $H_a$ must cover everything $H_0$ does not.
   (d) The alternative is being chosen **after seeing the data**, which makes the
   stated significance level a fiction. See question 4.

3. Because the whole calculation is conditional on $H_0$ being true, and you cannot
   compute a sampling distribution from a range of values. "If $\mu = 500$" pins down
   exactly one distribution for $\bar{X}$, from which a p-value follows; "if
   $\mu > 500$" pins down none, because the answer would differ for $\mu = 501$ and
   $\mu = 900$. $H_0$ has to be a specific claim precisely so that it can be
   contradicted by specific evidence.

4. (a) Whatever they say — typically 0.05.
   (b) Effectively **0.10**, because they would have run the test in the other
   direction had the data gone the other way, so there were two chances to reject at
   5% each.
   (c) Because it is invisible in the write-up. The reported test looks like a
   perfectly ordinary one-tailed test at 5%, and nothing in the published numbers
   reveals that the direction was chosen after the fact. The discipline of committing
   to $H_a$ before collecting data is the only thing that makes the stated error rate
   mean anything.

5. (a) $H_0: \mu = 500$ against $H_a: \mu \neq 500$.
   (b) SE $= 8/\sqrt{64} = 1.0000$, so $z = (497.5 - 500)/1.0 = -2.5000$. Note $z$,
   not $t$ — $\sigma$ is known.
   (c) $p = 2 \times \mathrm{P}(Z > 2.5) = 2(0.0062) = 0.0124$.
   (d) At $\alpha = 0.05$: $0.0124 < 0.05$, so **reject**. At $\alpha = 0.01$:
   $0.0124 > 0.01$, so **do not reject**. The data are the same; what changed is how
   much Type I error you were willing to tolerate. A result sitting between two
   conventional thresholds is exactly the situation in which reporting the p-value
   itself, rather than a verdict, earns its keep.

6. (a) $H_0: \mu = 100$ against $H_a: \mu > 100$ — right tail, because the programme
   claims to *raise* scores.
   (b) SE $= 12/\sqrt{16} = 3.0000$, so $t = (104-100)/3 = 1.3333$ with $\nu = 15$.
   (c) $t_{0.05,15} = 1.7531$. Since $1.3333 < 1.7531$, **do not reject**.
   (d) $p = 0.1012$ — about a one-in-ten chance of a sample mean this high or higher
   if the programme does nothing.

7. (a) $t_{0.025,15} = 2.1314$ and $p = 0.2024$, double the one-tailed value.
   (b) Because the two tests put the 5% allowance in different places. A one-tailed
   test concentrates all of it in the direction you predicted, making it easier to
   reject *in that direction* and impossible to reject in the other. Here the
   conclusion happens to be the same, but a statistic of, say, 1.80 would have been
   significant one-tailed and not two-tailed — which is why the tail must be chosen
   from the question, before the data, and never to secure a result.

8. (a) SE $= 4.9/\sqrt{49} = 0.7000$, so $t = (498.2 - 500)/0.7 = -2.5714$ with
   $\nu = 48$. The critical value is $t_{0.025,48} = 2.0106$, and
   $|-2.5714| > 2.0106$, so **reject $H_0$**.
   (b) $p = 0.0133$.
   (c) "The line is filling below 500 ml. A mean of 498.2 ml across 49 bottles is far
   enough below target that chance alone would produce it only about 1.3% of the time,
   so the machine should be recalibrated." Note that the actionable number is the
   1.8 ml shortfall, not the $t$ statistic.

9. (a) SE $= 6/\sqrt{36} = 1.0000$, so $t = (28.4 - 30)/1.0 = -1.6000$ with
   $\nu = 35$. The critical value is $t_{0.025,35} = 2.0301$, and
   $1.6 < 2.0301$, so **do not reject**. ($p = 0.1186$.)
   (b) 30 lies **inside** $(26.3699,\ 30.4301)$, so the interval does not reject it
   either. The general rule: a two-tailed test of $H_0: \mu = \mu_0$ at level
   $\alpha$ rejects precisely when $\mu_0$ falls outside the $100(1-\alpha)\%$
   confidence interval. They are the same statement rearranged.

10. (a) $t = (28.4 - 31)/1.0 = -2.6000$, and $2.6 > 2.0301$, so **reject**.
    (b) Yes — 31 is outside the interval. The interval is the complete set of null
    values that would *not* be rejected at the 5% level, so one interval answers the
    test for every possible $\mu_0$ at once. This is the strongest practical argument
    for reporting intervals rather than tests: a test answers one question, an interval
    answers all of them and shows you the effect size as well.

11. **(c) is correct.**
    (a) and (b) are wrong because the p-value is computed *assuming* $H_0$ is true —
    it is a probability about the data, not about the hypothesis. Classical statistics
    assigns no probability to a hypothesis at all.
    (d) is wrong because the Type I error rate is $\alpha$, which you choose in advance;
    the p-value is a property of the data you got.
    (e) is wrong in a subtler way: "due to chance" sounds like (a) in disguise. The
    p-value tells you how probable *this data* is under chance, not how probable chance
    is given this data — the same inversion as the prosecutor's fallacy in Chapter 6.

12. (a) $0.03 < 0.05$, so **reject**.
    (b) $0.03 > 0.01$, so **do not reject**.
    (c) Because $\alpha$ is not a property of the data — it is a decision about how
    much Type I error is acceptable, taken before the data arrive and on grounds
    outside the statistics. At the 1% level you have demanded stronger evidence, and
    this evidence does not meet that bar while meeting the looser one. Neither verdict
    is wrong; they are answers to different questions.

13. (a) **Type I**: rejecting a batch that was in fact fine. It costs the *producer* —
    good output is scrapped or reworked.
    (b) **Type II**: passing a batch that was defective. It costs the *customer*, and
    ultimately the producer's reputation.
    (c) For a **brake component**, a Type I error is vastly preferable: throw away good
    parts rather than ship bad ones, so set $\alpha$ high. For **crisps**, the
    asymmetry reverses — a slightly underweight packet is a minor matter against the
    cost of destroying good production, so a lower $\alpha$ is sensible. The choice of
    $\alpha$ is an economic decision, not a statistical one, and 0.05 is a convention
    rather than an answer.

14. (a) SE $= 15/\sqrt{25} = 3.0000$ and $z_{0.05} = 1.6449$, so you reject when
    $\bar{x} > 100 + 1.6449(3) = 104.9346$.
    (b) If $\mu = 106$, then
    $z = (104.9346 - 106)/3 = -0.3551$, so the power is
    $\mathrm{P}(Z > -0.3551) = 0.6387$.
    (c) $\beta = 1 - 0.6387 = 0.3613$ — a 36% chance of missing a real six-unit
    effect.

15. (a) SE $= 1.5000$, so the cut-off is $100 + 1.6449(1.5) = 102.4673$ and
    $z = (102.4673 - 106)/1.5 = -2.3551$, giving power $= 0.9907$.
    (b) Power rises with $n$, because the sampling distributions under $H_0$ and under
    the truth pull apart as the standard error shrinks. This is why "no significant
    effect" is uninterpretable without the sample size: at $n = 25$ this test misses a
    real effect more than a third of the time, so a non-rejection there is weak
    evidence of anything. The honest report of a null result always includes either the
    power or, better, the confidence interval showing which effect sizes remain
    consistent with the data.

16. For a fixed $n$, shrinking $\alpha$ moves the critical value further out, which
    makes rejection harder — and that reduces the chance of rejecting a true $H_0$
    (good) while also reducing the chance of rejecting a false one (bad). So $\beta$
    rises as $\alpha$ falls. You cannot simply set $\alpha = 0.001$ because you would
    then almost never reject anything, including every genuine effect in the data; a
    test with a Type I error rate of 0.001 and a Type II error rate of 0.8 is not a
    careful test, it is a broken one. The only way to reduce both at once is to
    increase $n$, which is why sample size is the real lever and $\alpha$ is only a
    dial for choosing which error you fear more.

17. (a) SE $= 5/\sqrt{5000} = 0.0707$, so $z = 0.3/0.0707 = 4.2426$ and
    $p < 0.0001$.
    (b) SE $= 5/\sqrt{25} = 1.0000$, so $z = 0.3000$ and $p = 0.7642$.
    (c) The **confidence interval**, or equivalently the effect size with its
    uncertainty. A difference of 0.3 units may be economically meaningless, and with
    5,000 observations the test detects it with overwhelming confidence — the p-value
    is answering "is the effect exactly zero?", which is almost never the interesting
    question. The interval answers "how big is it, and how sure are we?", which is.

18. (a) $20 \times 0.05 = 1$.
    (b) $1 - 0.95^{20} = 1 - 0.3585 = 0.6415$ — about a 64% chance.
    (c) That the single significant result is roughly what you would expect from
    nothing at all. A p-value of 0.04 means something when one test was run and very
    little when it is the best of twenty, because the 5% applies per test and not per
    paper. The remedies are to report every test run, to adjust the threshold, or to
    treat the finding as a hypothesis for a fresh dataset rather than as a result.

19. (a) "We **fail to reject** the null hypothesis." You never gather evidence *for*
    $H_0$; you only fail to find enough against it.
    (b) "$p = 0.20$, so there is **insufficient evidence of an effect**" — ideally with
    an interval showing what sizes remain plausible. Absence of evidence is not
    evidence of absence.
    (c) "$p = 0.001$, so the effect is **very unlikely to be zero**." A small p-value
    reflects the signal relative to the noise, and with a large $n$ a tiny effect
    produces a tiny p. Size is a separate question, answered by the estimate.
    (d) "The result is **statistically** significant." Importance is a judgement about
    magnitude and context, which no p-value contains.
    (e) "We reject $H_0$, so the data are **inconsistent with** $H_0$ at this level."
    Rejection is a decision under an error rate you have chosen to accept, not a proof;
    one test in twenty rejects a true null by design.

20. (i) **$H_0$ is true**, or close enough to true that the data cannot tell.
    (ii) **$n$ is too small** — the effect is real but the test lacks the power to
    detect it, as in question 15. (iii) **The data are too noisy**, with $s$ inflated
    by measurement error or an unmodelled source of variation, so a real signal is
    swamped. A fourth, worth noting: the test was the wrong one — a paired design
    analysed as independent, for example, which throws away the very structure that
    would have revealed the effect.

21. (a) $\mathrm{P}(Z > 1.85) = 0.0322$.
    (b) $2(0.0322) = 0.0643$.
    (c) The **one-tailed** test rejects at 5% ($0.0322 < 0.05$) while the two-tailed
    test does not ($0.0643 > 0.05$). This is exactly why the tail cannot be chosen
    after the fact — the same statistic yields opposite verdicts depending on a
    decision that must be made from the research question alone.

22. The student has compared a negative statistic with a positive critical value. For
    a **left-tailed** test the rejection region is $t < -t_{0.05,20} = -1.7247$, and
    $-2.45 < -1.7247$, so the correct conclusion is to **reject $H_0$**. The safe
    habit is to compare magnitudes — $|{-2.45}| = 2.45 > 1.7247$ — after confirming
    that the statistic falls on the side $H_a$ predicted. Here it does: a negative $t$
    is what a left-tailed alternative expects.

23. **Random sampling / independence.** Check it from the study design, not the data —
    no diagnostic reveals a clustered sample. If it fails, the standard error is wrong,
    usually too small, and the fix is a method that accounts for the structure.
    **Normality of the population, or a large enough $n$.** Check with a histogram or
    a normal plot of the sample. If it fails and $n$ is small, use a distribution-free
    test; if $n$ is large, the CLT covers you and nothing needs doing.
    **The data are quantitative and the parameter is a mean.** Check that the question
    is actually about a mean — for counts in categories you want Chapter 17 instead.
    **No outliers driving the result.** Check by inspecting the extremes and refitting
    without them. If a single observation reverses the verdict, say so in the write-up
    rather than choosing whichever version you prefer.

24. The steps: (1) state $H_0$ and $H_a$; (2) choose $\alpha$; (3) identify the test
    statistic and its distribution; (4) state the decision rule; (5) compute the
    standard error; (6) compute the statistic; (7) find the p-value or compare with the
    critical value; (8) state the conclusion in the language of the problem.
    Applying them: (1) $H_0: \mu = 52{,}000$ against $H_a: \mu \neq 52{,}000$.
    (2) $\alpha = 0.05$. (3) A one-sample $t$, since $\sigma$ is unknown, with
    $\nu = 35$. (4) Reject if $|t| > t_{0.025,35} = 2.0301$. (5) SE
    $= 7{,}200/\sqrt{36} = 1{,}200.0000$. (6)
    $t = (49{,}800 - 52{,}000)/1{,}200 = -1.8333$. (7) $|-1.8333| < 2.0301$, and
    $p = 0.0753$. (8) **Do not reject.** There is insufficient evidence at the 5% level
    that mean starting salary differs from \$52,000 — though note the 95% interval,
    $49{,}800 \pm 2.0301(1200) = (47{,}363.9,\ 52{,}236.1)$, is wide enough to include
    salaries well below the claim, so this is a statement about the data's
    inconclusiveness rather than a vindication of the college.

25. Essentially nothing separates them. The two p-values differ by 0.002, which is far
    less than the uncertainty in either, and the only reason they read as opposite
    findings is that 0.05 happens to sit between them. The threshold is a convention
    adopted for convenience, not a feature of the world, and nothing changes discretely
    at 0.05 — the evidence at 0.051 is almost exactly as strong as the evidence at
    0.049. The right response is to report both estimates with their confidence
    intervals, which will be very nearly identical, and to let the reader see that the
    two studies agree. Treating the pair as a disagreement is an artefact of
    dichotomising a continuous measure, and it is how a literature ends up with
    contradictory "findings" drawn from compatible data.
""", [
    ("q5b SE", 1.0000, 8 / np.sqrt(64)),
    ("q5b z", -2.5000, (497.5 - 500) / 1.0),
    ("q5c tail", 0.0062, float(stats.norm.sf(2.5))),
    ("q5c p", 0.0124, float(2 * stats.norm.sf(2.5))),
    ("q6b SE", 3.0000, 12 / np.sqrt(16)),
    ("q6b t", 1.3333, (104 - 100) / 3),
    ("q6c crit", 1.7531, _t15_90),
    ("q6d p", 0.1012, float(stats.t.sf(4 / 3, 15))),
    ("q7a crit", 2.1314, _t15_95),
    ("q7a p", 0.2024, float(2 * stats.t.sf(4 / 3, 15))),
    ("q8a SE", 0.7000, 4.9 / np.sqrt(49)),
    ("q8a t", -2.5714, (498.2 - 500) / 0.7),
    ("q8a crit", 2.0106, _t48),
    ("q8b p", 0.0133, float(2 * stats.t.sf(abs((498.2 - 500) / 0.7), 48))),
    ("q9a SE", 1.0000, 6 / np.sqrt(36)),
    ("q9a t", -1.6000, (28.4 - 30) / 1.0),
    ("q9a crit", 2.0301, _t35),
    ("q9a p", 0.1186, float(2 * stats.t.sf(1.6, 35))),
    ("q9b lo", 26.3699, 28.4 - _t35),
    ("q9b hi", 30.4301, 28.4 + _t35),
    ("q10a t", -2.6000, (28.4 - 31) / 1.0),
    ("q14a SE", 3.0000, 15 / np.sqrt(25)),
    ("q14a z", 1.6449, float(stats.norm.ppf(0.95))),
    ("q14a crit", 104.9346, float(_crit_pow)),
    ("q14b z", -0.3551, float((_crit_pow - 106) / 3)),
    ("q14b power", 0.6387, _power25),
    ("q14c beta", 0.3613, 1 - _power25),
    ("q15a SE", 1.5000, 15 / np.sqrt(100)),
    ("q15a crit", 102.4673, float(_crit_pow100)),
    ("q15a z", -2.3551, float((_crit_pow100 - 106) / 1.5)),
    ("q15a power", 0.9907, _power100),
    ("q17a SE", 0.0707, float(5 / np.sqrt(5000))),
    ("q17a z", 4.2426, float(0.3 / (5 / np.sqrt(5000)))),
    ("q17b z", 0.3000, 0.3 / 1.0),
    ("q17b p", 0.7642, float(2 * stats.norm.sf(0.3))),
    ("q18b survive", 0.3585, 0.95 ** 20),
    ("q18b", 0.6415, 1 - 0.95 ** 20),
    ("q21a", 0.0322, float(stats.norm.sf(1.85))),
    ("q21b", 0.0643, float(2 * stats.norm.sf(1.85))),
    ("q22 crit", 1.7247, float(stats.t.ppf(0.95, 20))),
    ("q24 SE", 1200.0000, 7200 / np.sqrt(36)),
    ("q24 t", -1.8333, (49800 - 52000) / 1200),
    ("q24 p", 0.0753, float(2 * stats.t.sf(2200 / 1200, 35))),
    ("q24 lo", 47363.9, float(49800 - _t35 * 1200)),
    ("q24 hi", 52236.1, float(49800 + _t35 * 1200)),
])
