# Practice problems

Twenty problems covering everything from the start of the course through
hypothesis testing. They are in book order, so if you are stuck on one, the
chapter it belongs to is the one to reread.

Work them with the solutions covered. Reading a worked answer and producing one
are different skills, and only the second is any use with a clock running.

Keep **four decimal places** throughout unless the question says otherwise.

---

## Describing data

**1.** A customer service centre logs the number of complaints received on each of
seven consecutive working days:

$$4,\quad 6,\quad 6,\quad 9,\quad 11,\quad 13,\quad 14$$

(a) Compute the mean, the median and the mode.
(b) Compute the sample variance and the sample standard deviation.
(c) The day with 14 complaints is found to have been recorded twice by mistake and
should have read 28. Without recomputing from scratch, state what happens to the
mean and to the median, and explain why they behave differently.

**2.** Two branches of a bank record the time customers wait to be served. Branch A
has a mean wait of 42 seconds with a standard deviation of 6 seconds.
Branch B has a mean of 78 seconds with a standard deviation of 9
seconds.

(a) Which branch has the larger absolute variation in waiting times?
(b) The coefficient of variation is $s / \bar{x}$, expressed as a percentage.
Compute it for both branches.
(c) A regional manager claims Branch B is "less consistent" because its standard
deviation is larger. Is that a fair reading? Answer in one sentence.

**3.** A logistics firm finds that delivery times have a mean of 3.2 days and a
standard deviation of 0.6 days.

(a) A shipment takes 4.7 days. Compute its $z$-score and say in words what it means.
(b) A second shipment takes 2.0 days. Compute its $z$-score.
(c) Which of the two is more unusual, and does the answer depend on knowing the
shape of the distribution?

**4.** A haulage company reports that the distances its vehicles travel per day have
a mean of 40 km and a standard deviation of 10 km. A contract requires
the figures in miles, where 1 km = 0.621371 miles.

(a) What is the mean distance in miles?
(b) What is the standard deviation in miles?
(c) What would happen to the standard deviation if, instead, every driver were
required to travel an extra 5 km per day on top of their current distance?

**5.** A retailer records monthly advertising spend $x$ (in thousands of dollars)
and sales $y$ (in thousands of units) for five months:

| Advertising ($x$) | 2 | 4 | 6 | 8 | 10 |
|---|---|---|---|---|---|
| Sales ($y$) | 14 | 18 | 20 | 26 | 32 |

(a) Compute $\bar{x}$ and $\bar{y}$.
(b) Compute the sample covariance $s_{xy}$.
(c) Compute the coefficient of correlation $r$ and describe the relationship in one
sentence.

**6.** Using the data in Question 5:

(a) Advertising spend is restated in dollars rather than thousands, so every $x$ is
multiplied by 1,000. What is the new covariance?
(b) What is the new correlation?
(c) Explain, in terms of the formulas, why one of them changed and the other did not.

---

## Probability

**7.** For two events $A$ and $B$, $\mathrm{P}(A) = 0.42$, $\mathrm{P}(B) = 0.37$
and $\mathrm{P}(A \cap B) = 0.15$.

(a) Find $\mathrm{P}(A \cup B)$.
(b) Find the probability that neither $A$ nor $B$ occurs.
(c) Are $A$ and $B$ independent? Justify with a calculation.

**8.** A credit union classifies 400 loan applications by outcome and by whether
the applicant is a first-time or a repeat borrower:

| | First-time | Repeat | Total |
|---|---|---|---|
| Approved | 180 | 120 | 300 |
| Declined | 70 | 30 | 100 |
| Total | 250 | 150 | 400 |

(a) What is the probability that a randomly chosen application was approved?
(b) What is the probability that an application was approved, given that it came
from a repeat borrower?
(c) Are "approved" and "repeat borrower" independent events? Show the calculation
that settles it.

**9.** A manufacturer sources one component from three plants. Riverside supplies
50% of units with a defect rate of 2%; Eastgate
supplies 30% with a defect rate of 4%; Northfield
supplies 20% with a defect rate of 6%.

