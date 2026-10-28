# Practice: The binomial

Chapter 8. 7 multiple choice and 8 worked questions, all with solutions.

These are the Checkpoint 2 practice questions for this topic. Work them with the answers covered.

---

## Multiple choice

**1.** 20% of parcels are flagged for inspection. In 15 processed independently, the probability exactly 3 are flagged is closest to

(A) 0.2501   (B) 0.2001   (C) 0.3101   (D) 0.2000

**2.** For those 15 parcels, the expected number flagged and the standard deviation are

(A) 3.0 and 2.4   (B) 2.4 and 1.5492   (C) 3.0 and 1.5492   (D) 3.0 and 1.7321

**3.** Each of 10 invoices is independently queried with probability 0.12. The probability at least one is queried is closest to

(A) 0.2785   (B) 0.7215   (C) 0.1200   (D) 0.8800

**4.** Of those 15 parcels, the probability that at most one is flagged is closest to

(A) 0.8329   (B) 0.0836   (C) 0.0352   (D) 0.1671

**5.** An auditor samples 6 invoices from a folder of 30 and counts errors. The binomial is inappropriate here because

(A) sampling without replacement changes $p$ between draws   (B) there are more than two outcomes   (C) the number sampled is not fixed   (D) the invoices are not random

**6.** A call centre answers 6% of calls within 10 seconds. For a sample of 60 calls, a normal approximation to the count is

(A) inappropriate, because $np < 5$   (B) appropriate, because $n > 30$   (C) appropriate, because $n(1-p) > 5$   (D) inappropriate, because $p$ is small

**7.** A seed supplier claims half of all seeds germinate. In a tray of $n$ seeds the standard deviation of the number germinating is 4. Then $n$ is

(A) 16   (B) 32   (C) 8   (D) 64

## Worked questions

**1.** 20% of parcels are flagged. 15 are processed independently. **(a)** State and check the four binomial conditions. **(b)** Find $\mathrm{P}(X=3)$. **(c)** Find $E(X)$ and $\sigma$.

**2.** Explain why 'at least one' questions are easier through the complement, using 8 independent trials each succeeding with probability 0.1.

**3.** A quality scheme rejects a batch if 2 or more of 12 sampled items are defective. If the true defect rate is 0.1, find the probability a batch is rejected.

**4.** A binomial has $E(X) = 12$ and $V(X) = 8.4$. Find $n$ and $p$.

**5.** Explain, with reference to the Bernoulli trial, why $E(X) = np$ for a binomial.

**6.** For $X \sim \mathrm{Bin}(25, 0.4)$, check whether the normal approximation applies, and if so give the approximating normal.

**7.** Lecture 6 showed a binomial at $p = 0.3$ approaching the normal as $n$ grew from 5 to 60. State the condition for using that approximation and check it at $n = 12$ and at $n = 60$.

**8.** A batch of 20 items has each independently defective with probability 0.15. **(a)** Find the expected number and the standard deviation. **(b)** Find the probability that none is defective. **(c)** Explain why $\mathrm{P}(X \ge 1)$ is easier through (b).

---

## Answers — multiple choice

**1. A** — $\binom{15}{3}(0.2)^3(0.8)^{12}$.

**2. C** — $np$ and $\sqrt{np(1-p)}$. The first distractor reports the variance as the standard deviation.

**3. B** — $1 - (0.88)^{10}$. **0.2785** is the probability that none is.

**4. D** — $\mathrm{P}(0)+\mathrm{P}(1)$. **0.8329** is the complement.

**5. A** — 6 of 30 is a large fraction of the folder, so the probability shifts materially as invoices are removed.

**6. A** — $np = 3.6$. Both $np$ and $n(1-p)$ must clear 5.

**7. D** — $0.25n = 16$. **16** stops at the variance.


## Answers — worked questions

**1.** (a) Fixed $n = 15$; two outcomes; constant $p = 0.2$; independent. (b) $\binom{15}{3}(0.2)^3(0.8)^{12} = 0.2501$. (c) $E(X) = 3$, $\sigma = 1.5492$.

**2.** Directly it needs the eight terms $X = 1, \ldots, 8$. The complement needs one: $1 - (0.9)^8 = 0.5695$.

**3.** $1 - \mathrm{P}(0) - \mathrm{P}(1) = 1 - (0.9)^{12} - 12(0.1)(0.9)^{11} = 0.3410$.

**4.** $np = 12$ and $np(1-p) = 8.4$, so $1-p = 8.4/12 = 0.7$, giving $p = 0.3$ and $n = 40$.

**5.** A binomial is the sum of $n$ independent Bernoulli trials, each with expectation $p$. Expectation is linear, so the sum of $n$ copies of $p$ is $np$.

**6.** $np = 10$ and $n(1-p) = 15$, both above 5, so it applies. The approximation is $N(10, 6)$ — mean $np = 10$ and variance $np(1-p) = 6$, so $\sigma = 2.4495$.

**7.** The condition is $np \ge 5$ and $n(1-p) \ge 5$. At $n = 12$: $np = 3.6$, which fails, so use the exact binomial. At $n = 60$: $np = 18$ and $n(1-p) = 42$, both clear, so the approximation is sound.

**8.** (a) $E(X) = 3$, $\sigma = \sqrt{20(0.15)(0.85)} = 1.5969$. (b) $(0.85)^{20} = 0.0388$. (c) 'At least one' spans twenty separate terms; its complement is the single case $X = 0$, so one calculation replaces twenty.
