# Practice: from sample to population

Chapters 11 to 14 — sampling distributions, the CLT, estimation and hypothesis testing.

Fifteen problems. Work them with the solutions covered — reading a worked answer and producing one are different skills, and only the second is any use with a clock running.

Keep **four decimal places** unless a question says otherwise.

---

**1.** A population has $\mu = 80$ and $\sigma = 24$. A random sample of
36 is drawn.

(a) State $E(\bar{X})$ and the standard error.
(b) Find $\mathrm{P}(\bar{X} > 88)$.
(c) How large would $n$ need to be for the standard error to be 2?

**2.** For the population $\{2, 4, 6\}$:

(a) Find $\mu$ and $\sigma$.
(b) List all nine samples of size 2 drawn with replacement and their means.
(c) Verify $E(\bar{X}) = \mu$ and $\mathrm{SD}(\bar{X}) = \sigma/\sqrt{2}$.

**3.** A population is strongly left-skewed. A sample of $n = 45$ is drawn.

(a) What can you say about the distribution of $\bar{X}$?
(b) What can you say about the distribution of a single observation $X$?
(c) A classmate computes $\mathrm{P}(X < 30)$ using the normal table. What is wrong?

**4.** Explain why quadrupling the sample size only halves the standard error.

**5.** A sample of 25 observations gives $\bar{x} = 54.8$ and
$s = 7.5$.

(a) Compute the standard error.
(b) Build a 95\% confidence interval. Use $t_{0.025,24} = 2.0639$.
(c) State precisely what "95\% confident" refers to.

**6.** Using the sample above, a planning figure assumes the mean is 50.

(a) State $H_0$ and $H_a$, and the tail.
(b) Compute the test statistic.
(c) Test at $\alpha = 0.05$ and state the conclusion in words.
(d) Show your interval and your test agree.

**7.** A study wants to estimate a mean to within $\pm 1.0$ at 95\% confidence,
believing $\sigma \approx 7.5$.

(a) How many observations are needed?
(b) How many to get within $\pm 0.5$?
(c) What does the comparison show?

**8.** For each, state $H_0$, $H_a$ and the tail.

(a) A supplier guarantees a mean lifetime of at least 800 hours; you are the buyer.
(b) Last year's mean was 45; the department asks whether this year differs.
(c) A process is targeted at 250 g; quality control checks for drift.
(d) A trainer claims a new method raises mean scores above 70.

**9.** A test returns $p = 0.02$.

(a) Write what this means as a sentence.
(b) A classmate says "there is a 2% chance the null is true". Correct them.
(c) Another says "$p = 0.002$ would mean a bigger effect". Correct them too.

**10.** Complete the table and define each cell.

| | $H_0$ true | $H_0$ false |
|---|---|---|
| Reject | ? | ? |
| Do not reject | ? | ? |

**11.** A researcher runs 20 independent tests on data where no effect exists.

(a) How many would you expect to be "significant" at $\alpha = 0.05$?
(b) What is this phenomenon called when only the significant one is reported?
(c) Which of the eight steps of a hypothesis test guards against it?

**12.** A 95% confidence interval for a mean comes out as $(12.4,\ 18.6)$.

(a) What is the point estimate?
(b) What is the margin of error?
(c) Would a two-tailed test of $H_0: \mu = 19$ at $\alpha = 0.05$ reject? Explain
without computing anything.

**13.** Two studies estimate the same quantity at 95% confidence. Study A reports
$8.2 \pm 0.4$; Study B reports $8.2 \pm 3.6$.

(a) Which is more useful, and why?
(b) Give two distinct reasons B's interval might be so much wider.
(c) Do the two disagree?

**14.** Explain why "not significant" does not mean "no effect", and give a concrete
circumstance in which a real effect would be missed.

**15.** A survey of 1,500 people is drawn by selecting 375 households and interviewing
all adults in each. The report quotes a margin of error based on $n = 1{,}500$.

(a) Is the quoted margin too large, too small or about right?
(b) Why?
(c) What would you need to report an honest margin?

---

# Solutions

**1.** (a) $E(\bar{X}) = 80$ and $\sigma_{\bar{X}} = 24/\sqrt{36}
= 4$.
(b) $z = (88-80)/4 = 2.00$, so $\mathrm{P} = 0.0228$.
(c) Set $24/\sqrt{n} = 2$, so $\sqrt{n} = 12$ and $n = 144$.

**2.** (a) $\mu = 4$; $\sigma^2 = [(2-4)^2 + 0 + (6-4)^2]/3 = 8/3 = 2.6667$, so
$\sigma = 1.6330$.
(b) Means: 2, 3, 4, 3, 4, 5, 4, 5, 6 — that is $\bar{x} = 2,3,4,5,6$ with probabilities
$1/9, 2/9, 3/9, 2/9, 1/9$.
(c) $E(\bar{X}) = (2 + 6 + 12 + 10 + 6)/9 = 4 = \mu$. And $V(\bar{X}) = 4/3$, so
$\mathrm{SD}(\bar{X}) = 1.1547 = 1.6330/\sqrt{2}$.

