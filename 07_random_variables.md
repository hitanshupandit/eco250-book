# Chapter 7 — Random variables, expectation and variance

> **The question:** how do you describe the centre and spread of something that has not
> happened yet?

## A number you do not know yet

A **random variable** attaches a number to each outcome of an experiment.

Something random is about to happen, and the random variable is the number you read off
once it has. Roll a die and $X$ is whatever comes up. Twelve applications land on your
desk and $X$ is how many are incomplete. You stand at a bus stop and $X$ is how long you
wait.

The thing people trip on: $X$ itself is not random, and it is not a variable in the
algebra sense either. The randomness is in *which outcome happens*. $X$ is just the
number we have agreed to attach to each one. Before the die lands, $X$ is a
distribution. After it lands, $X$ is 4.

Capital letters for the random variable, lower case for a value it took. $\mathrm{P}(X = x)$
reads "the probability that the random variable takes the particular value $x$".

## The fork that decides everything

**Discrete** — you can list the values. Number of defects, heads in ten flips, people in
a queue. Here $\mathrm{P}(X = k)$ is a real, usable number.

**Continuous** — the values fill an interval. Time, weight, price. Here
$\mathrm{P}(X = k) = 0$ for every single $k$, only intervals carry probability, and
probability is **area** under a curve.

That fork decides which tool you reach for: **discrete, add up probabilities;
continuous, find an area.** This chapter is discrete. Chapter 9 is continuous.

## A probability distribution

For a discrete random variable, the distribution is a list: every value, and its
probability.

| $x$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| $\mathrm{P}(X = x)$ | 0.10 | 0.30 | 0.40 | 0.20 |

To be valid it must satisfy two conditions, and checking them is often a mark:

- every probability lies in $[0, 1]$
- they sum to exactly 1

## Expectation

$$\mu = E(X) = \sum x\,\mathrm{P}(x)$$

A **weighted average** of the values, weighted by how often each occurs. It is what you
would average if you ran the experiment forever.

For the table above:

$$E(X) = 0(0.10) + 1(0.30) + 2(0.40) + 3(0.20) = 0 + 0.30 + 0.80 + 0.60 = 1.7$$

Note what just happened: **the expected value is 1.7, and $X$ can never be 1.7.** The
expected value is where the distribution balances, not a value to expect. A household
can have 2.4 children on average and no household has 2.4 children.

## Variance

$$\sigma^2 = V(X) = \sum (x - \mu)^2 \mathrm{P}(x) = E(X^2) - \mu^2$$

The same idea as Chapter 3 — average squared distance from the centre — but weighted by
probability instead of divided by $n$.

The second form is the **shortcut**, and it is nearly always faster by hand. Compute
$E(X^2)$ by squaring each value and weighting:

$$E(X^2) = 0^2(0.10) + 1^2(0.30) + 2^2(0.40) + 3^2(0.20) = 0 + 0.30 + 1.60 + 1.80 = 3.7$$

$$V(X) = 3.7 - (1.7)^2 = 3.7 - 2.89 = 0.81
\qquad \sigma = \sqrt{0.81} = 0.90$$

Both forms give the same answer. Use whichever the table in front of you makes easier,
but know the shortcut — on an exam it saves a column.

## The two laws

$$E(aX + b) = aE(X) + b
\qquad\qquad
V(aX + b) = a^2 V(X)$$

These do a surprising amount of work, so look at what each says.

In the expectation law, both $a$ and $b$ come through. Scale everything and the average
scales; shift everything and the average shifts.

In the variance law, **the $b$ has vanished**. Adding a constant slides the whole
distribution along without stretching it, so the spread is untouched. Only the
multiplier matters, and it arrives **squared** — which is why variance is in squared
units and why we report $\sigma$ instead.

### An example of the laws

A depot hires out vehicles with the distribution above. It charges \$50 per hire and
has fixed daily costs of \$20, so daily revenue net of costs is $R = 50X - 20$.

$$E(R) = 50(1.7) - 20 = 85 - 20 = 65$$
$$V(R) = 50^2 (0.81) = 2500(0.81) = 2025
\qquad \sigma_R = \sqrt{2025} = 45$$

Raise the fixed costs to \$100 and $E(R)$ falls by 80 while $V(R)$ does not move at all.

## Two variables

For two random variables, the covariance and correlation of Chapter 4 carry over
unchanged in meaning:

