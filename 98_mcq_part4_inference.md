# Multiple choice: from sample to population

Chapters 11 to 14. Twenty questions, one answer each.

**These are hard on purpose.** Most take more than one step, and every wrong option is the number you get by making one specific mistake — dividing by $n$ instead of $n-1$, forgetting a square root, using $\sigma$ where $\sigma/\sqrt{n}$ belongs, inverting a conditional.

So if you pick a wrong answer, the key tells you **which mistake you made**, which is more use than the letter.

---

**1.** A population has $\sigma = 30$. To make the standard error 2.5, the sample size must be

(A) 144   (B) 12   (C) 75   (D) 36

**2.** $\mu = 50$, $\sigma = 9$, $n = 36$. Then $\mathrm{P}(\bar X < 47.2)$ is closest to

(A) 0.378   (B) 0.969   (C) 0.031   (D) 0.122

**3.** A sample of 25 gives $\bar x = 42$ and $s = 7.5$. With $t_{0.025,24} = 2.0639$, the 95\% interval half-width is

(A) 15.48   (B) 3.10   (C) 0.62   (D) 2.06

**4.** Which change would make a confidence interval narrower?

(A) raising the confidence level   (B) increasing $\sigma$   (C) decreasing the sample size   (D) increasing the sample size

**5.** A 99\% interval is reported as $(18.2, 25.8)$. The point estimate and margin are

(A) 21.0 and 7.6   (B) 22.0 and 3.8   (C) 22.0 and 7.6   (D) 20.0 and 3.8

**6.** To estimate a mean within $\pm 1.5$ at 99\% confidence with $\sigma = 12$, the required sample size is

(A) 246   (B) 62   (C) 425   (D) 104

**7.** A test gives $t = 2.4$ with 20 degrees of freedom, two-tailed, $\alpha = 0.05$. The critical value is 2.086, so you

(A) fail to reject $H_0$   (B) accept $H_0$   (C) need the $p$-value to decide   (D) reject $H_0$

**8.** For that same test, the $p$-value is

(A) below 0.05   (B) above 0.05   (C) exactly 0.05   (D) not determinable

**9.** A 95\% confidence interval for $\mu$ is $(31.2, 38.8)$. A two-tailed test of $H_0: \mu = 40$ at $\alpha = 0.05$ will

(A) fail to reject   (B) be inconclusive   (C) reject   (D) require the raw data

**10.** Which is a correct reading of '95\% confident'?

(A) $\mu$ lies in this interval with probability 0.95   (B) 95\% of the data lies in this interval   (C) the estimate is accurate to within 5\%   (D) 95\% of intervals built this way contain $\mu$

**11.** A supplier guarantees a mean lifetime of at least 400 hours. As the buyer testing this, $H_a$ is

(A) $\mu < 400$   (B) $\mu > 400$   (C) $\mu \neq 400$   (D) $\mu = 400$

**12.** All 5\% of a one-tailed test sits in one tail. Compared with the two-tailed critical value, the one-tailed value is

(A) larger   (B) smaller   (C) the same   (D) larger only for small $n$

**13.** Failing to reject $H_0$ when it is false is

(A) a Type I error   (B) the power   (C) a correct decision   (D) a Type II error

**14.** For a fixed sample size, lowering $\alpha$ from 0.05 to 0.01

(A) raises $\beta$   (B) lowers $\beta$   (C) leaves $\beta$ unchanged   (D) raises the power

**15.** A study with $n = 20{,}000$ reports $p = 0.01$ for a difference of 0.3 points. The right response is

(A) accept the finding, since $p$ is small   (B) ask for the confidence interval, since a huge $n$ makes trivial effects significant   (C) reject the finding, since the effect is small   (D) repeat the study with a smaller sample

**16.** Twenty independent tests are run on data with no real effect, at $\alpha = 0.05$. The expected number of 'significant' results is

(A) 0   (B) 5   (C) 1   (D) 20

**17.** A $p$-value of 0.20 means

(A) $H_0$ is true with probability 0.80   (B) data this extreme arises 20\% of the time when $H_0$ is true   (C) the effect is 20\% as large as expected   (D) the test has 20\% power

**18.** The CLT guarantees that for large $n$

(A) the population becomes normal   (B) $X$ is approximately normal   (C) $\bar X$ is approximately normal whatever the population   (D) $s$ equals $\sigma$

**19.** A sample of 40 households is drawn by selecting 10 blocks and surveying every household in each. The true standard error is

(A) equal to $\sigma/\sqrt{40}$   (B) smaller than $\sigma/\sqrt{40}$   (C) not defined   (D) larger than $\sigma/\sqrt{40}$

**20.** You compute $t = 1.9$ with $\nu = 29$ against a two-tailed critical value of 2.045, then notice the question said 'has increased'. Correctly treated as one-tailed (critical 1.699), you

(A) reject, but only because the tail was fixed in advance by the wording   (B) reject, having found the better test   (C) fail to reject, since 1.9 < 2.045   (D) report both results

---

## Answers

**1. A** — $30/\sqrt{n} = 2.5$ gives $\sqrt{n} = 12$. **12** stops at $\sqrt{n}$ without squaring.

**2. C** — Standard error 1.5, so $z = -1.87$. **0.378** uses $\sigma = 9$ instead of the standard error — the single commonest error in this material.

**3. B** — $2.0639 \times 7.5/5$. **15.48** forgets to divide by $\sqrt{n}$.

**4. D** — Only three levers exist: $n$, the confidence level, and $\sigma$.

**5. B** — The midpoint and half the width. **22.0 and 7.6** reports the full width as the margin.

**6. C** — $(2.5758 \times 12/1.5)^2 = 424.6$, rounded up. **246** uses the 95\% value of 1.96 instead of the 99\% value.

**7. D** — $2.4 > 2.086$. Note you never *accept* $H_0$ in any case.

**8. A** — The two routes always agree: beyond the critical value means $p < \alpha$.

**9. C** — 40 lies outside the interval, and the two are built from the same inequality.

**10. D** — $\mu$ is fixed; the interval is what was random. The confidence describes the procedure's track record.

**11. A** — A guarantee is tested from the side of whoever it protects — you need evidence it *fails*.

**12. B** — 2.5\% in each tail needs a cutoff further out than 5\% in a single tail.

**13. D** — Its probability is $\beta$, which you influence through $n$ rather than choose.

**14. A** — The two trade off; only a larger sample improves both.

**15. B** — Significance is a statement about $n$ as much as about the effect.

**16. C** — $20 \times 0.05$. Reporting only that one is p-hacking.

**17. B** — It is computed *assuming* $H_0$, so it cannot be a probability about $H_0$.

**18. C** — It is a statement about the sample mean, and only about the sample mean.

**19. D** — Households in a block are not independent, so 40 clustered households carry less information than 40 unrelated ones.

**20. A** — The direction must come from the question. Switching tails after seeing the statistic would be p-hacking — here the wording justified it all along.