**3.** (a) Approximately **normal**, by the Central Limit Theorem, with mean $\mu$ and
standard error $\sigma/\sqrt{45}$.
(b) Still **left-skewed**. Taking a sample does not change the population.
(c) The CLT applies to $\bar{X}$, not to $X$. A probability for a single observation
needs the population's actual shape, which is skewed — so the normal table gives the
wrong answer.

**4.** The standard error is $\sigma/\sqrt{n}$, so it depends on $\sqrt{n}$ rather than
$n$. Averaging cancels independent errors, but each new observation adds less than the
one before — the tenth improves a mean of nine far more than the thousandth improves a
mean of 999. The exponent $\tfrac{1}{2}$ is the exact rate of those diminishing
returns.

**5.** (a) $7.5/\sqrt{25} = 1.5$.
(b) $54.8 \pm 2.0639(1.5)
= (51.7042,\ 57.8958)$.
(c) It describes the **procedure**, not this interval. Repeat the whole exercise many
times and 95\% of the intervals built this way would contain $\mu$. This one either
does or does not, and we cannot know which.

**6.** (a) $H_0\!: \mu = 50$ against $H_a\!: \mu \neq 50$,
**two-tailed** — the figure is "assumed", with no direction given.
(b) $t = (54.8 - 50)/1.5 = 3.2000$ with
$\nu = 24$.
(c) $3.2 > 2.0639$, so **reject $H_0$**. The sample gives strong
evidence the mean is not 50; it appears about
4.8 higher.
(d) The interval $(51.7042, 57.8958)$ does **not** contain
50, which matches the rejection. A two-tailed test at $\alpha$ rejects
exactly when the $(1-\alpha)$ interval excludes the claimed value.

**7.** (a) $n = (1.96 \times 7.5 / 1.0)^2 = 216.08$, so
**217**.
(b) $n = (1.96 \times 7.5 / 0.5)^2 = 864.33$, so
**865**.
(c) Halving the margin **quadruples** the sample. Precision is bought at a rate of
$\sqrt{n}$, so each further improvement costs more than the last.

**8.** (a) $H_0: \mu = 800$, $H_a: \mu < 800$, **left** — a guarantee is tested from the
side of whoever it protects.
(b) $H_0: \mu = 45$, $H_a: \mu \neq 45$, **two-tailed** — "differs" names no direction.
(c) $H_0: \mu = 250$, $H_a: \mu \neq 250$, **two-tailed** — drift either way is a fault.
(d) $H_0: \mu = 70$, $H_a: \mu > 70$, **right** — "raises above" names a direction.

**9.** (a) "If $H_0$ were true, data at least this extreme would arise about 2 times in
100."
(b) Backwards. The $p$-value is computed **assuming** $H_0$ is true, so it cannot also
be the probability that $H_0$ is true.
(c) A smaller $p$ means the data sits **more awkwardly** with $H_0$, not that the effect
is larger. With a big enough sample a trivial effect produces a tiny $p$. Read the
confidence interval to judge size.

**10.** Reject when $H_0$ is **true**: a **Type I error**, probability $\alpha$ — declaring
an effect that is not there.
Reject when $H_0$ is **false**: a correct decision, probability $1 - \beta$, called the
**power**.
Do not reject when $H_0$ is **true**: a correct decision.
Do not reject when $H_0$ is **false**: a **Type II error**, probability $\beta$ —
missing a real effect.

**11.** (a) About **one** — $20 \times 0.05 = 1$.
(b) **$p$-hacking** (or selective reporting). The arithmetic in the reported test is
perfectly correct; the omission of the other nineteen is what makes it misleading.
(c) Steps 3 and 4 — setting $\alpha$ and writing the decision rule **before** seeing the
data, which fixes the test in advance and makes selective reporting visible.

**12.** (a) The midpoint, $(12.4 + 18.6)/2 = 15.5$.
(b) Half the width, $(18.6 - 12.4)/2 = 3.1$.
(c) **Yes.** 19 lies outside the interval, and a two-tailed test at $\alpha = 0.05$
rejects exactly when the 95% interval excludes the claimed value.

**13.** (a) **A** — the same estimate with far more precision, so it rules out many more
values.
(b) Any two of: B had a much smaller sample (the margin goes as $1/\sqrt{n}$, so a
nine-fold wider margin suggests a sample on the order of 80 times smaller); B's
population is more variable; B measured less precisely, inflating $s$.
(c) **No.** They agree exactly on the point estimate. They differ in precision, not in
finding — and A's interval sits entirely inside B's.

**14.** Failing to reject means the evidence was insufficient, not that $H_0$ is true. A
small sample produces a large standard error, so even a substantial real difference can
fall short of the critical value. Concretely: a six-point difference on a population
with $\sigma = 15$ is missed more than half the time at $n = 25$ — the test simply lacks
the power to detect it, and reporting that as "no effect" misrepresents what happened.

**15.** (a) **Too small.**
(b) $\sigma/\sqrt{n}$ counts independent pieces of information, and adults in the same
household are not independent — they share income, location and often views. The
effective sample size is well below 1,500.
(c) An estimate of the design effect — how much the clustering inflates the variance —
obtained by comparing the variability between households with the variability within
them.

---
