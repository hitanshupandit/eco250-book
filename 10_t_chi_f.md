# Chapter 10 — Three distributions built out of normals: $t$, $\chi^2$ and $F$

> **The question:** the normal needs $\sigma$. What do you use when you have to
> estimate it?

## Learn them as constructions

These three arrive together and look like three new table formats to memorise. They are
not. Each is **built out of standard normals**, and if you can say what each is made
of, you can work out what it is for.

| | Built from | About |
|---|---|---|
| $\chi^2_\nu$ | $Z_1^2 + Z_2^2 + \cdots + Z_\nu^2$ — standard normals **squared and added** | one variance |
| $t_\nu$ | a $Z$ divided by $\sqrt{\chi^2_\nu/\nu}$ — a normal over an **estimated** spread | a mean, when $\sigma$ is unknown |
| $F_{\nu_1,\nu_2}$ | $\dfrac{\chi^2_{\nu_1}/\nu_1}{\chi^2_{\nu_2}/\nu_2}$ — a **ratio of two $\chi^2$s** | comparing two variances |

Everything below is commentary on that table.

## Student's $t$

Same bell shape as the normal, centred at zero, but with **fatter tails**. One
parameter: the degrees of freedom $\nu$, which in this course is almost always $n - 1$
— the same $n-1$ from Chapter 3.

### Why the tails are fatter

Here is the whole argument, and it is worth getting rather than accepting.

$$z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}}
\qquad\text{against}\qquad
t = \frac{\bar{x} - \mu}{s/\sqrt{n}}$$

In $z$, the denominator is a **fixed number**. In $t$, it is $s$, which is computed
from the same sample and therefore **jumps around**. Two sources of randomness instead
of one.

And the damage is asymmetric. When $s$ happens to come out small, the ratio blows up.
With only five observations, $s$ lands below $0.7\sigma$ about a quarter of the time —
so "blows up" is not a rare accident, it is a quarter of your samples.

A simulation makes it concrete. Drawing 1,000 samples from a normal population at
$n = 5$:

| | share beyond 1.96 |
|---|---|
| $\lvert z\rvert$ | 0.045 — the 5% the normal table promises |
| $\lvert t\rvert$ | **0.116** — more than double |

Use the normal's critical value on a $t$ statistic at $n = 5$ and you reject nearly
three times too often.

### It converges on the normal

As $\nu$ grows, $s$ settles down towards $\sigma$ and the surcharge shrinks:

| $\nu$ | $t_{0.025,\nu}$ | against $z = 1.96$ |
|---|---|---|
| 4 | 2.7764 | 42% larger |
| 10 | 2.2281 | 14% |
| 30 | 2.0423 | 4% |
| 100 | 1.9840 | 1% |
| $\infty$ | 1.9600 | — |

The bottom row *is* the normal. That is the real content of the "use $z$ for large
samples" rule of thumb.

### The rule people get wrong

> It is **not** "a standard error in the denominator means $t$."

The question is whether the denominator is **known** or **estimated from the same
data**.

$\dfrac{\bar{x}-\mu}{\sigma/\sqrt{n}}$ — $\sigma$ handed to you. This is $z$, and
$\sigma/\sqrt{n}$ is still called the standard error.

$\dfrac{\bar{x}-\mu}{s/\sqrt{n}}$ — you computed $s$. This is $t$.

The counterexample that settles it: tests about **proportions** use an estimated
standard error and still use $z$.

## Chi-squared

$\chi^2_\nu$ is a sum of $\nu$ squared standard normals. Two consequences fall straight
out of that, and you should be able to recite them:

**It cannot be negative.** It is a sum of squares.

**It is right-skewed.** Squaring stretches the large values and compresses the small
ones.

Because it is not symmetric, there is no trick for getting the lower tail from the
upper one — check which tail your table gives you. As $\nu$ grows it becomes more
symmetric, for the reason you would now guess: it is a sum, and sums go normal.

It is also built for exactly one job: **adding up squared errors**. Take your data,
subtract what your model predicted, square each gap, add them. That sum is a $\chi^2$,
which is why the same distribution reappears when we test categorical data later in the
course.

## The $F$ distribution

$F$ is one $\chi^2$ divided by another, each first divided by its own degrees of
freedom. So it is also **non-negative** and **right-skewed**, and it needs **two**
degrees of freedom — numerator first, always.

$$F_{\nu_1,\nu_2} \neq F_{\nu_2,\nu_1}$$

Getting the order backwards is the characteristic $F$ error.

Reading it: an $F$ near 1 says the two variances look alike. A large $F$ says the
numerator group is much more spread out.

## Reading the three tables

