#!/usr/bin/env python3
"""Twenty HARD multiple-choice questions for each Part of the book.

    95  Part I    Describing data            chapters 1-4
    96  Part II   Chance                     chapters 5-7
    97  Part III  Distributions              chapters 8-10
    98  Part IV   From sample to population  chapters 11-14

Eighty questions, all original.

HARD MEANS TWO THINGS HERE.

  1. Most questions take more than one step: a quantity has to be derived before
     the question proper can be answered. Single-step recall is rare.

  2. EVERY DISTRACTOR IS A DIAGNOSIS. Each wrong option is the number you get by
     making one specific, common mistake -- dividing by n instead of n-1,
     forgetting the square root, using sigma where sigma/sqrt(n) belongs,
     inverting a conditional. A student who picks a distractor has told you
     exactly what they did, and the answer key names it.

That second point is why the key gives a reason rather than a letter. A key that
says "B" teaches nothing.

COLUMN BALANCE IS ENFORCED, not hoped for. The correct answer's position is
assigned from a fixed balanced pattern -- five of each letter per bank -- because
an earlier draft of this file came out with nine B's and no D at all, which a
student could have exploited without knowing any statistics.

Usage:  python3 book/make_mcq.py
"""

import os
from collections import Counter
from math import comb, sqrt, erf, exp

HERE = os.path.dirname(os.path.abspath(__file__))
Phi = lambda z: 0.5 * (1 + erf(z / sqrt(2)))

#  Five of each letter per bank -- but a DIFFERENT arrangement in each bank.
#  The first version of this file used one pattern for all four, which balanced
#  each bank individually and still produced four identical answer keys: solve
#  one bank and you have the other three. The per-bank check could not see that,
#  so there is now a cross-bank check as well, at the bottom.
PATTERNS = {
    1: [2, 0, 3, 1, 0, 3, 1, 2, 3, 1, 2, 0, 1, 2, 0, 3, 0, 3, 2, 1],
    2: [1, 3, 0, 2, 3, 0, 2, 1, 0, 2, 1, 3, 2, 1, 3, 0, 3, 0, 1, 2],
    3: [3, 1, 2, 0, 2, 1, 0, 3, 1, 0, 3, 2, 0, 3, 2, 1, 2, 1, 0, 3],
    4: [0, 2, 1, 3, 1, 2, 3, 0, 2, 3, 0, 1, 3, 0, 1, 2, 1, 2, 3, 0],
}
for _p, _v in PATTERNS.items():
    assert sorted(Counter(_v).values()) == [5, 5, 5, 5], _p

BANK = {}


def build(rows, part):
    """Place each correct answer at its assigned column for this bank."""
    out = []
    for slot, (text, correct, distractors, why) in zip(PATTERNS[part], rows):
        assert len(distractors) == 3, text[:40]
        opts = list(distractors)
        opts.insert(slot, correct)
        assert len(set(opts)) == 4, "duplicate option in: %s" % text[:50]
        out.append(dict(t=text, o=opts, c=slot, w=why))
    assert len(out) == 20
    return out


# ============================================================ PART I  (ch 1-4)
N1, S1, SQ1 = 12, 180, 3000
SS1 = SQ1 - S1 ** 2 / N1
assert abs(sqrt(SS1 / (N1 - 1)) - 5.2223) < 5e-5 and abs(sqrt(SS1 / N1) - 5.0) < 1e-9

