"""Extra practice for chapters 8-11. Imported by make_more_practice.py."""

import numpy as np
from scipy import stats

BLOCKS = {}

# ---------------------------------------------------------------- chapter 8

BLOCKS["08_binomial.md"] = (r"""
## More practice

Ten more. Work questions 1 and 2 with the formula rather than Stata — the exam has
no Stata in it, and the only way the factorials stop being frightening is repetition.

1. A supplier's components are faulty 25% of the time, independently. Twelve are
   installed.
   (a) Check each of the four binomial conditions against this scenario.
   (b) Find $E(X)$, $V(X)$ and the standard deviation of the number faulty.
   (c) Find $\mathrm{P}(X = 3)$.

2. For the same twelve components:
   (a) Find $\mathrm{P}(X = 0)$.
   (b) Find $\mathrm{P}(X \geq 1)$, and say which rule saved you most of the work.
   (c) Find $\mathrm{P}(X \leq 2)$.

3. A call centre's lines fail to connect 10% of the time. Twenty calls are placed.
   (a) Find the probability exactly two fail.
   (b) Find the probability at least three fail.

4. For each scenario, say whether the binomial applies, and if not, which condition
   fails.
   (a) Counting heads in 50 tosses of a fair coin.
   (b) Drawing 5 cards from a deck and counting hearts.
   (c) Counting how many of 30 students pass, when they studied together.
   (d) Counting the number of customers arriving in an hour.
   (e) Counting defectives in a sample of 20 from a batch of 10,000 that is 3%
   defective.

5. Explain why $\mathrm{P}(X \geq 1) = 1 - \mathrm{P}(X = 0)$ saves so much work, and
   write down a question for which the complement rule would *not* help.

6. For each, say whether the normal approximation to the binomial is appropriate.
   (a) $n = 40$, $p = 0.5$. (b) $n = 40$, $p = 0.08$. (c) $n = 200$, $p = 0.02$.
   (d) $n = 15$, $p = 0.6$.

7. A batch of 10,000 items is 3% defective, and 20 are sampled without replacement.
   (a) Strictly, is this binomial?
   (b) Why is treating it as binomial nevertheless fine here?
   (c) At what sample size would you start to worry?

8. A basketball player makes 80% of free throws. In a game they take 10.
   (a) Find the expected number made.
   (b) Find $\mathrm{P}(\text{all } 10)$.
   (c) The commentator says "they make 8 out of 10, so expect exactly 8 tonight."
   What is wrong with that?

9. $X \sim \text{Bin}(n, 0.4)$. Write $E(X)$ and $\text{SD}(X)$ as functions of $n$,
   and say which grows faster as $n$ increases. What does that imply about $X/n$?

10. A table gives cumulative binomial probabilities $\mathrm{P}(X \leq x)$. Write down,
    in terms of table entries, how you would get (a) $\mathrm{P}(X = 4)$,
    (b) $\mathrm{P}(X \geq 4)$, (c) $\mathrm{P}(2 \leq X \leq 5)$.

### Answers to the extra problems

1. (a) **Fixed $n$**: 12 components, decided in advance. **Two outcomes**: faulty or
   not. **Constant $p$**: 0.25 for each, which the question asserts. **Independence**:
   stated. All four hold, so $X \sim \text{Bin}(12, 0.25)$.
   (b) $E(X) = 12(0.25) = 3.0000$; $V(X) = 12(0.25)(0.75) = 2.2500$;
   $\text{SD}(X) = 1.5000$.
   (c) $\mathrm{P}(X=3) = \binom{12}{3}(0.25)^3(0.75)^9 = 220(0.015625)(0.0750847)
   = 0.2581$.

2. (a) $\mathrm{P}(X=0) = (0.75)^{12} = 0.0317$.
   (b) $1 - 0.0317 = 0.9683$. The **complement rule** — the alternative is adding
   twelve separate terms.
   (c) $\mathrm{P}(X \leq 2) = 0.0317 + 0.1267 + 0.2323 = 0.3907$.

3. (a) $\binom{20}{2}(0.1)^2(0.9)^{18} = 190(0.01)(0.1500946) = 0.2852$.
   (b) $\mathrm{P}(X \geq 3) = 1 - \mathrm{P}(X \leq 2)
   = 1 - (0.1216 + 0.2702 + 0.2852) = 1 - 0.6769 = 0.3231$.

4. (a) Yes. (b) **No** — drawing without replacement from 52 cards changes $p$ between
   draws, so the constant-$p$ and independence conditions fail. This is
   hypergeometric. (c) **No** — studying together breaks independence; one student's
   outcome carries information about another's. (d) **No** — there is no fixed $n$;
   arrivals in a fixed period is a Poisson situation. (e) Yes in practice — see
   question 7.

5. Because "at least one" is the union of every outcome from 1 to $n$, while its
   complement is the single outcome 0. One term replaces $n$ of them, and the single
   term is the easiest one in the distribution, being just $(1-p)^n$. The rule does
   **not** help for something like $\mathrm{P}(3 \leq X \leq 7)$, whose complement is
   two separate tails and therefore no simpler than the original — there you add the
   five terms, or use cumulative values.

6. The condition is $np \geq 5$ **and** $n(1-p) \geq 5$.
   (a) $np = 20$, $n(1-p) = 20$. **Yes.**
   (b) $np = 3.2$. **No** — fails on the left even though $n(1-p) = 36.8$ passes.
   (c) $np = 4$. **No**, and only just: $n = 250$ would do it.
   (d) $np = 9$, $n(1-p) = 6$. **Yes**, if marginally.

7. (a) **No.** Sampling without replacement means $p$ changes from draw to draw, so
   strictly this is hypergeometric.
   (b) Because the batch is enormous relative to the sample. Removing one item from
   10,000 moves the defect rate from 0.0300 to roughly 0.0300 — the change is in the
   fifth decimal place, so the draws are independent for every practical purpose.
   (c) The usual rule of thumb is when the sample exceeds **5%** of the population.
   Here that is 500 items; at 20 you are nowhere near it.

8. (a) $10(0.8) = 8.0000$.
   (b) $0.8^{10} = 0.1074$.
   (c) The expected value is an average over many games, not a prediction for one.
   $\mathrm{P}(X = 8)$ is only $\binom{10}{8}(0.8)^8(0.2)^2 = 0.3020$, so the single
   most likely outcome happens under a third of the time and the other two-thirds of
   games land somewhere else. "Expect 8" is right about the long-run mean and wrong
   about tonight.

9. $E(X) = 0.4n$ and $\text{SD}(X) = \sqrt{0.24n}$. The mean grows **linearly** in
   $n$; the standard deviation grows only as $\sqrt{n}$. So the proportion
   $X/n$ has mean 0.4 fixed and standard deviation $\sqrt{0.24/n}$, which shrinks
   towards zero. The count becomes more variable in absolute terms and the proportion
   becomes less variable — which is the whole of Chapter 11 showing up early.

10. (a) $\mathrm{P}(X \leq 4) - \mathrm{P}(X \leq 3)$.
    (b) $1 - \mathrm{P}(X \leq 3)$ — note the 3, not the 4; "at least 4" excludes only
    0 through 3, and using $\mathrm{P}(X \leq 4)$ here is the commonest table mistake
    in the chapter.
    (c) $\mathrm{P}(X \leq 5) - \mathrm{P}(X \leq 1)$.
""", [
    ("q1b E", 3.0000, 12 * 0.25),
    ("q1b V", 2.2500, 12 * 0.25 * 0.75),
    ("q1b sd", 1.5000, float(np.sqrt(12 * 0.25 * 0.75))),
    ("q1c", 0.2581, float(stats.binom.pmf(3, 12, 0.25))),
    ("q1c tail factor", 0.0750847, 0.75 ** 9),
    ("q2a", 0.0317, 0.75 ** 12),
    ("q2b", 0.9683, 1 - 0.75 ** 12),
    ("q2c", 0.3907, float(stats.binom.cdf(2, 12, 0.25))),
    ("q2c term1", 0.1267, float(stats.binom.pmf(1, 12, 0.25))),
    ("q2c term2", 0.2323, float(stats.binom.pmf(2, 12, 0.25))),
    ("q3a", 0.2852, float(stats.binom.pmf(2, 20, 0.10))),
    ("q3a tail factor", 0.1500946, 0.9 ** 18),
    ("q3b", 0.3231, float(stats.binom.sf(2, 20, 0.10))),
    ("q3b cdf", 0.6769, float(stats.binom.cdf(2, 20, 0.10))),
    ("q3b term0", 0.1216, float(stats.binom.pmf(0, 20, 0.10))),
    ("q3b term1", 0.2702, float(stats.binom.pmf(1, 20, 0.10))),
    ("q8b", 0.1074, 0.8 ** 10),
    ("q8c", 0.3020, float(stats.binom.pmf(8, 10, 0.8))),
])