| | You need | Worked value |
|---|---|---|
| $t$ | $\nu$ and a tail area | $\nu = 10$, 2.5% above $\Rightarrow$ **2.2281** |
| $\chi^2$ | $\nu$ and a tail area | $\nu = 10$, 5% above $\Rightarrow$ **18.3070** |
| $F$ | **two** $\nu$s and a tail | $\nu_1 = 5$, $\nu_2 = 10$, 5% above $\Rightarrow$ **3.3258** |

$t$ is symmetric, so one column serves both tails. $\chi^2$ and $F$ are not, so read
the heading.

## In Stata

Two families, running in opposite directions, and keeping them straight is most of the
skill:

```stata
* AREA -> CUTOFF.  These take the area to the LEFT.
display "t,    nu=10, 2.5% above = " invt(10, 0.975)
display "t,    nu=inf (that is z) = " invnormal(0.975)
display "chi2, nu=10, 5% above    = " invchi2(10, 0.95)
display "chi2, nu=10, 5% below    = " invchi2(10, 0.05)
display "F,    5 over 10, 5% above = " invF(5, 10, 0.95)
display "F,    10 over 5, 5% above = " invF(10, 5, 0.95)
```

Note the last two differ — that is $F_{\nu_1,\nu_2} \neq F_{\nu_2,\nu_1}$ in one line.

```stata
* CUTOFF -> AREA.  The tail functions give the area ABOVE.
display "P(t_10 > 2.2281)  = " ttail(10, 2.2281)
display "P(chi2_10 > 18.31) = " chi2tail(10, 18.3070)
display "P(F_5,10 > 3.3258) = " Ftail(5, 10, 3.3258)
```

`invt` goes area → cutoff; `ttail` goes cutoff → area. **A critical value is the first
question. A p-value is the second.** That distinction is the whole of Chapter 14.

You can also watch the constructions happen:

```stata
* a chi-squared really is squared z's added up
clear
set seed 250
set obs 10000
generate double ss = 0
forvalues j = 1/10 {
    quietly generate double z`j' = rnormal()
    quietly replace ss = ss + z`j'^2
}
summarize ss
```

The mean should come out near 10 — because $E(\chi^2_\nu) = \nu$, which is another fact
that falls out of the construction: each $Z^2$ contributes 1 on average.

## What goes wrong

**Using $z$ when $\sigma$ was estimated.** At large $n$ the numerical difference is
cosmetic, but the reasoning is what is being marked.

**Getting the degrees of freedom wrong.** For a one-sample $t$ it is $n - 1$, not $n$.

**Reversing the $F$ degrees of freedom.** Numerator first.

**Assuming symmetry for $\chi^2$ or $F$.** Neither is symmetric, so you cannot flip a
sign to get the other tail.

**Confusing `invt` with `ttail`.** One takes an area, the other returns one.

**Thinking these are about new situations.** They are about the same questions as
before — a mean, a variance, two variances — under the realistic condition that you had
to estimate something.

## Exercises

1. Using Stata functions or a table, find:
   (a) $t_{0.05,\,15}$ (b) $t_{0.025,\,24}$ (c) $\chi^2_{0.05,\,8}$
   (d) $F_{0.05,\,3,\,12}$

2. Explain, in two sentences and without formulas, why the $t$ distribution has fatter
   tails than the normal.

3. A sample of $n = 16$ gives $\bar{x} = 52$ and $s = 8$, and the population mean is
   claimed to be 48.
   (a) Should you use $z$ or $t$? Why?
   (b) How many degrees of freedom?
   (c) Compute the test statistic.

4. Why can a $\chi^2$ value never be negative? Answer from the construction, not from
   a table.

5. A classmate computes $F_{10,5}$ when the question asked for $F_{5,10}$. Does it
   matter? Check with Stata or a table and explain.

### Answers

1. (a) 1.7531 (b) 2.0639 (c) 15.5073 (d) 3.4903.
   In Stata: `invt(15,0.95)`, `invt(24,0.975)`, `invchi2(8,0.95)`, `invF(3,12,0.95)`.

2. Because $t$ divides by $s$ rather than by $\sigma$, and $s$ is itself random — it
   changes from sample to sample. When $s$ comes out small the whole ratio is pushed
   far from zero, so extreme values occur more often than the normal predicts.

3. (a) **$t$** — $\sigma$ is unknown and $s$ was computed from the same 16
   observations.
   (b) $\nu = 15$.
   (c) SE $= 8/\sqrt{16} = 2$, so $t = (52-48)/2 = 2.00$.

4. A $\chi^2_\nu$ is the sum of $\nu$ squared standard normals. Every term is a square,
   so every term is at least zero, so the sum is at least zero. Nothing about the table
   is needed.

5. **Yes, it matters.** $F_{0.05,5,10} = 3.3258$ while $F_{0.05,10,5} = 4.7351$ — not
   remotely the same. The $F$ is a ratio, and swapping the degrees of freedom swaps
   which group is on top, which is a different question.

---
