# Chapter 18 — Regression

> **The question:** correlation said the two variables move together. Can you put a
> line through them and predict?

## From describing to predicting

Chapter 4 measured whether $x$ and $y$ move together and how tightly. It stopped
there, deliberately — $r$ is symmetric, and it tells you nothing about which variable
to treat as the cause, or by how much $y$ changes when $x$ changes by one.

Regression answers both. It fits

$$\hat{y} = b_0 + b_1 x$$

where $b_1$ is the **slope** — how much $\hat{y}$ moves per one-unit increase in $x$
— and $b_0$ is the **intercept**, the fitted value when $x = 0$.

The asymmetry is the point. Regressing $y$ on $x$ is a different exercise from
regressing $x$ on $y$, while $r$ is the same either way.

## Choosing the line

Infinitely many lines pass through a cloud of points. The one we fit is the one that
makes the **residuals** as small as possible, where a residual is what the line
missed:

$$e_i = y_i - \hat{y}_i$$

Squaring them and adding gives a single number to minimise:

$$\text{SSE} = \sum (y_i - \hat{y}_i)^2$$

Hence **least squares**. Squaring does the same two jobs as in Chapter 3: it removes
signs so positive and negative misses cannot cancel, and it penalises a big miss more
than several small ones.

Minimising gives formulas you already have the ingredients for:

$$b_1 = \frac{s_{xy}}{s_x^2} \qquad\qquad b_0 = \bar{y} - b_1\bar{x}$$

The slope is the covariance from Chapter 4 divided by the variance of $x$. And the
intercept formula rearranges to $\bar{y} = b_0 + b_1\bar{x}$ — **the line always
passes through the point of means**, which is a free check on your arithmetic.

## How well does it fit?

Total variation in $y$ splits in two, exactly as ANOVA's did:

$$\underbrace{\sum(y_i - \bar{y})^2}_{\text{SST}}
= \underbrace{\sum(\hat{y}_i - \bar{y})^2}_{\text{SSR, explained}}
+ \underbrace{\sum(y_i - \hat{y}_i)^2}_{\text{SSE, left over}}$$

$$R^2 = \frac{\text{SSR}}{\text{SST}} = 1 - \frac{\text{SSE}}{\text{SST}}$$

**$R^2$ is the fraction of the variation in $y$ the line accounts for.** It runs from
0 to 1, and for a simple regression with one predictor it is exactly $r^2$ — so an
$r$ of $0.7$ means the line explains 49% of the variation, not 70%.

## Is the slope real?

$b_1$ is computed from a sample, so it is a statistic with a sampling distribution —
Chapter 11's idea once more. A different sample gives a different slope. So test it:

$$H_0: \beta_1 = 0 \qquad\text{against}\qquad H_a: \beta_1 \neq 0$$

$$t = \frac{b_1}{\text{SE}(b_1)} \qquad \nu = n - 2$$

$H_0$ says the slope is zero — that $x$ tells you nothing about $y$. Degrees of
freedom are $n - 2$ because two parameters were estimated from the data, $b_0$ and
$b_1$. Chapter 3's logic again: each estimate costs a degree of freedom.

## Worked example

Advertising spend $x$ (thousands) and sales $y$ (thousands of units):

| $x$ | 2 | 4 | 6 | 8 | 10 | 12 |
|---|---|---|---|---|---|---|
| $y$ | 14 | 18 | 23 | 25 | 31 | 34 |

**(a) Fit the line. (b) Interpret the slope. (c) Find $R^2$. (d) Test the slope.**

### Solution

$\bar{x} = 7$ and $\bar{y} = 24.1667$.

**(a)** From the deviation table, $s_{xy} = 28.2$ and $s_x^2 = 14$, so

$$b_1 = \frac{28.2}{14} = 2.0143
\qquad
b_0 = 24.1667 - 2.0143(7) = 10.0667$$

$$\hat{y} = 10.0667 + 2.0143x$$

**(b)** Each extra **thousand dollars** of advertising is associated with about
**2,014 more units** sold. Note "associated with" — the data is observational, and
Chapter 4's warning has not expired.

**(c)** SSE $= 2.8190$ and SST $= 286.8333$, so

$$R^2 = 1 - \frac{2.8190}{286.8333} = 0.9902$$

The line accounts for **99%** of the variation in sales. Equivalently $r = 0.9951$,
and $0.9951^2 = 0.9902$.

**(d)** SE$(b_1) = 0.1003$, so

$$t = \frac{2.0143}{0.1003} = 20.0747 \qquad \nu = 4$$

