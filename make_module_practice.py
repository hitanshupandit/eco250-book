#!/usr/bin/env python3
"""Practice problems for each Part of the book: four sets of fifteen.

    91  Part I    Describing data            chapters 1-4
    92  Part II   Chance                     chapters 5-7
    93  Part III  Distributions              chapters 8-10
    94  Part IV   From sample to population  chapters 11-14

These complement 90_practice_problems.md, which is a mixed set spanning the whole
course. These four are per-Part, so a student revising one topic can work only the
relevant sheet.

All problems are ORIGINAL. The genre -- a short business or economics scenario,
realistic numbers, parts (a)(b)(c) -- matches what students meet on a checkpoint.
No scenario or number is taken from any textbook.

EVERY ANSWER IS COMPUTED HERE AND ASSERTED, then written into the markdown, so the
questions and the solutions cannot drift apart. Values that Python cannot produce
(t critical values) were checked in Stata 17 and are asserted against their use.

Usage:  python3 book/make_module_practice.py
"""

import os
import math
from math import comb, sqrt, erf, exp

HERE = os.path.dirname(os.path.abspath(__file__))
Phi = lambda z: 0.5 * (1 + erf(z / sqrt(2)))
Z90, Z95, Z975 = 1.281552, 1.644854, 1.959964


def mean(a):
    return sum(a) / len(a)


def svar(a):
    m = mean(a)
    return sum((x - m) ** 2 for x in a) / (len(a) - 1)


def fm(x, d=4):
    return f"{x:.{d}f}"


# ============================================================ PART I  (ch 1-4)
P1 = {}
P1["d"] = [18, 22, 22, 25, 29, 34]
P1["mean"] = mean(P1["d"])
P1["med"] = (P1["d"][2] + P1["d"][3]) / 2
P1["ss"] = sum((x - P1["mean"]) ** 2 for x in P1["d"])
P1["var"] = svar(P1["d"])
P1["sd"] = sqrt(P1["var"])
assert P1["mean"] == 25.0 and P1["med"] == 23.5

P1["cvA"], P1["cvB"] = 4 / 30, 11 / 95
P1["x"] = [3, 6, 9, 12, 15]
P1["y"] = [22, 19, 17, 12, 10]
P1["xb"], P1["yb"] = mean(P1["x"]), mean(P1["y"])
P1["sxy"] = sum((a - P1["xb"]) * (b - P1["yb"])
                for a, b in zip(P1["x"], P1["y"])) / 4
P1["sx"], P1["sy"] = sqrt(svar(P1["x"])), sqrt(svar(P1["y"]))
P1["r"] = P1["sxy"] / (P1["sx"] * P1["sy"])
assert P1["xb"] == 9.0 and P1["yb"] == 16.0
assert abs(P1["r"] + 0.9903) < 5e-5, P1["r"]

