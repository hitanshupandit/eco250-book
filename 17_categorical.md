# Chapter 17 — Categorical data: proportions and chi-squared

> **The question:** everything so far has tested a mean. What if the data is
> categories rather than numbers?

## Counting instead of measuring

Up to now the data has been quantitative — wages, times, weights — and the parameter
of interest has been $\mu$. This chapter handles data that comes as **counts in
categories**: how many customers were satisfied, how many items came from each
supplier, whether approval depends on borrower type.

Two tools, and the second does most of the work.

## A proportion is a mean in disguise

Code each observation as 1 for a success and 0 otherwise. Then the sample proportion

$$\hat{p} = \frac{\text{number of successes}}{n}$$

is just the **mean of those 0s and 1s**. Which means everything from Chapters 11 to 14
carries over unchanged: $\hat{p}$ is a statistic, it has a sampling distribution, and
the CLT makes that distribution approximately normal.

Its standard error is

$$\text{SE}(\hat{p}) = \sqrt{\frac{p(1-p)}{n}}$$

and the confidence interval has the usual shape:

$$\hat{p} \pm z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

### The $z$, not $t$, surprise

Look carefully: the standard error was **estimated from the data** — we substituted
$\hat{p}$ for the unknown $p$ — and yet the critical value is $z$.

This is the counterexample promised in Chapter 10. "Estimated denominator means $t$"
is *not* the rule. The $t$ distribution arises specifically because $s$ and $\bar{x}$
are independent and $s^2$ has a chi-squared distribution — a situation that does not
arise here. For proportions, the normal approximation is used directly.

The approximation needs $n\hat{p} \geq 5$ and $n(1-\hat{p}) \geq 5$, the same
condition as the binomial in Chapter 8, for the same reason.

### Worked example

In a sample of 400 customers, 168 report being satisfied, so $\hat{p} = 0.42$.

$$\text{SE} = \sqrt{\frac{0.42(0.58)}{400}} = 0.0247$$

$$0.42 \pm 1.96(0.0247) = (0.3716,\ 0.4684)$$

Check the condition: $400(0.42) = 168$ and $400(0.58) = 232$, both comfortably above
5. The interval is valid, and we are 95% confident the population satisfaction rate
lies between about **37% and 47%**.

## Chi-squared: comparing counts with expectations

The second tool handles tables of counts, and it is the same statistic in both of its
uses:

$$\chi^2 = \sum \frac{(O - E)^2}{E}$$

where $O$ is what you **observed** and $E$ is what you would **expect** if $H_0$ were
true.

Read the formula. Each term is a squared discrepancy, scaled by how big a discrepancy
you should expect in that cell. Scaling matters: being 10 off when you expected 20 is
serious, while being 10 off when you expected 1,000 is nothing.

Chapter 10 said chi-squared is built for exactly this — add up squared errors — and
this is the payoff. The test is always **upper-tailed**: only large discrepancies are
evidence against $H_0$.

## Use one: goodness of fit

Does one categorical variable follow a claimed distribution?

A shop expects its three branches to take 30%, 40% and 30% of orders. Out of 100
orders it observes 28, 42 and 30.

Expected counts: $100(0.30) = 30$, $100(0.40) = 40$, $100(0.30) = 30$.

$$\chi^2 = \frac{(28-30)^2}{30} + \frac{(42-40)^2}{40} + \frac{(30-30)^2}{30}
= 0.1333 + 0.1000 + 0 = 0.2333$$

Degrees of freedom are $k - 1 = 2$. The critical value is $\chi^2_{0.05,2} = 5.9915$.

Since $0.2333 < 5.9915$, **do not reject** — $p = 0.8899$. The observed split is
entirely consistent with the claimed one.

## Use two: independence

Does one categorical variable depend on another? This is Chapter 5's independence
question, now with a formal test behind it.

A firm classifies 200 applications by outcome and by whether the applicant was
referred:

| | Referred | Not referred | Total |
|---|---|---|---|
| **Accepted** | 60 | 40 | 100 |
| **Rejected** | 30 | 70 | 100 |
| **Total** | 90 | 110 | 200 |

Under independence, Chapter 5 says $\mathrm{P}(A \cap B) = \mathrm{P}(A)\mathrm{P}(B)$.
Turning that into an expected count gives the rule you actually use:

$$E = \frac{\text{row total} \times \text{column total}}{\text{grand total}}$$

So the top-left cell expects $100 \times 90 / 200 = 45$. All four expected counts are
45, 55, 45, 55.

$$\chi^2 = \frac{(60-45)^2}{45} + \frac{(40-55)^2}{55} + \frac{(30-45)^2}{45}
+ \frac{(70-55)^2}{55} = 18.1818$$

