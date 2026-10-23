"""Extra practice for chapters 12-13 -- the CLT and estimation.

The CLT set is deliberately the longest in the first half of the book. It is the
single result everything after it depends on, and it is the one students think
they understand because they can recite it.
"""

import numpy as np
from scipy import stats

BLOCKS = {}

# ---------------------------------------------------------------- chapter 12

_sA = 15 / np.sqrt(100)
_sC = float(np.sqrt(100 * 0.3 * 0.7))
_sD = 8 / np.sqrt(50)
_sE = 200 * np.sqrt(40)

BLOCKS["12_central_limit_theorem.md"] = (r"""
## More practice

Twenty more — the longest set in the book, because this is the result the whole
second half rests on and because it is the one people are most confident they have
understood. Questions 12, 13 and 19 are the ones that separate reciting the theorem
from knowing it.

1. A population has $\mu = 50$ and $\sigma = 15$ and is heavily right-skewed. A
   sample of $n = 100$ is drawn.
   (a) State the approximate distribution of $\bar{X}$, with both parameters.
   (b) Find $\mathrm{P}(\bar{X} < 47)$.
   (c) Find $\mathrm{P}(\bar{X} > 52)$.
   (d) Find $\mathrm{P}(48 < \bar{X} < 53)$.

2. For the population in question 1, find $\mathrm{P}(X < 47)$ for a single
   observation, or explain precisely why you cannot.

3. For each population, state roughly how large $n$ must be before you would trust
   the normal approximation for $\bar{X}$, and say why.
   (a) Already normal. (b) Symmetric but with fat tails. (c) Mildly right-skewed.
   (d) Severely right-skewed, like income. (e) Binary (0/1) with $p = 0.5$.
   (f) Binary with $p = 0.02$.

4. Weight lifted per set in a gym is strongly right-skewed with $\mu = 60$ kg and
   $\sigma = 24$ kg. A trainer records 36 sets.
   (a) Find the standard error of the mean.
   (b) Find $\mathrm{P}(\bar{X} > 68)$.
   (c) The trainer's own 36 sets averaged 68 kg. Is this good evidence they lift more
   than the gym average? Give the number that justifies your answer.

5. State the Central Limit Theorem in your own words. A complete answer says three
   things: what becomes normal, what its mean and standard deviation are, and what is
   required of the population.

6. $X \sim \text{Bin}(100, 0.3)$.
   (a) Find the mean and standard deviation.
   (b) Approximate $\mathrm{P}(X \leq 25)$ using the normal with a continuity
   correction.
   (c) The exact binomial answer is 0.1631. How close did you get?

7. Repeat 6(b) **without** the continuity correction.
   (a) What answer do you get?
   (b) By how much does it miss, and in which direction?
   (c) When does the correction stop mattering?

8. For each, say whether the normal approximation to the binomial is appropriate, and
   state the check. (a) $n=50$, $p=0.4$. (b) $n=50$, $p=0.05$.
   (c) $n=400$, $p=0.01$. (d) $n=25$, $p=0.5$.

9. Time between arrivals is exponential with a mean of 8 minutes — a distribution
   nothing like a bell. The mean of 50 such times is recorded.
   (a) Find the standard error.
   (b) Find $\mathrm{P}(\bar{X} > 10)$.
   (c) Which theorem licensed you to use the normal table on an exponential
   population?

10. An insurer expects 40 claims next month, each with mean \$500 and standard
    deviation \$200, independently.
    (a) Find the expected total and its standard deviation.
    (b) Find the probability the total exceeds \$22,000.
    (c) Which quantity did the CLT apply to here — the mean or the sum?

11. Write down the standardisation for a sum and for a mean side by side. Explain why
    one has $\sqrt{n}$ multiplying and the other has $\sqrt{n}$ dividing.

12. For each statement, say whether the CLT supports it.
    (a) "With a large sample, the population becomes normal."
    (b) "With a large sample, the sample data look normal."
    (c) "With a large sample, the sample mean is approximately normal."
    (d) "With a large sample, individual observations are approximately normal."
    (e) "The CLT is why $s$ approaches $\sigma$."

13. Name three situations in which the CLT does **not** rescue you, and say what fails
    in each.

14. In a simulation, 1,000 samples of $n = 36$ are drawn from a skewed population and
    a 95% interval is built each time. 919 of them contain $\mu$.
    (a) What should the number have been?
    (b) Is 919 close enough to call the approximation adequate? Justify.
    (c) At $n = 200$ the figure rises to 939. What does that trend tell you?

15. The skewness of a sample mean is the population skewness divided by $\sqrt{n}$.
    (a) A population has skewness 3. Find the skewness of $\bar{X}$ at $n = 9$,
    $n = 36$ and $n = 144$.
    (b) Explain how this formula makes the "how large is large enough" question
    quantitative rather than a matter of folklore.

16. Explain why so many naturally occurring measurements — heights, measurement
    errors, test scores — are approximately normal, when nothing arranged for them to
    be.

17. A population has $\mu = 100$ and $\sigma = 20$. Compare $\mathrm{P}(X > 110)$ for
    a single observation, assuming normality, with $\mathrm{P}(\bar{X} > 110)$ for
    $n = 25$. Explain the gap in one sentence.

18. "Thirty is large enough" is repeated everywhere.
    (a) Is it a theorem?
    (b) Where does the number come from?
    (c) Give a case where 30 is far too few and one where 5 would do.

19. Two populations have the same $\mu = 20$ and the same $\sigma = 5$. One is normal
    and one is a heavily skewed distribution of waiting times. Samples of $n = 100$
    are drawn from each.
    (a) Are the two sampling distributions of $\bar{X}$ the same?
    (b) Are the two populations' distributions the same?
    (c) What does the pair of answers tell you about what a sample mean throws away?

20. You are designing a study of household electricity use, which you know from
    previous work is severely right-skewed with a handful of very large users. Your
    budget allows $n = 40$ or $n = 400$. Argue, using this chapter, for the figure you
    would choose and say what specifically you are buying.

### Answers to the extra problems

1. (a) Approximately $N(50,\ 1.5^2)$: mean 50, standard error
   $15/\sqrt{100} = 1.5000$.
   (b) $z = (47-50)/1.5 = -2.00$, so $\mathrm{P} = 0.0228$.
   (c) $z = (52-50)/1.5 = 1.3333$, so $\mathrm{P} = 0.0912$.
   (d) $z$ runs from $-1.3333$ to $2.00$, so
   $\mathrm{P} = 0.9772 - 0.0912 = 0.8860$.

2. **You cannot.** The CLT describes $\bar{X}$, not $X$. For a single observation you
   would need the population's actual distribution, and all you have been told is that
   it is right-skewed with a particular mean and standard deviation — which is
   consistent with infinitely many shapes, giving different answers for
   $\mathrm{P}(X < 47)$. No sample size changes this: $n$ affects the mean's
   distribution, not an individual's.

3. (a) **Any $n$**, including 1 — the mean of normal draws is exactly normal, no
   approximation involved. (b) Moderate, perhaps 30 to 50: fat tails make extreme
   draws more common, so more averaging is needed to tame them. (c) Around 20 to 30 is
   usually ample. (d) **Several hundred.** Severe skew is slow to average away, and
   the one-tailed probabilities stay wrong long after the two-tailed ones look fine.
   (e) About 20 — at $p = 0.5$ the distribution is already symmetric, so only the
   discreteness needs smoothing. (f) **Several hundred**: $np \geq 5$ requires
   $n \geq 250$ on its own.

4. (a) $24/\sqrt{36} = 4.0000$ kg.
   (b) $z = (68-60)/4 = 2.00$, so $\mathrm{P} = 0.0228$.
   (c) It is reasonable evidence. If the trainer were an average lifter, a 36-set mean
   of 68 kg or more would arise about **2.3%** of the time — unlikely enough to doubt
   the assumption. Note what made this possible: the population of individual sets is
   badly skewed and we could say nothing about one set, but averaging 36 of them
   produced a quantity the normal table handles.

5. The **sample mean** $\bar{X}$ of $n$ independent draws becomes approximately
   normally distributed as $n$ grows. Its mean is the population mean $\mu$ and its
   standard deviation is $\sigma/\sqrt{n}$. What is required of the population is only
   that it has a finite mean and a finite variance and that the draws are independent
   — crucially, **not** that it is normal, or symmetric, or continuous.

6. (a) $\mu = 100(0.3) = 30.0000$ and
   $\sigma = \sqrt{100(0.3)(0.7)} = \sqrt{21} = 4.5826$.
   (b) With the correction, $z = (25.5 - 30)/4.5826 = -0.9820$, so
   $\mathrm{P} \approx 0.1630$.
   (c) The exact answer is 0.1631, so the approximation is out by about 0.0001 —
   accurate to three decimal places.

7. (a) $z = (25 - 30)/4.5826 = -1.0911$, giving $\mathrm{P} \approx 0.1376$.
   (b) It misses by about 0.0255, roughly **16% of the true value**, and it is too
   **small**. The reason is geometric: the binomial puts a bar of probability *at* 25
   and the uncorrected normal cuts straight through the middle of it, discarding half
   the bar.
   (c) When $n$ is large enough that a single bar is a negligible share of the
   distribution. At $n = 100$ it still matters; by $n = 1{,}000$ it is usually below
   the rounding in your answer. It never hurts to include it.

8. The check is $np \geq 5$ and $n(1-p) \geq 5$.
   (a) $20$ and $30$. **Yes.** (b) $2.5$ and $47.5$. **No.**
   (c) $4$ and $396$. **No**, narrowly. (d) $12.5$ and $12.5$. **Yes.**

9. (a) $8/\sqrt{50} = 1.1314$ minutes.
   (b) $z = (10 - 8)/1.1314 = 1.7678$, so $\mathrm{P} = 0.0386$.
   (c) The **Central Limit Theorem**. The exponential is about as un-normal as a
   distribution gets — right-skewed, bounded below at zero, with its mode at the
   boundary — and none of that matters, because the theorem makes no assumption about
   the population's shape. This is the point of the whole chapter: you may use the
   normal table on a population you know is not normal, provided you are asking about
   an average.

10. (a) $E(S) = 40(500) = \$20{,}000$ and
    $\text{SD}(S) = 200\sqrt{40} = \$1{,}264.9111$.
    (b) $z = (22{,}000 - 20{,}000)/1264.9111 = 1.5811$, so $\mathrm{P} = 0.0569$.
    (c) The **sum**. The CLT applies to both, since a sum is just $n$ times the mean —
    but the parameters differ, and using the mean's standard error of
    $200/\sqrt{40} = 31.62$ for a question about the total would be out by a factor of
    40.

11. For a sum, $z = \dfrac{S - n\mu}{\sigma\sqrt{n}}$; for a mean,
    $z = \dfrac{\bar{X} - \mu}{\sigma/\sqrt{n}}$. Both come from the same fact that
    variances add, giving $V(S) = n\sigma^2$. The sum keeps all of that accumulated
    variance, so its standard deviation *grows* as $\sqrt{n}$. The mean divides the
    sum by $n$, which divides its variance by $n^2$, leaving $\sigma^2/n$ — so its
    standard deviation *shrinks* as $\sqrt{n}$. Adding things up makes them more
    variable; averaging them makes them less.

12. (a) **No** — the population is a fixed set of numbers and nothing about it changes
    when you sample. (b) **No** — a histogram of a large sample converges on the
    *population's* shape, skew and all; it does not become a bell. (c) **Yes** — this
    is the theorem. (d) **No** — see question 2. (e) **No** — that $s \to \sigma$ is
    the Law of Large Numbers, a different result about consistency rather than about
    shape. (b) and (c) being different is the distinction this chapter exists to make:
    the histogram of *your data* and the histogram of *the mean across repeated
    samples* are not the same picture.

13. (i) **The population has no finite variance** — Cauchy-type heavy tails. The
    theorem's hypothesis fails outright, and the mean of a million draws is no better
    behaved than one. (ii) **The draws are not independent** — clustered sampling,
    time series with autocorrelation, students who studied together. The effective
    sample size is far below $n$, so the standard error is understated, sometimes
    badly. (iii) **$n$ is too small relative to the skew.** The theorem is asymptotic;
    at $n = 10$ from an income distribution it simply has not arrived yet, and the
    one-tailed probabilities will be wrong in a predictable direction.

14. (a) About **950** of 1,000 — a 95% interval should contain $\mu$ 95% of the time.
    (b) Not really. 919 against an expected 950 is a coverage of 91.9% when 95% was
    claimed, and the shortfall is about three times what sampling variation in the
    simulation itself would explain. The intervals are too narrow, and anyone using
    them believes they are being more careful than they are.
    (c) That the failure is the **approximation**, not the method. As $n$ rises the
    coverage climbs towards its nominal level, exactly as the CLT predicts — the
    intervals were not wrong in principle, they were being used at an $n$ the
    approximation had not reached.

15. (a) Skewness 3 gives $3/\sqrt{9} = 1.0000$ at $n=9$, $3/\sqrt{36} = 0.5000$ at
    $n=36$, and $3/\sqrt{144} = 0.2500$ at $n=144$.
    (b) Because it tells you how far along you are. If you regard a skewness below
    about 0.25 as negligible, then a population with skewness 3 needs $n = 144$ and a
    population with skewness 6 needs $n = 576$ — numbers you can compute rather than
    guess. "Thirty is enough" is the answer this formula gives for a population with
    skewness under about 1.4, which is why the rule works for the mildly skewed data
    textbooks use and fails for income.

16. Because such measurements are themselves sums or averages of many small
    independent contributions. A person's height is the accumulation of a great many
    genetic and environmental influences; a measurement error is the accumulation of
    many small independent errors; a test score is the sum of performance on many
    items. The CLT says any such accumulation tends to normality regardless of what the
    individual pieces look like, so the bell curve appears throughout nature without
    anything in nature having arranged it. It is a theorem about addition, not a law of
    biology.

17. For a single observation $z = (110-100)/20 = 0.50$, so
    $\mathrm{P} = 0.3085$. For the mean of 25, the standard error is 4, so
    $z = 2.50$ and $\mathrm{P} = 0.0062$. One person being 10 above average is
    unremarkable; twenty-five people averaging 10 above requires them to be unusual
    collectively, and that is about fifty times rarer.

18. (a) **No.** The CLT is a statement about the limit as $n \to \infty$ and contains
    no number 30.
    (b) From practice: for the mildly skewed distributions common in textbook examples,
    the approximation is adequate around $n = 30$, and the figure got repeated until it
    sounded like a rule.
    (c) **Far too few:** household wealth, insurance claims, or any binary variable
    with $p = 0.01$ — all need hundreds. **Five would do:** a population already
    normal, or very nearly so, where no approximation is needed at all.

19. (a) **Yes, approximately** — both are approximately $N(20,\ 0.5^2)$, since the CLT
    delivers the same answer from the same $\mu$ and $\sigma$ whatever the shape. (At
    $n = 100$ the skewed one will be very slightly off, by question 15's formula.)
    (b) **No** — one is a bell and one is a long-tailed waiting-time distribution.
    They are not remotely alike.
    (c) That a sample mean discards almost everything about the shape of the
    population. It is sensitive to $\mu$ and $\sigma$ and essentially blind to the
    rest, which is simultaneously why inference about $\mu$ is so portable across
    fields and why reporting a mean can be so misleading — two populations that no one
    would confuse produce the same confidence interval.

20. Choose **400**. Severe right skew with a few very large users is precisely the case
    in which $n = 40$ is not enough: by question 15's formula, if the skewness is
    around 4 then at $n=40$ the sample mean still has skewness $4/\sqrt{40} = 0.6325$,
    which is enough to make one-tailed probabilities and interval endpoints noticeably
    wrong. At $n = 400$ that falls to $4/\sqrt{400} = 0.2000$. What you are buying is
    two separate things: a standard error half the size, and — the point of this
    chapter — the right to use the normal table at all. The second is the one that
    would have invalidated the study rather than merely widened it.
""", [
    ("q1a SE", 1.5000, float(_sA)),
    ("q1b", 0.0228, float(stats.norm.cdf(-2.0))),
    ("q1c z", 1.3333, 2 / 1.5),
    ("q1c", 0.0912, float(stats.norm.sf(2 / 1.5))),
    ("q1d upper", 0.9772, float(stats.norm.cdf(2.0))),
    ("q1d", 0.8860, float(stats.norm.cdf(2.0) - stats.norm.cdf(-2 / 1.5))),
    ("q4a SE", 4.0000, 24 / 6),
    ("q4b", 0.0228, float(stats.norm.sf(2.0))),
    ("q6a mean", 30.0000, 100 * 0.3),
    ("q6a sd", 4.5826, _sC),
    ("q6b z", 0.9820, abs((25.5 - 30) / _sC)),
    ("q6b", 0.1630, float(stats.norm.cdf((25.5 - 30) / _sC))),
    ("q6c exact", 0.1631, float(stats.binom.cdf(25, 100, 0.3))),
    ("q7a z", 1.0911, abs((25 - 30) / _sC)),
    ("q7a", 0.1376, float(stats.norm.cdf((25 - 30) / _sC))),
    ("q7b miss", 0.0255,
     float(stats.binom.cdf(25, 100, 0.3) - stats.norm.cdf((25 - 30) / _sC))),
    ("q9a SE", 1.1314, float(_sD)),
    ("q9b z", 1.7678, float(2 / _sD)),
    ("q9b", 0.0386, float(stats.norm.sf(2 / _sD))),
    ("q10a sd", 1264.9111, float(_sE)),
    ("q10b z", 1.5811, float(2000 / _sE)),
    ("q10b", 0.0569, float(stats.norm.sf(2000 / _sE))),
    ("q10c mean SE", 31.62, float(200 / np.sqrt(40))),
    ("q15a n9", 1.0000, 3 / np.sqrt(9)),
    ("q15a n36", 0.5000, 3 / np.sqrt(36)),
    ("q15a n144", 0.2500, 3 / np.sqrt(144)),
    ("q17 single", 0.3085, float(stats.norm.sf(0.5))),
    ("q17 mean", 0.0062, float(stats.norm.sf(2.5))),
    ("q20 n40 skew", 0.6325, 4 / np.sqrt(40)),
    ("q20 n400 skew", 0.2000, 4 / np.sqrt(400)),
])