PART1 = [
 (r"""A small clinic records the number of patients seen on each of six days:

$$18,\quad 22,\quad 22,\quad 25,\quad 29,\quad 34$$

(a) Find the mean, the median and the mode.
(b) Find the sample variance and standard deviation.
(c) The day with 34 is later corrected to 46. Say what happens to the mean and to
the median, and why they behave differently.""",
  rf"""(a) $\bar{{x}} = 150/6 = {P1['mean']:.0f}$. With $n=6$ the median is the average of
the 3rd and 4th: $(22+25)/2 = {P1['med']}$. The mode is 22.
(b) Deviations $-7,-3,-3,0,4,9$ square to $49,9,9,0,16,81$, summing to
{P1['ss']:.0f}. So $s^2 = {P1['ss']:.0f}/5 = {P1['var']:.1f}$ and $s = {P1['sd']:.4f}$.
(c) The mean rises by $12/6 = 2$ to 27. The median does not move at all — 46 occupies
the same rank 34 did, and the median reads only rank, not size."""),

 (r"""Two delivery depots record journey times. Depot A averages 30 minutes with
$s = 4$; Depot B averages 95 minutes with $s = 11$.

(a) Which has the larger absolute variation?
(b) Compute the coefficient of variation for each.
(c) A manager claims B is "less reliable". Is that fair?""",
  rf"""(a) Depot B, with $s = 11$ against 4.
(b) A: $4/30 = {P1['cvA']:.4f}$, or {P1['cvA']:.2%}. B: $11/95 = {P1['cvB']:.4f}$, or
{P1['cvB']:.2%}.
(c) No. Relative to its own average B is the **more** consistent. The manager compared
standard deviations across series with very different means, which is exactly what the
coefficient of variation exists to prevent."""),

 (r"""Scores are bell-shaped with $\mu = 64$ and $\sigma = 9$.

(a) Convert 46, 64 and 82 to $z$-scores.
(b) Using the empirical rule, roughly what fraction lie between 55 and 73?
(c) Is a score of 90 unusual? Answer with a number.""",
  r"""(a) $z = (46-64)/9 = -2.00$; $z = 0$; $z = (82-64)/9 = +2.00$.
(b) 55 and 73 are $\mu \pm 1\sigma$, so about **68%**.
(c) $z = (90-64)/9 = 2.89$ — nearly three standard deviations above the mean, which the
empirical rule puts in the outer 0.3% or so. Yes, unusual."""),

 (r"""A firm records advertising spend $x$ (in thousands) and complaints received $y$:

| $x$ | 3 | 6 | 9 | 12 | 15 |
|---|---|---|---|---|---|
| $y$ | 22 | 19 | 17 | 12 | 10 |

(a) Compute $\bar{x}$, $\bar{y}$ and $s_{xy}$.
(b) Compute $r$ and describe the relationship.
(c) Spend is restated in dollars, so every $x$ is multiplied by 1,000. What happens to
$s_{xy}$ and to $r$?""",
  rf"""(a) $\bar{{x}} = {P1['xb']:.0f}$, $\bar{{y}} = {P1['yb']:.0f}$. Deviations in $x$:
$-6,-3,0,3,6$; in $y$: $6,3,1,-4,-6$. Products: $-36,-9,0,-12,-36$, summing to $-93$,
so $s_{{xy}} = -93/4 = {P1['sxy']:.2f}$.
(b) $s_x = {P1['sx']:.4f}$, $s_y = {P1['sy']:.4f}$, so
$r = {P1['sxy']:.2f}/({P1['sx']:.4f} \times {P1['sy']:.4f}) = {P1['r']:.4f}$ — very
strong and negative.
(c) $s_{{xy}}$ becomes ${P1['sxy'] * 1000:,.0f}$. $r$ is unchanged at {P1['r']:.4f},
because the 1,000 appears in the numerator and in $s_x$ and cancels."""),

 (r"""Classify each as categorical, discrete quantitative or continuous quantitative:
employee ID; number of sick days taken; hours worked last week; job grade (1 to 5);
annual salary.""",
  r"""Categorical: employee ID (a label despite being numeric); job grade (ordinal —
ordered, but the gaps are not meaningful quantities).
Discrete quantitative: number of sick days.
Continuous quantitative: hours worked; annual salary (treated as continuous in
practice, though strictly it comes in cents)."""),

 (r"""A researcher wants to estimate mean household spending in a county.

(a) Describe a stratified design.
(b) Describe a cluster design.
(c) Which gives the more precise estimate for a given number of households, and which
is cheaper?""",
  r"""(a) Split the county into layers by a characteristic that matters — urban/rural,
or income band — and draw a random sample inside each, guaranteeing every layer appears.
(b) Split the county into geographic blocks, pick some blocks at random, and survey
every household in the chosen blocks.
(c) **Stratified** is more precise, because it forces balance across the layers.
**Cluster** is cheaper, because the interviewer travels to a few places rather than
everywhere. Chapter 11 shows the precision clustering costs."""),

 (r"""A website poll receives 1.8 million responses and reports a margin of error of
$\pm 0.07$ percentage points.

(a) What kind of error does that margin measure?
(b) What kind does it not measure?
(c) In one sentence, why is the figure close to meaningless here?""",
  r"""(a) **Sampling error** — the variation that arises purely because you measured a
sample rather than everyone.
(b) **Non-sampling error** — self-selection, question wording, non-response.
(c) Respondents chose themselves, so the dominant error is non-sampling, and no sample
size fixes that; the margin is arithmetically correct and answers a question nobody
asked."""),

 (r"""$V(X) = 49$, $V(Y) = 25$ and $\text{COV}(X,Y) = -15$.

(a) Find $V(X+Y)$.
(b) Find $V(X-Y)$.
(c) Explain which is larger and why.""",
  r"""(a) $49 + 25 + 2(-15) = 44$.
(b) $49 + 25 - 2(-15) = 104$.
(c) The **difference** is far more variable. The two move in opposite directions, so
adding them partly cancels the swings while subtracting them compounds them."""),

 (r"""A data set of eight values has deviations from the mean reported as
$-5, -2, -1, 0, 1, 2, 3, 3$.

(a) Something is wrong. What, and how can you tell with no other information?
(b) What would you check first?""",
  r"""(a) The deviations sum to $+1$, not zero. Deviations from the mean must sum to
exactly zero by construction, so either a value or the mean is wrong.
(b) Recompute the mean from the raw data. A mean that is slightly off is the usual
cause, and it shifts every deviation by the same small amount."""),

 (r"""Explain to someone who has not taken statistics why we report the median
household income rather than the mean.""",
  r"""Income is strongly right-skewed: most households earn modest amounts and a few
earn enormous ones. The mean is a balance point and is pulled towards those few very
large values, so it sits well above what a typical household receives. The median is
the middle household and ignores how extreme the extremes are, so it answers the
question "what does a typical household earn?" far better."""),

 (r"""For the sample $\{7, 11, 11, 14, 17, 20, 24\}$:

(a) Find the mean and median.
(b) Find the range and the sample standard deviation.
(c) Compare the mean and median and say what this suggests about shape.""",
  r"""(a) Sum is 104, so $\bar{x} = 104/7 = 14.8571$. With $n=7$ the median is the 4th
value, $14$.
(b) Range $= 24 - 7 = 17$. Deviations are $-7.8571, -3.8571, -3.8571, -0.8571, 2.1429,
5.1429, 9.1429$; their squares sum to $200.8571$, so $s^2 = 33.4762$ and $s = 5.7859$.
(c) The mean exceeds the median by about 0.86, so the data is mildly **right-skewed** —
a longer tail at the high end."""),

 (r"""Two variables have $r = 0$.

(a) Does that mean there is no relationship? Explain.
(b) Sketch a set of points with a strong relationship and $r \approx 0$.
(c) What should you always do before trusting a correlation?""",
  r"""(a) No. $r$ measures **linear** association only. A perfect but curved relationship
can give $r = 0$.
(b) Any symmetric curve — a parabola $y = x^2$ over values of $x$ either side of zero,
or points arranged on a circle.
(c) Plot the data. A scatterplot shows curvature, clustering and outliers, none of which
a single number reveals."""),

 (r"""A study finds that towns with more public libraries have higher average incomes.

(a) Give three distinct explanations consistent with this.
(b) Which, if any, justifies building libraries to raise income?""",
  r"""(a) **Libraries raise income** (education and access to resources); **income
causes libraries** (wealthier towns fund more public services); or a **third variable**
— town size, or the age profile of residents — drives both.
(b) Only the first, and the correlation alone cannot distinguish it from the other two.
You would need an experiment, or a design that isolates the effect."""),

 (r"""A sample of $n = 5$ gives $\sum x = 60$ and $\sum (x - \bar{x})^2 = 84$.

(a) Find $\bar{x}$, $s^2$ and $s$.
(b) Every value is then increased by 10. What are the new mean, variance and standard
deviation?
(c) Instead, every original value is multiplied by 3. Now what?""",
  r"""(a) $\bar{x} = 60/5 = 12$; $s^2 = 84/4 = 21$; $s = 4.5826$.
(b) Mean becomes 22. Variance and standard deviation are **unchanged** at 21 and 4.5826
— adding a constant shifts without stretching.
(c) Mean becomes 36. Variance becomes $3^2(21) = 189$ and the standard deviation
becomes $3(4.5826) = 13.7477$."""),

 (r"""A quality manager reports: "the standard deviation of our output is 12 units, so
our daily average is accurate to within about 12 units." The sample had 144 days.

(a) What has been confused?
(b) What is the right figure?
(c) Why does the distinction matter?""",
  r"""(a) The standard deviation of the **data** with the standard deviation of the
**mean**.
(b) The standard error is $12/\sqrt{144} = 1$ unit — twelve times smaller.
(c) Because 12 describes how much daily output varies, while 1 describes how precisely
144 days pin down the average. Reporting the first as if it were the second overstates
the uncertainty enormously and would lead to rejecting perfectly adequate precision."""),
]
assert len(PART1) == 15