Degrees of freedom for a table are $(r-1)(c-1) = 1 \times 1 = 1$. The critical value
is $\chi^2_{0.05,1} = 3.8415$.

Since $18.1818 > 3.8415$, **reject** — $p = 0.00002$. Acceptance and referral are not
independent: referred applicants are accepted far more often.

### The degrees of freedom

| Test | df |
|---|---|
| Goodness of fit, $k$ categories | $k - 1$ |
| Independence, $r \times c$ table | $(r-1)(c-1)$ |

Both follow the same logic as Chapter 3's: once the margins are fixed, only that many
cells are free to vary.

**The condition:** every expected count should be at least 5. Note *expected*, not
observed — a cell can observe zero and still be fine if its expectation is large
enough.

## In Stata

*The snippets below assume the header and preamble from
[Chapter 1](01_what_statistics_is_for.md).*

```stata
use "DATA/cps_small.dta", clear

* confidence interval for a proportion
cii proportions 400 168, wald

* a test of independence
tabulate female black, chi2 expected
```

Use the `wald` option on `cii`: without it Stata reports an exact binomial interval,
which is a better interval but is **not** the formula above, so your hand calculation
will not match.

The `expected` option on `tabulate` prints the expected counts alongside the observed
ones, which is how you check the all-expectations-above-5 condition.

## In Python

```python
import numpy as np
from scipy import stats

# goodness of fit
stats.chisquare([28, 42, 30], f_exp=[30, 40, 30])     # 0.2333, p = 0.8899

# independence
table = np.array([[60, 40], [30, 70]])
chi2, p, dof, expected = stats.chi2_contingency(table, correction=False)
print(chi2, dof, p)      # 18.1818  1  0.00002
print(expected)          # [[45. 55.] [45. 55.]]
```

`chi2_contingency` returns the expected counts as its fourth value, so you can check
the condition without computing them by hand. Set `correction=False` to match the
formula above — with `True` it applies a continuity correction for $2\times2$ tables
and your arithmetic will differ.

## What goes wrong

**Using $t$ for a proportion.** It is $z$, despite the estimated standard error. This
is the exception that disproves the rule people invent.

**Checking observed counts instead of expected.** The condition is on $E$.

**Wrong degrees of freedom.** $k-1$ for goodness of fit; $(r-1)(c-1)$ for a table. For
a $2\times2$ table that is 1, not 3.

**Using percentages in the formula.** $\chi^2$ needs **counts**. Feeding it
percentages changes the answer entirely.

**A two-tailed critical value.** The chi-squared test is always upper-tailed.

**Concluding causation from independence.** Rejecting independence says the two
variables are associated, not that one causes the other — Chapter 4's warning, in a
new costume.

## Exercises

1. In a sample of 250, 95 prefer brand A.
   (a) Find $\hat{p}$ and its standard error.
   (b) Build a 95% confidence interval.
   (c) Check the condition for the approximation.

2. A die is rolled 120 times with these counts: 18, 22, 19, 21, 20, 20.
   (a) What are the expected counts if the die is fair?
   (b) Compute $\chi^2$ and state the degrees of freedom.
   (c) Test at $\alpha = 0.05$, given $\chi^2_{0.05,5} = 11.0705$.

3. A $3 \times 4$ contingency table is tested for independence. How many degrees of
   freedom?

4. In a $2\times2$ table the row totals are 80 and 120, the column totals 100 and
   100, and the grand total 200. Find all four expected counts.

5. A researcher tests independence of two variables, rejects $H_0$, and writes "the
   first variable causes the second". What is wrong?

### Answers

1. (a) $\hat{p} = 95/250 = 0.38$;
   SE $= \sqrt{0.38(0.62)/250} = \sqrt{0.000942} = 0.0307$.
   (b) $0.38 \pm 1.96(0.0307) = (0.3198,\ 0.4402)$.
   (c) $250(0.38) = 95$ and $250(0.62) = 155$, both well above 5. Valid.

2. (a) $120/6 = 20$ for each face.
   (b) Squared deviations are $4, 4, 1, 1, 0, 0$, each divided by 20, giving
   $\chi^2 = 10/20 = 0.50$ with $\nu = 5$.
   (c) $0.50 < 11.0705$, so **do not reject** — no evidence the die is unfair.

3. $(3-1)(4-1) = 6$.

4. Row 1: $80(100)/200 = 40$ and $40$. Row 2: $120(100)/200 = 60$ and $60$. All four
   are 40, 40, 60, 60, and they reproduce the margins — a useful check.

5. The test establishes **association**, not causation. Either variable could drive
   the other, or a third could drive both. The chi-squared test says the two are not
   independent and is silent on why.

---
