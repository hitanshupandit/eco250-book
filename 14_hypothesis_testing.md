# Chapter 14 — Hypothesis testing, and what a p-value is

> **The question:** somebody claims $\mu$ is 25. Is your data consistent with that?

## A narrower question than Chapter 13

Estimation asked *what is $\mu$?* and answered with a range. Testing asks something
smaller and far more common: a claim arrives from outside the data — a policy
document, a contract, a previous study, a competitor's advertisement — and you have
to say whether your sample is compatible with it.

You do not get to answer *yes* or *no*. You get to answer **surprising** or **not
surprising**, and the whole machinery exists to make that word precise.

## The logic

1. **Assume the boring thing is true.** That is the null hypothesis, $H_0$.
2. **Ask how surprising your data would be** if it were.
3. **If very surprising, reject $H_0$.** If not, you have learned nothing about it.

That is proof by contradiction with a probability attached.

The asymmetry is deliberate. $H_0$ gets the benefit of the doubt in the way a
defendant does — and "not guilty" is not the same verdict as "innocent". Failing to
reject is not evidence that $H_0$ is true. It is an absence of evidence that it is
false, which is a different and weaker thing.

## Setting up the hypotheses

This is the part Stata cannot do for you, and the part that carries the marks.

- **$H_0$ always contains the equality.** $H_0: \mu = 25$. You cannot test
  $H_0: \mu > 20$ — there is no single number to build a sampling distribution
  around.
- **$H_a$ is what you want evidence *for*.** It never contains the equality.
- **The direction comes from the wording**, never from the data.

| The claim says… | $H_a$ | Tail |
|---|---|---|
| "differs from", "has changed", "is there an effect" | $\mu \neq \mu_0$ | two |
| "exceeds", "is more than", "has increased" | $\mu > \mu_0$ | right |
| "is less than", "has fallen", "fewer" | $\mu < \mu_0$ | left |
| "at least", "guarantees", "meets the standard" | $\mu < \mu_0$ | left — you test *against* the guarantee |

Two questions, in this order. **What number is being claimed?** That is $\mu_0$.
**What would I have to show to overturn it?** That is $H_a$.

The last row catches people. A *guarantee* is tested from the side of whoever the
guarantee protects: a buyer told "at least 500 hours" looks for evidence that it
fails. A *target*, by contrast, is tested two-tailed, because missing it in either
direction is a problem.

> **Choose the direction before you look at the data.** Picking the tail afterwards
> halves your p-value for free. It has a name — p-hacking — and we will measure what
> it does later in this chapter.

## The test statistic

$$z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}
\qquad\text{or}\qquad
t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$$

Both ask: **how many standard errors is my sample mean from the value $H_0$ claims?**

Same $z$-or-$t$ question as Chapter 13 — is the denominator known, or estimated from
the same data? In practice it is nearly always $t$.

The numerator is **signal**, the denominator is **noise**. A test statistic is a
signal-to-noise ratio and nothing more. Which immediately tells you something
uncomfortable: there are two ways to make it large, a bigger gap or a smaller
standard error, and only the first is about the effect.

## The eight steps

Write all eight down every time until you stop needing to. Exams give marks for the
steps, not only the arithmetic.

1. **State the hypotheses.** $H_0$ says no effect; $H_a$ says what you want evidence
   of.
2. **Choose the test.** $z$ if $\sigma$ is known, $t$ if you estimated it.
3. **Set $\alpha$.** The Type I error rate you will live with — 0.05 by convention.
4. **Write the decision rule.** Critical value and tail: "reject if $|t| > 2.0301$".
5. **Get the data.**
6. **Compute the test statistic** and its p-value.
7. **Reach the statistical conclusion.** Reject if $p \leq \alpha$, otherwise fail to
   reject.
8. **Say what it means** — in commutes, wages, batteries. The thing somebody actually
   asked about.

**Steps 1 to 5 happen before you look at a single number.** That ordering is the
entire protection against fooling yourself, and a marker can see from the order of
your working whether you kept it.