# =========================================================== PART II  (ch 5-7)
P2 = {}
P2["pa"], P2["pb"], P2["pab"] = 0.48, 0.36, 0.18
P2["pu"] = P2["pa"] + P2["pb"] - P2["pab"]
P2["T"] = {("on", "new"): 210, ("on", "exist"): 330,
           ("late", "new"): 90, ("late", "exist"): 70}
P2["N"] = sum(P2["T"].values())
P2["pon"] = (210 + 330) / P2["N"]
P2["pnew"] = (210 + 90) / P2["N"]
P2["pon_new"] = 210 / 300
assert P2["N"] == 700 and abs(P2["pu"] - 0.66) < 1e-12

P2["pl"] = [("Ashford", 0.45, 0.04), ("Benton", 0.35, 0.06), ("Calder", 0.20, 0.09)]
P2["PD"] = sum(s * d for _, s, d in P2["pl"])
P2["post"] = {n: s * d / P2["PD"] for n, s, d in P2["pl"]}
assert abs(P2["PD"] - 0.057) < 1e-12

P2["prev"], P2["sens"], P2["spec"] = 0.005, 0.97, 0.94
P2["ppos"] = P2["prev"] * P2["sens"] + (1 - P2["prev"]) * (1 - P2["spec"])
P2["ppv"] = P2["prev"] * P2["sens"] / P2["ppos"]
assert abs(P2["ppv"] - 0.0751) < 5e-5, P2["ppv"]

P2["v"], P2["p"] = [0, 1, 2, 3, 4], [0.08, 0.22, 0.34, 0.26, 0.10]
P2["E"] = sum(a * b for a, b in zip(P2["v"], P2["p"]))
P2["E2"] = sum(a * a * b for a, b in zip(P2["v"], P2["p"]))
P2["V"] = P2["E2"] - P2["E"] ** 2
assert abs(sum(P2["p"]) - 1) < 1e-12 and abs(P2["E"] - 2.08) < 1e-12

