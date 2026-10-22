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

---
