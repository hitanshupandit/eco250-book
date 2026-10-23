"""Extra practice for chapters 1-7. Imported by make_more_practice.py.

Each entry is (markdown, checks), where checks is a list of
(label, number_as_written, number_recomputed_here) triples.
"""

import numpy as np

BLOCKS = {}

# ---------------------------------------------------------------- chapter 1

BLOCKS["01_what_statistics_is_for.md"] = (r"""
## More practice

Eight more. These are mostly about *naming* things correctly, which sounds like the
easy part of the course and is the part people lose marks on in week one.

1. For each, name the population, the sample, and say whether the number given is a
   parameter or a statistic.
   (a) The registrar reports that the mean GPA of all 1,800 Bates students is 3.41.
   (b) A pollster calls 600 Maine voters and finds 54% support a bond measure.
   (c) A firm records the salary of every one of its 40 employees; the mean is
   \$58,200.

2. Classify each variable as nominal, ordinal, or interval/ratio.
   (a) Postcode. (b) Course grade (A, B, C, D, F). (c) Household income in dollars.
   (d) Jersey number. (e) Temperature in degrees Celsius. (f) Number of children.
   (g) Rank in a marathon. (h) Blood type.

3. Name the sampling design in each case.
   (a) Every 25th name on an alphabetical list of 5,000 members.
   (b) The college is split into four class years; 50 students are drawn at random
   from each.
   (c) Twelve of Maine's 490 towns are chosen at random, and *every* household in
   those twelve is surveyed.
   (d) A researcher posts a link on social media and analyses whoever replies.

4. A survey of commuting times is mailed to 4,000 households; 380 reply, and the mean
   reported commute is 19 minutes. The researcher plans to fix the problem by mailing
   to 40,000 households next time.
   (a) What kind of error is the main threat here?
   (b) Will the bigger mailing fix it? Explain in one sentence.
   (c) Which direction do you expect the bias to run, and why?

5. Explain the difference between a **sampling error** and a **nonsampling error**,
   and give one example of each from a study you could actually run at Bates.

6. A researcher wants the mean weekly spending of students at a college with 2,000
   students, 1,400 of whom live on campus and 600 off. Off-campus students spend far
   more on average, and there are fewer of them.
   (a) Which design would you use, and why?
   (b) If you drew 200 students by simple random sampling, roughly how many
   off-campus students would you expect, and what is the risk?

7. For each statement, say whether it is descriptive or inferential.
   (a) "The median wage in this sample of 300 workers is \$21.40."
   (b) "We are 95% confident the population mean lies between 19.8 and 23.0."
   (c) "Forty-two per cent of respondents said yes."
   (d) "The difference between the two groups is unlikely to be chance."

8. You are asked to estimate the mean number of hours Bates students sleep. Write
   down, in four lines, a design: who the population is, how you would draw the
   sample, what could go wrong, and one thing you would do to reduce that risk.

### Answers to the extra problems

1. (a) Population: all 1,800 Bates students. Sample: none — this is a census.
   3.41 is a **parameter**. (b) Population: all Maine voters. Sample: the 600 called.
   54% is a **statistic**. (c) Population: all 40 employees, and every one was
   measured, so \$58,200 is a **parameter** even though 40 sounds like a sample size.
   What makes something a parameter is that it describes the whole group you care
   about, not that the group is large.

2. (a) Nominal — a postcode is a label, and averaging postcodes is meaningless.
   (b) Ordinal — ordered, but the gap from A to B is not a measured quantity.
   (c) Interval/ratio. (d) **Nominal** — numerals used as names.
   (e) **Interval, not ratio** — 0°C is not "no temperature", so 20°C is not twice
   10°C. (f) Ratio. (g) Ordinal — first and second are ordered, but the time gap
   between them is unknown. (h) Nominal.

3. (a) Systematic. (b) Stratified, with class year as the stratum.
   (c) Cluster — whole towns are sampled and then enumerated.
   (d) A self-selected or convenience sample, which is not a probability sample at
   all, and no amount of statistics repairs it.

4. (a) **Nonsampling error** — specifically nonresponse bias. Only 9.5% replied.
   (b) **No.** A larger mailing with the same response rate gives you more of the
   same biased respondents; it shrinks the standard error around the wrong number.
   (c) Probably **upward**: people with unusually long or unusually memorable
   commutes have more reason to bother replying, so the sample over-represents them.

5. Sampling error is the difference between a sample statistic and the parameter that
   arises purely because you looked at some units and not others. It is unavoidable,
   it is random, and it shrinks as $n$ grows — that is what the whole second half of
   this course measures. Nonsampling error is everything else: a badly worded
   question, a frame that omits people, nonresponse, data entry mistakes. It does not
   shrink with $n$ and it is often not random. Example of each: drawing 100 students
   and getting a mean sleep of 6.9 hours when the true mean is 7.1 (sampling);
   sampling from a list of students who use the library, so you miss everyone who
   does not (nonsampling).

6. (a) **Stratified**, with on-campus and off-campus as strata. The two groups differ
   sharply on the thing being measured, which is exactly the condition under which
   stratifying buys precision.
   (b) About $200 \times 0.30 = 60$. The risk is not the expected count but the
   variability around it — an unlucky draw could give 40 or 80, and since off-campus
   spending is so different, the estimate would swing with it. Stratifying fixes the
   count at 60 by construction.

7. (a) Descriptive. (b) Inferential. (c) Descriptive. (d) Inferential.

8. One acceptable answer. **Population:** all currently enrolled Bates students.
   **Sample:** a stratified random sample of 150, drawn proportionally from the four
   class years using the registrar's list as the frame. **What could go wrong:**
   nonresponse, and specifically that students who are sleeping badly during exam
   period are the least likely to fill in a survey — the bias runs in a known
   direction. **Reduction:** run the survey in an ordinary teaching week rather than
   finals, and follow up twice with nonrespondents so the response rate is high
   enough that the people who never reply cannot dominate the answer.
""", [])

# ---------------------------------------------------------------- chapter 2

_d2 = np.array([12, 15, 15, 18, 22, 27, 31])
_d2o = np.append(_d2, 140)
_grow = np.array([1.10, 1.05, 0.95])

