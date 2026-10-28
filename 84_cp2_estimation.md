# Practice: Estimation and confidence intervals

Chapter 13. 6 multiple choice and 8 worked questions, all with solutions.

These are the Checkpoint 2 practice questions for this topic. Work them with the answers covered.

---

## Multiple choice

**1.** A sample of 25 invoices has $s = 7.5$. The standard error of the mean invoice value is

(A) 7.5000   (B) 0.3000   (C) 1.5309   (D) 1.5000

**2.** With $\bar{x} = 54.8$ and $t_{0.025,24} = 2.0639$, the 95% interval for the mean invoice value runs

(A) (39.3208, 70.2792)   (B) (53.3000, 56.3000)   (C) (51.8601, 57.7399)   (D) (51.7042, 57.8958)

**3.** A market report widens its interval from 90% to 99% confidence. The interval becomes

(A) wider   (B) narrower   (C) unchanged   (D) narrower then wider

**4.** An auditor wants a narrower interval for mean order value. Which actually achieves it?

(A) raising the confidence level   (B) sampling more orders   (C) reporting the variance instead   (D) sampling fewer but larger orders

**5.** A consultant reports a 95% interval for mean wait time of $(4.2, 6.8)$ minutes. The correct reading is

(A) 95% of intervals built this way contain the true mean   (B) the true mean is in this interval with probability 0.95   (C) 95% of waits fall between 4.2 and 6.8   (D) the estimate is accurate to within 95%

**6.** A firm wants mean invoice value estimated within $\pm\$1$ at 95\% confidence, believing $\sigma \approx 7.5$. It must sample

(A) 153   (B) 55   (C) 216   (D) 217

## Worked questions

**1.** A sample of 25 invoices gives $\bar{x} = 54.8$ and $s = 7.5$. **(a)** Compute the standard error. **(b)** Build a 95% confidence interval using $t_{0.025,24} = 2.0639$. **(c)** State precisely what '95% confident' refers to.

**2.** Using $\sigma \approx 7.5$, find the sample size needed to estimate a mean within $\pm 1.0$, then within $\pm 0.5$, both at 95% confidence. Comment.

**3.** Explain why a point estimate reported without a margin of error is of little use.

**4.** A sample of 16 gives $\bar{x} = 50$, $s = 8$. Build a 95% interval using $t_{0.025,15} = 2.1314$, and say how it would change at 99%.

**5.** Name the three ways to reduce the margin of error and say which is the only honest one.

**6.** Explain why the sample size formula always rounds up.

**7.** A firm wants its mean order value estimated to within \$3 at 99\% confidence, and believes $\sigma \approx 25$. **(a)** Find the required sample size. **(b)** The budget allows 300 orders. What margin does that buy, at the same confidence?

**8.** Explain why a 95% confidence interval built from a skewed population at $n = 36$ may contain $\mu$ less than 95% of the time, and what fixes it.

---

## Answers — multiple choice

**1. D** — $s/\sqrt{n}$. The first distractor reports $s$ itself.

**2. D** — The first distractor forgets to divide by $\sqrt{n}$; the last uses $z$ where $\sigma$ was estimated.

**3. A** — More confidence is bought with more vagueness.

**4. B** — Only $n$, the confidence level and $\sigma$ move the width, and only $n$ improves precision without giving something up.

**5. A** — The true mean is fixed; the interval is what was random.

**6. D** — $(1.96(7.5)/1)^2 = 216.08$, rounded up. The first uses the 90% value; the last forgets to round up.


## Answers — worked questions

**1.** (a) $7.5/5 = 1.5$. (b) $54.8 \pm 2.0639(1.5) = (51.7042, 57.8958)$. (c) The procedure, not this interval: repeat the exercise many times and 95% of the intervals built this way contain $\mu$.

**2.** $(1.96(7.5)/1.0)^2 = 216.08 \Rightarrow 217$; $(1.96(7.5)/0.5)^2 = 864.33 \Rightarrow 865$. Halving the margin quadruples the sample — precision costs at the rate $\sqrt{n}$.

**3.** $\mathrm{P}(\bar{X} = \mu) = 0$, so the point estimate is certainly not exactly right. More practically, it hides how much the figure would move with a different sample: $n = 10$ and $n = 10{,}000$ can give the same $\bar{x}$ and do not deserve the same confidence.

**4.** SE $= 2$, so $50 \pm 2.1314(2) = (45.7371, 54.2629)$. At 99% the critical value rises to 2.9467, giving $\pm 5.89$ — a wider interval for the same data.

**5.** Raise $n$; accept lower confidence; reduce $\sigma$. Raising $n$ is the only one that buys genuine precision — lowering confidence just means being wrong more often, and reducing $\sigma$ means changing what you measure or how.

**6.** $n$ must be a whole number, and rounding down would leave the margin larger than the target, failing the requirement the calculation was made to meet.

**7.** (a) $n = (2.5758 \times 25/3)^2 = 460.75$, so 461. (b) $E = 2.5758(25/\sqrt{300}) = 3.72$ — so 300 orders buys about \$3.72, short of the \$3 target.

**8.** The interval's coverage relies on $\bar{X}$ being normal. At $n = 36$ a strongly skewed population has not finished converging, so the $t$ interval is slightly too narrow and under-covers — in simulation, about 92% rather than 95%. Raising $n$ fixes it, because the CLT approximation improves with $\sqrt{n}$.