(a) What proportion of all units are defective?
(b) A unit fails inspection. What is the probability it came from Northfield?
(c) Northfield supplies the smallest share. Explain in one sentence why it is
nonetheless a serious suspect.

---

## Random variables

**10.** The number of vehicles hired per day from a small depot has the following
distribution:

| $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $\mathrm{P}(X = x)$ | 0.1 | 0.25 | 0.3 | 0.25 | 0.1 |

(a) Verify that this is a valid probability distribution.
(b) Compute $E(X)$.
(c) Compute $V(X)$ and the standard deviation of $X$.

**11.** The depot in Question 10 charges \$45 per hire and has fixed daily
costs of \$200, so daily revenue net of fixed costs is
$R = 45X - 200$.

(a) Find $E(R)$.
(b) Find $V(R)$ and the standard deviation of $R$.
(c) The owner proposes raising the fixed costs to \$300. What happens to $E(R)$,
and what happens to $V(R)$?

**12.** Two product lines have monthly profits $X$ and $Y$ with
$V(X) = 16$, $V(Y) = 25$ and $\mathrm{COV}(X, Y) = 6$
(all in squared thousands of dollars).

(a) Find $V(X + Y)$.
(b) Find $V(X - Y)$.
(c) The firm can change its product mix so that the two profits become uncorrelated.
Would that raise or lower the variance of total profit, and by how much?

---

## Distributions

**13.** A quality inspector knows that 25% of items coming off a line require
rework. A sample of 12 items is drawn independently.

(a) State the four conditions for a binomial experiment and confirm each one here.
(b) Find the probability that exactly 3 items require rework.
(c) Find $E(X)$ and the standard deviation of $X$.

**14.** A firm sends out 8 invoices. Each has, independently, a 15%
probability of being queried by the customer.

(a) Find the probability that none of them is queried.
(b) Find the probability that at least one is queried.
(c) Explain why (b) is much easier to compute via (a) than directly.

**15.** Monthly electricity use in a district is normally distributed with a mean of
850 kWh and a standard deviation of 120 kWh.

(a) What proportion of households use more than 1,000 kWh?
(b) What proportion use between 700 and 1,000 kWh?
(c) Above what level of use does a household fall in the top 10%?

**16.** Using the distribution in Question 15, a household uses 1,090 kWh.

(a) Compute its $z$-score.
(b) What proportion of households use more than this?
(c) Explain why the answer to (a) can be interpreted without opening a table at all.

---

## From sample to population

**17.** A random sample of 36 households is drawn from the district in
Question 15.

(a) State the mean and the standard error of the sampling distribution of
$\bar{X}$.
(b) Find $\mathrm{P}(\bar{X} > 880)$.
(c) The distribution of household use turns out to be right-skewed rather than
normal. Does your answer to (b) survive? Explain.

**18.** A sample of 49 invoices has a mean value of \$63.4 and a sample
standard deviation of \$8.4.

(a) Compute the standard error of the mean.
(b) Construct a 95% confidence interval for the population mean invoice value.
(c) Explain precisely what the phrase "95% confident" refers to.

**19.** The finance department's planning model assumes the mean invoice value is
\$60. Use the sample in Question 18.

(a) State $H_0$ and $H_a$, and say whether the test is one-tailed or two-tailed.
(b) Compute the test statistic.
(c) Test at $\alpha = 0.05$ and state the conclusion in a sentence about invoices.
(d) Confirm that your answer agrees with the interval from Question 18(b).

**20.** The department wants to re-estimate the mean invoice value to within
\$2.00 at 95% confidence, and is willing to assume $\sigma \approx 8.4$.

(a) How many invoices must be sampled?
(b) How many would be needed to halve the margin to \$1.00?
(c) What does the comparison tell you about the cost of precision?

---

# Solutions

**1.** (a) $\bar{x} = 63/7 = 9$. Sorted, the middle value is
9, so the median is 9. The mode is 6.
(b) Deviations are $-5, -3, -3, 0, 2, 4, 5$, which square and sum to 88. So
$s^2 = 88/6 = 14.6667$ and $s = 3.8297$.
(c) The mean rises by $14/7 = 2$ to 11. The median does not move at
all. The mean uses the size of every observation, so a change of 14 in one value
moves it; the median uses only the rank order, and 28 occupies the same position
that 14 did.