BLOCKS["02_centre.md"] = (r"""
## More practice

Ten more. The arithmetic is deliberately light; what is being tested is whether you
can say *which* centre answers the question in front of you.

1. For the data $12,\ 15,\ 15,\ 18,\ 22,\ 27,\ 31$:
   (a) Find the mean, median and mode.
   (b) Is the distribution left- or right-skewed? Say how you can tell from (a).

2. Add the value 140 to the data in question 1.
   (a) Recompute the mean and the median.
   (b) Which moved more, and by how much?
   (c) What does this tell you about which centre to report for house prices?

3. Five numbers have a mean of 24. Four of them are $18,\ 22,\ 27,\ 31$. Find the
   fifth.

4. A course is graded 20% coursework, 30% midterm, 50% final. A student scores 85,
   78 and 92.
   (a) Find the weighted mean.
   (b) Find the unweighted mean of the three scores, and explain in one sentence why
   it is the wrong number to report.

5. A survey records commuting time in four classes:

   | Minutes | 0–10 | 10–20 | 20–30 | 30–40 |
   |---|---|---|---|---|
   | Households | 8 | 12 | 15 | 5 |

   (a) Estimate the mean using class midpoints.
   (b) Which class contains the median?
   (c) Why is (a) an estimate rather than the mean?

6. An investment returns $+10\%$, then $+5\%$, then $-5\%$.
   (a) Find the arithmetic mean of the three returns.
   (b) Find the geometric mean return.
   (c) \$100 invested at the start — what is it worth at the end? Which of (a) and (b)
   reproduces that figure?

7. A firm reports that its mean salary is \$74,000 and its median salary is \$46,000.
   (a) What shape is the salary distribution?
   (b) The union quotes the median and management quotes the mean. Neither is lying.
   Explain what each is really saying.

8. For each, name the centre you would report and why.
   (a) The most common shoe size a shop should stock.
   (b) The typical household income of a US county.
   (c) The average exam mark in a class of 40 with no outliers.
   (d) The typical brand of car in a car park.

9. A dataset of 50 values has a mean of 30. Every value is then increased by 4, and
   the result is doubled. What is the new mean? State the rule you used.

10. "The mean is the balance point of the data." Explain what that sentence means
    arithmetically, using the fact that deviations from the mean sum to zero.

### Answers to the extra problems

1. (a) Sum $= 140$, so mean $= 140/7 = 20$. The middle value of seven sorted numbers
   is the fourth, so median $= 18$. Mode $= 15$, the only repeated value.
   (b) **Right-skewed.** Mean $>$ median $>$ mode, which is the signature of a long
   right tail — the large values 27 and 31 pull the mean up while leaving the middle
   value where it is.

2. (a) Sum $= 280$ over 8 values, so mean $= 35$. With eight values the median is the
   average of the fourth and fifth: $(18+22)/2 = 20$.
   (b) The mean moved **15** (from 20 to 35); the median moved **2** (from 18 to 20).
   One observation in eight shifted the mean by three-quarters of its original value.
   (c) Report the **median**. House prices have a long right tail and a handful of
   very expensive sales, and the mean describes none of the houses anyone is actually
   buying.

3. The five values sum to $5 \times 24 = 120$. The four given sum to 98. The fifth is
   $120 - 98 = 22$.

4. (a) $0.20(85) + 0.30(78) + 0.50(92) = 17 + 23.4 + 46 = 86.4$.
   (b) The unweighted mean is $255/3 = 85$. It is wrong because it treats the
   coursework, worth a fifth of the grade, as mattering as much as the final, worth a
   half — the weights *are* the question.

5. (a) Midpoints 5, 15, 25, 35 with frequencies 8, 12, 15, 5. The weighted total is
   $40 + 180 + 375 + 175 = 770$ over $n = 40$, so the estimated mean is **19.25**.
   (b) With 40 observations the median sits between the 20th and 21st. The cumulative
   counts are 8, 20, 35, 40 — so the 21st value is in the **20–30** class.
   (c) Because the individual values were thrown away. Using the midpoint assumes
   every household in the 20–30 class sits at exactly 25, and unless the values are
   symmetric within each class that is not true.

6. (a) $(10 + 5 - 5)/3 = 3.3333\%$.
   (b) The growth factors are 1.10, 1.05, 0.95, whose product is 1.09725. The
   geometric mean factor is $1.09725^{1/3} = 1.0314$, so **3.14%** a year.
   (c) \$100 becomes $100(1.09725) = \$109.73$. Compounding at 3.14% for three years
   gives $100(1.0314)^3 = \$109.73$; compounding at the arithmetic mean of 3.3333%
   gives \$110.34, which is too high. **The geometric mean is the one that reproduces
   the actual outcome**, and the arithmetic mean of growth rates always overstates it.

7. (a) Strongly **right-skewed** — the mean sits far above the median, so a small
   number of very large salaries are pulling it up.
   (b) The median says "half the staff earn under \$46,000", which is a statement
   about a typical employee. The mean says "total payroll divided by headcount is
   \$74,000", which is a statement about the wage bill. Both are true; they answer
   different questions, and the gap between them is itself the interesting number.

8. (a) **Mode** — a shop stocks the size most people ask for, and no one wears the
   mean size. (b) **Median** — income is right-skewed. (c) **Mean** — with no
   outliers it uses every observation and is the most efficient. (d) **Mode** — brand
   is nominal, so the mean and median do not exist.

9. Adding 4 shifts the mean to 34; doubling scales it to 68. The rule is that for a
   linear transformation, $\overline{aX+b} = a\bar{x} + b$ — here
   $2(30 + 4) = 68$.

10. If you place the observations on a number line as equal weights, the mean is the
    point at which the line balances. Arithmetically, that is the statement
    $\sum(x_i - \bar{x}) = 0$: the deviations above the mean and the deviations below
    it sum to exactly the same amount. No other point has that property, which is also
    why a single extreme value drags the mean so far — it is a long lever arm, and the
    balance point must move to compensate.
""", [
    ("q1 mean", 20, float(_d2.mean())),
    ("q1 median", 18, float(np.median(_d2))),
    ("q2 mean", 35, float(_d2o.mean())),
    ("q2 median", 20, float(np.median(_d2o))),
    ("q4 weighted mean", 86.4, float(0.20 * 85 + 0.30 * 78 + 0.50 * 92)),
    ("q5 grouped mean", 19.25,
     float(np.dot([5, 15, 25, 35], [8, 12, 15, 5]) / 40)),
    ("q6 arithmetic mean", 3.3333, float(np.mean([10, 5, -5]))),
    ("q6 geometric factor", 1.0314, float(_grow.prod() ** (1 / 3))),
    ("q6 product", 1.09725, float(_grow.prod())),
    ("q6 terminal value", 109.73, float(100 * _grow.prod())),
    ("q6 arithmetic overstatement", 110.34, float(100 * 1.0333333 ** 3)),
])

# ---------------------------------------------------------------- chapter 3

_d3 = np.array([4, 8, 10, 14, 19])