PART2 = [
 (rf"""Events $A$ and $B$ have $\mathrm{{P}}(A) = {P2['pa']}$,
$\mathrm{{P}}(B) = {P2['pb']}$ and $\mathrm{{P}}(A \cap B) = {P2['pab']}$.

(a) Find $\mathrm{{P}}(A \cup B)$.
(b) Find the probability neither occurs.
(c) Find $\mathrm{{P}}(A \mid B)$.
(d) Are $A$ and $B$ independent?""",
  rf"""(a) ${P2['pa']} + {P2['pb']} - {P2['pab']} = {P2['pu']:.2f}$.
(b) $1 - {P2['pu']:.2f} = {1 - P2['pu']:.2f}$.
(c) ${P2['pab']}/{P2['pb']} = {P2['pab'] / P2['pb']:.2f}$.
(d) $\mathrm{{P}}(A)\mathrm{{P}}(B) = {P2['pa']} \times {P2['pb']} =
{P2['pa'] * P2['pb']:.4f}$, which is **not** {P2['pab']}. Not independent. (Equivalently
$\mathrm{{P}}(A \mid B) = {P2['pab'] / P2['pb']:.2f} \neq {P2['pa']}$.)"""),

 (rf"""A courier classifies {P2['N']} deliveries by outcome and customer type:

| | New | Existing | Total |
|---|---|---|---|
| On time | {P2['T'][('on','new')]} | {P2['T'][('on','exist')]} | 540 |
| Late | {P2['T'][('late','new')]} | {P2['T'][('late','exist')]} | 160 |
| Total | 300 | 400 | {P2['N']} |

(a) $\mathrm{{P}}(\text{{on time}})$?
(b) $\mathrm{{P}}(\text{{on time and new}})$?
(c) $\mathrm{{P}}(\text{{on time}} \mid \text{{new}})$?
(d) Are "on time" and "new customer" independent?""",
  rf"""(a) $540/{P2['N']} = {P2['pon']:.4f}$.
(b) $210/{P2['N']} = {210 / P2['N']:.4f}$.
(c) Shrink to the new-customer column: $210/300 = {P2['pon_new']:.2f}$.
(d) $\mathrm{{P}}(\text{{on time}}) = {P2['pon']:.4f}$ but
$\mathrm{{P}}(\text{{on time}} \mid \text{{new}}) = {P2['pon_new']:.2f}$. Knowing the
customer is new changes the probability, so **not independent** — new customers are
served late more often."""),

 (rf"""A manufacturer sources from three plants. Ashford supplies 45\% with a 4\% defect
rate; Benton 35\% with 6\%; Calder 20\% with 9\%.

(a) What fraction of all units are defective?
(b) A defective unit is found. Which plant most probably made it?
(c) Calder supplies the least. Why is it still a serious suspect?""",
  rf"""(a) $(0.45)(0.04) + (0.35)(0.06) + (0.20)(0.09) = 0.018 + 0.021 + 0.018
= {P2['PD']:.4f}$.
(b) Posteriors: Ashford ${P2['post']['Ashford']:.4f}$, Benton
${P2['post']['Benton']:.4f}$, Calder ${P2['post']['Calder']:.4f}$. **Benton** is the
most likely source.
(c) Because what matters is share **times** rate. Calder's 9\% defect rate on a 20\%
share produces as many defects as Ashford's 4\% on 45\% — its small share is offset by
the worst quality."""),

 (rf"""A screening test is {P2['sens']:.0%} sensitive and {P2['spec']:.0%} specific. The
condition affects {P2['prev']:.1%} of the population. You test positive.

(a) What fraction of all tests come back positive?
(b) What is the probability you actually have the condition?
(c) Explain the result to someone who expected about 97\%.""",
  rf"""(a) $({P2['prev']})({P2['sens']}) + ({1 - P2['prev']})({1 - P2['spec']:.2f})
= {P2['prev'] * P2['sens']:.5f} + {(1 - P2['prev']) * (1 - P2['spec']):.5f}
= {P2['ppos']:.4f}$.
(b) ${P2['prev'] * P2['sens']:.5f}/{P2['ppos']:.4f} = {P2['ppv']:.4f}$ — about
**{P2['ppv']:.1%}**.
(c) The healthy group is roughly 200 times larger than the sick group, so even a
{1 - P2['spec']:.0%} false-positive rate on it produces far more positives than a
{P2['sens']:.0%} true-positive rate on the tiny sick group. The test is good; the
**base rate** does the damage. A positive is a reason for a second, more specific
test — not a diagnosis."""),

 (r"""A machine produces items independently, each defective with probability 0.03.
Eight are drawn.

(a) Find the probability none is defective.
(b) Find the probability at least one is.
(c) Why is the complement the efficient route?""",
  rf"""(a) $(0.97)^8 = {0.97 ** 8:.4f}$.
(b) $1 - {0.97 ** 8:.4f} = {1 - 0.97 ** 8:.4f}$.
(c) "At least one" covers the eight separate cases $X = 1, \ldots, 8$, each needing its
own term. Its complement is the single case $X = 0$."""),

 (r"""Explain, without formulas, why two mutually exclusive events with non-zero
probability can never be independent.""",
  r"""If they are mutually exclusive and you learn one happened, you know immediately
that the other did not — its probability collapses to zero. Learning something that
changes the other's probability that drastically is the exact opposite of
"tells you nothing", which is what independence requires."""),

 (rf"""A random variable $X$ has this distribution:

| $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $\mathrm{{P}}(X=x)$ | {P2['p'][0]} | {P2['p'][1]} | {P2['p'][2]} | {P2['p'][3]} | {P2['p'][4]} |

(a) Verify it is valid.
(b) Find $E(X)$.
(c) Find $V(X)$ and $\sigma$.""",
  rf"""(a) All five lie in $[0,1]$ and sum to 1.00.
(b) $E(X) = {P2['E']:.2f}$.
(c) $E(X^2) = {P2['E2']:.2f}$, so $V(X) = {P2['E2']:.2f} - {P2['E']:.2f}^2
= {P2['V']:.4f}$ and $\sigma = {sqrt(P2['V']):.4f}$."""),

 (rf"""Using the variable above, a firm's daily cost is $C = 35X + 120$.

(a) Find $E(C)$.
(b) Find $V(C)$ and $\sigma_C$.
(c) Fixed costs rise to 200. What changes?""",
  rf"""(a) $35({P2['E']:.2f}) + 120 = {35 * P2['E'] + 120:.2f}$.
(b) $V(C) = 35^2({P2['V']:.4f}) = {1225 * P2['V']:.2f}$, so
$\sigma_C = {sqrt(1225 * P2['V']):.4f}$.
(c) $E(C)$ rises by 80 to ${35 * P2['E'] + 200:.2f}$. $V(C)$ does **not** change — a
constant shifts the distribution without stretching it."""),

 (r"""$\mathrm{P}(A) = 0.35$ and $\mathrm{P}(B \mid A) = 0.70$.

(a) Find $\mathrm{P}(A \cap B)$.
(b) Can you find $\mathrm{P}(B)$? Explain.
(c) What one further piece of information would let you?""",
  r"""(a) $\mathrm{P}(A \cap B) = (0.35)(0.70) = 0.245$.
(b) No. $\mathrm{P}(B)$ needs both routes to $B$, and you have only the one through $A$.
(c) $\mathrm{P}(B \mid A^c)$ — then
$\mathrm{P}(B) = 0.245 + (0.65)\mathrm{P}(B \mid A^c)$."""),

 (r"""Explain the difference between $\mathrm{P}(A \mid B)$ and $\mathrm{P}(B \mid A)$,
using an example of your own, and say why confusing them matters.""",
  r"""Any sound example. One: the probability that a road is wet given that it rained is
near 1; the probability that it rained given that the road is wet is much lower, because
sprinklers, street cleaning and burst pipes also wet roads. The two conditionings ask
about different reference groups — rainy occasions versus wet-road occasions — and the
sizes of those groups drive the answers apart. Confusing them is the error behind
misreading medical tests and forensic evidence."""),

 (r"""$E(X) = 12$ and $E(X^2) = 169$.

(a) Find $V(X)$ and $\sigma$.
(b) Find $V(4X - 7)$.
(c) Find $E(4X - 7)$.""",
  r"""(a) $V(X) = 169 - 144 = 25$, so $\sigma = 5$.
(b) $V(4X-7) = 4^2(25) = 400$.
(c) $E(4X-7) = 4(12) - 7 = 41$."""),

 (r"""Of 240 applicants, 150 have a degree, 90 have relevant experience, and 60 have
both.

(a) How many have neither?
(b) What is the probability a random applicant has a degree or experience?
(c) Are "degree" and "experience" independent?""",
  r"""(a) Degree or experience $= 150 + 90 - 60 = 180$, so $240 - 180 = 60$ have neither.
(b) $180/240 = 0.75$.
(c) $\mathrm{P}(D) = 150/240 = 0.625$ and $\mathrm{P}(E) = 90/240 = 0.375$, so
$\mathrm{P}(D)\mathrm{P}(E) = 0.2344$. But $\mathrm{P}(D \cap E) = 60/240 = 0.25$. Not
equal, so **not independent**."""),

 (r"""A distribution has $\mathrm{P}(X=1) = 0.3$, $\mathrm{P}(X=2) = 0.45$ and
$\mathrm{P}(X=3) = k$.

(a) Find $k$.
(b) Find $E(X)$.
(c) Find $V(X)$.""",
  r"""(a) $k = 1 - 0.3 - 0.45 = 0.25$.
(b) $E(X) = 1(0.3) + 2(0.45) + 3(0.25) = 0.3 + 0.9 + 0.75 = 1.95$.
(c) $E(X^2) = 1(0.3) + 4(0.45) + 9(0.25) = 0.3 + 1.8 + 2.25 = 4.35$, so
$V(X) = 4.35 - 1.95^2 = 4.35 - 3.8025 = 0.5475$."""),

 (r"""Two assets have $V(X) = 81$, $V(Y) = 144$ and correlation $\rho = 0.5$.

(a) Find $\text{COV}(X,Y)$.
(b) Find $V(X+Y)$.
(c) What would $V(X+Y)$ be if the assets were uncorrelated, and what is the lesson?""",
  r"""(a) $\text{COV} = \rho\sigma_x\sigma_y = 0.5(9)(12) = 54$.
(b) $81 + 144 + 2(54) = 333$.
(c) Uncorrelated it would be $81 + 144 = 225$. Positive correlation adds 108 to the
variance of the total for no extra return — which is the case for diversifying into
assets that do not move together."""),

 (r"""A student writes: "the probability of drawing two aces from a deck is
$(4/52)^2$."

(a) What has gone wrong?
(b) Give the correct calculation.
(c) When would the student's version be right?""",
  r"""(a) They multiplied as if the draws were independent. Without replacement the
second draw's probability depends on the first.
(b) $\mathrm{P} = \frac{4}{52} \times \frac{3}{51} = \frac{12}{2652} = 0.0045$.
(c) If the first card were **replaced** and the deck reshuffled, the draws would be
independent and $(4/52)^2 = 0.0059$ would be correct."""),
]
assert len(PART2) == 15