Against $t_{0.025,4} = 2.7764$ this is overwhelming — $p = 0.00004$. **Reject
$H_0$**: the slope is not zero.

## What the line does not license

Three limits, and each has cost somebody money.

**Extrapolation.** The data runs from $x = 2$ to $x = 12$. Predicting at $x = 50$
assumes the straight line continues far beyond anything observed, and nothing in the
data supports that. Advertising returns almost certainly flatten.

**Causation.** A significant slope establishes association. Spend may drive sales;
sales may fund spend; or a growing market may drive both — Chapter 4's three
explanations, unchanged.

**The intercept is often meaningless.** Here $b_0 = 10.07$ is the predicted sales at
zero advertising, which is an extrapolation to a point outside the data. Report it
because the line needs it; interpret it only if $x = 0$ is genuinely in range.

## Checking the assumptions

Least squares assumes the relationship is **linear**, the residuals have **constant
variance** and are **independent**, and for the $t$ test that they are roughly
**normal**.

The check is a picture, not a number: plot the residuals against $\hat{y}$. You want
a formless band around zero. A curve means the relationship is not linear; a fan
widening to the right means the variance is not constant. Both are invisible in $R^2$,
which is why a high $R^2$ never substitutes for looking.

## In Stata

*The snippets below assume the header and preamble from
[Chapter 1](01_what_statistics_is_for.md).*

```stata
use "DATA/cps_small.dta", clear

scatter wage educ
regress wage educ

predict yhat
predict resid, residuals
scatter resid yhat, yline(0)
```

`regress` prints the coefficients, their standard errors, the $t$ statistics and
$p$-values, $R^2$, and the ANOVA table splitting SST into model and residual — the
same decomposition as Chapter 16.

The last three lines are the assumption check, and they matter more than anything in
the output table.

## In Python

```python
import numpy as np
from scipy import stats

x = np.array([2, 4, 6, 8, 10, 12])
y = np.array([14, 18, 23, 25, 31, 34])

fit = stats.linregress(x, y)
print(fit.slope, fit.intercept)       # 2.0143   10.0667
print(fit.rvalue**2)                  # 0.9902
print(fit.stderr, fit.pvalue)         # 0.1003   0.00004
```

`linregress` returns everything in one object. Note `rvalue` is $r$, so square it for
$R^2$.

To plot the fit and then the residuals:

```python
import matplotlib.pyplot as plt

plt.scatter(x, y, color="#8b1a1a")
plt.plot(x, fit.intercept + fit.slope*x, color="#222222")
plt.show()

resid = y - (fit.intercept + fit.slope*x)
plt.scatter(fit.intercept + fit.slope*x, resid)
plt.axhline(0, color="#999999")
plt.show()
```

## What goes wrong

**Extrapolating.** The line is evidence only across the range of $x$ you observed.

**Reading causation into a slope.** It is association, however small the $p$-value.

**Reporting $R^2$ as a percentage of $r$.** $r = 0.7$ gives $R^2 = 0.49$, not 0.70.

**Interpreting $b_0$ when $x = 0$ is outside the data.**

**Using $n-1$ degrees of freedom.** It is $n - 2$ for simple regression: two
parameters were estimated.

**Trusting a high $R^2$ without plotting the residuals.** A curved relationship can
produce an impressive $R^2$ and a systematically wrong line.

**Regressing $x$ on $y$ when you meant $y$ on $x$.** The two give different slopes.

## Exercises

1. For $n = 10$ pairs, $s_{xy} = 24$, $s_x^2 = 16$, $\bar{x} = 5$, $\bar{y} = 30$.
   (a) Find $b_1$ and $b_0$.
   (b) Write the fitted line and predict $y$ at $x = 8$.

2. A regression gives SST $= 500$ and SSE $= 125$.
   (a) Find SSR and $R^2$.
   (b) What is $r$, and can you determine its sign?

3. A fitted line is $\hat{y} = 45 - 3.2x$, from data where $x$ ranged from 5 to 20.
   (a) Interpret the slope.
   (b) Would you use it to predict at $x = 40$? Explain.
   (c) Is the intercept meaningful here?

4. A slope is $b_1 = 1.8$ with SE$(b_1) = 0.9$, from $n = 12$ observations.
   (a) Compute $t$ and the degrees of freedom.
   (b) Test at $\alpha = 0.05$, given $t_{0.025,10} = 2.2281$.
   (c) What does your conclusion mean in words?

5. A residual plot shows a clear U shape. What has gone wrong, and would $R^2$ reveal
   it?

### Answers