BLOCKS["03_spread.md"] = (r"""
## More practice

Ten more. Several of these can be done without computing a standard deviation at
all, which is the point — knowing what the formula *does* is worth more than being
able to grind it.

1. For the sample $4,\ 8,\ 10,\ 14,\ 19$:
   (a) Find the mean and set out the deviation table.
   (b) Find $s^2$ and $s$.
   (c) Find the range, and say what the range ignores that $s$ does not.

2. Treat the same five numbers as a whole population.
   (a) Find $\sigma^2$ and $\sigma$.
   (b) Which is larger, $s$ or $\sigma$, and why must that always be so?

3. Verify your answer to 1(b) using the shortcut $\sum x^2 - (\sum x)^2/n$.

4. Two funds are compared. Fund A has a mean annual return of 8% with a standard
   deviation of 12%; Fund B has a mean of 3% with a standard deviation of 6%.
   (a) Which is riskier in absolute terms?
   (b) Compute the coefficient of variation for each.
   (c) Which is riskier per unit of return, and why does that question need the CV
   rather than $s$?

5. Exam marks have $\mu = 70$ and $\sigma = 8$, and the distribution is bell-shaped.
   (a) Between which two marks do about 68% of students fall?
   (b) About 95%?
   (c) A student scores 86. How unusual is that?

6. Now suppose the same marks are *not* bell-shaped, and you know nothing about the
   shape.
   (a) What is the most you can say about the fraction within 2 standard deviations?
   (b) Within 2.5 standard deviations?
   (c) Why is this bound so much weaker than the answer to 5(b)?

7. Every value in a dataset with mean 40 and standard deviation 6 is increased by 10.
   (a) What happens to the mean?
   (b) What happens to the standard deviation? Explain using the deviation table.
   (c) Now every value is instead multiplied by 3. What are the new mean and standard
   deviation?

8. A student's score is 72 on a test with mean 65 and standard deviation 10, and 81
   on a test with mean 75 and standard deviation 4. On which did they do better
   relative to the class? Show the comparison.

9. A dataset has $s = 0$. What does the data look like? Can $s$ be negative?

10. Explain, in your own words and without the algebra, why the sample variance
    divides by $n - 1$ rather than $n$. Your answer must mention the word "mean".

### Answers to the extra problems

1. (a) Sum $= 55$, so $\bar{x} = 11$. Deviations: $-7, -3, -1, 3, 8$; squared:
   $49, 9, 1, 9, 64$, summing to **132**. (The deviations summing to zero is the free
   check: $-7-3-1+3+8 = 0$.)
   (b) $s^2 = 132/4 = 33.00$ and $s = 5.7446$.
   (c) Range $= 19 - 4 = 15$. The range uses only the two extreme values and throws
   away everything in between, so two datasets with the same range can have wildly
   different spreads. It is also, for that reason, maximally sensitive to a single
   outlier.

2. (a) $\sigma^2 = 132/5 = 26.40$ and $\sigma = 5.1381$.
   (b) $s$ is larger. Both divide the *same* sum of squares, 132, but $s$ divides by
   the smaller number, so the quotient is bigger. That is the whole correction: the
   deviations were taken from $\bar{x}$, which sits in the middle of this particular
   sample by construction, so they understate the spread around the true $\mu$, and
   dividing by $n-1$ inflates the answer to compensate.

3. $\sum x^2 = 16 + 64 + 100 + 196 + 361 = 737$, and $(\sum x)^2/n = 55^2/5 = 605$.
   The difference is $737 - 605 = 132$, matching the deviation table exactly. The
   shortcut is faster but tells you nothing about the shape of the data; the deviation
   table is slower and shows you which observations are doing the damage.

4. (a) **Fund A**, with a standard deviation of 12% against 6%.
   (b) CV$_A = 12/8 = 1.5000$; CV$_B = 6/3 = 2.0000$.
   (c) **Fund B** is riskier per unit of return. The question needs the CV because
   $s$ has units and B's returns are on a smaller scale — 6% of variation around a 3%
   mean is proportionally worse than 12% around 8%. Comparing raw standard deviations
   across series with different means answers a different question from the one asked.

5. (a) $70 \pm 8$, so about **62 to 78**.
   (b) $70 \pm 16$, so about **54 to 86**.
   (c) $z = (86-70)/8 = 2.00$, so the score is two standard deviations above the mean
   — at the top edge of the middle 95%, which puts roughly 2.5% of the class above it.

6. (a) Chebyshev gives at least $1 - 1/2^2 = 0.7500$, so **at least 75%**.
   (b) At least $1 - 1/2.5^2 = 1 - 1/6.25 = 0.8400$, so **at least 84%**.
   (c) Because it assumes nothing. The empirical rule's 95% is a statement about a
   specific shape; Chebyshev's 75% has to hold for *every* distribution including the
   nastiest one anyone can construct, so it is necessarily loose for well-behaved
   data. The price of needing no assumptions is a weaker conclusion.

7. (a) The mean becomes **50**.
   (b) **It does not change.** Each value rose by 10 and so did the mean, so every
   deviation $x_i - \bar{x}$ is exactly what it was. Shifting the data moves its
   location, not its spread.
   (c) Mean $= 120$, standard deviation $= 18$. Multiplying scales every deviation by
   3, and since $s$ is in the original units it scales by 3 too — note that $s^2$
   scales by 9.

8. Test 1: $z = (72-65)/10 = 0.7000$. Test 2: $z = (81-75)/4 = 1.5000$. The second
   score is 1.5 standard deviations above its class mean against 0.7 for the first, so
   **the 81 was the better performance relative to the class**, even though the raw
   gap above the mean was smaller in absolute terms on the test with the tighter
   spread.

9. Every value is identical and equal to the mean, so every deviation is zero. $s$
   **cannot** be negative: it is the square root of a sum of squares divided by a
   positive number, and that sum is zero at best.

10. The deviations are measured from the sample mean, and the sample mean is itself
    computed from the very data whose spread you are measuring. It sits, by
    construction, in the middle of this particular sample rather than at the
    population's true centre — so the squared deviations around it are systematically
    a little too small. Dividing by $n-1$ instead of $n$ makes the answer slightly
    larger, by exactly the right amount on average. The other way to say it: once you
    know $\bar{x}$ and any $n-1$ of the observations, the last one is determined, so
    only $n-1$ of the deviations are free to vary.
""", [
    ("q1 mean", 11, float(_d3.mean())),
    ("q1 SS", 132, float(((_d3 - _d3.mean()) ** 2).sum())),
    ("q1 s2", 33.00, float(_d3.var(ddof=1))),
    ("q1 s", 5.7446, float(_d3.std(ddof=1))),
    ("q1 range", 15, float(_d3.max() - _d3.min())),
    ("q2 sigma2", 26.40, float(_d3.var())),
    ("q2 sigma", 5.1381, float(_d3.std())),
    ("q3 sum of squares", 737, float((_d3 ** 2).sum())),
    ("q3 correction", 605, float(_d3.sum() ** 2 / len(_d3))),
    ("q4 CV A", 1.5000, 12 / 8),
    ("q4 CV B", 2.0000, 6 / 3),
    ("q6 chebyshev k=2", 0.7500, 1 - 1 / 2 ** 2),
    ("q6 chebyshev k=2.5", 0.8400, 1 - 1 / 2.5 ** 2),
    ("q8 z first", 0.7000, (72 - 65) / 10),
    ("q8 z second", 1.5000, (81 - 75) / 4),
])

# ---------------------------------------------------------------- chapter 4

_x4 = np.array([2, 4, 6, 8, 10], dtype=float)
_y4 = np.array([5, 9, 10, 14, 17], dtype=float)
_sxy = float(np.cov(_x4, _y4, ddof=1)[0, 1])
_r4 = float(np.corrcoef(_x4, _y4)[0, 1])

