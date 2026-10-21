#!/usr/bin/env python3
"""Twenty practice problems covering the course to date, with solutions.

Written for Checkpoint 2 revision: descriptive statistics through hypothesis
testing, in the order the book covers them.

These are ORIGINAL problems. The genre is the standard business-and-economics
style -- a short scenario, realistic numbers, parts (a)(b)(c) -- because that is
what students will meet on the checkpoint. None of the scenarios or numbers are
taken from any textbook.

Every answer below is COMPUTED here and asserted, then written into the markdown.
Nothing is typed in by hand, so the problems and the solutions cannot drift apart.

Usage:  python3 book/make_practice.py
"""

import os
import math
from math import comb, sqrt, erf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "90_practice_problems.md")

Phi = lambda z: 0.5 * (1 + erf(z / sqrt(2)))


def mean(a):
    return sum(a) / len(a)


def svar(a):
    m = mean(a)
    return sum((x - m) ** 2 for x in a) / (len(a) - 1)


# ----------------------------------------------------------------- 1 complaints
C = [4, 6, 6, 9, 11, 13, 14]
C_mean, C_med = mean(C), sorted(C)[len(C) // 2]
C_ss = sum((x - C_mean) ** 2 for x in C)
C_var, C_sd = svar(C), sqrt(svar(C))
assert (C_mean, C_med, C_ss) == (9.0, 9, 88.0)

# ------------------------------------------------------------ 2 coefficient of var
A_m, A_s = 42.0, 6.0
B_m, B_s = 78.0, 9.0
A_cv, B_cv = A_s / A_m, B_s / B_m
assert abs(A_cv - 0.142857) < 1e-5 and abs(B_cv - 0.115385) < 1e-5

# ----------------------------------------------------------------- 3 z-scores
S_m, S_s = 3.2, 0.6
z_late, z_fast = (4.7 - S_m) / S_s, (2.0 - S_m) / S_s
assert abs(z_late - 2.5) < 1e-12 and abs(z_fast + 2.0) < 1e-12

# ------------------------------------------------------------- 4 unit conversion
K_m, K_s, FACTOR = 40.0, 10.0, 0.621371
M_m, M_s = K_m * FACTOR, K_s * FACTOR

# ------------------------------------------------------- 5/6 advertising and sales
X = [2, 4, 6, 8, 10]
Y = [14, 18, 20, 26, 32]
XB, YB = mean(X), mean(Y)
SXY = sum((a - XB) * (b - YB) for a, b in zip(X, Y)) / (len(X) - 1)
SX, SY = sqrt(svar(X)), sqrt(svar(Y))
R = SXY / (SX * SY)
assert (XB, YB, SXY) == (6.0, 22.0, 22.0)
assert abs(R - 0.9838699) < 1e-6

# --------------------------------------------------------------- 7 addition rule
PA, PB, PAB = 0.42, 0.37, 0.15
P_union = PA + PB - PAB
P_neither = 1 - P_union
assert abs(P_union - 0.64) < 1e-12 and abs(P_neither - 0.36) < 1e-12

# -------------------------------------------------------- 8 conditional from a table
#  400 loan applications, cross-classified
T = {("approved", "first"): 180, ("approved", "repeat"): 120,
     ("declined", "first"): 70, ("declined", "repeat"): 30}
N_T = sum(T.values())
p_app = (T[("approved", "first")] + T[("approved", "repeat")]) / N_T
p_rep = (T[("approved", "repeat")] + T[("declined", "repeat")]) / N_T
p_app_given_rep = T[("approved", "repeat")] / (T[("approved", "repeat")]
                                               + T[("declined", "repeat")])
assert N_T == 400 and p_app == 0.75 and p_rep == 0.375
assert p_app_given_rep == 0.8

# ------------------------------------------------------------------- 9 Bayes
PLANTS = [("Riverside", 0.50, 0.02), ("Eastgate", 0.30, 0.04), ("Northfield", 0.20, 0.06)]
PD = sum(s * d for _, s, d in PLANTS)
POST = [(n, s * d / PD) for n, s, d in PLANTS]
assert abs(PD - 0.034) < 1e-12
assert abs(dict(POST)["Northfield"] - 0.3529412) < 1e-6

# ------------------------------------------------------- 10/11 discrete random variable
V = [0, 1, 2, 3, 4]
P = [0.10, 0.25, 0.30, 0.25, 0.10]
assert abs(sum(P) - 1) < 1e-12
EX = sum(v * p for v, p in zip(V, P))
EX2 = sum(v * v * p for v, p in zip(V, P))
VX = EX2 - EX ** 2
assert abs(EX - 2.0) < 1e-12 and abs(EX2 - 5.3) < 1e-12 and abs(VX - 1.3) < 1e-12
A_LIN, B_LIN = 45.0, 200.0
E_REV = A_LIN * EX + B_LIN
V_REV = A_LIN ** 2 * VX
assert E_REV == 290.0 and abs(V_REV - 2632.5) < 1e-9

# ----------------------------------------------------------- 12 variance of a sum
VXX, VYY, COVXY = 16.0, 25.0, 6.0
V_SUM = VXX + VYY + 2 * COVXY
V_DIFF = VXX + VYY - 2 * COVXY
assert V_SUM == 53.0 and V_DIFF == 29.0

# ------------------------------------------------------------------ 13/14 binomial
NB, PB_ = 12, 0.25
PB3 = comb(NB, 3) * PB_ ** 3 * (1 - PB_) ** (NB - 3)
PB_le2 = sum(comb(NB, k) * PB_ ** k * (1 - PB_) ** (NB - k) for k in range(3))
EB, SDB = NB * PB_, sqrt(NB * PB_ * (1 - PB_))
assert EB == 3.0 and SDB == 1.5
N2, P2_ = 8, 0.15
P_none = (1 - P2_) ** N2
P_atleast1 = 1 - P_none

# -------------------------------------------------------------------- 15/16 normal
MU_N, SD_N = 850.0, 120.0
p_over_1000 = 1 - Phi((1000 - MU_N) / SD_N)
p_700_1000 = Phi((1000 - MU_N) / SD_N) - Phi((700 - MU_N) / SD_N)
#  the 90th percentile: z = 1.2816
Z90 = 1.281552
x90 = MU_N + Z90 * SD_N

# ------------------------------------------------------------------------ 17 CLT
N_CLT = 36
SE_CLT = SD_N / sqrt(N_CLT)
p_xbar_880 = 1 - Phi((880 - MU_N) / SE_CLT)
assert SE_CLT == 20.0

# ------------------------------------------------------------- 18/19/20 inference
N_I, XB_I, S_I = 49, 63.4, 8.4
SE_I = S_I / sqrt(N_I)
T_CRIT = 2.010635          # invttail(48, 0.025), checked in Stata
CI = (XB_I - T_CRIT * SE_I, XB_I + T_CRIT * SE_I)
MU0_I = 60.0
T_STAT = (XB_I - MU0_I) / SE_I
P_TWO = 0.0067             # 2*ttail(48, 2.8333), checked in Stata
Z95 = 1.959964
N_REQ = (Z95 * S_I / 2.0) ** 2
assert SE_I == 1.2
assert abs(T_STAT - 2.833333) < 1e-5
assert not (CI[0] <= MU0_I <= CI[1])       # interval and test must agree


MD = f"""# Practice problems

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

$$4,\\quad 6,\\quad 6,\\quad 9,\\quad 11,\\quad 13,\\quad 14$$

(a) Compute the mean, the median and the mode.
(b) Compute the sample variance and the sample standard deviation.
(c) The day with 14 complaints is found to have been recorded twice by mistake and
should have read 28. Without recomputing from scratch, state what happens to the
mean and to the median, and explain why they behave differently.

**2.** Two branches of a bank record the time customers wait to be served. Branch A
has a mean wait of {A_m:.0f} seconds with a standard deviation of {A_s:.0f} seconds.
Branch B has a mean of {B_m:.0f} seconds with a standard deviation of {B_s:.0f}
seconds.

(a) Which branch has the larger absolute variation in waiting times?
(b) The coefficient of variation is $s / \\bar{{x}}$, expressed as a percentage.
Compute it for both branches.
(c) A regional manager claims Branch B is "less consistent" because its standard
deviation is larger. Is that a fair reading? Answer in one sentence.

**3.** A logistics firm finds that delivery times have a mean of {S_m} days and a
standard deviation of {S_s} days.

(a) A shipment takes 4.7 days. Compute its $z$-score and say in words what it means.
(b) A second shipment takes 2.0 days. Compute its $z$-score.
(c) Which of the two is more unusual, and does the answer depend on knowing the
shape of the distribution?

**4.** A haulage company reports that the distances its vehicles travel per day have
a mean of {K_m:.0f} km and a standard deviation of {K_s:.0f} km. A contract requires
the figures in miles, where 1 km = {FACTOR} miles.

(a) What is the mean distance in miles?
(b) What is the standard deviation in miles?
(c) What would happen to the standard deviation if, instead, every driver were
required to travel an extra 5 km per day on top of their current distance?

**5.** A retailer records monthly advertising spend $x$ (in thousands of dollars)
and sales $y$ (in thousands of units) for five months:

| Advertising ($x$) | {X[0]} | {X[1]} | {X[2]} | {X[3]} | {X[4]} |
|---|---|---|---|---|---|
| Sales ($y$) | {Y[0]} | {Y[1]} | {Y[2]} | {Y[3]} | {Y[4]} |

(a) Compute $\\bar{{x}}$ and $\\bar{{y}}$.
(b) Compute the sample covariance $s_{{xy}}$.
(c) Compute the coefficient of correlation $r$ and describe the relationship in one
sentence.

**6.** Using the data in Question 5:

(a) Advertising spend is restated in dollars rather than thousands, so every $x$ is
multiplied by 1,000. What is the new covariance?
(b) What is the new correlation?
(c) Explain, in terms of the formulas, why one of them changed and the other did not.

---

## Probability

**7.** For two events $A$ and $B$, $\\mathrm{{P}}(A) = {PA}$, $\\mathrm{{P}}(B) = {PB}$
and $\\mathrm{{P}}(A \\cap B) = {PAB}$.

(a) Find $\\mathrm{{P}}(A \\cup B)$.
(b) Find the probability that neither $A$ nor $B$ occurs.
(c) Are $A$ and $B$ independent? Justify with a calculation.

**8.** A credit union classifies {N_T} loan applications by outcome and by whether
the applicant is a first-time or a repeat borrower:

| | First-time | Repeat | Total |
|---|---|---|---|
| Approved | {T[("approved", "first")]} | {T[("approved", "repeat")]} | {T[("approved", "first")] + T[("approved", "repeat")]} |
| Declined | {T[("declined", "first")]} | {T[("declined", "repeat")]} | {T[("declined", "first")] + T[("declined", "repeat")]} |
| Total | {T[("approved", "first")] + T[("declined", "first")]} | {T[("approved", "repeat")] + T[("declined", "repeat")]} | {N_T} |

(a) What is the probability that a randomly chosen application was approved?
(b) What is the probability that an application was approved, given that it came
from a repeat borrower?
(c) Are "approved" and "repeat borrower" independent events? Show the calculation
that settles it.

**9.** A manufacturer sources one component from three plants. Riverside supplies
{PLANTS[0][1]:.0%} of units with a defect rate of {PLANTS[0][2]:.0%}; Eastgate
supplies {PLANTS[1][1]:.0%} with a defect rate of {PLANTS[1][2]:.0%}; Northfield
supplies {PLANTS[2][1]:.0%} with a defect rate of {PLANTS[2][2]:.0%}.

(a) What proportion of all units are defective?
(b) A unit fails inspection. What is the probability it came from Northfield?
(c) Northfield supplies the smallest share. Explain in one sentence why it is
nonetheless a serious suspect.

---

## Random variables

**10.** The number of vehicles hired per day from a small depot has the following
distribution:

| $x$ | {V[0]} | {V[1]} | {V[2]} | {V[3]} | {V[4]} |
|---|---|---|---|---|---|
| $\\mathrm{{P}}(X = x)$ | {P[0]} | {P[1]} | {P[2]} | {P[3]} | {P[4]} |

(a) Verify that this is a valid probability distribution.
(b) Compute $E(X)$.
(c) Compute $V(X)$ and the standard deviation of $X$.

**11.** The depot in Question 10 charges \\${A_LIN:.0f} per hire and has fixed daily
costs of \\${B_LIN:.0f}, so daily revenue net of fixed costs is
$R = {A_LIN:.0f}X - {B_LIN:.0f}$.

(a) Find $E(R)$.
(b) Find $V(R)$ and the standard deviation of $R$.
(c) The owner proposes raising the fixed costs to \\$300. What happens to $E(R)$,
and what happens to $V(R)$?

**12.** Two product lines have monthly profits $X$ and $Y$ with
$V(X) = {VXX:.0f}$, $V(Y) = {VYY:.0f}$ and $\\mathrm{{COV}}(X, Y) = {COVXY:.0f}$
(all in squared thousands of dollars).

(a) Find $V(X + Y)$.
(b) Find $V(X - Y)$.
(c) The firm can change its product mix so that the two profits become uncorrelated.
Would that raise or lower the variance of total profit, and by how much?

---

## Distributions

**13.** A quality inspector knows that {PB_:.0%} of items coming off a line require
rework. A sample of {NB} items is drawn independently.

(a) State the four conditions for a binomial experiment and confirm each one here.
(b) Find the probability that exactly 3 items require rework.
(c) Find $E(X)$ and the standard deviation of $X$.

**14.** A firm sends out {N2} invoices. Each has, independently, a {P2_:.0%}
probability of being queried by the customer.

(a) Find the probability that none of them is queried.
(b) Find the probability that at least one is queried.
(c) Explain why (b) is much easier to compute via (a) than directly.

**15.** Monthly electricity use in a district is normally distributed with a mean of
{MU_N:.0f} kWh and a standard deviation of {SD_N:.0f} kWh.

(a) What proportion of households use more than 1,000 kWh?
(b) What proportion use between 700 and 1,000 kWh?
(c) Above what level of use does a household fall in the top 10%?

**16.** Using the distribution in Question 15, a household uses 1,090 kWh.

(a) Compute its $z$-score.
(b) What proportion of households use more than this?
(c) Explain why the answer to (a) can be interpreted without opening a table at all.

---

## From sample to population

**17.** A random sample of {N_CLT} households is drawn from the district in
Question 15.

(a) State the mean and the standard error of the sampling distribution of
$\\bar{{X}}$.
(b) Find $\\mathrm{{P}}(\\bar{{X}} > 880)$.
(c) The distribution of household use turns out to be right-skewed rather than
normal. Does your answer to (b) survive? Explain.

**18.** A sample of {N_I} invoices has a mean value of \\${XB_I} and a sample
standard deviation of \\${S_I}.

(a) Compute the standard error of the mean.
(b) Construct a 95% confidence interval for the population mean invoice value.
(c) Explain precisely what the phrase "95% confident" refers to.

**19.** The finance department's planning model assumes the mean invoice value is
\\${MU0_I:.0f}. Use the sample in Question 18.

(a) State $H_0$ and $H_a$, and say whether the test is one-tailed or two-tailed.
(b) Compute the test statistic.
(c) Test at $\\alpha = 0.05$ and state the conclusion in a sentence about invoices.
(d) Confirm that your answer agrees with the interval from Question 18(b).

**20.** The department wants to re-estimate the mean invoice value to within
\\$2.00 at 95% confidence, and is willing to assume $\\sigma \\approx {S_I}$.

(a) How many invoices must be sampled?
(b) How many would be needed to halve the margin to \\$1.00?
(c) What does the comparison tell you about the cost of precision?

---

# Solutions

**1.** (a) $\\bar{{x}} = {sum(C)}/7 = {C_mean:.0f}$. Sorted, the middle value is
{C_med}, so the median is {C_med}. The mode is 6.
(b) Deviations are $-5, -3, -3, 0, 2, 4, 5$, which square and sum to {C_ss:.0f}. So
$s^2 = {C_ss:.0f}/6 = {C_var:.4f}$ and $s = {C_sd:.4f}$.
(c) The mean rises by $14/7 = 2$ to {C_mean + 2:.0f}. The median does not move at
all. The mean uses the size of every observation, so a change of 14 in one value
moves it; the median uses only the rank order, and 28 occupies the same position
that 14 did.

**2.** (a) Branch B, with a standard deviation of {B_s:.0f} seconds against
{A_s:.0f}.
(b) Branch A: ${A_s:.0f}/{A_m:.0f} = {A_cv:.4f}$, or {A_cv:.2%}. Branch B:
${B_s:.0f}/{B_m:.0f} = {B_cv:.4f}$, or {B_cv:.2%}.
(c) No. Relative to its own mean, Branch B is the **more** consistent of the two —
its variation is {B_cv:.2%} of its average wait against {A_cv:.2%} for Branch A. The
manager compared standard deviations across series with very different means.

**3.** (a) $z = (4.7 - {S_m})/{S_s} = {z_late:.4f}$ — the shipment took two and a
half standard deviations longer than average.
(b) $z = (2.0 - {S_m})/{S_s} = {z_fast:.4f}$.
(c) The 4.7-day shipment, since $|{z_late:.1f}| > |{z_fast:.1f}|$. Comparing
$z$-scores requires no assumption about shape; converting them into probabilities
does.

**4.** (a) ${K_m:.0f} \\times {FACTOR} = {M_m:.4f}$ miles.
(b) ${K_s:.0f} \\times {FACTOR} = {M_s:.4f}$ miles. Multiplying every value by a
constant multiplies the standard deviation by that same constant.
(c) Nothing. Adding a constant shifts every value equally and leaves the spread
unchanged — $V(X + b) = V(X)$.

**5.** (a) $\\bar{{x}} = {XB:.0f}$, $\\bar{{y}} = {YB:.0f}$.
(b) The deviation products are $32, 8, 0, 8, 40$, summing to 88, so
$s_{{xy}} = 88/4 = {SXY:.2f}$.
(c) $s_x = \\sqrt{{40/4}} = {SX:.4f}$ and $s_y = \\sqrt{{200/4}} = {SY:.4f}$, so
$r = {SXY:.2f}/({SX:.4f} \\times {SY:.4f}) = {R:.4f}$. A very strong positive linear
relationship: higher advertising spend goes with higher sales, and the points lie
close to a straight line.

**6.** (a) $s_{{xy}} \\times 1{{,}}000 = {SXY * 1000:,.0f}$.
(b) Unchanged at ${R:.4f}$.
(c) Covariance carries the units of $x$ times the units of $y$, so rescaling $x$
rescales it. Correlation divides the covariance by $s_x s_y$, and the 1,000 appears
in both the numerator and in $s_x$, so it cancels. That cancellation is the whole
reason $r$ is reported rather than $s_{{xy}}$.

**7.** (a) $\\mathrm{{P}}(A \\cup B) = {PA} + {PB} - {PAB} = {P_union:.2f}$.
(b) $1 - {P_union:.2f} = {P_neither:.2f}$.
(c) If independent, $\\mathrm{{P}}(A \\cap B)$ would equal
${PA} \\times {PB} = {PA * PB:.4f}$. It is {PAB}, so they are **not** independent.

**8.** (a) ${T[("approved", "first")] + T[("approved", "repeat")]}/{N_T} = {p_app:.2f}$.
(b) Restrict to the repeat column:
${T[("approved", "repeat")]}/{T[("approved", "repeat")] + T[("declined", "repeat")]} = {p_app_given_rep:.2f}$.
(c) Not independent. $\\mathrm{{P}}(\\text{{approved}}) = {p_app:.2f}$ but
$\\mathrm{{P}}(\\text{{approved}} \\mid \\text{{repeat}}) = {p_app_given_rep:.2f}$.
Knowing the applicant is a repeat borrower changes the probability, which is exactly
what dependence means.

**9.** (a) Total probability:
$({PLANTS[0][1]})({PLANTS[0][2]}) + ({PLANTS[1][1]})({PLANTS[1][2]}) + ({PLANTS[2][1]})({PLANTS[2][2]}) = {PD:.4f}$.
(b) Bayes:
$({PLANTS[2][1]})({PLANTS[2][2]})/{PD:.4f} = {dict(POST)["Northfield"]:.4f}$.
(c) Because the defect rate matters as much as the share: Northfield ships the
fewest units but spoils the highest fraction of them, so it accounts for
{dict(POST)["Northfield"]:.1%} of all defects despite supplying only
{PLANTS[2][1]:.0%} of output.

**10.** (a) All five probabilities are non-negative and sum to
{sum(P):.2f}. Valid.
(b) $E(X) = {EX:.1f}$.
(c) $E(X^2) = {EX2:.1f}$, so $V(X) = {EX2:.1f} - {EX:.1f}^2 = {VX:.1f}$ and
$\\sigma = {sqrt(VX):.4f}$.

**11.** (a) $E(R) = {A_LIN:.0f}({EX:.1f}) - {B_LIN:.0f} = {A_LIN * EX - B_LIN:.0f}$.
(b) $V(R) = {A_LIN:.0f}^2({VX:.1f}) = {V_REV:.1f}$, so
$\\sigma_R = {sqrt(V_REV):.4f}$.
(c) $E(R)$ falls by 100, to {A_LIN * EX - 300:.0f}. $V(R)$ does not change at all —
a constant shifts the distribution without stretching it.

**12.** (a) $V(X + Y) = {VXX:.0f} + {VYY:.0f} + 2({COVXY:.0f}) = {V_SUM:.0f}$.
(b) $V(X - Y) = {VXX:.0f} + {VYY:.0f} - 2({COVXY:.0f}) = {V_DIFF:.0f}$.
(c) It would **lower** it, from {V_SUM:.0f} to {VXX + VYY:.0f}, a fall of
{2 * COVXY:.0f}. Positively correlated lines rise and fall together, which makes the
total more volatile than the parts suggest — the argument for diversification, in
one line of algebra.

**13.** (a) A fixed number of trials ($n = {NB}$); two outcomes per trial (rework or
not); constant probability ($p = {PB_}$); independent draws. All four hold.
(b) $\\mathrm{{P}}(X = 3) = \\binom{{{NB}}}{{3}}({PB_})^3({1 - PB_})^{{9}} = {comb(NB, 3)} \\times {PB_ ** 3:.6f} \\times {(1 - PB_) ** 9:.6f} = {PB3:.4f}$.
(c) $E(X) = {NB}({PB_}) = {EB:.1f}$ and
$\\sigma = \\sqrt{{{NB}({PB_})({1 - PB_})}} = {SDB:.1f}$.

**14.** (a) $({1 - P2_})^{{{N2}}} = {P_none:.4f}$.
(b) $1 - {P_none:.4f} = {P_atleast1:.4f}$.
(c) "At least one" covers the eight separate cases $X = 1, 2, \\ldots, {N2}$, each
needing its own binomial term. Its complement is the single case $X = 0$. Computing
one term and subtracting from 1 replaces eight calculations with one.

**15.** (a) $z = (1000 - {MU_N:.0f})/{SD_N:.0f} = {(1000 - MU_N) / SD_N:.4f}$, so the
proportion is $1 - {Phi((1000 - MU_N) / SD_N):.4f} = {p_over_1000:.4f}$.
(b) $700 \\to z = {(700 - MU_N) / SD_N:.4f}$ and $1000 \\to z = {(1000 - MU_N) / SD_N:.4f}$,
giving ${Phi((1000 - MU_N) / SD_N):.4f} - {Phi((700 - MU_N) / SD_N):.4f} = {p_700_1000:.4f}$.
(c) The top 10% begins at $z = {Z90:.4f}$, so at
${MU_N:.0f} + {Z90:.4f}({SD_N:.0f}) = {x90:.2f}$ kWh.

**16.** (a) $z = (1090 - {MU_N:.0f})/{SD_N:.0f} = {(1090 - MU_N) / SD_N:.4f}$.
(b) $1 - {Phi((1090 - MU_N) / SD_N):.4f} = {1 - Phi((1090 - MU_N) / SD_N):.4f}$.
(c) A $z$ of {(1090 - MU_N) / SD_N:.1f} already says the household is two standard
deviations above average, which is a complete answer to "how unusual is this?" The
table only converts that into a proportion.

**17.** (a) $E(\\bar{{X}}) = {MU_N:.0f}$ and
$\\sigma_{{\\bar{{X}}}} = {SD_N:.0f}/\\sqrt{{{N_CLT}}} = {SE_CLT:.0f}$.
(b) $z = (880 - {MU_N:.0f})/{SE_CLT:.0f} = {(880 - MU_N) / SE_CLT:.4f}$, so
$\\mathrm{{P}}(\\bar{{X}} > 880) = {p_xbar_880:.4f}$.
(c) Yes. The Central Limit Theorem makes the sampling distribution of $\\bar{{X}}$
approximately normal for $n = {N_CLT}$ whatever the population's shape. Note what
does *not* survive: a probability statement about a **single** household would now
require the population to be normal, and it is not.

**18.** (a) ${S_I}/\\sqrt{{{N_I}}} = {SE_I:.1f}$.
(b) With $\\nu = {N_I - 1}$, $t_{{0.025}} = {T_CRIT:.4f}$, so the interval is
${XB_I} \\pm {T_CRIT:.4f}({SE_I:.1f}) = ({CI[0]:.4f},\\ {CI[1]:.4f})$.
(c) It describes the **procedure**, not this interval. If the whole exercise were
repeated many times, 95% of the intervals constructed this way would contain $\\mu$.
This particular interval either does or does not, and we will never know which.

**19.** (a) $H_0: \\mu = {MU0_I:.0f}$ against $H_a: \\mu \\neq {MU0_I:.0f}$. The
question gives no direction — the model simply "assumes" a value — so it is
**two-tailed**.
(b) $t = ({XB_I} - {MU0_I:.0f})/{SE_I:.1f} = {T_STAT:.4f}$ with $\\nu = {N_I - 1}$.
(c) The critical values are $\\pm{T_CRIT:.4f}$. Since
${T_STAT:.4f} > {T_CRIT:.4f}$, reject $H_0$ ($p = {P_TWO:.4f}$). The sample gives
strong evidence that the mean invoice value is not \\${MU0_I:.0f} — it appears to be
about \\${XB_I - MU0_I:.1f} higher, so the planning model understates it.
(d) The interval $({CI[0]:.4f},\\ {CI[1]:.4f})$ does not contain {MU0_I:.0f}. A
two-tailed test at $\\alpha = 0.05$ rejects exactly when the 95% interval excludes
the claimed value, so the two agree, as they must.

**20.** (a) $n = \\left(\\dfrac{{{Z95:.2f} \\times {S_I}}}{{2.00}}\\right)^2 = {N_REQ:.4f}$,
so sample **{math.ceil(N_REQ)}** invoices. Always round up.
(b) $n = \\left(\\dfrac{{{Z95:.2f} \\times {S_I}}}{{1.00}}\\right)^2 = {(Z95 * S_I / 1.0) ** 2:.4f}$,
so **{math.ceil((Z95 * S_I / 1.0) ** 2)}**.
(c) Halving the margin does not double the sample, it **quadruples** it. Precision
is bought at a rate of $\\sqrt{{n}}$, so each further improvement costs more than the
last.

---
"""

open(OUT, "w").write(MD)

print(f"  wrote {os.path.relpath(OUT)}")
print(f"       problems: 20   words: {len(MD.split()):,}")
print(f"       Q5  r = {R:.4f}        Q9  P(D) = {PD:.4f}, P(N|D) = {dict(POST)['Northfield']:.4f}")
print(f"       Q13 P(X=3) = {PB3:.4f}  Q15 P(>1000) = {p_over_1000:.4f}")
print(f"       Q18 CI = ({CI[0]:.4f}, {CI[1]:.4f})   Q19 t = {T_STAT:.4f}")
print(f"       Q20 n = {math.ceil(N_REQ)} then {math.ceil((Z95 * S_I / 1.0) ** 2)}")
print("       interval excludes mu0, so 19(d) is consistent:",
      not (CI[0] <= MU0_I <= CI[1]))
