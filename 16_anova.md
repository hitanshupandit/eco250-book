# Chapter 16 — Comparing several means: ANOVA

> **The question:** three groups, three averages. Why can you not just run three
> $t$ tests?

## Why not just do it three times

With three groups there are three pairwise comparisons: 1 vs 2, 1 vs 3, 2 vs 3. With
four groups there are six. The temptation is obvious and the problem is the one from
Chapter 14.

Each test at $\alpha = 0.05$ has a 5% chance of a false positive when nothing is
going on. Run three independent tests on groups that are genuinely identical and the
chance that **at least one** comes out significant is

$$1 - (0.95)^3 = 0.1426$$

Not 5% but **14%**. With six comparisons it is 26%. You have quietly abandoned the
error rate you claimed to be using — and this is just the twenty-tests simulation
from Chapter 14, in a form that looks respectable.

**Analysis of variance** asks one question instead, at one $\alpha$:

$$H_0: \mu_1 = \mu_2 = \mu_3 \qquad\text{against}\qquad
H_a: \text{at least one mean differs}$$

Note what $H_a$ does *not* say. It does not name which. A rejection tells you the
means are not all equal and nothing more.

## The idea: two kinds of variation

Here is the move that gives the method its name. Take all the observations together
and ask where their variation comes from. There are exactly two sources.

**Between groups.** The group means differ from each other. If the treatments really
do something, this is large.

**Within groups.** Observations differ from their own group's mean. This is noise —
it would be there even if every treatment were identical.

The test compares them:

$$F = \frac{\text{variation between groups}}{\text{variation within groups}}
= \frac{\text{signal}}{\text{noise}}$$

Which is the same signal-to-noise ratio as every test statistic in this course. If
$H_0$ is true, the two estimate the same thing and $F$ sits near 1. If the group
means genuinely differ, the numerator inflates and $F$ grows.

## The arithmetic

With $k$ groups and $N$ observations in total:

$$\text{SSB} = \sum_j n_j(\bar{x}_j - \bar{x})^2
\qquad
\text{SSW} = \sum_j \sum_i (x_{ij} - \bar{x}_j)^2$$

where $\bar{x}$ is the **grand mean** over everything. These add to the total:
$\text{SST} = \text{SSB} + \text{SSW}$, which is a useful arithmetic check.

Divide each by its degrees of freedom to get a **mean square**:

$$\text{MSB} = \frac{\text{SSB}}{k-1}
\qquad
\text{MSW} = \frac{\text{SSW}}{N-k}
\qquad
F = \frac{\text{MSB}}{\text{MSW}}$$

with $\nu_1 = k-1$ and $\nu_2 = N-k$. **Numerator first**, as Chapter 10 insisted.

The test is always **one-tailed, upper**. Only a large $F$ is evidence against $H_0$;
a small $F$ means the groups look alike, which is what $H_0$ claims.

## Worked example

Three production lines, five days each:

| Line A | 12 | 15 | 14 | 16 | 13 |
|---|---|---|---|---|---|
| **Line B** | 18 | 20 | 17 | 19 | 21 |
| **Line C** | 14 | 13 | 16 | 15 | 12 |

Group means are **14, 19, 14**, and the grand mean is $235/15 = 15.67$.

**Between:**

$$\text{SSB} = 5(14-15.67)^2 + 5(19-15.67)^2 + 5(14-15.67)^2 = 83.3333$$

**Within:** each group's own squared deviations — 10, 10 and 10 — so
$\text{SSW} = 30$.

Check: $83.3333 + 30 = 113.3333$, which is SST computed directly.

$$\text{MSB} = \frac{83.3333}{2} = 41.6667
\qquad
\text{MSW} = \frac{30}{12} = 2.5000$$

$$F = \frac{41.6667}{2.5000} = 16.6667 \qquad \nu_1 = 2,\ \nu_2 = 12$$

The critical value is $F_{0.05,2,12} = 3.8853$. Since $16.6667 > 3.8853$, **reject
$H_0$** — $p = 0.0003$. The three lines do not all have the same mean output.

**And then stop.** The $F$ test says "not all equal". It does not say Line B is the
odd one out — even though the means make that obvious here, the test itself has not
established it. Establishing *which* needs a follow-up procedure designed to control
the error rate across multiple comparisons, which is beyond this course.

## The ANOVA table

Results are conventionally laid out like this, and you should be able to read one or
fill in its gaps:

| Source | SS | df | MS | $F$ |
|---|---|---|---|---|
| Between groups | 83.3333 | 2 | 41.6667 | 16.6667 |
| Within groups | 30.0000 | 12 | 2.5000 | |
| **Total** | **113.3333** | **14** | | |

Every number in it follows from the ones around it: the df column sums, the SS column
sums, each MS is its SS over its df, and $F$ is the ratio of the two MS values. A
common exam question gives you three entries and asks for the rest.

## The assumptions

ANOVA assumes the groups are **independent**, each population is roughly **normal**,
and the population **variances are equal**. The third is the one people forget, and
it is the reason MSW can be pooled across groups at all. As a rough field check, the
largest group standard deviation should be under about twice the smallest.

## In Stata

*The snippets below assume the header and preamble from
[Chapter 1](01_what_statistics_is_for.md).*

```stata
use "DATA/cps_small.dta", clear

oneway wage educ, tabulate
```

`oneway` prints the full ANOVA table — between, within, total, with the $F$ and its
$p$-value. The `tabulate` option adds each group's mean and standard deviation, which
is how you check the equal-variance assumption.

## In Python

```python
from scipy import stats

A = [12, 15, 14, 16, 13]
B = [18, 20, 17, 19, 21]
C = [14, 13, 16, 15, 12]

F, p = stats.f_oneway(A, B, C)
print(F, p)              # 16.6667  0.000344
```

To see the pieces rather than just the answer:

```python
import numpy as np
groups = [A, B, C]
allv = np.concatenate(groups)
gm = allv.mean()

SSB = sum(len(g)*(np.mean(g) - gm)**2 for g in groups)
SSW = sum(((np.array(g) - np.mean(g))**2).sum() for g in groups)

print(SSB, SSW, SSB + SSW)                    # 83.33  30.0  113.33
print((SSB/2) / (SSW/12))                     # 16.6667
```

## What goes wrong

**Running pairwise $t$ tests instead.** Three tests at 5% give a 14% false-positive
rate. That is the whole reason this method exists.

**Concluding which group differs.** The $F$ test does not say. It says "not all
equal".

**Reversing the degrees of freedom.** $\nu_1 = k-1$ on top, $\nu_2 = N-k$ below, and
$F_{2,12} \neq F_{12,2}$.

**Using a two-tailed critical value.** ANOVA is always upper-tailed.

**Ignoring unequal variances.** If one group is far more variable than the others,
pooling is not legitimate.

**Forgetting that SSB + SSW = SST.** It is a free check, and it catches most
arithmetic slips.

## Exercises

1. Four groups, 8 observations each. State $\nu_1$, $\nu_2$ and the total degrees of
   freedom.

2. Complete this ANOVA table.

   | Source | SS | df | MS | $F$ |
   |---|---|---|---|---|
   | Between | 48 | 3 | ? | ? |
   | Within | ? | 20 | 4 | |
   | Total | ? | ? | | |

3. Three teaching methods give means 70, 74 and 78 with 10 students each. SSW is 900.
   (a) Find the grand mean and SSB.
   (b) Find $F$.
   (c) Test at $\alpha = 0.05$, given $F_{0.05,2,27} = 3.354$.

4. Explain, in your own words, why running six pairwise tests at $\alpha = 0.05$ is
   not a 5% procedure.

5. An ANOVA gives $F = 0.42$. What do you conclude, and could a small $F$ ever be
   evidence against $H_0$?

### Answers

1. $k = 4$ and $N = 32$, so $\nu_1 = 3$, $\nu_2 = 28$, and the total is 31.

2. MSB $= 48/3 = 16$. SSW $= 4 \times 20 = 80$. $F = 16/4 = 4$. SST $= 48 + 80 = 128$
   on $3 + 20 = 23$ degrees of freedom.

3. (a) Grand mean $= (70+74+78)/3 = 74$. SSB $= 10(16) + 10(0) + 10(16) = 320$.
   (b) MSB $= 320/2 = 160$; MSW $= 900/27 = 33.33$; $F = 160/33.33 = 4.80$.
   (c) $4.80 > 3.354$, so **reject** — the three methods do not all have the same mean.

4. Each test carries its own 5% chance of a false positive. Across six tests those
   chances accumulate, so the probability that *at least one* is significant when all
   groups are identical rises to about 26%. The claimed 5% applies to a single
   comparison, not to the whole family of them.

5. **Do not reject.** An $F$ below 1 means the between-group variation is smaller than
   the within-group noise, which is exactly what $H_0$ predicts. A small $F$ is never
   evidence *against* $H_0$ — which is why the test is one-tailed.

---