BLOCKS["04_covariance_correlation.md"] = (r"""
## More practice

Ten more. Question 5 is the one worth your time — portfolio variance is covariance
doing something useful, and it is the reason the topic is in an economics course
rather than a maths one.

1. For the pairs

   | $x$ | 2 | 4 | 6 | 8 | 10 |
   |---|---|---|---|---|---|
   | $y$ | 5 | 9 | 10 | 14 | 17 |

   (a) Set out the deviation table and find $s_{xy}$.
   (b) Find $s_x^2$ and $s_y^2$.
   (c) Find $r$ and interpret it.

2. Using the quantities from question 1, find $V(X+Y)$ and $V(X-Y)$. Explain why one
   is so much larger than the other.

3. The $x$ values in question 1 are measured in thousands of dollars and the $y$
   values in units sold. Suppose $x$ is re-expressed in dollars, so every value is
   multiplied by 1,000.
   (a) What happens to $s_{xy}$?
   (b) What happens to $r$?
   (c) What does this tell you about which of the two to quote in a report?

4. A researcher finds $r = -0.85$ between hours of television watched and exam marks,
   from 200 students.
   (a) Interpret the number.
   (b) Give three different explanations for the finding, only one of which is
   "television lowers marks".

5. A portfolio puts 60% of its money in asset 1 ($\sigma_1 = 10$) and 40% in asset 2
   ($\sigma_2 = 16$). The correlation between them is 0.30.
   (a) Find the covariance.
   (b) Find the variance and standard deviation of the portfolio return.
   (c) Now suppose the correlation were $-1$ instead. Recompute the standard
   deviation and say what has happened.

6. $X$ takes values $-2, -1, 0, 1, 2$ with equal probability, and $Y = X^2$.
   (a) Find the covariance of $X$ and $Y$.
   (b) Are $X$ and $Y$ independent?
   (c) What does this pair of answers tell you about what $r = 0$ does and does not
   mean?

7. A report states $s_x = 4$, $s_y = 9$ and $s_{xy} = 40$. One of these three numbers
   must be wrong. Explain how you know, and state the rule being violated.

8. For each, say whether you would expect the covariance to be positive, negative, or
   near zero. (a) Height and weight. (b) Price and quantity demanded.
   (c) Shoe size and IQ. (d) A firm's advertising spend and its sales.
   (e) Hours of sleep and hours spent on a phone at night.

9. Explain why covariance is almost never reported in a published paper even though
   correlation is reported constantly, when the two are computed from the same
   deviation table.

10. A diversified portfolio of 20 assets has a lower variance than any single asset in
    it, even though each asset is individually risky. Explain how, using the formula
    for the variance of a sum.

### Answers to the extra problems

1. (a) $\bar{x} = 6$ and $\bar{y} = 11$. Deviations in $x$: $-4, -2, 0, 2, 4$; in
   $y$: $-6, -2, -1, 3, 6$. Products: $24, 4, 0, 6, 24$, summing to 58. So
   $s_{xy} = 58/4 = 14.5000$.
   (b) Squared $x$ deviations sum to 40, so $s_x^2 = 10.0000$. Squared $y$ deviations
   sum to 86, so $s_y^2 = 21.5000$.
   (c) $s_x = 3.1623$, $s_y = 4.6368$, so
   $r = 14.5/(3.1623 \times 4.6368) = 0.9889$. Very strong positive linear
   association — the points sit almost exactly on a rising straight line.

2. $V(X+Y) = 10 + 21.5 + 2(14.5) = 60.5000$ and
   $V(X-Y) = 10 + 21.5 - 2(14.5) = 2.5000$. The two variables move together almost
   perfectly, so adding them compounds the movement while subtracting them cancels
   nearly all of it. The difference between the two answers is $4s_{xy} = 58$, and
   that term is where all the information about co-movement lives.

3. (a) It is multiplied by **1,000**, becoming 14,500. Covariance carries the units of
   both variables.
   (b) **Nothing.** $r$ is unchanged at 0.9889, because the 1,000 appears in both the
   numerator and in $s_x$ in the denominator, and cancels.
   (c) Quote $r$. A covariance of 14,500 and a covariance of 14.5 describe the
   identical relationship, so the number on its own tells a reader nothing until they
   know the units — whereas $-1 \leq r \leq 1$ always, and 0.99 means the same thing
   in every field.

4. (a) A strong negative linear association: students who watch more television tend
   to have lower marks, and the relationship is tight enough that knowing one tells
   you a good deal about the other.
   (b) (i) Television displaces study time, so it causes lower marks. (ii) Reverse
   causation — students who are struggling and have given up study watch more
   television. (iii) A third variable, such as household circumstances or a job
   outside college, drives both. The correlation is identical under all three, and
   nothing in $r$ distinguishes them.

5. (a) $\text{COV} = \rho\sigma_1\sigma_2 = 0.30(10)(16) = 48.0000$.
   (b) $V = 0.6^2(100) + 0.4^2(256) + 2(0.6)(0.4)(48) = 36 + 40.96 + 23.04 =
   100.0000$, so the standard deviation is **10.0000** — the same as asset 1 alone,
   despite 40% of the money sitting in the much riskier asset 2.
   (c) With $\rho = -1$ the covariance is $-160$, so
   $V = 36 + 40.96 - 76.8 = 0.1600$ and the standard deviation is **0.4000**. The two
   assets now almost exactly offset each other, and a portfolio of two risky assets is
   very nearly riskless. This is the whole argument for diversification, and it lives
   entirely in the covariance term.

6. (a) $E(X) = 0$ by symmetry, and $E(XY) = E(X^3) = 0$ for the same reason — the
   cubes $-8, -1, 0, 1, 8$ cancel in pairs. So
   $\text{COV} = E(XY) - E(X)E(Y) = 0 - 0 = 0$.
   (b) **No.** $Y$ is a deterministic function of $X$: tell me $X$ and I know $Y$
   exactly. Nothing could be less independent.
   (c) $r = 0$ rules out a *linear* relationship and nothing else. Here the
   relationship is perfect and the correlation cannot see it, because the parabola
   rises on one side and falls on the other and the two halves cancel in the deviation
   products. A scatterplot would show it immediately, which is why you plot before you
   compute.

7. Dividing out gives $r = 40/(4 \times 9) = 40/36 = 1.1111$, and a correlation
   cannot exceed 1. The rule is $|s_{xy}| \leq s_x s_y$: the covariance is bounded by
   the product of the two standard deviations, with equality only when the points lie
   exactly on a straight line. Here the reported covariance is larger than that
   product, so at least one of the three figures is mistyped. This is a worthwhile
   check to run on any table you are handed — it costs one multiplication and catches
   a transposed digit.

8. (a) Positive. (b) Negative. (c) Near zero. (d) Positive.
   (e) Negative.

9. Because the magnitude of a covariance is uninterpretable without knowing the units
   of both variables, and changing either unit changes the number without changing the
   relationship. Correlation is the same quantity with the units divided out, bounded
   between $-1$ and $1$, so a reader can judge it on sight. The covariance still does
   all the work — it is what gets reported whenever the units matter, as in the
   portfolio variance above.

10. $V(\sum X_i) = \sum V(X_i) + \sum\sum_{i \neq j}\text{COV}(X_i, X_j)$. The
    variance terms are all positive and cannot be reduced, but the covariance terms
    can be small, zero, or negative. With 20 assets there are 20 variance terms and
    380 covariance terms, so the covariances dominate the sum — and if the assets are
    weakly or negatively correlated, those 380 terms drag the total far below what the
    individual variances alone would suggest. Diversification is not about owning many
    things; it is about owning things whose covariances are low.
""", [
    ("q1 sxy", 14.5000, _sxy),
    ("q1 sx2", 10.0000, float(_x4.var(ddof=1))),
    ("q1 sy2", 21.5000, float(_y4.var(ddof=1))),
    ("q1 sx", 3.1623, float(_x4.std(ddof=1))),
    ("q1 sy", 4.6368, float(_y4.std(ddof=1))),
    ("q1 r", 0.9889, _r4),
    ("q2 V sum", 60.5000, float((_x4 + _y4).var(ddof=1))),
    ("q2 V diff", 2.5000, float((_x4 - _y4).var(ddof=1))),
    ("q5 cov", 48.0000, 0.30 * 10 * 16),
    ("q5 variance", 100.0000,
     0.6 ** 2 * 100 + 0.4 ** 2 * 256 + 2 * 0.6 * 0.4 * 48),
    ("q5 sd rho -1", 0.4000,
     float(np.sqrt(0.6 ** 2 * 100 + 0.4 ** 2 * 256 - 2 * 0.6 * 0.4 * 160))),
    ("q5 variance rho -1", 0.1600,
     float(0.6 ** 2 * 100 + 0.4 ** 2 * 256 - 2 * 0.6 * 0.4 * 160)),
    ("q7 implied r", 1.1111, 40 / 36),
])