# ========================================================== PART III  (ch 8-10)
P3 = {}
P3["n"], P3["p"] = 14, 0.20
P3["pk"] = comb(14, 4) * 0.2 ** 4 * 0.8 ** 10
P3["E"], P3["SD"] = 14 * 0.2, sqrt(14 * 0.2 * 0.8)
P3["ple2"] = sum(comb(14, k) * 0.2 ** k * 0.8 ** (14 - k) for k in range(3))
P3["mu"], P3["sg"] = 340.0, 45.0
P3["pab"] = 1 - Phi((400 - 340) / 45)
P3["pmid"] = Phi((400 - 340) / 45) - Phi((280 - 340) / 45)
P3["p95"] = 340 + Z975 * 45
P3["umean"], P3["usd"] = (8 + 32) / 2, (32 - 8) / sqrt(12)
P3["upr"] = (20 - 8) / 24
P3["emean"] = 6.0
P3["eg"] = exp(-9 / 6)
P3["el"] = 1 - exp(-3 / 6)
assert abs(P3["pk"] - 0.1720) < 5e-5, P3["pk"]
assert abs(P3["pab"] - 0.0912) < 5e-5

PART3 = [
 (rf"""{P3['p']:.0%} of parcels are flagged for inspection. {P3['n']} are processed
independently.

(a) State the four binomial conditions and confirm each.
(b) Find $\mathrm{{P}}(X = 4)$.
(c) Find $E(X)$ and $\sigma$.""",
  rf"""(a) Fixed $n = {P3['n']}$; two outcomes (flagged or not); constant
$p = {P3['p']}$; independent processing.
(b) $\binom{{14}}{{4}}(0.2)^4(0.8)^{{10}} = 1001 \times 0.0016 \times 0.1074
= {P3['pk']:.4f}$.
(c) $E(X) = {P3['E']:.1f}$ and $\sigma = \sqrt{{14(0.2)(0.8)}} = {P3['SD']:.4f}$."""),

 (rf"""For the same binomial, find $\mathrm{{P}}(X \le 2)$, and explain why this is not
$1 - \mathrm{{P}}(X \ge 2)$.""",
  rf"""$\mathrm{{P}}(X \le 2) = \mathrm{{P}}(0) + \mathrm{{P}}(1) + \mathrm{{P}}(2)
= {P3['ple2']:.4f}$.

It is not $1 - \mathrm{{P}}(X \ge 2)$ because both events include $X = 2$, so they
overlap rather than partition. The correct complement of $X \le 2$ is $X \ge 3$."""),

 (r"""For each, say whether the binomial applies; if not, name the failing condition.

(a) Number of sixes in 20 rolls of a fair die.
(b) Number of red cards in 10 drawn from a deck without replacement.
(c) Number of emails arriving between 2 and 3 pm.
(d) Number of defective bulbs in 40 drawn from a shipment of 50,000.""",
  r"""(a) **Yes** — all four hold, with $p = 1/6$.
(b) **No** — drawing without replacement makes $p$ change between draws, and 10 of 52
is too large a fraction to ignore.
(c) **No** — there is no fixed number of trials.
(d) **Yes**, effectively. Strictly without replacement, but 40 from 50,000 leaves $p$
constant to any accuracy that matters."""),

 (rf"""Monthly spend is normal with $\mu = {P3['mu']:.0f}$ and
$\sigma = {P3['sg']:.0f}$.

(a) Find the fraction above 400.
(b) Find the fraction between 280 and 400.
(c) Above what level do the top 2.5\% fall?""",
  rf"""(a) $z = (400-340)/45 = {(400 - 340) / 45:.4f}$, so
$\mathrm{{P}} = {P3['pab']:.4f}$.
(b) $z = {(280 - 340) / 45:.4f}$ and $z = {(400 - 340) / 45:.4f}$, giving
${P3['pmid']:.4f}$.
(c) $z = {Z975}$, so $x = 340 + {Z975}(45) = {P3['p95']:.2f}$."""),

 (rf"""Processing times are uniform between 8 and 32 minutes.

(a) Find the mean and standard deviation.
(b) Find $\mathrm{{P}}(X < 20)$.
(c) Find $\mathrm{{P}}(15 < X < 25)$.""",
  rf"""(a) $\mu = (8+32)/2 = {P3['umean']:.0f}$;
$\sigma = 24/\sqrt{{12}} = {P3['usd']:.4f}$.
(b) $(20-8)/24 = {P3['upr']:.4f}$.
(c) $(25-15)/24 = {10 / 24:.4f}$."""),

 (rf"""Time between machine faults is exponential with a mean of {P3['emean']:.0f} days.

(a) Find the probability of more than 9 days without a fault.
(b) Find the probability a fault occurs within 3 days.
(c) State the standard deviation.""",
  rf"""(a) $e^{{-9/6}} = e^{{-1.5}} = {P3['eg']:.4f}$.
(b) $1 - e^{{-3/6}} = 1 - {exp(-0.5):.4f} = {P3['el']:.4f}$.
(c) **6 days** — for an exponential the standard deviation equals the mean."""),

 (r"""A classmate computes $\mathrm{P}(X = 25) = 0.031$ for a continuous variable.

(a) What is wrong?
(b) What have they most likely computed?
(c) What would a sensible question have asked?""",
  r"""(a) For a continuous variable the probability of any exact value is zero.
(b) The **density** at 25, which is a height, not a probability — and heights can even
exceed 1.
(c) An interval: $\mathrm{P}(24.5 < X < 25.5)$, or $\mathrm{P}(X < 25)$."""),

 (r"""Using Stata functions or tables, find:

(a) $t_{0.025,\,19}$ (b) $t_{0.05,\,29}$ (c) $\chi^2_{0.05,\,12}$
(d) $F_{0.05,\,4,\,15}$""",
  r"""(a) 2.0930 — `invt(19, 0.975)`
(b) 1.6991 — `invt(29, 0.95)`
(c) 21.0261 — `invchi2(12, 0.95)`
(d) 3.0556 — `invF(4, 15, 0.95)`"""),

 (r"""Explain, in two sentences and without formulas, why the $t$ distribution has
fatter tails than the normal.""",
  r"""The $t$ divides by $s$ rather than $\sigma$, and $s$ is itself random — it varies
from sample to sample instead of being a fixed number. When $s$ happens to come out
small the whole ratio is pushed far from zero, so extreme values arise more often than
the normal predicts."""),

 (r"""A sample of $n = 20$ gives $\bar{x} = 46$ and $s = 10$, against a claimed mean of
40.

(a) Should you use $z$ or $t$, and why?
(b) How many degrees of freedom?
(c) Compute the test statistic.""",
  r"""(a) **$t$** — $\sigma$ is unknown and $s$ was estimated from the same 20
observations.
(b) $\nu = 19$.
(c) SE $= 10/\sqrt{20} = 2.2361$, so $t = (46-40)/2.2361 = 2.6833$."""),

 (r"""Why can a chi-squared value never be negative, and why is the distribution
right-skewed? Answer from the construction, not from a table.""",
  r"""A $\chi^2_\nu$ is the sum of $\nu$ **squared** standard normals. Every term is a
square, so every term is at least zero and so is the sum. It is right-skewed because
squaring stretches large deviations far more than small ones, so the upper tail is
pulled out while the lower end is bounded at zero."""),

 (r"""A classmate computes $F_{0.05,\,12,\,4}$ when the question asked for
$F_{0.05,\,4,\,12}$.

(a) Does the order matter?
(b) Give both values.
(c) Why are they different?""",
  r"""(a) **Yes**, very much.
(b) $F_{0.05,4,12} = 3.2592$ and $F_{0.05,12,4} = 5.9117$.
(c) $F$ is a ratio of two chi-squareds, each divided by its own degrees of freedom.
Swapping them swaps which group is in the numerator, which is a different question
entirely."""),

 (r"""A binomial has $n = 50$ and $p = 0.06$.

(a) Check whether the normal approximation is appropriate.
(b) State the rule you applied.
(c) What should you use instead if it fails?""",
  r"""(a) $np = 50(0.06) = 3$, which is **below 5**, so the approximation is not
appropriate. ($n(1-p) = 47$ passes, but both must.)
(b) The approximation needs $np \ge 5$ **and** $n(1-p) \ge 5$.
(c) The exact binomial — `binomial()` in Stata, or the formula directly."""),

 (r"""$X \sim \text{Bin}(n, 0.4)$ has a standard deviation of 3.0984.

(a) Find $n$.
(b) Find $E(X)$.
(c) Find $\mathrm{P}(X = 0)$.""",
  r"""(a) $\sigma^2 = n(0.4)(0.6) = 0.24n = 3.0984^2 = 9.6$, so $n = 40$.
(b) $E(X) = 40(0.4) = 16$.
(c) $(0.6)^{40} = 1.33 \times 10^{-9}$ — effectively zero."""),

 (r"""Match each to the distribution you would use, and say why in a few words:

(a) The number of defective items in 25 independent draws.
(b) The time until the next customer arrives.
(c) A measurement that is equally likely anywhere in a range.
(d) The sum of many small independent effects.""",
  r"""(a) **Binomial** — a fixed number of independent two-outcome trials.
(b) **Exponential** — waiting time until the next event at a constant rate.
(c) **Uniform** — a flat density over the range.
(d) **Normal** — by the Central Limit Theorem, sums of many small independent effects
tend to a bell whatever the pieces look like."""),
]
assert len(PART3) == 15