## Two routes, one verdict

**Rejection region.** Pick $\alpha$, find the critical value, reject if the statistic
lands beyond it. Set up before you see the data.

**p-value.** Compute the probability of data at least this extreme *if $H_0$ were
true*. Reject if $p < \alpha$.

They always agree. The p-value is the rejection region read backwards — it reports
*how far* past the line you landed, not merely that you did.

## Worked example — the commute

The same $n = 36$ staff from Chapter 13: $\bar{x} = 28.4$, $s = 6$. Management's
planning document assumes the mean commute is **25 minutes**.

| step | | |
|---|---|---|
| 1 | hypotheses | $H_0: \mu = 25$ against $H_a: \mu \neq 25$ (two-tailed) |
| 2 | test | one mean, $\sigma$ unknown $\Rightarrow$ one-sample $t$, $\nu = 35$ |
| 3 | $\alpha$ | 0.05 |
| 4 | decision rule | reject if $\lvert t\rvert > 2.0301$ |
| 5 | data | $n = 36$, $\bar{x} = 28.4$, $s = 6$ |
| 6 | compute | SE $= 1$, $t = (28.4 - 25)/1 = 3.4$, $p = 0.0017$ |
| 7 | conclusion | $3.4 > 2.0301$ and $p < 0.05$ $\Rightarrow$ **reject $H_0$** |
| 8 | meaning | the mean commute is **not** 25 minutes; it appears about 3.4 minutes longer, so the planning figure is too low |

Why two-tailed? Nothing in the question says management's figure is too low — only
that it is "assumed". No direction is given, so both must be allowed.

Every test you meet this term fills in that same table. **Only rows 2, 4 and 6 ever
change.**

## Worked example — one tail, and why the choice matters

Your working weight on a gym machine averaged **65 lb**. You start a new routine, and
over the next block you log **20 sessions**: $\bar{x} = 72$ lb, $s = 12$ lb.

**(a)** You believe the routine made you *stronger*. State the hypotheses.
**(b)** Test at $\alpha = 0.05$.
**(c)** Redo it two-tailed.
**(d)** What if you had only logged **10** sessions, with the same $\bar{x}$ and $s$?

### Solution

**(a)** "Stronger" names a direction, so one tail pointing up:
$H_0: \mu = 65$ against $H_a: \mu > 65$.

**(b)** SE $= 12/\sqrt{20} = 2.6833$, so $t = (72-65)/2.6833 = 2.6087$ with
$\nu = 19$. The critical value is $t_{0.05,19} = 1.7291$. Since $2.6087 > 1.7291$,
**reject**. One-tailed $p = 0.0086$.

**(c)** Two-tailed: critical $\pm 2.0930$, and $p = 0.0173$ — exactly double. Still a
rejection, but you spent twice the evidence for it.

**(d)** With $n = 10$: SE $= 3.7947$, $t = 1.8447$, $\nu = 9$.

| | statistic vs critical | verdict | $p$ |
|---|---|---|---|
| one-tailed | $1.8447 > 1.8331$ | **reject** | 0.0491 |
| two-tailed | $1.8447 < 2.2622$ | **do not reject** | 0.0982 |

**Same data. Opposite verdicts.** Which is why the tail is chosen from your question
before you lift, and never from the numbers afterwards.

## What a p-value actually is

Here is the definition, and every word is load-bearing:

> the probability of getting data **at least this extreme**, **if $H_0$ were true**

Say your result out loud as a sentence. For the gym test, $p = 0.0086$:

*"If the routine had done nothing at all, I would see a jump this big or bigger about
9 times in 1,000 blocks of training."*

It is an area under a curve, not a verdict a computer reached. For the commute test,
$2 \times \mathrm{ttail}(35, 3.4) = 0.0017$ reproduces Stata's p-value exactly.

### The p-value is a random variable

This is the fact that changes how you read research.

