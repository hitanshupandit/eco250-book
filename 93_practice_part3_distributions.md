# Practice: distributions

Chapters 8 to 10 — the binomial, continuous distributions, and $t$, chi-squared and $F$.

Fifteen problems. Work them with the solutions covered — reading a worked answer and producing one are different skills, and only the second is any use with a clock running.

Keep **four decimal places** unless a question says otherwise.

---

**1.** 20% of parcels are flagged for inspection. 14 are processed
independently.

(a) State the four binomial conditions and confirm each.
(b) Find $\mathrm{P}(X = 4)$.
(c) Find $E(X)$ and $\sigma$.

**2.** For the same binomial, find $\mathrm{P}(X \le 2)$, and explain why this is not
$1 - \mathrm{P}(X \ge 2)$.

**3.** For each, say whether the binomial applies; if not, name the failing condition.

(a) Number of sixes in 20 rolls of a fair die.
(b) Number of red cards in 10 drawn from a deck without replacement.
(c) Number of emails arriving between 2 and 3 pm.
(d) Number of defective bulbs in 40 drawn from a shipment of 50,000.

**4.** Monthly spend is normal with $\mu = 340$ and
$\sigma = 45$.

(a) Find the fraction above 400.
(b) Find the fraction between 280 and 400.
(c) Above what level do the top 2.5\% fall?

**5.** Processing times are uniform between 8 and 32 minutes.

(a) Find the mean and standard deviation.
(b) Find $\mathrm{P}(X < 20)$.
(c) Find $\mathrm{P}(15 < X < 25)$.

**6.** Time between machine faults is exponential with a mean of 6 days.

(a) Find the probability of more than 9 days without a fault.
(b) Find the probability a fault occurs within 3 days.
(c) State the standard deviation.

**7.** A classmate computes $\mathrm{P}(X = 25) = 0.031$ for a continuous variable.

(a) What is wrong?
(b) What have they most likely computed?
(c) What would a sensible question have asked?

**8.** Using Stata functions or tables, find:

(a) $t_{0.025,\,19}$ (b) $t_{0.05,\,29}$ (c) $\chi^2_{0.05,\,12}$
(d) $F_{0.05,\,4,\,15}$

**9.** Explain, in two sentences and without formulas, why the $t$ distribution has
fatter tails than the normal.

**10.** A sample of $n = 20$ gives $\bar{x} = 46$ and $s = 10$, against a claimed mean of
40.

(a) Should you use $z$ or $t$, and why?
(b) How many degrees of freedom?
(c) Compute the test statistic.

**11.** Why can a chi-squared value never be negative, and why is the distribution
right-skewed? Answer from the construction, not from a table.

**12.** A classmate computes $F_{0.05,\,12,\,4}$ when the question asked for
$F_{0.05,\,4,\,12}$.

(a) Does the order matter?
(b) Give both values.
(c) Why are they different?

**13.** A binomial has $n = 50$ and $p = 0.06$.

(a) Check whether the normal approximation is appropriate.
(b) State the rule you applied.
(c) What should you use instead if it fails?

**14.** $X \sim \text{Bin}(n, 0.4)$ has a standard deviation of 3.0984.

(a) Find $n$.
(b) Find $E(X)$.
(c) Find $\mathrm{P}(X = 0)$.

**15.** Match each to the distribution you would use, and say why in a few words:

(a) The number of defective items in 25 independent draws.
(b) The time until the next customer arrives.
(c) A measurement that is equally likely anywhere in a range.
(d) The sum of many small independent effects.

---

# Solutions

**1.** (a) Fixed $n = 14$; two outcomes (flagged or not); constant
$p = 0.2$; independent processing.
(b) $\binom{14}{4}(0.2)^4(0.8)^{10} = 1001 \times 0.0016 \times 0.1074
= 0.1720$.
(c) $E(X) = 2.8$ and $\sigma = \sqrt{14(0.2)(0.8)} = 1.4967$.