# ---------------------------------------------------------------- chapter 13

_t35 = float(stats.t.ppf(0.975, 35))
_t35_90 = float(stats.t.ppf(0.95, 35))
_t35_99 = float(stats.t.ppf(0.995, 35))
_t15 = float(stats.t.ppf(0.975, 15))

BLOCKS["13_estimation.md"] = (r"""
## More practice

Fifteen more. The commute data from the worked example runs through the first three,
so you can see what changes when only the confidence level moves and nothing else
does.

1. A sample of $n = 36$ commutes gives $\bar{x} = 28.4$ minutes and $s = 6$.
   (a) Find the estimated standard error.
   (b) Find the critical value for a 95% interval, stating the degrees of freedom.
   (c) Build the 95% confidence interval.
   (d) State the margin of error.

2. Using the same data, build the **90%** and **99%** intervals.
   (a) Give both.
   (b) Compare the three widths and state the trade-off in one sentence.

3. Now suppose $\sigma = 6$ were somehow known exactly, with the same $\bar{x}$ and
   $n$.
   (a) Build the 95% interval.
   (b) Compare it with 1(c). Which is wider, by how much, and why?

4. Explain what "95% confident" means. Then say explicitly what it does **not** mean.

5. A 95% interval for a population mean is $(26.37,\ 30.43)$. For each statement, say
   whether it is true.
   (a) 95% of the sample values lie between 26.37 and 30.43.
   (b) There is a 95% probability that $\mu$ lies between 26.37 and 30.43.
   (c) If the study were repeated many times, 95% of the intervals so constructed
   would contain $\mu$.
   (d) A test of $H_0: \mu = 31$ at $\alpha = 0.05$ would reject.
   (e) A test of $H_0: \mu = 27$ at $\alpha = 0.05$ would reject.

6. With $\sigma = 6$ and 95% confidence, find the sample size needed for a margin of
   error of (a) 1.0 minute, (b) 0.5 minutes.

7. Look at your two answers to question 6.
   (a) What happened to $n$ when the margin of error halved?
   (b) Name the three ways to reduce the margin of error, and say which of the three
   is free.

8. A 95% confidence interval is reported as $(12.4,\ 19.6)$. Find the point estimate
   and the margin of error.

9. A firm claims its mean delivery time is 27 minutes. Using the interval from
   question 1(c), what do you conclude at the 5% level, and why can you answer without
   computing a test statistic?

10. A sample of 16 gives $\bar{x} = 52$ and $s = 8$.
    (a) Build the 95% interval.
    (b) Why is the critical value so much larger than 1.96 here?

11. A student uses $z = 1.96$ for a sample of 16 because "1.96 is the 95% number".
    (a) What should they have used?
    (b) Is their interval too wide or too narrow?
    (c) What does that do to the interval's actual coverage?

12. Two studies estimate the same mean. Study A has $n = 100$, Study B has $n = 400$,
    and both find $s = 20$. Without computing the intervals, state the ratio of their
    widths.

13. A researcher writes: "there is a 95% probability that $\mu$ lies between 26.37 and
    30.43." Rewrite the sentence correctly and explain in one line what is wrong with
    the original.

14. Using the data in question 1, construct a **one-sided** 95% lower bound for the
    mean commute. Compare the bound with the lower end of the two-sided 95% interval
    and explain the difference.

15. The $t$ interval assumes the population is normal. A colleague has $n = 12$
    observations from a badly skewed population and builds one anyway.
    (a) What is the problem?
    (b) Would $n = 300$ fix it? Which result are you appealing to?

### Answers to the extra problems

1. (a) $s/\sqrt{n} = 6/\sqrt{36} = 1.0000$ minute.
   (b) $\nu = 35$, so $t_{0.025,35} = 2.0301$.
   (c) $28.4 \pm 2.0301(1.0) = (26.3699,\ 30.4301)$.
   (d) The margin of error is **2.0301** minutes — the critical value times the
   standard error, which here happen to be numerically equal because SE $= 1$.

2. (a) 90%: $t_{0.05,35} = 1.6896$, giving $(26.7104,\ 30.0896)$.
   99%: $t_{0.005,35} = 2.7238$, giving $(25.6762,\ 31.1238)$.
   (b) Widths are 3.3791, 4.0602 and 5.4476 for 90%, 95% and 99%. **Higher confidence
   costs width**: you can be more certain of catching $\mu$ only by casting a wider
   net, and an interval certain to contain $\mu$ would run from minus to plus
   infinity, which is certain and useless.

3. (a) With $\sigma$ known the critical value is $z_{0.025} = 1.9600$, giving
   $28.4 \pm 1.96 = (26.4400,\ 30.3600)$.
   (b) The $t$ interval from 1(c) is **wider**, by 0.0702 minutes in each direction.
   The reason is that $s$ is an estimate with its own sampling variability, and the
   wider $t$ distribution is the price of not knowing $\sigma$. At $\nu = 35$ that
   price is small; at $\nu = 8$ it would be substantial.

4. It means the **procedure** captures $\mu$ in 95% of repetitions. Build an interval
   this way from sample after sample, and 95 in 100 of those intervals will contain
   the true mean. It does **not** mean there is a 95% probability that $\mu$ lies in
   the one interval you computed. $\mu$ is a fixed number and your interval is a fixed
   pair of numbers; either it contains $\mu$ or it does not, and the 95% describes the
   long-run reliability of the method, not the standing of a particular result.

5. (a) **False** — confidence intervals are about the mean, not about where individual
   observations fall. Most of the data lies well outside this interval.
   (b) **False** — see question 4. This is the commonest misstatement in the subject.
   (c) **True.** This is the correct reading.
   (d) **True** — 31 is outside the interval, and a two-tailed test at $\alpha = 0.05$
   rejects exactly the values the 95% interval excludes.
   (e) **False** — 27 is inside, so the test does not reject.

6. The formula is $n = (z\sigma/E)^2$.
   (a) $n = (1.96 \times 6/1.0)^2 = 11.76^2 = 138.2976$, so round **up** to
   $n = 139$.
   (b) $n = (1.96 \times 6/0.5)^2 = 23.52^2 = 553.1904$, so $n = 554$.

7. (a) It roughly **quadrupled**, from 139 to 554. $E$ appears squared in the
   denominator, so halving it multiplies $n$ by four.
   (b) Increase $n$; accept lower confidence; reduce $\sigma$. Lowering the confidence
   level is **free in money and expensive in meaning** — you get a narrower interval
   by making a weaker claim, which is not a gain. Reducing $\sigma$ means measuring
   more precisely or stratifying, which is sometimes possible and is the only genuinely
   free lunch available. Increasing $n$ costs money, at a quadratic rate.

8. The point estimate is the midpoint: $(12.4 + 19.6)/2 = 16.0000$. The margin of
   error is half the width: $(19.6 - 12.4)/2 = 3.6000$. Every reported interval can be
   read backwards like this, which is worth knowing because papers often print the
   interval and not the standard error.

9. 27 **lies inside** $(26.3699,\ 30.4301)$, so you do not reject the firm's claim at
   the 5% level. You can answer without a test statistic because the two procedures are
   algebraically the same thing: a two-tailed test at $\alpha$ rejects $\mu_0$ precisely
   when $\mu_0$ falls outside the $100(1-\alpha)\%$ interval. The interval is the set
   of values that would not be rejected.

10. (a) SE $= 8/\sqrt{16} = 2.0000$ and $t_{0.025,15} = 2.1314$, so the margin of
    error is 4.2629 and the interval is $(47.7371,\ 56.2629)$.
    (b) Because $\nu = 15$. With only 16 observations, $s$ is a poor estimate of
    $\sigma$, and the $t$ distribution compensates by being wider in the tails. The
    gap from 1.96 to 2.1314 is the cost of that ignorance, and it closes as $n$ grows.

11. (a) $t_{0.025,15} = 2.1314$.
    (b) **Too narrow** — 1.96 is smaller, so the interval is shorter than it should be.
    (c) Its real coverage is below the advertised 95%: the interval misses $\mu$ more
    often than once in twenty. The error flatters the result, which is the direction
    that matters, since it makes the researcher look more precise than the data
    supports.

12. Width scales as $1/\sqrt{n}$, so Study B's interval is $\sqrt{400/100} = 2.0000$
    times narrower. Four times the data buys twice the precision, which is the same
    trade-off as question 7 seen from the other end.

13. Correctly: **"We are 95% confident that $\mu$ lies between 26.37 and 30.43"**, or
    more fully, "this interval was produced by a method that captures $\mu$ 95% of the
    time." The original assigns a probability to $\mu$, treating a fixed constant as
    random; the randomness is in the interval, which varies from sample to sample,
    not in the parameter, which does not vary at all.

14. A one-sided 95% lower bound uses $t_{0.05,35} = 1.6896$, putting all 5% in one
    tail: the bound is $28.4 - 1.6896(1.0) = 26.7104$. It is **higher** than the
    two-sided interval's lower end of 26.3699, and the reason is that the two-sided
    interval spends half its error allowance guarding the upper end as well. If you
    genuinely only care about one direction, the one-sided bound is tighter — but you
    must decide which direction before seeing the data, exactly as with a one-tailed
    test.

15. (a) With $n = 12$ there is no normality to appeal to from either direction: the
    population is not normal, and the CLT has not had enough observations to make
    $\bar{X}$ normal either. The stated 95% coverage is simply not what the interval
    delivers, and for a skewed population the two tails will be wrong by different
    amounts.
    (b) **Yes**, broadly — at $n = 300$ the **Central Limit Theorem** makes $\bar{X}$
    approximately normal whatever the population looks like, so the interval recovers
    close to its nominal coverage. The assumption was never really about the population
    being normal; it was about $\bar{X}$ being normal, and there are two routes to that.
""", [
    ("q1a SE", 1.0000, 6 / np.sqrt(36)),
    ("q1b t", 2.0301, _t35),
    ("q1c lo", 26.3699, 28.4 - _t35),
    ("q1c hi", 30.4301, 28.4 + _t35),
    ("q2a t90", 1.6896, _t35_90),
    ("q2a lo90", 26.7104, 28.4 - _t35_90),
    ("q2a hi90", 30.0896, 28.4 + _t35_90),
    ("q2a t99", 2.7238, _t35_99),
    ("q2a lo99", 25.6762, 28.4 - _t35_99),
    ("q2a hi99", 31.1238, 28.4 + _t35_99),
    ("q2b width90", 3.3791, 2 * _t35_90),
    ("q2b width95", 4.0602, 2 * _t35),
    ("q2b width99", 5.4476, 2 * _t35_99),
    ("q3a z", 1.9600, float(stats.norm.ppf(0.975))),
    ("q3a lo", 26.4400, 28.4 - 1.96),
    ("q3a hi", 30.3600, 28.4 + 1.96),
    ("q3b gap", 0.0702, _t35 - 1.96),
    ("q6a raw", 138.2976, (1.96 * 6 / 1.0) ** 2),
    ("q6a product", 11.76, 1.96 * 6),
    ("q6b raw", 553.1904, (1.96 * 6 / 0.5) ** 2),
    ("q6b product", 23.52, 1.96 * 6 / 0.5),
    ("q8 midpoint", 16.0000, (12.4 + 19.6) / 2),
    ("q8 ME", 3.6000, (19.6 - 12.4) / 2),
    ("q10a SE", 2.0000, 8 / np.sqrt(16)),
    ("q10a t", 2.1314, _t15),
    ("q10a ME", 4.2629, 2 * _t15),
    ("q10a lo", 47.7371, 52 - 2 * _t15),
    ("q10a hi", 56.2629, 52 + 2 * _t15),
    ("q12 ratio", 2.0000, float(np.sqrt(400 / 100))),
    ("q14 bound", 26.7104, 28.4 - _t35_90),
])