Draw a fresh sample, test the same **true** hypothesis, record $p$. Do it a thousand
times. If a p-value measured truth, it would come out small every time or large every
time. Here is what it actually does — 1,000 tests, $H_0$ true in every one:

| | |
|---|---|
| $p < 0.05$ | **50** of 1000 |
| $p < 0.10$ | 105 of 1000 |
| $p < 0.50$ | 479 of 1000 |
| mean $p$ | 0.511 |

The histogram is **flat**. When $H_0$ is true the p-value is uniform on $[0,1]$: any
value is as likely as any other.

Read the first row again. $\alpha$ was 0.05, $H_0$ was true every single time, and we
rejected it 50 times out of 1,000. **Five per cent.** The Type I error rate is not a
convention you are asked to trust — it is built into the definition, and that is it
measured.

### Now make $H_0$ false

Same test, same $n = 25$. The only change: the true mean is 106, not 100. Now $p$
piles up near zero, and $p < 0.05$ in **476 of 1,000**.

That 476 is the **power** of the test. Sit with it. The effect is genuine, it is six
points, it is nearly half a standard deviation — and with 25 observations we **miss
it more than half the time**.

> "Not significant" does not mean "no effect". Here it mostly means $n$ was 25.

## What a small p does not tell you

Two sentences students write every year, both false.

**"$p = 0.03$, so there is a 3% chance $H_0$ is true."** Backwards. $p$ is computed
*assuming* $H_0$ is true — you cannot then use it as the probability of the thing you
assumed.

**"$p = 0.001$ is a bigger effect than $p = 0.04$."** No. Consider a population whose
mean is 100.5 when the claim is 100 — an effect of half a point that nobody would
care about:

| $n$ | $p$ | 95% interval |
|---|---|---|
| 25 | 0.927 | — |
| 5,000 | **0.037** | (100.03, 100.87) |

At $n = 5{,}000$ it is "significant", and the effect is exactly as pointless as
before. The interval is what saves you: the whole thing sits within one point of 100.
The test says *not 100*; the interval says *not 100, but by at most 0.87*.

A big enough $n$ makes any difference significant, because the standard error in the
denominator goes to zero. **Significance is a statement about $n$ as much as about
the effect**, which is why a p-value should never be reported on its own.

| $p$ **is** | $p$ **is not** |
|---|---|
| the probability of data this extreme, assuming $H_0$ | the probability that $H_0$ is true |
| a measure of how *surprising* the data is | a measure of how *big* the effect is |
| small $\Rightarrow$ the data sits badly with $H_0$ | small $\Rightarrow$ the finding matters |

## Running lots of tests

Twenty studies. In every one $H_0$ is **true** — the true mean is 100 and we test 100.
There is nothing to find. Watch anyway:

> test 7 gives $p = 0.0159$. Test 20 gives $p = 0.0336$.

Two "significant" findings out of twenty, and **not one of them is real**. We know
that for certain, because the data was generated with no effect in it.

Now imagine running twenty tests and publishing test 7. The arithmetic is correct.
The p-value is correctly computed. The finding is nothing at all.

That is what p-hacking *is* — not fraud, not bad arithmetic, just not telling anyone
about the other nineteen. It is also why steps 3 and 4 come before step 5.

## Two ways to be wrong

| | $H_0$ is actually true | $H_0$ is actually false |
|---|---|---|
| **You reject** | **Type I error**, probability $\alpha$ | correct (power, $1-\beta$) |
| **You do not reject** | correct | **Type II error**, probability $\beta$ |

**Type I** — convicting the innocent. You declared an effect that is not there.
**Type II** — acquitting the guilty. There was an effect and you missed it.

You *choose* $\alpha$. You only *influence* $\beta$, mostly through $n$. For a fixed
$n$, lowering $\alpha$ raises $\beta$ — the only way to cut both is a bigger sample.

$\alpha = 0.05$ is a convention, not a law. Choose it by what the two mistakes cost. A
smoke alarm should have a high $\alpha$: false alarms are cheap and misses are not. A
murder conviction should not.