$$\text{COV}(X,Y) = E\big[(X-\mu_x)(Y-\mu_y)\big]
\qquad
\rho = \frac{\text{COV}(X,Y)}{\sigma_x \sigma_y}$$

And the rule that matters later:

$$V(X + Y) = V(X) + V(Y) + 2\,\text{COV}(X,Y)$$

**Variances add only when the covariance is zero** — that is, when the two are
uncorrelated. Chapter 11 leans on this to derive the standard error, so it is worth
having it fixed now.

## In Stata

Stata is built for data, not for probability tables, so most of this chapter is pencil
work. But you can compute expectations from a table directly:

```stata
clear
input x px
0 0.10
1 0.30
2 0.40
3 0.20
end

generate double xp  = x*px
generate double x2p = x*x*px
summarize xp x2p, meanonly

quietly summarize xp
scalar EX = r(sum)
quietly summarize x2p
scalar EX2 = r(sum)

display "E(X)   = " EX
display "E(X^2) = " EX2
display "V(X)   = " EX2 - EX^2
display "SD(X)  = " sqrt(EX2 - EX^2)
```

Note `r(sum)` rather than `r(mean)`: an expectation is a weighted **sum**, and the
weights are already in the column.

## What goes wrong

**Probabilities that do not sum to 1.** Check before computing anything.

**Expecting the expected value.** $E(X) = 1.7$ when $X$ is a count of vehicles is
correct and perfectly normal.

**Forgetting to square the $a$** in $V(aX + b)$, or wrongly adding the $b$.

**Using $E(X^2) = [E(X)]^2$.** These are different, and the gap between them *is* the
variance. Here $E(X^2) = 3.7$ while $[E(X)]^2 = 2.89$.

**Assuming variances add.** Only when the covariance is zero.

## Exercises

1. A random variable has this distribution:

   | $x$ | 1 | 2 | 3 | 4 | 5 |
   |---|---|---|---|---|---|
   | $\mathrm{P}(X=x)$ | 0.15 | 0.20 | 0.30 | 0.25 | 0.10 |

   (a) Verify it is valid. (b) Find $E(X)$. (c) Find $V(X)$ and $\sigma$.

2. For the variable in question 1, let $Y = 20X + 5$. Find $E(Y)$, $V(Y)$ and
   $\sigma_Y$.

3. A distribution has $\mathrm{P}(X=0) = 0.2$, $\mathrm{P}(X=1) = 0.5$ and
   $\mathrm{P}(X=2) = p$. Find $p$, then find $E(X)$.

4. $E(X) = 8$ and $E(X^2) = 73$. Find $V(X)$ and $\sigma$. Then find $V(3X - 4)$.

5. Two product lines have $V(X) = 36$, $V(Y) = 64$ and $\text{COV}(X,Y) = 24$.
   (a) Find $V(X+Y)$.
   (b) What would it be if the two were uncorrelated?
   (c) Which arrangement would a risk-averse manager prefer, and why?

### Answers

1. (a) All five lie in $[0,1]$ and they sum to $1.00$. Valid.
   (b) $E(X) = 1(0.15)+2(0.20)+3(0.30)+4(0.25)+5(0.10) = 0.15+0.40+0.90+1.00+0.50
   = 2.95$.
   (c) $E(X^2) = 1(0.15)+4(0.20)+9(0.30)+16(0.25)+25(0.10) = 0.15+0.80+2.70+4.00+2.50
   = 10.15$. So $V(X) = 10.15 - 2.95^2 = 10.15 - 8.7025 = 1.4475$ and
   $\sigma = 1.2031$.

2. $E(Y) = 20(2.95) + 5 = 64$. $V(Y) = 20^2(1.4475) = 579$. $\sigma_Y = 24.0624$.
   (Equivalently $\sigma_Y = 20 \times 1.2031$ — the multiplier passes straight through
   to the standard deviation, unsquared.)

3. Probabilities sum to 1, so $p = 1 - 0.2 - 0.5 = 0.3$. Then
   $E(X) = 0(0.2) + 1(0.5) + 2(0.3) = 1.1$.

4. $V(X) = 73 - 64 = 9$, so $\sigma = 3$. And $V(3X-4) = 3^2(9) = 81$ — the $-4$ does
   nothing.

5. (a) $36 + 64 + 2(24) = 148$.
   (b) $36 + 64 = 100$.
   (c) The uncorrelated arrangement. Expected total profit is unchanged either way, but
   its variance falls from 148 to 100 — the same return with less risk. That is
   diversification, and it is entirely a statement about the covariance term.

---