# ---------------------------------------------------------------- chapter 9

BLOCKS["09_continuous_distributions.md"] = (r"""
## More practice

Ten more, across all three distributions. Draw the picture first every single time —
every mistake in this chapter is a shaded region on the wrong side of a line, and a
sketch costs ten seconds.

1. Waiting time at a service desk is uniform on $[10, 50]$ minutes.
   (a) Find the mean, variance and standard deviation.
   (b) Find $\mathrm{P}(X < 25)$.
   (c) Find $\mathrm{P}(20 < X < 35)$.
   (d) Find $\mathrm{P}(X = 25)$, and explain the answer.

2. Test scores are $N(500, 100^2)$.
   (a) Find $\mathrm{P}(X > 650)$.
   (b) Find $\mathrm{P}(400 < X < 600)$.
   (c) Find $\mathrm{P}(X < 430)$.
   (d) Find the 90th percentile.

3. For the same distribution, a scholarship goes to the top 5%. What is the cut-off,
   and which direction does the $z$ run?

4. The time between arrivals at a till is exponential with a mean of 8 minutes.
   (a) Find $\lambda$ and the standard deviation.
   (b) Find $\mathrm{P}(X > 10)$.
   (c) Find $\mathrm{P}(X < 5)$.
   (d) Find the median waiting time, and say why it is not 8.

5. For the same arrivals: five minutes have passed with no one arriving. Find the
   probability you wait at least ten more. Compare it with your answer to 4(b) and
   name the property.

6. Explain why $\mathrm{P}(X = c) = 0$ for any continuous random variable, and why
   this does not mean the value $c$ is impossible.

7. For each quantity, name the distribution you would reach for first and say what
   feature of the situation decides it.
   (a) The height of adult women. (b) The time until a lightbulb fails.
   (c) A random number generated between 0 and 1. (d) The sum of 40 small independent
   shocks. (e) The time between emails arriving.

8. A process is $N(\mu, \sigma^2)$ and 2.5% of output falls below 46 while 2.5% falls
   above 74. Find $\mu$ and $\sigma$ without using a single probability table entry
   beyond $z = 1.96$.

9. A student computes $z = (430 - 500)/100 = -0.70$ and reports
   $\mathrm{P}(X < 430) = 0.7580$. Identify the error and give the correct answer.

10. Scores are $N(500, 100^2)$. Explain why
    $\mathrm{P}(X > 650)$ and $\mathrm{P}(\bar{X} > 650)$ for a sample of 25 are
    wildly different numbers, without computing the second one.

### Answers to the extra problems

1. (a) Mean $= (10+50)/2 = 30.0000$;
   $V = (50-10)^2/12 = 1600/12 = 133.3333$; SD $= 11.5470$.
   (b) The density is $1/40$ throughout, so the probability is the width over the
   range: $(25-10)/40 = 0.3750$.
   (c) $(35-20)/40 = 0.3750$ — the same answer, because the interval has the same
   width. Under a uniform, only the width matters, never the location.
   (d) **Zero.** A single point has no width, and probability is area. See question 6.

2. (a) $z = (650-500)/100 = 1.50$, so $\mathrm{P} = 0.0668$.
   (b) $z = \pm 1.00$, so $\mathrm{P} = 0.6827$ — the familiar 68%.
   (c) $z = -0.70$, so $\mathrm{P} = 0.2420$.
   (d) $z_{0.90} = 1.2816$, so the 90th percentile is
   $500 + 1.2816(100) = 628.1552$.

3. The top 5% means 5% in the **upper** tail, so $z = +1.6449$ and the cut-off is
   $500 + 1.6449(100) = 664.4854$. The sign is the thing to get right: a cut-off above
   the mean must have a positive $z$, and if your arithmetic returns something below
   500 you have used $-1.6449$ by mistake.

4. (a) $\lambda = 1/8 = 0.1250$ per minute. For an exponential the standard deviation
   equals the mean, so SD $= 8.0000$ minutes.
   (b) $\mathrm{P}(X > 10) = e^{-10/8} = e^{-1.25} = 0.2865$.
   (c) $\mathrm{P}(X < 5) = 1 - e^{-5/8} = 1 - 0.5353 = 0.4647$.
   (d) The median solves $e^{-\lambda m} = 0.5$, giving
   $m = \ln 2/\lambda = 0.6931 \times 8 = 5.5452$ minutes. It is below the mean
   because the exponential is strongly right-skewed — most waits are short and a few
   very long ones drag the mean up past the middle.

5. $\mathrm{P}(X > 15 \mid X > 5) = e^{-10/8} = 0.2865$, identical to 4(b). This is
   the **memoryless** property: the distribution of the remaining wait does not depend
   on how long you have already waited. It is the defining feature of the exponential
   and the reason it describes arrivals that have no pattern — the process does not
   know you are standing there.

6. Probability is the area under the density, and the area above a single point is a
   rectangle of zero width, hence zero. It does not mean $c$ is impossible, because
   *every* value has probability zero and yet one of them occurs. For a continuous
   variable, zero probability and impossibility are different things — which is why
   continuous questions are always asked about intervals, and why it makes no
   difference whether you write $<$ or $\leq$.

7. (a) **Normal** — a quantity built from many small additive influences.
   (b) **Exponential** — a waiting time with a constant failure rate.
   (c) **Uniform** — every value in the range equally likely by construction.
   (d) **Normal**, by the CLT — the giveaway is the word "sum".
   (e) **Exponential** — a gap between events in a memoryless process.

8. The two cut-offs are symmetric about the mean, so
   $\mu = (46 + 74)/2 = 60.0000$. Each is 14 away from the mean and sits at
   $z = \pm 1.96$, so $1.96\sigma = 14$ and $\sigma = 14/1.96 = 7.1429$. Reading a
   normal problem backwards like this — from the tails to the parameters — is exactly
   what confidence intervals will ask you to do in Chapter 13.

9. The $z$ is right and the probability is the **complement of the answer**. The
   student has looked up $\mathrm{P}(Z < 0.70) = 0.7580$, dropping the minus sign. For
   a negative $z$ the lower-tail area must be below 0.5, so 0.7580 should have been
   rejected on sight. The correct answer is $\mathrm{P}(Z < -0.70) = 0.2420$, and
   $0.2420 + 0.7580 = 1$ confirms the relationship between the two.

10. Because the two questions are about different random variables. A single score has
    standard deviation 100, so 650 is 1.5 standard deviations out — unusual but
    ordinary. A sample mean of 25 scores has standard error $100/\sqrt{25} = 20$, so
    650 is seven and a half standard errors out. Averaging destroys the extremes: for
    the mean of 25 students to exceed 650, essentially all of them have to be
    exceptional at once, and that is enormously rarer than one student being so.
""", [
    ("q1a mean", 30.0000, (10 + 50) / 2),
    ("q1a var", 133.3333, (50 - 10) ** 2 / 12),
    ("q1a sd", 11.5470, float(np.sqrt((50 - 10) ** 2 / 12))),
    ("q1b", 0.3750, (25 - 10) / 40),
    ("q1c", 0.3750, (35 - 20) / 40),
    ("q2a", 0.0668, float(stats.norm.sf(1.5))),
    ("q2b", 0.6827, float(stats.norm.cdf(1) - stats.norm.cdf(-1))),
    ("q2c", 0.2420, float(stats.norm.cdf(-0.7))),
    ("q2d z", 1.2816, float(stats.norm.ppf(0.90))),
    ("q2d percentile", 628.1552, float(500 + 100 * stats.norm.ppf(0.90))),
    ("q3 z", 1.6449, float(stats.norm.ppf(0.95))),
    ("q3 cutoff", 664.4854, float(500 + 100 * stats.norm.ppf(0.95))),
    ("q4a lambda", 0.1250, 1 / 8),
    ("q4a sd", 8.0000, 8.0),
    ("q4b", 0.2865, float(np.exp(-1.25))),
    ("q4c", 0.4647, float(1 - np.exp(-0.625))),
    ("q4c survival", 0.5353, float(np.exp(-0.625))),
    ("q4d ln2", 0.6931, float(np.log(2))),
    ("q4d median", 5.5452, float(np.log(2) * 8)),
    ("q5", 0.2865, float(np.exp(-1.25))),
    ("q8 mu", 60.0000, (46 + 74) / 2),
    ("q8 sigma", 7.1429, 14 / 1.96),
    ("q9 wrong", 0.7580, float(stats.norm.cdf(0.7))),
    ("q9 right", 0.2420, float(stats.norm.cdf(-0.7))),
])