**2.** (a) Branch B, with a standard deviation of 9 seconds against
6.
(b) Branch A: $6/42 = 0.1429$, or 14.29%. Branch B:
$9/78 = 0.1154$, or 11.54%.
(c) No. Relative to its own mean, Branch B is the **more** consistent of the two —
its variation is 11.54% of its average wait against 14.29% for Branch A. The
manager compared standard deviations across series with very different means.

**3.** (a) $z = (4.7 - 3.2)/0.6 = 2.5000$ — the shipment took two and a
half standard deviations longer than average.
(b) $z = (2.0 - 3.2)/0.6 = -2.0000$.
(c) The 4.7-day shipment, since $|2.5| > |-2.0|$. Comparing
$z$-scores requires no assumption about shape; converting them into probabilities
does.

**4.** (a) $40 \times 0.621371 = 24.8548$ miles.
(b) $10 \times 0.621371 = 6.2137$ miles. Multiplying every value by a
constant multiplies the standard deviation by that same constant.
(c) Nothing. Adding a constant shifts every value equally and leaves the spread
unchanged — $V(X + b) = V(X)$.

**5.** (a) $\bar{x} = 6$, $\bar{y} = 22$.
(b) The deviation products are $32, 8, 0, 8, 40$, summing to 88, so
$s_{xy} = 88/4 = 22.00$.
(c) $s_x = \sqrt{40/4} = 3.1623$ and $s_y = \sqrt{200/4} = 7.0711$, so
$r = 22.00/(3.1623 \times 7.0711) = 0.9839$. A very strong positive linear
relationship: higher advertising spend goes with higher sales, and the points lie
close to a straight line.

**6.** (a) $s_{xy} \times 1{,}000 = 22,000$.
(b) Unchanged at $0.9839$.
(c) Covariance carries the units of $x$ times the units of $y$, so rescaling $x$
rescales it. Correlation divides the covariance by $s_x s_y$, and the 1,000 appears
in both the numerator and in $s_x$, so it cancels. That cancellation is the whole
reason $r$ is reported rather than $s_{xy}$.

**7.** (a) $\mathrm{P}(A \cup B) = 0.42 + 0.37 - 0.15 = 0.64$.
(b) $1 - 0.64 = 0.36$.
(c) If independent, $\mathrm{P}(A \cap B)$ would equal
$0.42 \times 0.37 = 0.1554$. It is 0.15, so they are **not** independent.

**8.** (a) $300/400 = 0.75$.
(b) Restrict to the repeat column:
$120/150 = 0.80$.
(c) Not independent. $\mathrm{P}(\text{approved}) = 0.75$ but
$\mathrm{P}(\text{approved} \mid \text{repeat}) = 0.80$.
Knowing the applicant is a repeat borrower changes the probability, which is exactly
what dependence means.

**9.** (a) Total probability:
$(0.5)(0.02) + (0.3)(0.04) + (0.2)(0.06) = 0.0340$.
(b) Bayes:
$(0.2)(0.06)/0.0340 = 0.3529$.
(c) Because the defect rate matters as much as the share: Northfield ships the
fewest units but spoils the highest fraction of them, so it accounts for
35.3% of all defects despite supplying only
20% of output.

**10.** (a) All five probabilities are non-negative and sum to
1.00. Valid.
(b) $E(X) = 2.0$.
(c) $E(X^2) = 5.3$, so $V(X) = 5.3 - 2.0^2 = 1.3$ and
$\sigma = 1.1402$.

**11.** (a) $E(R) = 45(2.0) - 200 = -110$.
(b) $V(R) = 45^2(1.3) = 2632.5$, so
$\sigma_R = 51.3079$.
(c) $E(R)$ falls by 100, to -210. $V(R)$ does not change at all —
a constant shifts the distribution without stretching it.