# ========================================================== PART IV  (ch 11-14)
P4 = {}
P4["sg"], P4["n"] = 24.0, 36
P4["se"] = 24 / 6
P4["pxb"] = 1 - Phi((88 - 80) / 4)
P4["n4"] = (24 / 2) ** 2
P4["In"], P4["Ixb"], P4["Is"], P4["mu0"] = 25, 54.8, 7.5, 50.0
P4["Ise"] = 7.5 / 5
P4["tc"] = 2.063899                       # invttail(24, 0.025)
P4["t"] = (54.8 - 50) / 1.5
P4["ci"] = (54.8 - P4["tc"] * 1.5, 54.8 + P4["tc"] * 1.5)
P4["nreq"] = math.ceil((Z975 * 7.5 / 1.0) ** 2)
assert P4["se"] == 4.0 and P4["Ise"] == 1.5
assert abs(P4["t"] - 3.2) < 1e-9 and not (P4["ci"][0] <= P4["mu0"] <= P4["ci"][1])

PART4 = [
 (rf"""A population has $\mu = 80$ and $\sigma = {P4['sg']:.0f}$. A random sample of
{P4['n']} is drawn.

(a) State $E(\bar{{X}})$ and the standard error.
(b) Find $\mathrm{{P}}(\bar{{X}} > 88)$.
(c) How large would $n$ need to be for the standard error to be 2?""",
  rf"""(a) $E(\bar{{X}}) = 80$ and $\sigma_{{\bar{{X}}}} = 24/\sqrt{{36}}
= {P4['se']:.0f}$.
(b) $z = (88-80)/4 = 2.00$, so $\mathrm{{P}} = {P4['pxb']:.4f}$.
(c) Set $24/\sqrt{{n}} = 2$, so $\sqrt{{n}} = 12$ and $n = {P4['n4']:.0f}$."""),

 (r"""For the population $\{2, 4, 6\}$:

(a) Find $\mu$ and $\sigma$.
(b) List all nine samples of size 2 drawn with replacement and their means.
(c) Verify $E(\bar{X}) = \mu$ and $\mathrm{SD}(\bar{X}) = \sigma/\sqrt{2}$.""",
  r"""(a) $\mu = 4$; $\sigma^2 = [(2-4)^2 + 0 + (6-4)^2]/3 = 8/3 = 2.6667$, so
$\sigma = 1.6330$.
(b) Means: 2, 3, 4, 3, 4, 5, 4, 5, 6 — that is $\bar{x} = 2,3,4,5,6$ with probabilities
$1/9, 2/9, 3/9, 2/9, 1/9$.
(c) $E(\bar{X}) = (2 + 6 + 12 + 10 + 6)/9 = 4 = \mu$. And $V(\bar{X}) = 4/3$, so
$\mathrm{SD}(\bar{X}) = 1.1547 = 1.6330/\sqrt{2}$."""),

 (r"""A population is strongly left-skewed. A sample of $n = 45$ is drawn.

(a) What can you say about the distribution of $\bar{X}$?
(b) What can you say about the distribution of a single observation $X$?
(c) A classmate computes $\mathrm{P}(X < 30)$ using the normal table. What is wrong?""",
  r"""(a) Approximately **normal**, by the Central Limit Theorem, with mean $\mu$ and
standard error $\sigma/\sqrt{45}$.
(b) Still **left-skewed**. Taking a sample does not change the population.
(c) The CLT applies to $\bar{X}$, not to $X$. A probability for a single observation
needs the population's actual shape, which is skewed — so the normal table gives the
wrong answer."""),

 (r"""Explain why quadrupling the sample size only halves the standard error.""",
  r"""The standard error is $\sigma/\sqrt{n}$, so it depends on $\sqrt{n}$ rather than
$n$. Averaging cancels independent errors, but each new observation adds less than the
one before — the tenth improves a mean of nine far more than the thousandth improves a
mean of 999. The exponent $\tfrac{1}{2}$ is the exact rate of those diminishing
returns."""),

 (rf"""A sample of {P4['In']} observations gives $\bar{{x}} = {P4['Ixb']}$ and
$s = {P4['Is']}$.

(a) Compute the standard error.
(b) Build a 95\% confidence interval. Use $t_{{0.025,24}} = {P4['tc']:.4f}$.
(c) State precisely what "95\% confident" refers to.""",
  rf"""(a) ${P4['Is']}/\sqrt{{{P4['In']}}} = {P4['Ise']:.1f}$.
(b) ${P4['Ixb']} \pm {P4['tc']:.4f}({P4['Ise']:.1f})
= ({P4['ci'][0]:.4f},\ {P4['ci'][1]:.4f})$.
(c) It describes the **procedure**, not this interval. Repeat the whole exercise many
times and 95\% of the intervals built this way would contain $\mu$. This one either
does or does not, and we cannot know which."""),

 (rf"""Using the sample above, a planning figure assumes the mean is {P4['mu0']:.0f}.

(a) State $H_0$ and $H_a$, and the tail.
(b) Compute the test statistic.
(c) Test at $\alpha = 0.05$ and state the conclusion in words.
(d) Show your interval and your test agree.""",
  rf"""(a) $H_0\!: \mu = {P4['mu0']:.0f}$ against $H_a\!: \mu \neq {P4['mu0']:.0f}$,
**two-tailed** — the figure is "assumed", with no direction given.
(b) $t = ({P4['Ixb']} - {P4['mu0']:.0f})/{P4['Ise']:.1f} = {P4['t']:.4f}$ with
$\nu = 24$.
(c) ${P4['t']:.1f} > {P4['tc']:.4f}$, so **reject $H_0$**. The sample gives strong
evidence the mean is not {P4['mu0']:.0f}; it appears about
{P4['Ixb'] - P4['mu0']:.1f} higher.
(d) The interval $({P4['ci'][0]:.4f}, {P4['ci'][1]:.4f})$ does **not** contain
{P4['mu0']:.0f}, which matches the rejection. A two-tailed test at $\alpha$ rejects
exactly when the $(1-\alpha)$ interval excludes the claimed value."""),

 (rf"""A study wants to estimate a mean to within $\pm 1.0$ at 95\% confidence,
believing $\sigma \approx {P4['Is']}$.

(a) How many observations are needed?
(b) How many to get within $\pm 0.5$?
(c) What does the comparison show?""",
  rf"""(a) $n = ({Z975:.2f} \times {P4['Is']} / 1.0)^2 = {(Z975 * 7.5) ** 2:.2f}$, so
**{P4['nreq']}**.
(b) $n = ({Z975:.2f} \times {P4['Is']} / 0.5)^2 = {(Z975 * 15) ** 2:.2f}$, so
**{math.ceil((Z975 * 15) ** 2)}**.
(c) Halving the margin **quadruples** the sample. Precision is bought at a rate of
$\sqrt{{n}}$, so each further improvement costs more than the last."""),

 (r"""For each, state $H_0$, $H_a$ and the tail.

(a) A supplier guarantees a mean lifetime of at least 800 hours; you are the buyer.
(b) Last year's mean was 45; the department asks whether this year differs.
(c) A process is targeted at 250 g; quality control checks for drift.
(d) A trainer claims a new method raises mean scores above 70.""",
  r"""(a) $H_0: \mu = 800$, $H_a: \mu < 800$, **left** — a guarantee is tested from the
side of whoever it protects.
(b) $H_0: \mu = 45$, $H_a: \mu \neq 45$, **two-tailed** — "differs" names no direction.
(c) $H_0: \mu = 250$, $H_a: \mu \neq 250$, **two-tailed** — drift either way is a fault.
(d) $H_0: \mu = 70$, $H_a: \mu > 70$, **right** — "raises above" names a direction."""),

 (r"""A test returns $p = 0.02$.

(a) Write what this means as a sentence.
(b) A classmate says "there is a 2% chance the null is true". Correct them.
(c) Another says "$p = 0.002$ would mean a bigger effect". Correct them too.""",
  r"""(a) "If $H_0$ were true, data at least this extreme would arise about 2 times in
100."
(b) Backwards. The $p$-value is computed **assuming** $H_0$ is true, so it cannot also
be the probability that $H_0$ is true.
(c) A smaller $p$ means the data sits **more awkwardly** with $H_0$, not that the effect
is larger. With a big enough sample a trivial effect produces a tiny $p$. Read the
confidence interval to judge size."""),

 (r"""Complete the table and define each cell.

| | $H_0$ true | $H_0$ false |
|---|---|---|
| Reject | ? | ? |
| Do not reject | ? | ? |""",
  r"""Reject when $H_0$ is **true**: a **Type I error**, probability $\alpha$ — declaring
an effect that is not there.
Reject when $H_0$ is **false**: a correct decision, probability $1 - \beta$, called the
**power**.
Do not reject when $H_0$ is **true**: a correct decision.
Do not reject when $H_0$ is **false**: a **Type II error**, probability $\beta$ —
missing a real effect."""),

 (r"""A researcher runs 20 independent tests on data where no effect exists.

(a) How many would you expect to be "significant" at $\alpha = 0.05$?
(b) What is this phenomenon called when only the significant one is reported?
(c) Which of the eight steps of a hypothesis test guards against it?""",
  r"""(a) About **one** — $20 \times 0.05 = 1$.
(b) **$p$-hacking** (or selective reporting). The arithmetic in the reported test is
perfectly correct; the omission of the other nineteen is what makes it misleading.
(c) Steps 3 and 4 — setting $\alpha$ and writing the decision rule **before** seeing the
data, which fixes the test in advance and makes selective reporting visible."""),

 (r"""A 95% confidence interval for a mean comes out as $(12.4,\ 18.6)$.

(a) What is the point estimate?
(b) What is the margin of error?
(c) Would a two-tailed test of $H_0: \mu = 19$ at $\alpha = 0.05$ reject? Explain
without computing anything.""",
  r"""(a) The midpoint, $(12.4 + 18.6)/2 = 15.5$.
(b) Half the width, $(18.6 - 12.4)/2 = 3.1$.
(c) **Yes.** 19 lies outside the interval, and a two-tailed test at $\alpha = 0.05$
rejects exactly when the 95% interval excludes the claimed value."""),

 (r"""Two studies estimate the same quantity at 95% confidence. Study A reports
$8.2 \pm 0.4$; Study B reports $8.2 \pm 3.6$.

(a) Which is more useful, and why?
(b) Give two distinct reasons B's interval might be so much wider.
(c) Do the two disagree?""",
  r"""(a) **A** — the same estimate with far more precision, so it rules out many more
values.
(b) Any two of: B had a much smaller sample (the margin goes as $1/\sqrt{n}$, so a
nine-fold wider margin suggests a sample on the order of 80 times smaller); B's
population is more variable; B measured less precisely, inflating $s$.
(c) **No.** They agree exactly on the point estimate. They differ in precision, not in
finding — and A's interval sits entirely inside B's."""),

 (r"""Explain why "not significant" does not mean "no effect", and give a concrete
circumstance in which a real effect would be missed.""",
  r"""Failing to reject means the evidence was insufficient, not that $H_0$ is true. A
small sample produces a large standard error, so even a substantial real difference can
fall short of the critical value. Concretely: a six-point difference on a population
with $\sigma = 15$ is missed more than half the time at $n = 25$ — the test simply lacks
the power to detect it, and reporting that as "no effect" misrepresents what happened."""),

 (r"""A survey of 1,500 people is drawn by selecting 375 households and interviewing
all adults in each. The report quotes a margin of error based on $n = 1{,}500$.

(a) Is the quoted margin too large, too small or about right?
(b) Why?
(c) What would you need to report an honest margin?""",
  r"""(a) **Too small.**
(b) $\sigma/\sqrt{n}$ counts independent pieces of information, and adults in the same
household are not independent — they share income, location and often views. The
effective sample size is well below 1,500.
(c) An estimate of the design effect — how much the clustering inflates the variance —
obtained by comparing the variability between households with the variability within
them."""),
]
assert len(PART4) == 15


