# Multiple choice: distributions

Chapters 8 to 10. Twenty questions, one answer each.

**These are hard on purpose.** Most take more than one step, and every wrong option is the number you get by making one specific mistake — dividing by $n$ instead of $n-1$, forgetting a square root, using $\sigma$ where $\sigma/\sqrt{n}$ belongs, inverting a conditional.

So if you pick a wrong answer, the key tells you **which mistake you made**, which is more use than the letter.

---

**1.** $X \sim \mathrm{Bin}(6, 0.2)$. Then $\mathrm{P}(X \ge 2)$ is closest to

(A) 0.246   (B) 0.262   (C) 0.655   (D) 0.345

**2.** $X \sim \mathrm{Bin}(20, 0.4)$. Its standard deviation is

(A) 4.80   (B) 2.19   (C) 8.00   (D) 3.10

**3.** A binomial has $n = 50$, $p = 0.08$. The normal approximation is

(A) appropriate, because $n > 30$   (B) appropriate, because $n(1-p) > 5$   (C) inappropriate, because $np < 5$   (D) inappropriate, because $p < 0.5$

**4.** Twelve items are drawn *without replacement* from a batch of 30, and defectives counted. The binomial is

(A) not appropriate, because $p$ changes between draws   (B) appropriate, because the draws are random   (C) appropriate, because there are two outcomes   (D) not appropriate, because $n$ is too small

**5.** $X \sim N(500, 80^2)$. The value below which 25\% of the distribution falls is closest to

(A) 420   (B) 480   (C) 446   (D) 554

**6.** For that same distribution, $\mathrm{P}(420 < X < 620)$ is closest to

(A) 0.841   (B) 0.775   (C) 0.933   (D) 0.593

**7.** Waiting time is exponential with mean 8 minutes. $\mathrm{P}(X > 10)$ is closest to

(A) 0.287   (B) 0.125   (C) 0.713   (D) 0.800

**8.** For that same exponential, the standard deviation is

(A) $\sqrt{8}$   (B) 64   (C) 4   (D) 8

**9.** $X$ is uniform on $[10, 50]$. Its standard deviation is closest to

(A) 20.00   (B) 11.55   (C) 13.33   (D) 6.67

**10.** For a continuous variable, which is NOT true?

(A) $\mathrm{P}(X = a)$ is a small positive number   (B) $\mathrm{P}(X = a) = 0$   (C) $\mathrm{P}(X < a) = \mathrm{P}(X \le a)$   (D) the density can exceed 1

**11.** $t_{0.05,\,12}$ compared with $t_{0.05,\,30}$ is

(A) smaller   (B) equal   (C) larger only if $n < 10$   (D) larger

**12.** A $\chi^2$ distribution with 1 degree of freedom is

(A) symmetric about 1   (B) bell-shaped   (C) right-skewed and bounded below by zero   (D) bounded above by 1

**13.** $F_{0.05,\,8,\,20}$ and $F_{0.05,\,20,\,8}$ are

(A) different values   (B) the same value   (C) reciprocals   (D) the same only at $\alpha = 0.05$

**14.** In Stata, `ttail(20, 2.086)` returns approximately

(A) 0.95   (B) 2.086   (C) 0.05   (D) 0.025

**15.** Which is the inverse of Stata's `invchi2(10, 0.95)`?

(A) `invchi2(10, 0.05)`   (B) `chi2(10, 0.95)`   (C) `chi2tail(10, 18.307)`   (D) `chi2tail(10, 0.95)`

**16.** A standardised binomial approaches the normal as $n$ grows because

(A) the binomial formula simplifies   (B) a binomial is a sum of independent Bernoulli trials   (C) $p$ approaches 0.5   (D) the variance approaches 1

**17.** $X \sim N(\mu, \sigma^2)$. The distribution of $(X - \mu)/\sigma$ is

(A) $N(\mu, 1)$   (B) $N(0, \sigma)$   (C) $N(0, 1)$   (D) $t$ with $n-1$ df

**18.** For a $t$ distribution, as $\nu \to \infty$ the critical value $t_{0.025,\nu}$ approaches

(A) 1.645   (B) 1.960   (C) 2.000   (D) 0

**19.** Which requires exactly one parameter?

(A) the exponential   (B) the normal   (C) the binomial   (D) the uniform

**20.** A density curve reaches a height of 2.5 at its peak. This

(A) is impossible, since probabilities cannot exceed 1   (B) means the variable is discrete   (C) means the curve is mis-scaled   (D) is possible, since only the area must equal 1

---

## Answers

**1. D** — $1 - \mathrm{P}(0) - \mathrm{P}(1)$. **0.655** is $\mathrm{P}(X \le 1)$, the complement — taken without subtracting from 1.

**2. B** — $\sqrt{20(0.4)(0.6)} = \sqrt{4.8}$. **4.80** is the variance, left un-rooted.

**3. C** — $np = 4$. Both $np$ and $n(1-p)$ must clear 5; here only one does.

**4. A** — 12 of 30 is a large fraction of the batch, so the probability shifts materially as items are removed.

**5. C** — $z = -0.6745$, so $500 - 0.6745(80)$. **554** uses $+0.6745$ and finds the 75th percentile instead.

**6. B** — $z = -1.00$ and $z = +1.50$, so $0.9332 - 0.1587$. **0.933** forgets to subtract the lower tail.

**7. A** — $e^{-10/8}$. **0.713** is $\mathrm{P}(X < 10)$, the complement.

**8. D** — For an exponential, $\sigma = \mu$ — unusual, and worth remembering.

**9. B** — $(b-a)/\sqrt{12} = 40/3.4641$. **20.00** is half the range, which is not the standard deviation of anything here.

**10. A** — Exactly zero, not merely small — which is why strict and weak inequalities agree.

**11. D** — Fewer degrees of freedom means fatter tails, so the cutoff sits further out.

**12. C** — It is a single squared standard normal, so it cannot be negative and its upper tail stretches.

**13. A** — $F$ is a ratio, so swapping the degrees of freedom asks a different question — 3.33 against 2.45 in this case.

**14. D** — `ttail` is cutoff-to-area and gives the upper tail. **0.05** would be the two-tailed total.

**15. C** — `invchi2` takes an area and returns a cutoff; `chi2tail` takes a cutoff and returns an area.

**16. B** — Sums of many independent things go normal — the CLT, applied to a count.

**17. C** — Standardising always produces mean 0 and standard deviation 1. It becomes $t$ only when $\sigma$ is replaced by an estimate.

**18. B** — The normal's two-tailed 5\% value. **1.645** is the *one*-tailed figure.

**19. A** — The others each take two: $(\mu,\sigma)$, $(n,p)$ and $(a,b)$.

**20. D** — A uniform on $[0, 0.4]$ has height 2.5 throughout.