**12.** (a) $V(X + Y) = 16 + 25 + 2(6) = 53$.
(b) $V(X - Y) = 16 + 25 - 2(6) = 29$.
(c) It would **lower** it, from 53 to 41, a fall of
12. Positively correlated lines rise and fall together, which makes the
total more volatile than the parts suggest — the argument for diversification, in
one line of algebra.

**13.** (a) A fixed number of trials ($n = 12$); two outcomes per trial (rework or
not); constant probability ($p = 0.25$); independent draws. All four hold.
(b) $\mathrm{P}(X = 3) = \binom{12}{3}(0.25)^3(0.75)^{9} = 220 \times 0.015625 \times 0.075085 = 0.2581$.
(c) $E(X) = 12(0.25) = 3.0$ and
$\sigma = \sqrt{12(0.25)(0.75)} = 1.5$.

**14.** (a) $(0.85)^{8} = 0.2725$.
(b) $1 - 0.2725 = 0.7275$.
(c) "At least one" covers the eight separate cases $X = 1, 2, \ldots, 8$, each
needing its own binomial term. Its complement is the single case $X = 0$. Computing
one term and subtracting from 1 replaces eight calculations with one.

**15.** (a) $z = (1000 - 850)/120 = 1.2500$, so the
proportion is $1 - 0.8944 = 0.1056$.
(b) $700 \to z = -1.2500$ and $1000 \to z = 1.2500$,
giving $0.8944 - 0.1056 = 0.7887$.
(c) The top 10% begins at $z = 1.2816$, so at
$850 + 1.2816(120) = 1003.79$ kWh.

**16.** (a) $z = (1090 - 850)/120 = 2.0000$.
(b) $1 - 0.9772 = 0.0228$.
(c) A $z$ of 2.0 already says the household is two standard
deviations above average, which is a complete answer to "how unusual is this?" The
table only converts that into a proportion.

**17.** (a) $E(\bar{X}) = 850$ and
$\sigma_{\bar{X}} = 120/\sqrt{36} = 20$.
(b) $z = (880 - 850)/20 = 1.5000$, so
$\mathrm{P}(\bar{X} > 880) = 0.0668$.
(c) Yes. The Central Limit Theorem makes the sampling distribution of $\bar{X}$
approximately normal for $n = 36$ whatever the population's shape. Note what
does *not* survive: a probability statement about a **single** household would now
require the population to be normal, and it is not.

**18.** (a) $8.4/\sqrt{49} = 1.2$.
(b) With $\nu = 48$, $t_{0.025} = 2.0106$, so the interval is
$63.4 \pm 2.0106(1.2) = (60.9872,\ 65.8128)$.
(c) It describes the **procedure**, not this interval. If the whole exercise were
repeated many times, 95% of the intervals constructed this way would contain $\mu$.
This particular interval either does or does not, and we will never know which.

**19.** (a) $H_0: \mu = 60$ against $H_a: \mu \neq 60$. The
question gives no direction — the model simply "assumes" a value — so it is
**two-tailed**.
(b) $t = (63.4 - 60)/1.2 = 2.8333$ with $\nu = 48$.
(c) The critical values are $\pm2.0106$. Since
$2.8333 > 2.0106$, reject $H_0$ ($p = 0.0067$). The sample gives
strong evidence that the mean invoice value is not \$60 — it appears to be
about \$3.4 higher, so the planning model understates it.
(d) The interval $(60.9872,\ 65.8128)$ does not contain 60. A
two-tailed test at $\alpha = 0.05$ rejects exactly when the 95% interval excludes
the claimed value, so the two agree, as they must.

**20.** (a) $n = \left(\dfrac{1.96 \times 8.4}{2.00}\right)^2 = 67.7633$,
so sample **68** invoices. Always round up.
(b) $n = \left(\dfrac{1.96 \times 8.4}{1.00}\right)^2 = 271.0533$,
so **272**.
(c) Halving the margin does not double the sample, it **quadruples** it. Precision
is bought at a rate of $\sqrt{n}$, so each further improvement costs more than the
last.

---