# ---------------------------------------------------------------- chapter 10

BLOCKS["10_t_chi_f.md"] = (r"""
## More practice

Nine more. These are table-reading drills, and they are worth doing because a test
statistic computed perfectly and compared against the wrong critical value scores
zero.

1. Find each critical value.
   (a) $t_{0.025, 15}$. (b) $t_{0.05, 15}$. (c) $t_{0.025, 24}$.
   (d) $t_{0.025, 100}$. (e) $z_{0.025}$.

2. Look at your answers to 1(c), 1(d) and 1(e) together. What is happening as the
   degrees of freedom rise, and why?

3. Find each.
   (a) $\chi^2_{0.05, 10}$. (b) $\chi^2_{0.95, 10}$. (c) $\chi^2_{0.025, 20}$.

4. Why does the chi-squared distribution have two different critical values for a
   two-tailed problem at 5%, when the $t$ has one value used twice?

5. Find (a) $F_{0.05, 5, 10}$ and (b) $F_{0.05, 10, 5}$. Explain why they differ.

6. Verify that $\big(t_{0.025, 10}\big)^2 = F_{0.05, 1, 10}$, and explain the
   relationship between the two distributions that makes this true.

7. For each situation, name the distribution you would use.
   (a) Testing a mean with $\sigma$ known.
   (b) Testing a mean with $\sigma$ estimated from a sample of 18.
   (c) Testing whether three group means are all equal.
   (d) Testing whether observed counts match a claimed distribution.
   (e) Testing a mean with $\sigma$ estimated from a sample of 2,000.

8. A researcher has $n = 16$ and uses $z = 1.96$ because "the sample is large enough".
   (a) What should they have used?
   (b) By how much is their critical value too small, in percentage terms?
   (c) Which way does the error push their conclusions?

9. Explain, in two or three sentences each, where the degrees of freedom come from in
   (a) a one-sample $t$ test, (b) a chi-squared test on a $3 \times 4$ table, and
   (c) the numerator of an $F$ test comparing four group means.

### Answers to the extra problems

1. (a) **2.1314**. (b) **1.7531**. (c) **2.0639**. (d) **1.9840**.
   (e) **1.9600**.

2. The $t$ critical value is falling towards the $z$ value: 2.0639 at $\nu = 24$,
   1.9840 at $\nu = 100$, against 1.9600 for the normal. The $t$ is wider than the
   normal because $s$ is itself estimated and therefore uncertain, and that extra
   uncertainty has to be paid for with a longer interval. As $n$ grows, $s$ pins down
   $\sigma$ more and more tightly, the extra uncertainty vanishes, and the two
   distributions converge. By $\nu = 100$ the difference is in the second decimal
   place, which is why people get away with using $z$ — but it is a convenience, not a
   rule.

3. (a) **18.3070**. (b) **3.9403**. (c) **34.1696**.

4. Because the chi-squared distribution is **not symmetric**. It lives on $[0,
   \infty)$ and is right-skewed, so the point cutting off 2.5% in the upper tail is
   not the mirror image of the point cutting off 2.5% in the lower one, and both must
   be looked up separately. The $t$ is symmetric about zero, so one magnitude serves
   for both tails with a sign attached.

5. (a) **3.3258**. (b) **4.7351**. They differ because $F$ is a ratio of two
   variance estimates and the two degrees of freedom do different jobs — one describes
   the numerator, one the denominator. Swapping them is not a relabelling, it is a
   different distribution, which is why the convention "numerator first" has to be
   held to.

6. $t_{0.025, 10} = 2.2281$, and $2.2281^2 = 4.9646$, which is
   $F_{0.05, 1, 10} = 4.9646$. The reason: a $t$ variable is a standard normal over
   the square root of a scaled chi-squared, so squaring it gives a chi-squared with
   1 degree of freedom over a chi-squared with 10 — and that ratio is precisely an $F$
   with $\nu_1 = 1$ and $\nu_2 = 10$. The practical consequence is that a two-tailed
   $t$ test and an $F$ test on the same single parameter are the same test, which is
   why a regression's $t$ on a lone slope and its overall $F$ always agree.

7. (a) $z$. (b) $t$ with $\nu = 17$. (c) $F$. (d) $\chi^2$.
   (e) Strictly $t$ with $\nu = 1999$, which to four decimal places is $z$ — but write
   $t$, because what licenses $z$ is knowing $\sigma$, and a large $n$ only makes the
   $t$ look like a $z$.

8. (a) $t_{0.025, 15} = 2.1314$.
   (b) $(2.1314 - 1.96)/2.1314 = 8.0438\%$ too small.
   (c) Towards **over-rejection**. A critical value that is too small makes the
   rejection region too large, so the researcher rejects null hypotheses more often
   than their stated 5% allows — their real Type I error rate is above the one they
   are claiming.

9. (a) The deviations are taken from $\bar{x}$, which was itself computed from the
   data. Once $\bar{x}$ and any $n-1$ observations are known, the last one is
   determined, so only $n-1$ of the deviations are free. One estimated parameter costs
   one degree of freedom.
   (b) $(3-1)(4-1) = 6$. With the row and column totals fixed, you can fill in six
   cells freely and the remaining six are forced by the margins. The margins are not
   extra information — they are the data's own totals.
   (c) $k - 1 = 3$ for four groups. The between-group variation is built from four
   group means measured against the grand mean, and since the grand mean is a weighted
   average of those four, knowing three of them and the grand mean fixes the fourth.
""", [
    ("1a", 2.1314, float(stats.t.ppf(0.975, 15))),
    ("1b", 1.7531, float(stats.t.ppf(0.95, 15))),
    ("1c", 2.0639, float(stats.t.ppf(0.975, 24))),
    ("1d", 1.9840, float(stats.t.ppf(0.975, 100))),
    ("1e", 1.9600, float(stats.norm.ppf(0.975))),
    ("3a", 18.3070, float(stats.chi2.ppf(0.95, 10))),
    ("3b", 3.9403, float(stats.chi2.ppf(0.05, 10))),
    ("3c", 34.1696, float(stats.chi2.ppf(0.975, 20))),
    ("5a", 3.3258, float(stats.f.ppf(0.95, 5, 10))),
    ("5b", 4.7351, float(stats.f.ppf(0.95, 10, 5))),
    ("6 t", 2.2281, float(stats.t.ppf(0.975, 10))),
    ("6 F", 4.9646, float(stats.f.ppf(0.95, 1, 10))),
    ("8b", 8.0438, float(100 * (stats.t.ppf(0.975, 15) - 1.96)
                         / stats.t.ppf(0.975, 15))),
])

