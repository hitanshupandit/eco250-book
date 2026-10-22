# Practice: describing data

Chapters 1 to 4 — population and sample, centre, spread, covariance and correlation.

Fifteen problems. Work them with the solutions covered — reading a worked answer and producing one are different skills, and only the second is any use with a clock running.

Keep **four decimal places** unless a question says otherwise.

---

**1.** A small clinic records the number of patients seen on each of six days:

$$18,\quad 22,\quad 22,\quad 25,\quad 29,\quad 34$$

(a) Find the mean, the median and the mode.
(b) Find the sample variance and standard deviation.
(c) The day with 34 is later corrected to 46. Say what happens to the mean and to
the median, and why they behave differently.

**2.** Two delivery depots record journey times. Depot A averages 30 minutes with
$s = 4$; Depot B averages 95 minutes with $s = 11$.

(a) Which has the larger absolute variation?
(b) Compute the coefficient of variation for each.
(c) A manager claims B is "less reliable". Is that fair?

**3.** Scores are bell-shaped with $\mu = 64$ and $\sigma = 9$.

(a) Convert 46, 64 and 82 to $z$-scores.
(b) Using the empirical rule, roughly what fraction lie between 55 and 73?
(c) Is a score of 90 unusual? Answer with a number.

**4.** A firm records advertising spend $x$ (in thousands) and complaints received $y$:

| $x$ | 3 | 6 | 9 | 12 | 15 |
|---|---|---|---|---|---|
| $y$ | 22 | 19 | 17 | 12 | 10 |

(a) Compute $\bar{x}$, $\bar{y}$ and $s_{xy}$.
(b) Compute $r$ and describe the relationship.
(c) Spend is restated in dollars, so every $x$ is multiplied by 1,000. What happens to
$s_{xy}$ and to $r$?

**5.** Classify each as categorical, discrete quantitative or continuous quantitative:
employee ID; number of sick days taken; hours worked last week; job grade (1 to 5);
annual salary.

**6.** A researcher wants to estimate mean household spending in a county.

(a) Describe a stratified design.
(b) Describe a cluster design.
(c) Which gives the more precise estimate for a given number of households, and which
is cheaper?

**7.** A website poll receives 1.8 million responses and reports a margin of error of
$\pm 0.07$ percentage points.

(a) What kind of error does that margin measure?
(b) What kind does it not measure?
(c) In one sentence, why is the figure close to meaningless here?

**8.** $V(X) = 49$, $V(Y) = 25$ and $\text{COV}(X,Y) = -15$.

(a) Find $V(X+Y)$.
(b) Find $V(X-Y)$.
(c) Explain which is larger and why.

**9.** A data set of eight values has deviations from the mean reported as
$-5, -2, -1, 0, 1, 2, 3, 3$.

(a) Something is wrong. What, and how can you tell with no other information?
(b) What would you check first?

**10.** Explain to someone who has not taken statistics why we report the median
household income rather than the mean.

**11.** For the sample $\{7, 11, 11, 14, 17, 20, 24\}$:

(a) Find the mean and median.
(b) Find the range and the sample standard deviation.
(c) Compare the mean and median and say what this suggests about shape.

**12.** Two variables have $r = 0$.

(a) Does that mean there is no relationship? Explain.
(b) Sketch a set of points with a strong relationship and $r \approx 0$.
(c) What should you always do before trusting a correlation?

**13.** A study finds that towns with more public libraries have higher average incomes.

(a) Give three distinct explanations consistent with this.
(b) Which, if any, justifies building libraries to raise income?

**14.** A sample of $n = 5$ gives $\sum x = 60$ and $\sum (x - \bar{x})^2 = 84$.

(a) Find $\bar{x}$, $s^2$ and $s$.
(b) Every value is then increased by 10. What are the new mean, variance and standard
deviation?
(c) Instead, every original value is multiplied by 3. Now what?

**15.** A quality manager reports: "the standard deviation of our output is 12 units, so
our daily average is accurate to within about 12 units." The sample had 144 days.

(a) What has been confused?
(b) What is the right figure?
(c) Why does the distinction matter?

---

# Solutions

**1.** (a) $\bar{x} = 150/6 = 25$. With $n=6$ the median is the average of
the 3rd and 4th: $(22+25)/2 = 23.5$. The mode is 22.
(b) Deviations $-7,-3,-3,0,4,9$ square to $49,9,9,0,16,81$, summing to
164. So $s^2 = 164/5 = 32.8$ and $s = 5.7271$.
(c) The mean rises by $12/6 = 2$ to 27. The median does not move at all — 46 occupies
the same rank 34 did, and the median reads only rank, not size.

**2.** (a) Depot B, with $s = 11$ against 4.
(b) A: $4/30 = 0.1333$, or 13.33%. B: $11/95 = 0.1158$, or
11.58%.
(c) No. Relative to its own average B is the **more** consistent. The manager compared
standard deviations across series with very different means, which is exactly what the
coefficient of variation exists to prevent.