1. (a) $b_1 = 24/16 = 1.5$; $b_0 = 30 - 1.5(5) = 22.5$.
   (b) $\hat{y} = 22.5 + 1.5x$, so at $x = 8$, $\hat{y} = 34.5$.

2. (a) SSR $= 500 - 125 = 375$, so $R^2 = 375/500 = 0.75$.
   (b) $r = \pm\sqrt{0.75} = \pm 0.8660$. **The sign cannot be determined from $R^2$**
   — you need the sign of the slope or the covariance.

3. (a) Each one-unit increase in $x$ is associated with a decrease of 3.2 in $\hat{y}$.
   (b) **No.** 40 is double the largest observed $x$; the linear relationship is
   evidence only within 5 to 20.
   (c) **No.** $x = 0$ lies outside the observed range, so 45 is an extrapolation.

4. (a) $t = 1.8/0.9 = 2.00$ with $\nu = 12 - 2 = 10$.
   (b) $2.00 < 2.2281$, so **do not reject**.
   (c) There is insufficient evidence that the slope differs from zero — this sample
   does not establish that $x$ helps predict $y$. Note that is not the same as showing
   the slope *is* zero; with $n = 12$ the test has little power.

5. The relationship is **not linear** — a straight line is being fitted to a curve, so
   the residuals are positive at the extremes and negative in the middle. $R^2$ would
   **not** reveal it: it can be high while the line is systematically wrong, which is
   exactly why the residual plot is not optional.

<!-- more-practice:start -->

## More practice

Eight more. Question 1 is a full fit by hand — slow, and worth doing once, because
every quantity in a regression output is built from the two sums you compute there.

1. Advertising spend $x$ (thousands) and sales $y$ (thousands of units):

   | $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
   |---|---|---|---|---|---|---|---|---|
   | $y$ | 14 | 21 | 18 | 23 | 27 | 26 | 35 | 36 |

   (a) Find $\bar{x}$, $\bar{y}$, $\sum(x-\bar{x})(y-\bar{y})$ and
   $\sum(x-\bar{x})^2$.
   (b) Find $b_1$ and $b_0$, and write the fitted line.
   (c) Interpret the slope in the units of the problem.
   (d) Verify that the line passes through $(\bar{x}, \bar{y})$.

2. For the same data:
   (a) Find SST, SSE and SSR.
   (b) Find $R^2$ and interpret it.
   (c) Find $r$, and say how you know its sign.

3. Still with the same data, SE$(b_1) = 0.3883$.
   (a) Find $t$ and state $\nu$.
   (b) Test $H_0: \beta_1 = 0$ at $\alpha = 0.05$, given $t_{0.025,6} = 2.4469$.
   (c) State what rejection means in the language of the problem.

4. Using the fitted line from question 1:
   (a) Predict sales at $x = 5$.
   (b) Predict sales at $x = 20$.
   (c) Which prediction would you report, and why?

5. A different regression gives SST $= 800$ and SSE $= 200$.
   (a) Find SSR and $R^2$.
   (b) Find $|r|$.
   (c) Can you determine the sign of $r$ from these figures? Explain.

6. A fitted line is $\hat{y} = 80 - 2.5x$, from data where $x$ ran from 10 to 40.
   (a) Interpret the slope.
   (b) Interpret the intercept, or explain why you would not.
   (c) What is $\hat{y}$ at $x = 32$, and is that a defensible prediction?

7. Two residual plots are described. In the first, the residuals form a shapeless band
   around zero. In the second, they fan out steadily as $\hat{y}$ increases.
   (a) Which assumption does the second violate?
   (b) Would $R^2$ have revealed it?
   (c) Why is the plot not optional?

8. A paper reports a slope of 1.4 on years of schooling in a wage regression, with
   $p < 0.001$ and $R^2 = 0.18$.
   (a) Does the small p-value establish that schooling raises wages?
   (b) What does $R^2 = 0.18$ tell you?
   (c) Are (a) and (b) in tension? Explain.

### Answers to the extra problems

1. (a) $\bar{x} = 4.5000$ and $\bar{y} = 25.0000$. The $x$ deviations are
   $-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5$ and the $y$ deviations are
   $-11, -4, -7, -2, 2, 1, 10, 11$. The cross-products sum to $126$ and the squared $x$
   deviations sum to $42$.
   (b) $b_1 = 126/42 = 3.0000$ and $b_0 = 25 - 3(4.5) = 11.5000$, so
   $\hat{y} = 11.5 + 3x$.
   (c) Each additional **thousand dollars** of advertising is associated with about
   **3,000 more units** sold. "Associated with", not "causes" — the data is
   observational.
   (d) $11.5 + 3(4.5) = 25.0000 = \bar{y}$. The least-squares line always passes
   through the point of means, which is a free check on $b_0$.