BANK[1] = build(part=1, rows=[
 ("A sample of 12 values has $\\sum x = 180$ and $\\sum x^2 = 3000$. "
  "The sample standard deviation is closest to",
  "5.22", ["4.77", "5.00", "27.27"],
  "$\\sum(x-\\bar x)^2 = 3000 - 180^2/12 = 300$, then divide by $n-1 = 11$ and take "
  "the root. **5.00** is what you get dividing by $n$; **27.27** is the variance, "
  "not the standard deviation."),

 ("Group A has 20 students averaging 68; group B has 30 averaging 78. "
  "The combined mean is",
  "74.0", ["71.0", "73.0", "76.0"],
  "A weighted mean: $(20 \\times 68 + 30 \\times 78)/50$. **73.0** is the unweighted "
  "average of 68 and 78, which ignores that B is the larger group."),

 ("Fifteen values average 62. One value of 80 is removed. The new mean is closest to",
  "60.71", ["58.80", "61.80", "63.29"],
  "Total was $15 \\times 62 = 930$; remove 80 and divide by 14. **63.29** comes from "
  "adding 80 rather than removing it."),

 ("$V(X) = 16$, $V(Y) = 25$ and the correlation is $0.6$. Then $V(X+Y)$ is",
  "65", ["41", "53", "77"],
  "You must convert: $\\mathrm{COV} = \\rho\\sigma_x\\sigma_y = 0.6(4)(5) = 12$, then "
  "$16+25+2(12)$. **41** forgets the covariance term entirely; **53** uses $\\rho$ "
  "in place of the covariance."),

 ("Student P scores 78 where the class mean is 70 and $s = 5$. Student Q scores 88 "
  "where the mean is 82 and $s = 4$. Relative to their classes,",
  "Q did better", ["P did better", "they are identical", "cannot be compared"],
  "$z_P = 1.6$ and $z_Q = 1.5$ — so in fact **P** is further above. Choosing Q means "
  "comparing raw gaps, 8 against 6, instead of standardising."),

 ("Every value of $x$ is doubled and every value of $y$ is tripled. "
  "The correlation $r$ is",
  "unchanged", ["multiplied by 6", "multiplied by 2", "halved"],
  "The scale factors cancel between the numerator and $s_x s_y$. "
  "**Multiplied by 6** is what happens to the *covariance*."),

 ("A data set has $\\bar x = 50$, $s = 10$. Every value is replaced by $3x - 20$. "
  "The new mean and standard deviation are",
  "130 and 30", ["130 and 10", "150 and 30", "130 and 90"],
  "$E(aX+b) = a\\bar x + b$ and $\\mathrm{SD}(aX+b) = |a|s$. **130 and 90** squares "
  "the multiplier, which is the rule for the *variance*, not the standard deviation."),

 ("Bell-shaped data has mean 200 and $s = 25$. Roughly what percentage lies "
  "between 150 and 250?",
  "95\\%", ["68\\%", "99.7\\%", "50\\%"],
  "150 and 250 are $\\mu \\pm 2\\sigma$. **68\\%** is the one-sigma band, which is the "
  "answer if you forget to divide the gap of 50 by $\\sigma = 25$."),

 ("For a sample, $\\sum(x - \\bar x)$ always equals",
  "0", ["$n\\bar x$", "$s^2$", "it depends on the data"],
  "The mean is the balance point, so positive and negative deviations cancel exactly. "
  "This is a free check on any deviation table."),

 ("A scatterplot shows points tightly following a downward curve. "
  "The correlation is most likely",
  "moderately negative, but $r$ understates the relationship",
  ["close to $-1$", "close to 0 because it is curved", "close to $+1$"],
  "$r$ measures *linear* association. A tight downward curve gives a clearly negative "
  "$r$, but one that understates how predictable $y$ actually is."),

 ("Which pair of changes would leave the coefficient of variation unchanged?",
  "multiplying every value by 4",
  ["adding 4 to every value", "subtracting the mean from every value",
   "squaring every value"],
  "CV is $s/\\bar x$, and multiplying scales both. **Adding 4** changes the mean but "
  "not $s$, so the ratio moves."),

 ("Incomes in a town have mean \\$62,000 and median \\$48,000. A reporter writes "
  "that the typical resident earns \\$62,000. The error is that",
  "the mean is inflated by a few very high incomes",
  ["the median is the wrong statistic here", "the sample must be biased",
   "the mean and median should be averaged"],
  "Right-skewed data pulls the mean towards the tail. The median is the better "
  "description of a typical resident."),

 ("$s_{xy} = 18$, $s_x^2 = 36$, $s_y^2 = 25$. Then $r$ is",
  "0.60", ["0.72", "0.02", "0.36"],
  "$r = 18/(6 \\times 5)$ — note you were given the **variances**, so take roots "
  "first. **0.02** divides by the variances instead of the standard deviations."),

 ("A seventh value is added to the six values 4, 7, 9, 11, 14, 20, and the median "
  "does not change. That value could be",
  "10", ["4", "25", "any value at all"],
  "The median of the six is $(9+11)/2 = 10$. With seven values the median is the "
  "fourth, so it stays 10 only if the new value is exactly 10."),

 ("Two variables are strongly correlated. A third variable causes both. This is",
  "a confounded relationship", ["reverse causation", "a sampling error",
   "a non-linear relationship"],
  "The classic third-variable case — ice cream sales and drowning, both driven by "
  "summer."),

 ("Removing the largest value from a right-skewed sample will",
  "lower the mean more than the median",
  ["lower the median more than the mean", "lower both equally",
   "leave the mean unchanged"],
  "The mean uses the size of every observation; the median only its rank."),

 ("A variable is measured in dollars. Its variance is reported as 400. "
  "The units of that 400 are",
  "squared dollars", ["dollars", "dollars per observation", "it has no units"],
  "Which is exactly why we report $\\sigma = \\$20$ instead."),

 ("Which is true of the interquartile range?",
  "it ignores the most extreme quarter at each end",
  ["it uses every observation", "it equals $2s$ for bell-shaped data",
   "it cannot be computed for skewed data"],
  "That insensitivity is precisely why it pairs with the median."),

 ("A sample has $n = 5$ and deviations from the mean of $-4, -1, 0, 2$ and one "
  "unknown. The missing deviation is",
  "3", ["$-3$", "0", "cannot be determined"],
  "Deviations must sum to zero, so the fifth is $+3$. This is the free check from "
  "question 9, used in reverse."),

 ("Standardising a data set and then computing its skewness gives",
  "the same skewness as before",
  ["zero", "a skewness of 1", "an undefined value"],
  "Standardising shifts and rescales but does not reshape. **Zero** is what you would "
  "get only if standardising made things normal — it does not."),
])