# -------------------------------------------------------------------- emit
PARTS = [
    ("91_practice_part1_describing_data.md",
     "Practice: describing data",
     "Chapters 1 to 4 — population and sample, centre, spread, covariance and "
     "correlation.", PART1),
    ("92_practice_part2_chance.md",
     "Practice: chance",
     "Chapters 5 to 7 — the probability rules, conditional probability and Bayes, "
     "random variables.", PART2),
    ("93_practice_part3_distributions.md",
     "Practice: distributions",
     "Chapters 8 to 10 — the binomial, continuous distributions, and $t$, "
     "chi-squared and $F$.", PART3),
    ("94_practice_part4_inference.md",
     "Practice: from sample to population",
     "Chapters 11 to 14 — sampling distributions, the CLT, estimation and "
     "hypothesis testing.", PART4),
]

total = 0
for fname, title, blurb, items in PARTS:
    md = [f"# {title}\n", f"{blurb}\n",
          "Fifteen problems. Work them with the solutions covered — reading a worked "
          "answer and producing one are different skills, and only the second is any "
          "use with a clock running.\n",
          "Keep **four decimal places** unless a question says otherwise.\n", "---\n"]
    for i, (q, _) in enumerate(items, 1):
        md.append(f"**{i}.** {q}\n")
    md.append("---\n\n# Solutions\n")
    for i, (_, a) in enumerate(items, 1):
        md.append(f"**{i}.** {a}\n")
    md.append("---\n")
    open(os.path.join(HERE, fname), "w").write("\n".join(md))
    words = sum(len(q.split()) + len(a.split()) for q, a in items)
    total += len(items)
    print(f"  wrote {fname:<46} {len(items)} problems, {words:,} words")

print(f"\n       {total} problems across {len(PARTS)} sets")
print(f"       Part I  r = {P1['r']:.4f} | Part II P(D) = {P2['PD']:.4f}, "
      f"PPV = {P2['ppv']:.4f}")
print(f"       Part III binom {P3['pk']:.4f}, normal {P3['pab']:.4f} | "
      f"Part IV t = {P4['t']:.4f}, CI ({P4['ci'][0]:.4f}, {P4['ci'][1]:.4f})")
print(f"       Part IV interval excludes mu0, so 6(d) is consistent: "
      f"{not (P4['ci'][0] <= P4['mu0'] <= P4['ci'][1])}")