# ---------------------------------------------------------------- chapter 5

BLOCKS["05_probability_rules.md"] = (r"""
## More practice

Ten more. Most probability mistakes at this level are not arithmetic — they are
reading $\mathrm{P}(A \mid B)$ when the question asked for $\mathrm{P}(B \mid A)$,
or multiplying when the draws are not independent. These are built to catch both.

1. Two hundred graduates are classified by whether they took a statistics course and
   whether they were employed within six months:

   | | Employed | Not employed | Total |
   |---|---|---|---|
   | **Took stats** | 60 | 40 | 100 |
   | **Did not** | 50 | 50 | 100 |
   | **Total** | 110 | 90 | 200 |

   (a) $\mathrm{P}(\text{employed})$.
   (b) $\mathrm{P}(\text{took stats and employed})$.
   (c) $\mathrm{P}(\text{employed} \mid \text{took stats})$.
   (d) $\mathrm{P}(\text{took stats} \mid \text{employed})$.
   (e) Are the two events independent? Show the check.

2. Why are the answers to 1(c) and 1(d) different? State in words what each one is
   the answer to.

3. $\mathrm{P}(A) = 0.4$, $\mathrm{P}(B) = 0.5$, $\mathrm{P}(A \cap B) = 0.2$.
   (a) Find $\mathrm{P}(A \cup B)$.
   (b) Find $\mathrm{P}(A \mid B)$.
   (c) Are $A$ and $B$ independent? Mutually exclusive? Answer both.

4. A machine produces items that are defective 20% of the time, independently.
   (a) Find the probability all three of the next three are good.
   (b) Find the probability at least one of the three is defective.
   (c) Which of these was easier to compute directly, and why does the complement
   rule exist?

5. A box holds 10 components, 3 of them faulty. Two are drawn **without**
   replacement.
   (a) Find the probability both are faulty.
   (b) Find the probability both are faulty if the draws are **with** replacement.
   (c) Explain which rule changed between (a) and (b).

6. In the same box of 10 with 3 faulty, two are drawn without replacement. Find the
   probability that **exactly one** is faulty.

7. A student says: "Mutually exclusive events are independent, because if one happens
   the other cannot, so they have nothing to do with each other." Explain why this is
   exactly backwards, using $\mathrm{P}(A \mid B)$.

8. Of a firm's invoices, 70% are domestic and 30% foreign. Of domestic invoices 5%
   are paid late; of foreign invoices 20% are.
   (a) Draw the tree and find the probability a randomly chosen invoice is paid late.
   (b) What fraction of all invoices are foreign *and* late?

9. A fair coin is tossed four times.
   (a) Find the probability of four heads.
   (b) A gambler who has just seen three heads says the next toss is "due" to be
   tails. What probability does the gambler have in mind, and what is the correct one?

10. Explain why $\mathrm{P}(A \cap B) = \mathrm{P}(A)\mathrm{P}(B)$ is a *test* for
    independence rather than a rule you may always apply.

### Answers to the extra problems

1. (a) $110/200 = 0.5500$. (b) $60/200 = 0.3000$. (c) $60/100 = 0.6000$.
   (d) $60/110 = 0.5455$.
   (e) Independence requires $\mathrm{P}(\text{stats} \cap \text{employed}) =
   \mathrm{P}(\text{stats})\mathrm{P}(\text{employed})$, that is
   $0.30 = 0.5(0.55) = 0.2750$. It does not, so the events are **not independent**.
   Equivalently, $\mathrm{P}(\text{employed} \mid \text{stats}) = 0.60$ against an
   unconditional 0.55 — knowing someone took the course changes the probability.

2. (c) takes the 100 students who took statistics as the denominator and asks what
   fraction of *them* were employed. (d) takes the 110 employed graduates as the
   denominator and asks what fraction of *them* took statistics. Different
   denominators, so different numbers, even though the numerator — the 60 people in
   both groups — is the same. Mixing the two up is the single most common error in
   this chapter and the next.

3. (a) $0.4 + 0.5 - 0.2 = 0.7000$.
   (b) $0.2/0.5 = 0.4000$.
   (c) **Independent**: $\mathrm{P}(A \mid B) = 0.40 = \mathrm{P}(A)$, so yes — or
   equivalently $0.4(0.5) = 0.2$ as required. **Mutually exclusive**: no, since
   $\mathrm{P}(A \cap B) = 0.2 \neq 0$. Note that two events can be independent and
   overlapping at once; the two ideas are unrelated.

4. (a) $0.8^3 = 0.5120$.
   (b) $1 - 0.8^3 = 0.4880$.
   (c) (a) was easier, which is the point. "At least one" would otherwise require
   adding the cases of exactly one, exactly two and exactly three defective; the
   complement rule replaces three calculations with one, because the opposite of "at
   least one defective" is the single event "all good".

5. (a) $\dfrac{3}{10} \times \dfrac{2}{9} = \dfrac{6}{90} = 0.0667$.
   (b) $0.3 \times 0.3 = 0.0900$.
   (c) The multiplication rule. Without replacement the draws are dependent, so the
   second factor is the *conditional* probability $\mathrm{P}(B \mid A) = 2/9$ — one
   faulty component has been removed from a box now holding nine. With replacement the
   draws are independent and the conditional probability equals the unconditional one.

6. Two routes give exactly one faulty: faulty then good, or good then faulty.
   $\dfrac{3}{10}\cdot\dfrac{7}{9} + \dfrac{7}{10}\cdot\dfrac{3}{9} =
   \dfrac{21}{90} + \dfrac{21}{90} = \dfrac{42}{90} = 0.4667$. Forgetting the second
   route and reporting 0.2333 is the standard error here.

7. It is backwards because mutually exclusive events are **maximally dependent**. If
   $A$ and $B$ cannot both happen then $\mathrm{P}(A \mid B) = 0$, and unless
   $\mathrm{P}(A)$ was zero to begin with, that is not equal to $\mathrm{P}(A)$ —
   learning $B$ occurred has told you everything about $A$, namely that it did not.
   Independence means learning $B$ tells you *nothing*; exclusivity means it tells you
   everything.

8. (a) $\mathrm{P}(\text{late}) = 0.70(0.05) + 0.30(0.20) = 0.035 + 0.060 = 0.0950$.
   (b) $0.30(0.20) = 0.0600$ — six per cent of all invoices. Note that foreign
   invoices are 30% of the book but supply $0.06/0.095 = 63.16\%$ of the late ones,
   which is the kind of number the finance department actually wants.

9. (a) $0.5^4 = 0.0625$.
   (b) The gambler is thinking of $\mathrm{P}(\text{four heads}) = 0.0625$ and
   concluding a fourth head is unlikely. But that probability applied *before any
   tosses*. Three heads have already happened, the coin has no memory, and the
   probability of tails on the fourth toss is **0.5**. The gambler's fallacy is
   applying an unconditional probability to a situation where the conditioning
   information is already in hand.

10. Because it is a statement that happens to be true for some pairs of events and
    false for others, and which one you have is an empirical matter. Applying it to
    dependent events — drawing without replacement, or anything where one outcome
    shifts the odds of another — gives a confidently wrong answer with no warning
    sign. The general rule is always
    $\mathrm{P}(A \cap B) = \mathrm{P}(A)\mathrm{P}(B \mid A)$; the product form is
    what that reduces to in the special case where $\mathrm{P}(B \mid A)$ happens to
    equal $\mathrm{P}(B)$.
""", [
    ("q1a", 0.5500, 110 / 200),
    ("q1b", 0.3000, 60 / 200),
    ("q1c", 0.6000, 60 / 100),
    ("q1d", 0.5455, 60 / 110),
    ("q1e product", 0.2750, 0.5 * 0.55),
    ("q3a", 0.7000, 0.4 + 0.5 - 0.2),
    ("q3b", 0.4000, 0.2 / 0.5),
    ("q4a", 0.5120, 0.8 ** 3),
    ("q4b", 0.4880, 1 - 0.8 ** 3),
    ("q5a", 0.0667, (3 / 10) * (2 / 9)),
    ("q5b", 0.0900, 0.3 * 0.3),
    ("q6 exactly one", 0.4667, (3 / 10) * (7 / 9) + (7 / 10) * (3 / 9)),
    ("q6 one route only", 0.2333, (3 / 10) * (7 / 9)),
    ("q8a", 0.0950, 0.70 * 0.05 + 0.30 * 0.20),
    ("q8b", 0.0600, 0.30 * 0.20),
    ("q8 share of late", 0.6316, (0.30 * 0.20) / (0.70 * 0.05 + 0.30 * 0.20)),
    ("q9a", 0.0625, 0.5 ** 4),
])