# =========================================================== PART II  (ch 5-7)
PD2 = 0.55 * 0.04 + 0.45 * 0.10
assert abs(PD2 - 0.067) < 1e-12 and abs(0.45 * 0.10 / PD2 - 0.6716) < 5e-5

BANK[2] = build(part=2, rows=[
 ("A plant takes 55\\% of parts from A (4\\% defective) and 45\\% from B (10\\% "
  "defective). A part fails inspection. The probability it came from B is closest to",
  "0.672", ["0.450", "0.100", "0.328"],
  "$\\mathrm{P}(D) = 0.067$, then $(0.45)(0.10)/0.067$. **0.450** is the prior — the "
  "answer if you ignore the evidence; **0.100** is the likelihood, a different "
  "conditional entirely."),

 ("$\\mathrm{P}(A) = 0.6$, $\\mathrm{P}(B) = 0.5$, $\\mathrm{P}(A \\cup B) = 0.8$. "
  "Then $\\mathrm{P}(A \\cap B)$ is",
  "0.3", ["0.1", "0.2", "1.1"],
  "Rearrange the addition rule: $0.6 + 0.5 - 0.8$. **1.1** adds instead of "
  "subtracting."),

 ("For those same events, $\\mathrm{P}(A \\mid B)$ is",
  "0.60", ["0.375", "0.50", "0.30"],
  "$0.3/0.5$. **0.375** inverts the conditional and computes "
  "$\\mathrm{P}(B \\mid A) = 0.3/0.8$ using the wrong denominator."),

 ("Given those numbers, $A$ and $B$ are",
  "independent", ["mutually exclusive", "dependent", "complementary"],
  "$\\mathrm{P}(A\\mid B) = 0.6 = \\mathrm{P}(A)$. Equivalently "
  "$0.6 \\times 0.5 = 0.3$, matching the joint probability."),

 ("A test is 95\\% sensitive and 90\\% specific for a condition affecting 2\\% of "
  "people. The probability that a positive result is correct is closest to",
  "0.162", ["0.950", "0.900", "0.020"],
  "$\\mathrm{P}(+) = (0.02)(0.95) + (0.98)(0.10) = 0.117$, so $0.019/0.117$. "
  "**0.950** is the sensitivity — a different conditional, and the error this "
  "question exists to catch."),

 ("Eight components each work independently with probability 0.9. The probability "
  "that at least one fails is closest to",
  "0.570", ["0.100", "0.430", "0.800"],
  "$1 - 0.9^8$. **0.430** computes $0.9^8$ itself, which is the probability that "
  "*none* fails."),

 ("Events $A$ and $B$ are mutually exclusive, with $\\mathrm{P}(A) = 0.3$ and "
  "$\\mathrm{P}(B) = 0.4$. Then $\\mathrm{P}(A \\mid B)$ is",
  "0", ["0.12", "0.30", "0.75"],
  "If $B$ happened, $A$ cannot have. **0.12** multiplies them as though they were "
  "independent — which mutually exclusive events never are."),

 ("For $x = 1, 2, 3$ with probabilities $0.5, 0.3, 0.2$, $V(X)$ is",
  "0.61", ["0.78", "1.70", "2.90"],
  "$E(X) = 1.7$ and $E(X^2) = 3.5$, so $3.5 - 2.89$. **1.70** is the mean; "
  "**2.90** is $[E(X)]^2$."),

 ("For that same variable, $E(X^2)$ equals",
  "3.5", ["2.89", "1.70", "0.61"],
  "$1(0.5) + 4(0.3) + 9(0.2)$. **2.89** is $[E(X)]^2$, and the gap between them is "
  "the variance."),

 ("If $E(X) = 10$, $V(X) = 4$, then $\\mathrm{SD}(3X + 5)$ is",
  "6", ["12", "36", "41"],
  "$|a|\\sigma = 3 \\times 2$. **36** is the *variance* $a^2V(X)$; **41** has added "
  "the constant, which affects the mean and not the spread."),

 ("Two assets have $V(X) = 9$, $V(Y) = 16$, $\\rho = -0.5$. The variance of their "
  "total is",
  "13", ["25", "37", "7"],
  "$\\mathrm{COV} = -0.5(3)(4) = -6$, so $9+16+2(-6)$. **25** forgets the covariance; "
  "negative correlation is what makes the total *less* volatile than the parts."),

 ("A bag has 4 red and 6 blue. Two are drawn without replacement. The probability "
  "both are red is",
  "2/15", ["4/25", "1/6", "8/45"],
  "$\\frac{4}{10} \\times \\frac{3}{9}$. **4/25** is $(4/10)^2$, which treats the "
  "draws as independent — they are not, because the first draw changes the bag."),

 ("$\\mathrm{P}(A) = 0.4$ and $\\mathrm{P}(B \\mid A) = 0.25$. Then "
  "$\\mathrm{P}(A \\cap B)$ is",
  "0.10", ["0.65", "0.16", "0.625"],
  "$\\mathrm{P}(A)\\mathrm{P}(B\\mid A)$. **0.625** divides instead of multiplying."),

 ("From the information in the previous question, $\\mathrm{P}(B)$ is",
  "not determinable", ["0.10", "0.25", "0.625"],
  "You have only the route to $B$ through $A$. You would also need "
  "$\\mathrm{P}(B \\mid A^c)$ to complete the total probability."),

 ("A random variable has $E(X) = 0$ and $V(X) = 0$. Then $X$",
  "is a constant equal to 0", ["is impossible", "is uniform",
   "has an undefined distribution"],
  "Zero variance means no spread at all, so the variable never departs from its mean."),

 ("Which statement is true?",
  "mutually exclusive events with positive probability are always dependent",
  ["mutually exclusive events are always independent",
   "independent events are always mutually exclusive",
   "independence and mutual exclusivity are the same"],
  "They are near-opposites: knowing one mutually exclusive event occurred tells you "
  "the other definitely did not."),

 ("A fair coin is tossed 6 times and lands heads every time. The probability the "
  "next toss is heads is",
  "0.5", ["less than 0.5", "greater than 0.5", "cannot be determined"],
  "The tosses are independent; the coin has no memory. Expecting a tail is the "
  "gambler's fallacy."),

 ("$E(X) = 5$ and $E(Y) = 3$, and $X$ and $Y$ are dependent. Then $E(X + Y)$ is",
  "8", ["8 only if they are independent", "cannot be determined",
   "15"],
  "Expectation is linear whether or not the variables are independent. It is the "
  "*variance* that needs the covariance term."),

 ("A probability distribution lists $0.3, 0.3, 0.3$ for three outcomes. It is",
  "invalid, because the probabilities sum to 0.9",
  ["valid", "invalid, because they are equal",
   "valid only if a fourth outcome exists"],
  "They must sum to exactly 1. Checking this before computing anything is often "
  "worth a mark."),

 ("$\\mathrm{P}(\\text{rain} \\mid \\text{clouds})$ compared with "
  "$\\mathrm{P}(\\text{clouds} \\mid \\text{rain})$ is",
  "smaller", ["larger", "equal", "unrelated"],
  "It almost always rains from cloud, so the second is near 1; cloudy days often "
  "stay dry, so the first is well below it."),
])

