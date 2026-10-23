# Practice: Sampling distributions and the CLT

Chapters 11 and 12. 9 multiple choice and 8 worked questions, all with solutions.

These are the Checkpoint 2 practice questions for this topic. Work them with the answers covered.

---

## Multiple choice

**1.** Weekly study hours have $\sigma = 24$. For a sample of 36 students the standard error of the mean is

(A) 24.0000   (B) 0.6667   (C) 4.0000   (D) 0.8165

**2.** If the true mean is 80 hours, the probability that a sample of 36 averages above 88 is closest to

(A) 0.3694   (B) 0.9772   (C) 0.5000   (D) 0.0228

**3.** How many students must be sampled for that standard error to fall to 2?

(A) 144   (B) 12   (C) 48   (D) 24

**4.** A market researcher quadruples her sample. The margin of error

(A) quarters   (B) halves   (C) stays the same   (D) falls by three quarters

**5.** Household incomes in a city are strongly right-skewed. For a sample of 50 households, which is approximately normal?

(A) a single household's income only   (B) both   (C) the sample mean income only   (D) neither

**6.** A factory's output per shift has $\sigma = 40$. A manager wants the standard error of mean output below 2.5. The smallest number of shifts is

(A) 16   (B) 64   (C) 1024   (D) 256

**7.** Claim sizes at an insurer have mean 60 and $\sigma = 15$. For 9 claims, the range containing the middle 95% of sample means is closest to

(A) (50.2, 69.8)   (B) (30.6, 89.4)   (C) (55.1, 64.9)   (D) (58.4, 61.6)

**8.** A pollster draws 300 people by selecting 60 households and interviewing every adult. The true standard error is

(A) equal to $\sigma/\sqrt{300}$   (B) larger than $\sigma/\sqrt{300}$   (C) smaller than $\sigma/\sqrt{300}$   (D) not defined

**9.** An agronomist averages yields from 4 plots drawn from a strongly skewed population. The distribution of that average is

(A) exactly normal   (B) approximately normal   (C) still noticeably skewed   (D) uniform

## Worked questions

**1.** A population has $\mu = 80$, $\sigma = 24$, and a sample of 36 is drawn. **(a)** State $E(\bar{X})$ and the standard error. **(b)** Find $\mathrm{P}(\bar{X} > 88)$. **(c)** Find $\mathrm{P}(76 < \bar{X} < 84)$.

**2.** For the population $\{3, 6, 9\}$, list all nine samples of size 2 drawn with replacement, and verify $E(\bar{X}) = \mu$ and $\mathrm{SD}(\bar{X}) = \sigma/\sqrt{2}$.

**3.** Explain why quadrupling the sample size only halves the standard error.

**4.** A skewed population is sampled at $n = 4$. Of 1{,}000 simulated means, 95.1% fall inside the nominal 95% interval, but the tails are 0.049 and 0.000. Explain why the headline figure is misleading.

**5.** Distinguish sampling error from non-sampling error, and say which a larger sample fixes.

**6.** State the three things the CLT tells you about $\bar{X}$, and which of them needs the theorem.

**7.** In Lab 6 we drew 1{,}000 samples of 36 from a population and found the standard deviation of the sample means close to $\sigma/6$. Explain what that simulation demonstrates and what it cannot demonstrate.

**8.** A population has $\mu = 450$, $\sigma = 60$. **(a)** For $n = 100$, find $\mathrm{P}(\bar{X} < 440)$. **(b)** Find $\mathrm{P}(X < 440)$ for one observation, or explain why you cannot.

---

## Answers — multiple choice

**1. C** — $\sigma/\sqrt{n}$. **0.6667** divides by $n$ rather than $\sqrt{n}$.

**2. D** — The first distractor uses $\sigma$ instead of the standard error — the commonest error in this material.

**3. A** — $\sigma/\sqrt{n}=2$ gives $\sqrt{n}=12$. **12** stops at $\sqrt{n}$.

**4. B** — It falls with $\sqrt{n}$.

**5. C** — The CLT is about $\bar{X}$. Sampling does not reshape the population.

**6. D** — $40/\sqrt{n}\le 2.5$ gives $\sqrt{n}\ge 16$. **16** stops at $\sqrt{n}$.

**7. A** — SE $= 5$, so $60 \pm 1.96(5)$. **(30.6, 89.4)** uses $\sigma = 15$ instead of the standard error.

**8. B** — People in a household are not independent draws, so 300 clustered people carry less information than 300 unrelated ones.

**9. C** — At $n = 4$ the CLT has barely begun. Convergence depends on how far the population starts from normal.


## Answers — worked questions

**1.** (a) $E(\bar{X}) = 80$, $\sigma_{\bar{X}} = 4$. (b) $z = 2.00$, so $0.0228$. (c) $z = \mp 1$, so $0.6827$.

**2.** $\mu = 6$, $\sigma^2 = 6$, $\sigma = 2.4495$. The nine means are 3, 4.5, 6, 4.5, 6, 7.5, 6, 7.5, 9 — so $\bar{x} = 3, 4.5, 6, 7.5, 9$ with probabilities $1/9, 2/9, 3/9, 2/9, 1/9$. Then $E(\bar{X}) = 6 = \mu$ and $V(\bar{X}) = 3$, so $\mathrm{SD}(\bar{X}) = 1.7321 = 2.4495/\sqrt{2}$.

**3.** The standard error depends on $\sqrt{n}$. Averaging cancels independent errors, but each new observation adds less than the one before, so precision accumulates at the rate $\sqrt{n}$ rather than $n$.

**4.** The two tails are wrong in opposite directions and the errors cancel in the total. A two-sided statement survives by luck; any one-tailed probability would be badly wrong — the lower tail is about double what it should be and the upper tail is empty.

**5.** Sampling error is $\bar{x} - \mu$, arising because you measured a sample; it is random and shrinks as $n$ grows. Non-sampling error is mistyped data, leading questions, non-response; it is often systematic and does not shrink with $n$. A bigger sample fixes only the first.

**6.** Centre $E(\bar{X}) = \mu$; spread $\sigma/\sqrt{n}$; shape approximately normal. The first two follow from the rules for expectation and variance and hold for any population. Only the third needs the CLT.

**7.** It demonstrates the *spread* result, $\mathrm{SD}(\bar X) = \sigma/\sqrt{n}$, which holds for any population. It cannot by itself demonstrate the CLT's *shape* claim — for that you must look at the histogram of the means and check it is bell-shaped, not merely narrow.

**8.** (a) SE $= 6$, so $z = -1.6667$ and $\mathrm{P} = 0.0478$. (b) You cannot, unless the population is normal. The CLT licenses a statement about $\bar{X}$ only; a probability for a single observation needs the population's own shape, which was not given.