## The interval and the test are the same object

One data set, two questions:

| | |
|---|---|
| 95% CI for mean wage | $(9.8254,\ 10.6007)$ |
| test $\mu = 10.5$ | $p = 0.1466$ — inside, so **not** rejected |
| test $\mu = 10.7$ | $p = 0.0139$ — outside, so **rejected** |

> A two-tailed test of $\mu = \mu_0$ at level $\alpha$ rejects **exactly when** the
> $(1-\alpha)$ confidence interval excludes $\mu_0$.

Not a coincidence — the interval was built from the same inequality the test checks.

Which makes the interval the more useful object: it tests *every* possible claim at
once. Any value inside survives at 5%, any value outside is rejected. So why learn
the test at all? Because it hands you the p-value, which says how far past the line
you landed. **Report both.** The interval gives the size, the p-value gives the
surprise.

## In Stata

*The snippets below assume the header and preamble from [Chapter 1](01_what_statistics_is_for.md) — `clear all`, the log, and a `cd` to your own folder.*

```stata
use "DATA/cps_small.dta", clear
ttest wage == 5
```

The output carries everything: `Mean`, `Std. err.` (the denominator of $t$), `t`,
`Degrees of freedom`, and three p-values across the bottom:

```
Ha: mean < 5          Ha: mean != 5          Ha: mean > 5
Pr(T < t) = 1.0000    Pr(|T| > |t|) = 0.0000  Pr(T > t) = 0.0000
```

Stata does not know which test you meant, so it prints all three. **You** choose,
from the wording, before looking. The two one-sided values always sum to 1, and the
middle is twice the smaller — they are one computation reported three ways.

For problems that give you summary statistics rather than data, the immediate forms
take the numbers directly:

```stata
ztesti 16 82.5 6 80        // n, mean, sd, claimed value -- sigma known
ttesti 36 28.4 6 25        // same, sigma estimated
```

And `ttail` is the function behind the p-value — the mirror image of `invt`:

```stata
display "p = " 2*ttail(35, 3.4)
```

`invt` takes an **area** and returns a **cutoff**; `ttail` takes a cutoff and returns
an area. A critical value is the first question, a p-value is the second.

## In Python

One call does the whole test:

```python
from scipy import stats
import numpy as np

x = np.array([...])                       # your sample
t, p = stats.ttest_1samp(x, 25)           # tests H0: mu = 25
```

`ttest_1samp` returns the statistic and the **two-tailed** p-value. For a one-tailed
test, halve it — but only after checking the sign points the way your $H_a$ does.

From summary statistics rather than data, the p-value is one line:

```python
t, df = 3.4, 35
print(2 * stats.t.sf(abs(t), df))         # 0.0017, the two-tailed p
print(stats.t.sf(abs(t), df))             # 0.0009, the one-tailed p
```

That is the chapter's definition executed: the area in the tails beyond your statistic.

### A p-value is a random variable

![p-values when H0 is true and when it is false](figures/pvalue_uniform.png)

**Left:** 20,000 tests where $H_0$ is true. The histogram is **flat** — every p-value
is as likely as any other — and 5.1% fall below 0.05. That is $\alpha$, measured.

**Right:** the same test when $H_0$ is false. Now the p-values pile up near zero, and
48.7% fall below 0.05. That 48.7% is the **power**: a real six-point effect, missed
more than half the time at $n = 25$.

```python
rng = np.random.default_rng(250)
reps, n = 20_000, 25

true  = rng.normal(100, 15, size=(reps, n))    # H0 is TRUE
false = rng.normal(106, 15, size=(reps, n))    # H0 is FALSE

p_true  = stats.ttest_1samp(true,  100, axis=1).pvalue
p_false = stats.ttest_1samp(false, 100, axis=1).pvalue

print((p_true  < 0.05).mean())    # 0.0514  -- the Type I error rate
print((p_false < 0.05).mean())    # 0.4865  -- the power
```