# ---------------------------------------------------------------- chapter 11

_se36 = 12 / np.sqrt(36)
_sep = float(np.sqrt(0.4 * 0.6 / 100))

BLOCKS["11_sampling.md"] = (r"""
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
""", [
    ("q1a SE", 2.0000, float(_se36)),
    ("q2a", 4.0000, 12 / 3),
    ("q2c", 1.0000, 12 / 12),
    ("q4a", 0.0668, float(stats.norm.sf(1.5))),
    ("q4b", 0.0228, float(stats.norm.cdf(-2.0))),
    ("q4c", 0.8664, float(stats.norm.cdf(1.5) - stats.norm.cdf(-1.5))),
    ("q5 n", 64, (12 / 1.5) ** 2),
    ("q8b mu", 5.0000, float(np.mean([2, 4, 6, 8]))),
    ("q8b sigma", 2.2361, float(np.std([2, 4, 6, 8]))),
    ("q8c SE", 1.5811, float(np.std([2, 4, 6, 8]) / np.sqrt(2))),
    ("q8c root2", 1.4142, float(np.sqrt(2))),
    ("q9a", 1.6971, float(12 / np.sqrt(50))),
    ("q9b factor", 0.9496, float(np.sqrt(450 / 499))),
    ("q9b corrected", 1.6116, float(12 / np.sqrt(50) * np.sqrt(450 / 499))),
    ("q10a", 0.0490, _sep),
    ("q10b z", 2.0412, float(0.10 / _sep)),
    ("q10b p", 0.0206, float(stats.norm.sf(0.10 / _sep))),
])