# ---------------------------------------------------------------- chapter 6

BLOCKS["06_bayes.md"] = (r"""
## More practice

Ten more. The screening-test problem appears three times with different base rates,
on purpose: the arithmetic is identical and the conclusion changes completely, and
that is the only thing about Bayes worth remembering.

1. A disease affects 2% of a population. A test returns positive for 95% of people
   who have it, and for 10% of people who do not.
   (a) Find $\mathrm{P}(\text{positive})$.
   (b) Find $\mathrm{P}(\text{disease} \mid \text{positive})$.
   (c) Explain to a patient, in one sentence, why a positive result from a "95%
   accurate" test still leaves them probably healthy.

2. Repeat 1(b) for a population in which the disease affects **20%**, with the same
   test. Compare the two answers and say what changed.

3. Using the figures in question 1, find
   $\mathrm{P}(\text{no disease} \mid \text{negative})$, and comment on why this test
   is much more useful for ruling out than for ruling in.

4. A firm buys components from two suppliers: 60% from A, which has a 2% defect rate,
   and 40% from B, which has a 5% rate.
   (a) Find the overall defect rate.
   (b) A defective component arrives. Find the probability it came from A.
   (c) A manager says "B is the problem, since B's rate is higher". Comment, using
   your answer to (b).

5. Three machines produce output: M1 makes 50% with a 1% defect rate, M2 makes 30%
   with 2%, M3 makes 20% with 4%.
   (a) Find the overall defect rate.
   (b) Given a defective item, find the probability it came from each machine.
   (c) Check that your three answers sum to 1, and say why they must.

6. Explain, using the law of total probability, why the overall defect rate in
   question 5 is not the average of 1%, 2% and 4%.

7. A spam filter flags 90% of spam and 3% of legitimate email. Sixty per cent of
   incoming email is spam.
   (a) Find the probability a flagged message is actually spam.
   (b) Find the probability a message that got through is actually spam.

8. In a courtroom, a forensic match occurs in 1 in 10,000 innocent people, and the
   defendant matched. The prosecutor says "so there is a 1 in 10,000 chance the
   defendant is innocent."
   (a) What quantity has the prosecutor actually been given?
   (b) What quantity did they claim?
   (c) If the match was found by searching a database of 50,000 people, roughly how
   many innocent matches would you expect?

9. Two events have $\mathrm{P}(A) = 0.3$ and $\mathrm{P}(B \mid A) = 0.3$. Are they
   independent? What extra information would you need to be sure?

10. Write down Bayes' theorem, then say in one sentence what each of the three
    quantities in it is called and what question each one answers.

### Answers to the extra problems

1. (a) $\mathrm{P}(+) = 0.02(0.95) + 0.98(0.10) = 0.019 + 0.098 = 0.1170$.
   (b) $\mathrm{P}(D \mid +) = 0.019/0.117 = 0.1624$.
   (c) Because the disease is rare: out of 1,000 people only 20 have it and 19 of
   those test positive, but 98 of the 980 healthy people also test positive — so 98 of
   the 117 positives are false alarms, simply because there are so many more healthy
   people for the test to be wrong about.

2. $\mathrm{P}(+) = 0.20(0.95) + 0.80(0.10) = 0.19 + 0.08 = 0.2700$, so
   $\mathrm{P}(D \mid +) = 0.19/0.27 = 0.7037$. **The test did not change — only the
   base rate did**, and the answer went from 16% to 70%. The same evidence supports a
   completely different conclusion depending on how common the condition is, which is
   why the prevalence is not an optional extra in a diagnostic question.

3. $\mathrm{P}(-) = 1 - 0.117 = 0.8830$, and
   $\mathrm{P}(D \cap -) = 0.02(0.05) = 0.0010$, so
   $\mathrm{P}(D \mid -) = 0.001/0.883 = 0.0011$ and
   $\mathrm{P}(\text{no } D \mid -) = 0.9989$. A negative result is almost conclusive
   while a positive one is weak evidence. The asymmetry comes from the base rate: when
   a condition is rare, "you do not have it" is a claim that was very probably true
   before the test and the test only reinforces it.

4. (a) $0.60(0.02) + 0.40(0.05) = 0.012 + 0.020 = 0.0320$, so 3.2%.
   (b) $0.012/0.032 = 0.3750$.
   (c) The manager is right that B's *rate* is worse, but 37.5% of all defects still
   come from A, because A supplies half again as many components. Whether to act on
   the rate or on the count depends on the decision: renegotiating a contract is about
   the rate, while staffing an inspection line is about the count.

5. (a) $0.50(0.01) + 0.30(0.02) + 0.20(0.04) = 0.005 + 0.006 + 0.008 = 0.0190$.
   (b) $\mathrm{P}(M1 \mid D) = 0.005/0.019 = 0.2632$;
   $\mathrm{P}(M2 \mid D) = 0.006/0.019 = 0.3158$;
   $\mathrm{P}(M3 \mid D) = 0.008/0.019 = 0.4211$.
   (c) They sum to 1 because the three machines are exhaustive and mutually exclusive
   — every defective item came from exactly one of them, so the posterior probability
   has to be distributed entirely among the three. It is a free check on the
   arithmetic and catches a dropped term immediately.

6. Because the three rates apply to three groups of different sizes, and the law of
   total probability weights each conditional probability by the probability of the
   branch it sits on. The unweighted average of 1%, 2% and 4% is 2.3333%, which would
   be correct only if each machine made a third of the output. M1 is the cleanest
   machine and makes half of everything, so it pulls the true figure down to 1.9%.

7. (a) $\mathrm{P}(\text{flagged}) = 0.60(0.90) + 0.40(0.03) = 0.54 + 0.012 = 0.5520$,
   so $\mathrm{P}(\text{spam} \mid \text{flagged}) = 0.54/0.552 = 0.9783$.
   (b) $\mathrm{P}(\text{through}) = 0.60(0.10) + 0.40(0.97) = 0.06 + 0.388 = 0.4480$,
   so $\mathrm{P}(\text{spam} \mid \text{through}) = 0.06/0.448 = 0.1339$. The filter
   is trustworthy when it flags and leaves about one message in seven of the survivors
   as spam.

8. (a) $\mathrm{P}(\text{match} \mid \text{innocent}) = 0.0001$ — the probability of
   the evidence given innocence.
   (b) $\mathrm{P}(\text{innocent} \mid \text{match})$ — the probability of innocence
   given the evidence. These are not the same quantity, and converting one into the
   other requires a prior probability that the defendant was involved at all. This is
   the **prosecutor's fallacy**, and it is question 2 of this set wearing a wig.
   (c) About $50{,}000 \times 0.0001 = 5$ innocent matches. Finding a match by
   trawling a database is very different evidence from testing a suspect identified
   some other way, and the number 1 in 10,000 does not distinguish them.

9. **Yes**, as far as this goes: $\mathrm{P}(B \mid A) = 0.3$ tells you the
   conditional probability of $B$, and independence requires that to equal
   $\mathrm{P}(B)$. You would need $\mathrm{P}(B)$ to confirm it. The fact that
   $\mathrm{P}(B \mid A)$ happens to equal $\mathrm{P}(A)$ is a coincidence of the
   numbers and is irrelevant — a trap worth noticing.

10. $\mathrm{P}(A \mid B) = \dfrac{\mathrm{P}(B \mid A)\mathrm{P}(A)}{\mathrm{P}(B)}$.
    $\mathrm{P}(A)$ is the **prior** — what you believed before seeing the evidence.
    $\mathrm{P}(B \mid A)$ is the **likelihood** — how probable this evidence would be
    if $A$ were true. $\mathrm{P}(A \mid B)$ is the **posterior** — what you should
    believe now. The denominator is just the total probability of the evidence,
    computed across all the ways it could have arisen, and it is what makes the
    posteriors sum to one.
""", [
    ("q1a", 0.1170, 0.02 * 0.95 + 0.98 * 0.10),
    ("q1b", 0.1624, (0.02 * 0.95) / (0.02 * 0.95 + 0.98 * 0.10)),
    ("q2 P(+)", 0.2700, 0.20 * 0.95 + 0.80 * 0.10),
    ("q2 posterior", 0.7037, (0.20 * 0.95) / (0.20 * 0.95 + 0.80 * 0.10)),
    ("q3 P(-)", 0.8830, 1 - (0.02 * 0.95 + 0.98 * 0.10)),
    ("q3 joint", 0.0010, 0.02 * 0.05),
    ("q3 P(D|-)", 0.0011, (0.02 * 0.05) / (1 - (0.02 * 0.95 + 0.98 * 0.10))),
    ("q3 P(no D|-)", 0.9989, 1 - (0.02 * 0.05) / (1 - (0.02 * 0.95 + 0.98 * 0.10))),
    ("q4a", 0.0320, 0.60 * 0.02 + 0.40 * 0.05),
    ("q4b", 0.3750, (0.60 * 0.02) / (0.60 * 0.02 + 0.40 * 0.05)),
    ("q5a", 0.0190, 0.50 * 0.01 + 0.30 * 0.02 + 0.20 * 0.04),
    ("q5 M1", 0.2632, 0.005 / 0.019),
    ("q5 M2", 0.3158, 0.006 / 0.019),
    ("q5 M3", 0.4211, 0.008 / 0.019),
    ("q6 naive average", 2.3333, float(np.mean([1, 2, 4]))),
    ("q7 P(flagged)", 0.5520, 0.60 * 0.90 + 0.40 * 0.03),
    ("q7a", 0.9783, (0.60 * 0.90) / (0.60 * 0.90 + 0.40 * 0.03)),
    ("q7 P(through)", 0.4480, 0.60 * 0.10 + 0.40 * 0.97),
    ("q7b", 0.1339, (0.60 * 0.10) / (0.60 * 0.10 + 0.40 * 0.97)),
    ("q8c", 5, 50000 * 0.0001),
])