**Change 106 to 103** and the power collapses. **Change `n` to 100** and it recovers.
Power depends on the effect size and the sample size together, and two lines of code
show that faster than any amount of prose.

## What goes wrong

**Putting the equality in $H_a$.** It belongs in $H_0$, always.

**Choosing the tail after seeing $\bar{x}$.** This halves your p-value for nothing
and invalidates the test.

**"Fail to reject" read as "$H_0$ is true".** You found insufficient evidence. With
$n = 25$ you would miss a real six-point effect more than half the time.

**Reporting $p$ alone.** At a large $n$, significant and trivial are compatible. Give
the interval.

**Stopping at step 7.** A paper that ends at "$p = 0.0017$" has not answered the
question. Somebody asked about commutes, not about $t$.

## Exercises

1. For each, state $H_0$ and $H_a$ and the tail.
   (a) A bus company advertises a mean journey of 45 minutes; commuters suspect it is
   longer.
   (b) Last year's mean score was 72; the department asks whether this year differs.
   (c) A supplier guarantees a mean life of at least 500 hours; you are the buyer.
   (d) A packing machine is set to 500 g; QC checks each morning that it has not
   drifted.

2. A sample of $n = 25$ batteries gives $\bar{x} = 486$ hours and $s = 30$. The
   supplier guarantees at least 500.
   (a) State the hypotheses and compute $t$.
   (b) Test at $\alpha = 0.05$, noting that all 5% goes in one tail.
   (c) The 95% interval is $(473.62,\ 498.38)$. Confirm it agrees.

3. A study reports $p = 0.04$ from a sample of 50,000. What is the first question you
   should ask?

4. Explain why, when $H_0$ is true, p-values are uniformly distributed — and what
   that implies about running many tests.

5. A researcher writes: "$p = 0.08$, so we accept the null hypothesis and conclude
   the treatment has no effect." Identify two errors.

### Answers

1. (a) $H_0: \mu = 45$, $H_a: \mu > 45$, right tail — "suspect it is longer" names a
   direction. (b) $H_0: \mu = 72$, $H_a: \mu \neq 72$, two-tailed — "differs" is not a
   direction. (c) $H_0: \mu = 500$, $H_a: \mu < 500$, left tail — the buyer needs
   evidence the guarantee *fails*. (d) $H_0: \mu = 500$, $H_a: \mu \neq 500$,
   two-tailed — drift either way is a fault.

2. (a) $H_0: \mu = 500$ against $H_a: \mu < 500$. SE $= 30/\sqrt{25} = 6$, so
   $t = (486-500)/6 = -2.3333$ with $\nu = 24$.
   (b) One tail, so the critical value is $-t_{0.05,24} = -1.7109$, **not** $-2.0639$.
   Since $-2.3333 < -1.7109$, **reject**. ($p = 0.0142$.)
   (c) 500 is not in $(473.62,\ 498.38)$, so the interval rejects it too. Agrees.

3. **"What is the confidence interval?"** — or equivalently, how big is the effect.
   With 50,000 observations the standard error is tiny, so a completely trivial
   difference will clear any significance threshold. The p-value alone cannot
   distinguish an important finding from a meaningless one.

4. The p-value is the probability of data at least as extreme as what you saw,
   computed under $H_0$. If $H_0$ is true, that probability is itself a draw from
   $[0,1]$ with every value equally likely — $p < 0.05$ happens 5% of the time, $p <
   0.10$ happens 10% of the time, and so on. The implication: run enough tests on
   nothing and some will be "significant" by construction. Twenty tests of true nulls
   produce about one false positive on average.

5. **(i)** You never "accept" $H_0$ — you fail to reject it. **(ii)** "No effect" does
   not follow: $p = 0.08$ with a small sample is entirely consistent with a real and
   substantial effect that the study lacked the power to detect. The honest sentence
   is "insufficient evidence to reject", and it should be accompanied by a confidence
   interval showing what effect sizes remain plausible.

---
