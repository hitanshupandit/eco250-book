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

<!-- more-practice:start -->

## More practice

Eight more. Watch the degrees of freedom in questions 2 and 3 — they are the single
commonest slip in this chapter, and a correct $\chi^2$ compared against the wrong row
of the table scores nothing.

1. In a survey of 300 customers, 108 say they would recommend the product.
   (a) Find $\hat{p}$ and its standard error.
   (b) Build a 95% confidence interval.
   (c) Check the condition for the approximation.
   (d) Why is the critical value $z$ and not $t$, when the standard error was
   estimated from the data?

2. A firm expects its four regional offices to handle equal shares of enquiries. Out
   of 200 enquiries the counts are 42, 55, 61 and 42.
   (a) State the hypotheses and the expected counts.
   (b) Compute $\chi^2$ and state the degrees of freedom.
   (c) Test at $\alpha = 0.05$, given $\chi^2_{0.05,3} = 7.8147$.
   (d) Find the p-value.

3. Two hundred and fifty applicants are classified by outcome and by which of three
   channels they applied through:

   | | A | B | C | Total |
   |---|---|---|---|---|
   | **Accepted** | 30 | 45 | 25 | 100 |
   | **Rejected** | 50 | 35 | 65 | 150 |
   | **Total** | 80 | 80 | 90 | 250 |

   (a) Compute all six expected counts.
   (b) Compute $\chi^2$ and state the degrees of freedom.
   (c) Test at $\alpha = 0.05$, given $\chi^2_{0.05,2} = 5.9915$.
   (d) State the conclusion in words.

4. State the degrees of freedom for a test of independence on a table that is
   (a) $2 \times 2$, (b) $4 \times 5$, (c) $2 \times 6$, (d) $3 \times 3$. Then say why
   a $2 \times 2$ table has 1 and not 3.

5. A researcher's $2 \times 2$ table has one cell with an observed count of 2 and an
   expected count of 8.
   (a) Is the condition satisfied?
   (b) Which of the two numbers does the condition apply to, and why does that make
   sense?

6. A student converts a table of counts into row percentages, then feeds the
   percentages into $\chi^2 = \sum (O-E)^2/E$.
   (a) What goes wrong?
   (b) Why does the statistic depend on the counts rather than only the proportions?

7. Explain why the chi-squared test is always upper-tailed, and what an unusually
   *small* $\chi^2$ would suggest.

8. A test of independence between an applicant's channel and their outcome rejects
   $H_0$. A manager concludes "channel C is causing rejections."
   (a) What does the test establish?
   (b) Give two explanations consistent with the result that are not causal.

### Answers to the extra problems

1. (a) $\hat{p} = 108/300 = 0.3600$ and
   SE $= \sqrt{0.36(0.64)/300} = \sqrt{0.000768} = 0.0277$.
   (b) $0.36 \pm 1.96(0.0277) = 0.36 \pm 0.0543 = (0.3057,\ 0.4143)$.
   (c) $n\hat{p} = 108$ and $n(1-\hat{p}) = 192$, both far above 5. Valid.
   (d) Because the $t$ distribution arises from a very specific construction — a
   standard normal over the square root of an independent scaled chi-squared, which is
   what you get when $s$ and $\bar{x}$ are computed from normal data. For a proportion
   there is no separate $s$: the standard error is a function of $\hat{p}$ itself, so
   the ratio is not a $t$ variable. "Estimated denominator means $t$" is a useful
   habit and not a rule, and this is the counterexample.

2. (a) $H_0$: the four offices handle equal shares, so each expected count is
   $200/4 = 50$. $H_a$: the shares are not all equal.
   (b) $\chi^2 = \dfrac{64 + 25 + 121 + 64}{50} = \dfrac{274}{50} = 5.4800$ with
   $\nu = k - 1 = 3$.
   (c) $5.4800 < 7.8147$, so **do not reject** — the observed split is consistent with
   equal shares.
   (d) $p = 0.1398$.

3. (a) Each is row total times column total over 250:
   Accepted — $32.0000$, $32.0000$, $36.0000$; Rejected — $48.0000$, $48.0000$,
   $54.0000$. They reproduce the margins, which is the check.
   (b) $\chi^2 = \dfrac{4}{32} + \dfrac{169}{32} + \dfrac{121}{36} + \dfrac{4}{48}
   + \dfrac{169}{48} + \dfrac{121}{54} = 14.6128$ with
   $\nu = (2-1)(3-1) = 2$.
   (c) $14.6128 > 5.9915$, so **reject $H_0$** ($p = 0.0007$).
   (d) Outcome and channel are not independent. Channel B's applicants are accepted far
   more often than its share of applications would suggest — 45 accepted against an
   expected 32 — while channel C's are accepted far less, 25 against an expected 36.

4. (a) 1. (b) 12. (c) 5. (d) 4. A $2 \times 2$ table has 1 rather than 3 because the
   row and column totals are fixed by the data itself, not supplied from outside: once
   you know the margins and any **one** cell, the other three are forced by
   subtraction. Only one number in the table is free to vary, so there is one degree of
   freedom. Counting four cells and subtracting one is the wrong arithmetic and happens
   to give 3.

5. (a) **Yes.** The condition is that every *expected* count be at least 5, and 8
   clears it.
   (b) It applies to the **expected** count. That makes sense because $E$ is the
   denominator in each term of $\chi^2 = \sum (O-E)^2/E$ — a tiny expectation makes the
   term explode and destroys the chi-squared approximation, regardless of what was
   observed. A cell can observe zero and be perfectly well behaved provided enough was
   expected there.

6. (a) The test statistic changes, usually becoming far too small. Converting 60 out of
   100 into "60%" and 600 out of 1,000 into "60%" makes two completely different bodies
   of evidence look identical, and $\chi^2$ computed on percentages effectively asserts
   $n = 100$ for every row.
   (b) Because the strength of evidence depends on how much data there is, not only on
   the pattern. A 10-point gap in proportions from 40 observations is noise; the same
   gap from 4,000 is decisive. Proportions describe the pattern, counts carry the
   sample size, and $\chi^2$ needs both — which is exactly why it is built from counts.

7. The statistic is a sum of squared discrepancies, so it is zero when observation
   matches expectation exactly and grows as they diverge — in either direction, since
   the squaring removes the sign. Only *large* values are evidence against $H_0$, so
   all of $\alpha$ goes in the upper tail. An unusually **small** $\chi^2$ means the
   data fit the expectation more closely than chance would normally allow, which is not
   evidence for $H_0$ so much as grounds for suspecting the data were not generated the
   way they were described — the classic reason to be sceptical of results that are
   *too* good.

8. (a) Only **association**: the distribution of outcomes differs across channels by
   more than chance would explain. It identifies no cause and no direction.
   (b) (i) **Selection** — stronger applicants may choose channel B, so the channel is
   marking a difference in applicants rather than creating one. (ii) **A confounder** —
   channels may differ in what roles they advertise, in which case both channel and
   outcome are driven by the type of position. A third: the channels may be used at
   different times of year, with different acceptance rates for unrelated reasons.

<!-- more-practice:end -->

---