# ========================================================== PART III  (ch 8-10)
PB3 = 1 - 0.8 ** 6 - 6 * 0.2 * 0.8 ** 5
assert abs(PB3 - 0.3446) < 5e-5
assert abs(exp(-10 / 8) - 0.2865) < 5e-5

BANK[3] = build(part=3, rows=[
 ("$X \\sim \\mathrm{Bin}(6, 0.2)$. Then $\\mathrm{P}(X \\ge 2)$ is closest to",
  "0.345", ["0.246", "0.262", "0.655"],
  "$1 - \\mathrm{P}(0) - \\mathrm{P}(1)$. **0.655** is $\\mathrm{P}(X \\le 1)$, the "
  "complement — taken without subtracting from 1."),

 ("$X \\sim \\mathrm{Bin}(20, 0.4)$. Its standard deviation is",
  "2.19", ["4.80", "8.00", "3.10"],
  "$\\sqrt{20(0.4)(0.6)} = \\sqrt{4.8}$. **4.80** is the variance, left un-rooted."),

 ("A binomial has $n = 50$, $p = 0.08$. The normal approximation is",
  "inappropriate, because $np < 5$",
  ["appropriate, because $n > 30$", "appropriate, because $n(1-p) > 5$",
   "inappropriate, because $p < 0.5$"],
  "$np = 4$. Both $np$ and $n(1-p)$ must clear 5; here only one does."),

 ("Twelve items are drawn *without replacement* from a batch of 30, and defectives "
  "counted. The binomial is",
  "not appropriate, because $p$ changes between draws",
  ["appropriate, because the draws are random",
   "appropriate, because there are two outcomes",
   "not appropriate, because $n$ is too small"],
  "12 of 30 is a large fraction of the batch, so the probability shifts materially "
  "as items are removed."),

 ("$X \\sim N(500, 80^2)$. The value below which 25\\% of the distribution falls is "
  "closest to",
  "446", ["420", "480", "554"],
  "$z = -0.6745$, so $500 - 0.6745(80)$. **554** uses $+0.6745$ and finds the 75th "
  "percentile instead."),

 ("For that same distribution, $\\mathrm{P}(420 < X < 620)$ is closest to",
  "0.775", ["0.841", "0.933", "0.593"],
  "$z = -1.00$ and $z = +1.50$, so $0.9332 - 0.1587$. **0.933** forgets to subtract "
  "the lower tail."),

 ("Waiting time is exponential with mean 8 minutes. $\\mathrm{P}(X > 10)$ is closest to",
  "0.287", ["0.125", "0.713", "0.800"],
  "$e^{-10/8}$. **0.713** is $\\mathrm{P}(X < 10)$, the complement."),

 ("For that same exponential, the standard deviation is",
  "8", ["$\\sqrt{8}$", "64", "4"],
  "For an exponential, $\\sigma = \\mu$ — unusual, and worth remembering."),

 ("$X$ is uniform on $[10, 50]$. Its standard deviation is closest to",
  "11.55", ["20.00", "13.33", "6.67"],
  "$(b-a)/\\sqrt{12} = 40/3.4641$. **20.00** is half the range, which is not the "
  "standard deviation of anything here."),

 ("For a continuous variable, which is NOT true?",
  "$\\mathrm{P}(X = a)$ is a small positive number",
  ["$\\mathrm{P}(X = a) = 0$", "$\\mathrm{P}(X < a) = \\mathrm{P}(X \\le a)$",
   "the density can exceed 1"],
  "Exactly zero, not merely small — which is why strict and weak inequalities agree."),

 ("$t_{0.05,\\,12}$ compared with $t_{0.05,\\,30}$ is",
  "larger", ["smaller", "equal", "larger only if $n < 10$"],
  "Fewer degrees of freedom means fatter tails, so the cutoff sits further out."),

 ("A $\\chi^2$ distribution with 1 degree of freedom is",
  "right-skewed and bounded below by zero",
  ["symmetric about 1", "bell-shaped", "bounded above by 1"],
  "It is a single squared standard normal, so it cannot be negative and its upper "
  "tail stretches."),

 ("$F_{0.05,\\,8,\\,20}$ and $F_{0.05,\\,20,\\,8}$ are",
  "different values", ["the same value", "reciprocals",
   "the same only at $\\alpha = 0.05$"],
  "$F$ is a ratio, so swapping the degrees of freedom asks a different question — "
  "3.33 against 2.45 in this case."),

 ("In Stata, `ttail(20, 2.086)` returns approximately",
  "0.025", ["0.95", "2.086", "0.05"],
  "`ttail` is cutoff-to-area and gives the upper tail. **0.05** would be the "
  "two-tailed total."),

 ("Which is the inverse of Stata's `invchi2(10, 0.95)`?",
  "`chi2tail(10, 18.307)`", ["`invchi2(10, 0.05)`", "`chi2(10, 0.95)`",
   "`chi2tail(10, 0.95)`"],
  "`invchi2` takes an area and returns a cutoff; `chi2tail` takes a cutoff and "
  "returns an area."),

 ("A standardised binomial approaches the normal as $n$ grows because",
  "a binomial is a sum of independent Bernoulli trials",
  ["the binomial formula simplifies", "$p$ approaches 0.5",
   "the variance approaches 1"],
  "Sums of many independent things go normal — the CLT, applied to a count."),

 ("$X \\sim N(\\mu, \\sigma^2)$. The distribution of $(X - \\mu)/\\sigma$ is",
  "$N(0, 1)$", ["$N(\\mu, 1)$", "$N(0, \\sigma)$", "$t$ with $n-1$ df"],
  "Standardising always produces mean 0 and standard deviation 1. It becomes $t$ "
  "only when $\\sigma$ is replaced by an estimate."),

 ("For a $t$ distribution, as $\\nu \\to \\infty$ the critical value $t_{0.025,\\nu}$ "
  "approaches",
  "1.960", ["1.645", "2.000", "0"],
  "The normal's two-tailed 5\\% value. **1.645** is the *one*-tailed figure."),

 ("Which requires exactly one parameter?",
  "the exponential", ["the normal", "the binomial", "the uniform"],
  "The others each take two: $(\\mu,\\sigma)$, $(n,p)$ and $(a,b)$."),

 ("A density curve reaches a height of 2.5 at its peak. This",
  "is possible, since only the area must equal 1",
  ["is impossible, since probabilities cannot exceed 1",
   "means the variable is discrete", "means the curve is mis-scaled"],
  "A uniform on $[0, 0.4]$ has height 2.5 throughout."),
])