**3.** (a) $z = (46-64)/9 = -2.00$; $z = 0$; $z = (82-64)/9 = +2.00$.
(b) 55 and 73 are $\mu \pm 1\sigma$, so about **68%**.
(c) $z = (90-64)/9 = 2.89$ — nearly three standard deviations above the mean, which the
empirical rule puts in the outer 0.3% or so. Yes, unusual.

**4.** (a) $\bar{x} = 9$, $\bar{y} = 16$. Deviations in $x$:
$-6,-3,0,3,6$; in $y$: $6,3,1,-4,-6$. Products: $-36,-9,0,-12,-36$, summing to $-93$,
so $s_{xy} = -93/4 = -23.25$.
(b) $s_x = 4.7434$, $s_y = 4.9497$, so
$r = -23.25/(4.7434 \times 4.9497) = -0.9903$ — very
strong and negative.
(c) $s_{xy}$ becomes $-23,250$. $r$ is unchanged at -0.9903,
because the 1,000 appears in the numerator and in $s_x$ and cancels.

**5.** Categorical: employee ID (a label despite being numeric); job grade (ordinal —
ordered, but the gaps are not meaningful quantities).
Discrete quantitative: number of sick days.
Continuous quantitative: hours worked; annual salary (treated as continuous in
practice, though strictly it comes in cents).

**6.** (a) Split the county into layers by a characteristic that matters — urban/rural,
or income band — and draw a random sample inside each, guaranteeing every layer appears.
(b) Split the county into geographic blocks, pick some blocks at random, and survey
every household in the chosen blocks.
(c) **Stratified** is more precise, because it forces balance across the layers.
**Cluster** is cheaper, because the interviewer travels to a few places rather than
everywhere. Chapter 11 shows the precision clustering costs.

**7.** (a) **Sampling error** — the variation that arises purely because you measured a
sample rather than everyone.
(b) **Non-sampling error** — self-selection, question wording, non-response.
(c) Respondents chose themselves, so the dominant error is non-sampling, and no sample
size fixes that; the margin is arithmetically correct and answers a question nobody
asked.

**8.** (a) $49 + 25 + 2(-15) = 44$.
(b) $49 + 25 - 2(-15) = 104$.
(c) The **difference** is far more variable. The two move in opposite directions, so
adding them partly cancels the swings while subtracting them compounds them.

**9.** (a) The deviations sum to $+1$, not zero. Deviations from the mean must sum to
exactly zero by construction, so either a value or the mean is wrong.
(b) Recompute the mean from the raw data. A mean that is slightly off is the usual
cause, and it shifts every deviation by the same small amount.

**10.** Income is strongly right-skewed: most households earn modest amounts and a few
earn enormous ones. The mean is a balance point and is pulled towards those few very
large values, so it sits well above what a typical household receives. The median is
the middle household and ignores how extreme the extremes are, so it answers the
question "what does a typical household earn?" far better.

**11.** (a) Sum is 104, so $\bar{x} = 104/7 = 14.8571$. With $n=7$ the median is the 4th
value, $14$.
(b) Range $= 24 - 7 = 17$. Deviations are $-7.8571, -3.8571, -3.8571, -0.8571, 2.1429,
5.1429, 9.1429$; their squares sum to $200.8571$, so $s^2 = 33.4762$ and $s = 5.7859$.
(c) The mean exceeds the median by about 0.86, so the data is mildly **right-skewed** —
a longer tail at the high end.

**12.** (a) No. $r$ measures **linear** association only. A perfect but curved relationship
can give $r = 0$.
(b) Any symmetric curve — a parabola $y = x^2$ over values of $x$ either side of zero,
or points arranged on a circle.
(c) Plot the data. A scatterplot shows curvature, clustering and outliers, none of which
a single number reveals.

**13.** (a) **Libraries raise income** (education and access to resources); **income
causes libraries** (wealthier towns fund more public services); or a **third variable**
— town size, or the age profile of residents — drives both.
(b) Only the first, and the correlation alone cannot distinguish it from the other two.
You would need an experiment, or a design that isolates the effect.

**14.** (a) $\bar{x} = 60/5 = 12$; $s^2 = 84/4 = 21$; $s = 4.5826$.
(b) Mean becomes 22. Variance and standard deviation are **unchanged** at 21 and 4.5826
— adding a constant shifts without stretching.
(c) Mean becomes 36. Variance becomes $3^2(21) = 189$ and the standard deviation
becomes $3(4.5826) = 13.7477$.

**15.** (a) The standard deviation of the **data** with the standard deviation of the
**mean**.
(b) The standard error is $12/\sqrt{144} = 1$ unit — twelve times smaller.
(c) Because 12 describes how much daily output varies, while 1 describes how precisely
144 days pin down the average. Reporting the first as if it were the second overstates
the uncertainty enormously and would lead to rejecting perfectly adequate precision.

---