# ---------------------------------------------------------------- chapter 7

_v7 = np.array([0, 1, 2, 3], dtype=float)
_p7 = np.array([0.1, 0.3, 0.4, 0.2])
_EX7 = float((_v7 * _p7).sum())
_EX27 = float((_v7 ** 2 * _p7).sum())
_VX7 = _EX27 - _EX7 ** 2

BLOCKS["07_random_variables.md"] = (r"""
## More practice

Ten more. Question 10 is the derivation itself — if you can reproduce it from a
blank page you will never again wonder which of $E(X^2)$ and $E(X)^2$ gets
subtracted from which.

1. The number of claims a policyholder files in a year, $X$, has

   | $x$ | 0 | 1 | 2 | 3 |
   |---|---|---|---|---|
   | $\mathrm{P}(X=x)$ | 0.1 | 0.3 | 0.4 | 0.2 |

   (a) Confirm this is a valid probability distribution.
   (b) Find $E(X)$.
   (c) Find $E(X^2)$, then $V(X)$ and the standard deviation.

2. Using the distribution in question 1, let $Y = 3X + 2$.
   (a) Find $E(Y)$ and $V(Y)$ without re-tabulating.
   (b) Find the standard deviation of $Y$.
   (c) Why does the $+2$ affect the mean but not the variance?

3. An insurer charges a premium of \$50 and pays out \$10,000 if a claim occurs,
   which happens with probability 0.003.
   (a) Find the expected profit per policy.
   (b) The insurer writes 20,000 such policies. Find the expected total profit.
   (c) Why is the expected value a sensible basis for pricing 20,000 policies but a
   poor guide to whether *you* should buy one?

4. $X$ and $Y$ have the joint distribution

   | | $Y=0$ | $Y=1$ |
   |---|---|---|
   | $X=0$ | 0.2 | 0.1 |
   | $X=1$ | 0.3 | 0.4 |

   (a) Find the marginal distributions of $X$ and $Y$, and $E(X)$, $E(Y)$.
   (b) Find $E(XY)$ and hence $\text{COV}(X,Y)$.
   (c) Are $X$ and $Y$ independent? Show the check.
   (d) Find $V(X+Y)$.

5. A game pays \$10 with probability 0.2, \$2 with probability 0.5, and nothing
   otherwise. It costs \$4 to play.
   (a) Find the expected net gain.
   (b) Would you play it repeatedly? Once?

6. $X$ has mean 20 and standard deviation 4. Find the mean and standard deviation of
   (a) $X + 10$, (b) $5X$, (c) $(X - 20)/4$.

7. Two independent random variables have $V(X) = 9$ and $V(Y) = 16$.
   (a) Find $V(X+Y)$ and $V(X-Y)$.
   (b) Now suppose instead that $\text{COV}(X,Y) = -6$. Recompute both.
   (c) In (b), is it possible for $V(X-Y)$ to exceed $V(X)+V(Y)$? Explain.

8. $S = X_1 + X_2 + \cdots + X_{25}$, where the $X_i$ are independent with mean 8 and
   standard deviation 3.
   (a) Find $E(S)$ and the standard deviation of $S$.
   (b) Find $E(\bar{X})$ and the standard deviation of $\bar{X}$.
   (c) Note that one of these grows with $n$ and one shrinks. Say which, and why.

9. A student computes $V(X) = -2$ and concludes the variable is "negatively
   variable". What has gone wrong, and what is the most likely arithmetic slip?

10. Starting from $V(X) = E\big[(X-\mu)^2\big]$, derive
    $V(X) = E(X^2) - \big[E(X)\big]^2$, justifying each step.

### Answers to the extra problems

1. (a) All four probabilities are between 0 and 1 and they sum to
   $0.1+0.3+0.4+0.2 = 1$. Valid.
   (b) $E(X) = 0(0.1) + 1(0.3) + 2(0.4) + 3(0.2) = 1.7000$.
   (c) $E(X^2) = 0(0.1) + 1(0.3) + 4(0.4) + 9(0.2) = 3.7000$, so
   $V(X) = 3.7 - 1.7^2 = 3.7 - 2.89 = 0.8100$ and the standard deviation is
   **0.9000**. Note $E(X^2) = 3.70 \neq [E(X)]^2 = 2.89$; the gap between them *is*
   the variance.

2. (a) $E(Y) = 3(1.7) + 2 = 7.1000$ and $V(Y) = 3^2(0.81) = 7.2900$.
   (b) $\sqrt{7.29} = 2.7000$ — which is $3 \times 0.9$, as it must be.
   (c) Adding 2 shifts every outcome and the mean by the same amount, so every
   deviation from the mean is unchanged and the spread is untouched. Multiplying by 3
   stretches the deviations by 3, so the standard deviation scales by 3 and the
   variance by $3^2$. Location and spread respond to different parts of a linear
   transformation.

3. (a) $50 - 0.003(10{,}000) = 50 - 30 = \$20.0000$.
   (b) $20{,}000 \times 20 = \$400{,}000$.
   (c) Because expectation is an average over many repetitions, and the insurer gets
   those repetitions — across 20,000 policies the realised total will land close to
   the expected one. You buy one policy once. For you the distribution is \$50 lost
   with probability 0.997 and \$9,950 gained with probability 0.003, and the
   \$20 "expected" figure describes neither outcome. Insurance is rational for the
   buyer because of the *shape* of that distribution, not its mean.

4. (a) $X$: $\mathrm{P}(0) = 0.3$, $\mathrm{P}(1) = 0.7$, so $E(X) = 0.7000$ and
   $V(X) = 0.7 - 0.49 = 0.2100$. $Y$: $\mathrm{P}(0) = 0.5$, $\mathrm{P}(1) = 0.5$,
   so $E(Y) = 0.5000$ and $V(Y) = 0.2500$.
   (b) $XY$ is 1 only in the bottom-right cell, so $E(XY) = 0.4000$ and
   $\text{COV} = 0.4 - 0.7(0.5) = 0.0500$.
   (c) **Not independent**: $\mathrm{P}(X{=}1, Y{=}1) = 0.4$ but
   $\mathrm{P}(X{=}1)\mathrm{P}(Y{=}1) = 0.7(0.5) = 0.35$. One failing cell is enough.
   (d) $V(X+Y) = 0.21 + 0.25 + 2(0.05) = 0.5600$.

5. (a) $E(\text{payout}) = 10(0.2) + 2(0.5) + 0(0.3) = 2 + 1 = \$3.0000$, so the
   expected net gain is $3 - 4 = -\$1.0000$.
   (b) Not repeatedly — you lose a dollar a go on average, and over many plays that
   average is what you get. Once is a different question: a single play is a 20%
   chance of being \$6 up against a 30% chance of being \$4 down, and whether that
   trade appeals is about your tolerance for the spread, not about the mean.

6. (a) Mean 30, standard deviation **4** — unchanged.
   (b) Mean 100, standard deviation 20.
   (c) Mean **0**, standard deviation **1**. This is the $z$-score transformation
   from Chapter 3, and the general rule $E(aX+b) = aE(X)+b$,
   $\text{SD}(aX+b) = |a|\,\text{SD}(X)$ is what guarantees it always lands on mean 0
   and standard deviation 1.

7. (a) Independent, so the covariance is zero and both are $9 + 16 = 25.0000$.
   (b) $V(X+Y) = 9 + 16 + 2(-6) = 13.0000$ and
   $V(X-Y) = 9 + 16 - 2(-6) = 37.0000$.
   (c) **Yes, and it just did.** Subtracting a negatively correlated variable adds
   variance, because the minus sign in $-2\text{COV}$ meets the minus sign in the
   covariance. Variances add; the covariance term is the only one whose sign can go
   either way, and it is where every interesting answer in this section comes from.

8. (a) $E(S) = 25(8) = 200$ and $V(S) = 25(9) = 225$, so
   $\text{SD}(S) = 15.0000$.
   (b) $E(\bar{X}) = 8$ and $\text{SD}(\bar{X}) = 3/\sqrt{25} = 0.6000$.
   (c) The standard deviation of the **sum** grows, as $\sqrt{n}\sigma$; the standard
   deviation of the **mean** shrinks, as $\sigma/\sqrt{n}$. Both follow from the same
   fact that variances add: a sum of 25 things accumulates 25 variances, while the
   mean divides that accumulated total by $25^2$. This is the result Chapter 11 is
   built on.

9. Variance is an expected **squared** deviation, so it is an average of non-negative
   numbers and cannot be negative. The likely slip is subtracting the wrong way round
   — computing $[E(X)]^2 - E(X^2)$ instead of $E(X^2) - [E(X)]^2$. A negative variance
   is always an arithmetic error, never a finding, and it is worth treating as a
   built-in alarm.

10. Expand the square inside the expectation:
    $$E\big[(X-\mu)^2\big] = E\big[X^2 - 2\mu X + \mu^2\big]$$
    Expectation is linear, so it passes through the sum:
    $$= E(X^2) - 2\mu E(X) + \mu^2$$
    The step that needs care is $E(\mu^2) = \mu^2$ and $E(2\mu X) = 2\mu E(X)$: $\mu$
    is a fixed number, not a random variable, so it comes out of the expectation
    untouched. Now substitute $E(X) = \mu$:
    $$= E(X^2) - 2\mu^2 + \mu^2 = E(X^2) - \mu^2 = E(X^2) - \big[E(X)\big]^2$$
    Check it against question 1: $3.70 - 1.7^2 = 0.81$, which is what the deviation
    route gave. The identity is not a different definition of variance — it is the
    same quantity rearranged so you only need one pass through the table.
""", [
    ("q1b E(X)", 1.7000, _EX7),
    ("q1c E(X2)", 3.7000, _EX27),
    ("q1c V(X)", 0.8100, _VX7),
    ("q1c sd", 0.9000, float(np.sqrt(_VX7))),
    ("q2a E(Y)", 7.1000, 3 * _EX7 + 2),
    ("q2a V(Y)", 7.2900, 9 * _VX7),
    ("q2b sd", 2.7000, float(np.sqrt(9 * _VX7))),
    ("q3a", 20.0000, 50 - 0.003 * 10000),
    ("q4a E(X)", 0.7000, 0.3 + 0.4),
    ("q4a V(X)", 0.2100, 0.7 - 0.49),
    ("q4a E(Y)", 0.5000, 0.1 + 0.4),
    ("q4a V(Y)", 0.2500, 0.5 - 0.25),
    ("q4b E(XY)", 0.4000, 0.4),
    ("q4b cov", 0.0500, 0.4 - 0.7 * 0.5),
    ("q4d", 0.5600, 0.21 + 0.25 + 2 * 0.05),
    ("q5a payout", 3.0000, 10 * 0.2 + 2 * 0.5),
    ("q5a net", -1.0000, 10 * 0.2 + 2 * 0.5 - 4),
    ("q7a", 25.0000, 9 + 16),
    ("q7b sum", 13.0000, 9 + 16 + 2 * (-6)),
    ("q7b diff", 37.0000, 9 + 16 - 2 * (-6)),
    ("q8a sd", 15.0000, float(np.sqrt(25 * 9))),
    ("q8b sd", 0.6000, 3 / np.sqrt(25)),
])