**2.** $\mathrm{P}(X \le 2) = \mathrm{P}(0) + \mathrm{P}(1) + \mathrm{P}(2)
= 0.4481$.

It is not $1 - \mathrm{P}(X \ge 2)$ because both events include $X = 2$, so they
overlap rather than partition. The correct complement of $X \le 2$ is $X \ge 3$.

**3.** (a) **Yes** — all four hold, with $p = 1/6$.
(b) **No** — drawing without replacement makes $p$ change between draws, and 10 of 52
is too large a fraction to ignore.
(c) **No** — there is no fixed number of trials.
(d) **Yes**, effectively. Strictly without replacement, but 40 from 50,000 leaves $p$
constant to any accuracy that matters.

**4.** (a) $z = (400-340)/45 = 1.3333$, so
$\mathrm{P} = 0.0912$.
(b) $z = -1.3333$ and $z = 1.3333$, giving
$0.8176$.
(c) $z = 1.959964$, so $x = 340 + 1.959964(45) = 428.20$.

**5.** (a) $\mu = (8+32)/2 = 20$;
$\sigma = 24/\sqrt{12} = 6.9282$.
(b) $(20-8)/24 = 0.5000$.
(c) $(25-15)/24 = 0.4167$.

**6.** (a) $e^{-9/6} = e^{-1.5} = 0.2231$.
(b) $1 - e^{-3/6} = 1 - 0.6065 = 0.3935$.
(c) **6 days** — for an exponential the standard deviation equals the mean.

**7.** (a) For a continuous variable the probability of any exact value is zero.
(b) The **density** at 25, which is a height, not a probability — and heights can even
exceed 1.
(c) An interval: $\mathrm{P}(24.5 < X < 25.5)$, or $\mathrm{P}(X < 25)$.

**8.** (a) 2.0930 — `invt(19, 0.975)`
(b) 1.6991 — `invt(29, 0.95)`
(c) 21.0261 — `invchi2(12, 0.95)`
(d) 3.0556 — `invF(4, 15, 0.95)`

**9.** The $t$ divides by $s$ rather than $\sigma$, and $s$ is itself random — it varies
from sample to sample instead of being a fixed number. When $s$ happens to come out
small the whole ratio is pushed far from zero, so extreme values arise more often than
the normal predicts.

**10.** (a) **$t$** — $\sigma$ is unknown and $s$ was estimated from the same 20
observations.
(b) $\nu = 19$.
(c) SE $= 10/\sqrt{20} = 2.2361$, so $t = (46-40)/2.2361 = 2.6833$.

**11.** A $\chi^2_\nu$ is the sum of $\nu$ **squared** standard normals. Every term is a
square, so every term is at least zero and so is the sum. It is right-skewed because
squaring stretches large deviations far more than small ones, so the upper tail is
pulled out while the lower end is bounded at zero.

**12.** (a) **Yes**, very much.
(b) $F_{0.05,4,12} = 3.2592$ and $F_{0.05,12,4} = 5.9117$.
(c) $F$ is a ratio of two chi-squareds, each divided by its own degrees of freedom.
Swapping them swaps which group is in the numerator, which is a different question
entirely.

**13.** (a) $np = 50(0.06) = 3$, which is **below 5**, so the approximation is not
appropriate. ($n(1-p) = 47$ passes, but both must.)
(b) The approximation needs $np \ge 5$ **and** $n(1-p) \ge 5$.
(c) The exact binomial — `binomial()` in Stata, or the formula directly.

**14.** (a) $\sigma^2 = n(0.4)(0.6) = 0.24n = 3.0984^2 = 9.6$, so $n = 40$.
(b) $E(X) = 40(0.4) = 16$.
(c) $(0.6)^{40} = 1.33 \times 10^{-9}$ — effectively zero.

**15.** (a) **Binomial** — a fixed number of independent two-outcome trials.
(b) **Exponential** — waiting time until the next event at a constant rate.
(c) **Uniform** — a flat density over the range.
(d) **Normal** — by the Central Limit Theorem, sums of many small independent effects
tend to a bell whatever the pieces look like.

---