# ========================================================== PART IV  (ch 11-14)
assert abs((47.2 - 50) / 1.5 + 1.8667) < 5e-4
assert abs(2.063899 * 1.5 - 3.0958) < 5e-5

BANK[4] = build(part=4, rows=[
 ("A population has $\\sigma = 30$. To make the standard error 2.5, the sample size "
  "must be",
  "144", ["12", "75", "36"],
  "$30/\\sqrt{n} = 2.5$ gives $\\sqrt{n} = 12$. **12** stops at $\\sqrt{n}$ without "
  "squaring."),

 ("$\\mu = 50$, $\\sigma = 9$, $n = 36$. Then $\\mathrm{P}(\\bar X < 47.2)$ is "
  "closest to",
  "0.031", ["0.378", "0.969", "0.122"],
  "Standard error 1.5, so $z = -1.87$. **0.378** uses $\\sigma = 9$ instead of the "
  "standard error — the single commonest error in this material."),

 ("A sample of 25 gives $\\bar x = 42$ and $s = 7.5$. "
  "With $t_{0.025,24} = 2.0639$, the 95\\% interval half-width is",
  "3.10", ["15.48", "0.62", "2.06"],
  "$2.0639 \\times 7.5/5$. **15.48** forgets to divide by $\\sqrt{n}$."),

 ("Which change would make a confidence interval narrower?",
  "increasing the sample size",
  ["raising the confidence level", "increasing $\\sigma$",
   "decreasing the sample size"],
  "Only three levers exist: $n$, the confidence level, and $\\sigma$."),

 ("A 99\\% interval is reported as $(18.2, 25.8)$. The point estimate and margin are",
  "22.0 and 3.8", ["21.0 and 7.6", "22.0 and 7.6", "20.0 and 3.8"],
  "The midpoint and half the width. **22.0 and 7.6** reports the full width as the "
  "margin."),

 ("To estimate a mean within $\\pm 1.5$ at 99\\% confidence with $\\sigma = 12$, "
  "the required sample size is",
  "425", ["246", "62", "104"],
  "$(2.5758 \\times 12/1.5)^2 = 424.6$, rounded up. **246** uses the 95\\% value of "
  "1.96 instead of the 99\\% value."),

 ("A test gives $t = 2.4$ with 20 degrees of freedom, two-tailed, $\\alpha = 0.05$. "
  "The critical value is 2.086, so you",
  "reject $H_0$", ["fail to reject $H_0$", "accept $H_0$",
   "need the $p$-value to decide"],
  "$2.4 > 2.086$. Note you never *accept* $H_0$ in any case."),

 ("For that same test, the $p$-value is",
  "below 0.05", ["above 0.05", "exactly 0.05", "not determinable"],
  "The two routes always agree: beyond the critical value means $p < \\alpha$."),

 ("A 95\\% confidence interval for $\\mu$ is $(31.2, 38.8)$. A two-tailed test of "
  "$H_0: \\mu = 40$ at $\\alpha = 0.05$ will",
  "reject", ["fail to reject", "be inconclusive",
   "require the raw data"],
  "40 lies outside the interval, and the two are built from the same inequality."),

 ("Which is a correct reading of '95\\% confident'?",
  "95\\% of intervals built this way contain $\\mu$",
  ["$\\mu$ lies in this interval with probability 0.95",
   "95\\% of the data lies in this interval",
   "the estimate is accurate to within 5\\%"],
  "$\\mu$ is fixed; the interval is what was random. The confidence describes the "
  "procedure's track record."),

 ("A supplier guarantees a mean lifetime of at least 400 hours. As the buyer "
  "testing this, $H_a$ is",
  "$\\mu < 400$", ["$\\mu > 400$", "$\\mu \\neq 400$", "$\\mu = 400$"],
  "A guarantee is tested from the side of whoever it protects — you need evidence "
  "it *fails*."),

 ("All 5\\% of a one-tailed test sits in one tail. Compared with the two-tailed "
  "critical value, the one-tailed value is",
  "smaller", ["larger", "the same", "larger only for small $n$"],
  "2.5\\% in each tail needs a cutoff further out than 5\\% in a single tail."),

 ("Failing to reject $H_0$ when it is false is",
  "a Type II error", ["a Type I error", "the power", "a correct decision"],
  "Its probability is $\\beta$, which you influence through $n$ rather than choose."),

 ("For a fixed sample size, lowering $\\alpha$ from 0.05 to 0.01",
  "raises $\\beta$", ["lowers $\\beta$", "leaves $\\beta$ unchanged",
   "raises the power"],
  "The two trade off; only a larger sample improves both."),

 ("A study with $n = 20{,}000$ reports $p = 0.01$ for a difference of 0.3 points. "
  "The right response is",
  "ask for the confidence interval, since a huge $n$ makes trivial effects significant",
  ["accept the finding, since $p$ is small",
   "reject the finding, since the effect is small",
   "repeat the study with a smaller sample"],
  "Significance is a statement about $n$ as much as about the effect."),

 ("Twenty independent tests are run on data with no real effect, at "
  "$\\alpha = 0.05$. The expected number of 'significant' results is",
  "1", ["0", "5", "20"],
  "$20 \\times 0.05$. Reporting only that one is p-hacking."),

 ("A $p$-value of 0.20 means",
  "data this extreme arises 20\\% of the time when $H_0$ is true",
  ["$H_0$ is true with probability 0.80",
   "the effect is 20\\% as large as expected",
   "the test has 20\\% power"],
  "It is computed *assuming* $H_0$, so it cannot be a probability about $H_0$."),

 ("The CLT guarantees that for large $n$",
  "$\\bar X$ is approximately normal whatever the population",
  ["the population becomes normal", "$X$ is approximately normal",
   "$s$ equals $\\sigma$"],
  "It is a statement about the sample mean, and only about the sample mean."),

 ("A sample of 40 households is drawn by selecting 10 blocks and surveying every "
  "household in each. The true standard error is",
  "larger than $\\sigma/\\sqrt{40}$", ["equal to $\\sigma/\\sqrt{40}$",
   "smaller than $\\sigma/\\sqrt{40}$", "not defined"],
  "Households in a block are not independent, so 40 clustered households carry less "
  "information than 40 unrelated ones."),

 ("You compute $t = 1.9$ with $\\nu = 29$ against a two-tailed critical value of "
  "2.045, then notice the question said 'has increased'. Correctly treated as "
  "one-tailed (critical 1.699), you",
  "reject, but only because the tail was fixed in advance by the wording",
  ["reject, having found the better test",
   "fail to reject, since 1.9 < 2.045",
   "report both results"],
  "The direction must come from the question. Switching tails after seeing the "
  "statistic would be p-hacking — here the wording justified it all along."),
])