2. (a) SST $=$ the squared $y$ deviations $= 416$. SSE $= 38.0000$. SSR $= 416 - 38 =
   378$ — or, equivalently, $b_1^2 \sum(x-\bar{x})^2 = 9(42) = 378$.
   (b) $R^2 = 378/416 = 0.9087$. The line accounts for **90.9%** of the variation in
   sales.
   (c) $r = \sqrt{0.9087} = 0.9532$, **positive**, because the slope is positive.
   $R^2$ on its own cannot give you the sign — the square root is taken with the sign
   of $b_1$.

3. (a) $t = 3.0/0.3883 = 7.7256$ with $\nu = n - 2 = 6$.
   (b) $7.7256 > 2.4469$, so **reject $H_0$**. ($p = 0.0002$.)
   (c) The relationship between advertising and sales is not plausibly zero: a slope
   this far from zero would arise by chance in well under one study in a thousand if
   advertising had no association with sales at all. It does **not** establish that
   advertising causes sales, and it says nothing about whether a slope of 3 is
   commercially worth having — that depends on the cost of the advertising.

4. (a) $11.5 + 3(5) = 26.5000$ thousand units.
   (b) $11.5 + 3(20) = 71.5000$ thousand units.
   (c) Only **(a)**. $x = 5$ sits in the middle of the observed range of 1 to 8;
   $x = 20$ is two and a half times the largest value ever seen. The straight line is
   evidence only across the range where there is data, and extrapolating assumes
   linearity continues into territory that was never tested. Advertising returns in
   particular almost certainly flatten, so 71.5 is not a cautious estimate — it is a
   guess dressed as arithmetic.

5. (a) SSR $= 800 - 200 = 600$, so $R^2 = 600/800 = 0.7500$.
   (b) $|r| = \sqrt{0.75} = 0.8660$.
   (c) **No.** $R^2$ is a squared quantity and discards the sign. You need the sign of
   $b_1$ or of the covariance; a relationship explaining 75% of the variation could be
   strongly rising or strongly falling.

6. (a) Each one-unit increase in $x$ is associated with a decrease of **2.5** in
   $\hat{y}$.
   (b) **I would not interpret it.** $x = 0$ lies well outside the observed range of 10
   to 40, so 80 is the fitted value at a point the data says nothing about. Report it
   because the line requires it; interpret it only when $x = 0$ is genuinely in range
   and meaningful.
   (c) $80 - 2.5(32) = 0.0000$. That is **inside** the range of $x$, so the prediction
   is defensible as arithmetic — but a predicted value of exactly zero at the upper end
   of the data is worth a second look, since it suggests the relationship may bend
   rather than continuing straight to zero and beyond. The residual plot would tell
   you.

7. (a) **Constant variance** of the residuals. A fan shape means the spread of the
   errors grows with the fitted value, so the single $s$ that the standard errors are
   built from describes neither end of the data.
   (b) **No.** $R^2$ measures how much variation the line explains and is completely
   silent on whether the residuals are well behaved. A fanning pattern can sit under a
   high $R^2$, and the coefficient estimates will be fine while their standard errors —
   and therefore every p-value and interval — are wrong.
   (c) Because the two most consequential failures, non-linearity and
   non-constant variance, are both invisible in the output table and both obvious in
   the plot. It takes one line of code and it is the only part of the diagnostics that
   cannot be skipped.

8. (a) **No.** It establishes that the slope is very unlikely to be zero. Schooling may
   raise wages; higher-ability people may acquire more of both; family background may
   drive both. Identifying the causal effect requires a design, not a smaller p-value,
   and this is the problem the rest of econometrics exists to address.
   (b) That schooling accounts for 18% of the variation in wages, leaving 82% to
   everything else — experience, occupation, location, luck. That is a perfectly
   ordinary figure for a cross-section of individuals.
   (c) **Not at all**, and the pair is worth understanding together. $p < 0.001$ is a
   statement about whether the slope is distinguishable from zero, which with a large
   sample it easily can be; $R^2 = 0.18$ is a statement about how much of the outcome
   the model predicts. A variable can matter reliably and still explain only a modest
   share of the variation, because the thing being explained has many causes. Confusing
   the two is how a well-identified small effect gets dismissed and a large $R^2$ from
   an uninformative model gets believed.

<!-- more-practice:end -->

---