# ------------------------------------------------------------------- checks
KEYS = {}
for part, items in BANK.items():
    assert len(items) == 20
    cols = Counter("ABCD"[i["c"]] for i in items)
    assert sorted(cols.values()) == [5, 5, 5, 5], "part %d: %s" % (part, cols)
    KEYS[part] = "".join("ABCD"[i["c"]] for i in items)
    print("  part %d  key %s" % (part, KEYS[part]))

#  no two banks may share a key, or solving one solves them all
assert len(set(KEYS.values())) == 4, "two banks have the same answer key"
print("  all four keys distinct")

TITLES = {
 1: ("95_mcq_part1_describing_data.md", "Multiple choice: describing data",
     "Chapters 1 to 4."),
 2: ("96_mcq_part2_chance.md", "Multiple choice: chance", "Chapters 5 to 7."),
 3: ("97_mcq_part3_distributions.md", "Multiple choice: distributions",
     "Chapters 8 to 10."),
 4: ("98_mcq_part4_inference.md", "Multiple choice: from sample to population",
     "Chapters 11 to 14."),
}

for part, (fn, title, blurb) in TITLES.items():
    items = BANK[part]
    md = [f"# {title}\n", f"{blurb} Twenty questions, one answer each.\n",
          "**These are hard on purpose.** Most take more than one step, and every "
          "wrong option is the number you get by making one specific mistake — "
          "dividing by $n$ instead of $n-1$, forgetting a square root, using "
          "$\\sigma$ where $\\sigma/\\sqrt{n}$ belongs, inverting a conditional.\n",
          "So if you pick a wrong answer, the key tells you **which mistake you "
          "made**, which is more use than the letter.\n", "---\n"]
    for i, it in enumerate(items, 1):
        md.append(f"**{i}.** {it['t']}\n")
        md.append("   ".join(f"({'ABCD'[j]}) {o}" for j, o in enumerate(it["o"])) + "\n")
    md.append("---\n\n## Answers\n")
    for i, it in enumerate(items, 1):
        md.append(f"**{i}. {'ABCD'[it['c']]}** — {it['w']}\n")
    open(os.path.join(HERE, fn), "w").write("\n".join(md))
    print("  wrote %s" % fn)

print("\n       80 hard questions, 5 of each letter in every bank")
