# Practice: Expectation and variance

Chapter 7. 7 multiple choice and 8 worked questions, all with solutions.

These are the Checkpoint 2 practice questions for this topic. Work them with the answers covered.

---

## Multiple choice

**1.** A help desk logs 0, 1, 2 or 3 escalations an hour with probabilities 0.15, 0.30, 0.35, 0.20. The expected number per hour is

(A) 1.30   (B) 2.00   (C) 1.60   (D) 1.50

**2.** For that same help desk, the variance of escalations per hour is

(A) 3.5000   (B) 2.5600   (C) 1.4400   (D) 0.9400

**3.** Each escalation costs \$90 to resolve and the desk carries \$200 of fixed hourly cost. Expected hourly cost is

(A) 344.00   (B) 144.00   (C) 434.00   (D) 201.60

**4.** For that same cost, the standard deviation is closest to

(A) 7614.00   (B) 0.97   (C) 84.60   (D) 87.26

**5.** A courier's daily profit has mean \$400 and variance 900. If a \$50 fixed fee is added to every day's profit, the new variance is

(A) 950   (B) 900   (C) 2500   (D) 1000

**6.** Two warehouses have daily cost variances 25 and 16, with covariance $-10$. The variance of their combined daily cost is

(A) 21   (B) 41   (C) 61   (D) 31

**7.** Two shops have sales variances 9 and 25, correlation 0.4. Their covariance is

(A) 3.6   (B) 6   (C) 90   (D) 0.4

## Worked questions

**1.** A machine produces 0, 1, 2 or 3 faults per shift with probabilities 0.15, 0.30, 0.35, 0.20. **(a)** Verify the distribution is valid. **(b)** Find $E(X)$. **(c)** Find $V(X)$ and $\sigma$.

**2.** Each fault costs \$80 to clear and the shift carries \$250 of fixed cost, so cost is $C = 80X + 250$ for the $X$ above. Find $E(C)$, $V(C)$ and $\sigma_C$.

**3.** $E(X) = 20$ and $E(X^2) = 449$. Find $V(X)$ and $\sigma$, then find $V(2X+7)$.

**4.** Two product lines have $V(X) = 36$, $V(Y) = 64$ and correlation $0.25$. **(a)** Find the covariance. **(b)** Find $V(X+Y)$. **(c)** What would $V(X+Y)$ be if the lines were uncorrelated, and what is the lesson?

**5.** A distribution has $\mathrm{P}(X{=}1){=}0.4$, $\mathrm{P}(X{=}2){=}0.35$ and $\mathrm{P}(X{=}3){=}k$. Find $k$, then $E(X)$ and $V(X)$.

**6.** Explain why the expected value of a random variable need not be a value the variable can take, giving an example.

**7.** Derive $V(X) = E(X^2) - \mu^2$ from the definition $V(X) = E[(X-\mu)^2]$.

**8.** $X$ has $E(X) = 5$, $V(X) = 9$. Find $E(X^2)$.

---

## Answers — multiple choice

**1. C** — A weighted sum. **1.50** is the unweighted average of 0,1,2,3, which ignores how likely each is.

**2. D** — $E(X^2) = 3.50$, so $V(X) = 3.50 - 1.60^2$. The distractors are $E(X^2)$ and $[E(X)]^2$ reported on their own.

**3. A** — $90E(X) + 200$. The first distractor drops the fixed cost.

**4. D** — $|a|\sigma = 90\sqrt{V(X)}$. The first distractor is the variance, un-rooted.

**5. B** — Adding a constant shifts the distribution without stretching it, so $V(X+b)=V(X)$.

**6. A** — $25+16+2(-10)$. **41** omits the covariance entirely.

**7. B** — $\rho\sigma_x\sigma_y = 0.4(3)(5)$. **3.6** multiplies by the variances rather than the standard deviations.


## Answers — worked questions

**1.** (a) All four lie in $[0,1]$ and sum to 1.00. (b) $E(X) = 1.60$. (c) $E(X^2) = 3.50$, so $V(X) = 0.9400$ and $\sigma = 0.9695$.

**2.** $E(C) = 80(1.60) + 250 = 378.00$. $V(C) = 80^2(0.9400) = 6016.00$, so $\sigma_C = 77.56$. The $+250$ shifts the mean and leaves the variance untouched.

**3.** $V(X) = 449 - 400 = 49$, so $\sigma = 7$. And $V(2X+7) = 4(49) = 196$.

**4.** (a) $0.25(6)(8) = 12$. (b) $36+64+2(12) = 124$. (c) It would be 100. Positive correlation adds 24 to the variance of the total for no extra return, which is the case for diversifying into things that do not move together.

**5.** $k = 0.25$. $E(X) = 0.4+0.7+0.75 = 1.85$. $E(X^2) = 0.4+1.4+2.25 = 4.05$, so $V(X) = 4.05 - 3.4225 = 0.6275$.

**6.** $E(X)$ is a balance point, a probability-weighted average, not an outcome. A die has $E(X) = 3.5$, which no face shows; a household can average 2.4 children.

**7.** Expand: $E[X^2 - 2\mu X + \mu^2] = E(X^2) - 2\mu E(X) + \mu^2$, using that expectation is linear and $\mu$ is a constant. Since $E(X) = \mu$, this is $E(X^2) - 2\mu^2 + \mu^2 = E(X^2) - \mu^2$.

**8.** Rearranging the shortcut, $E(X^2) = V(X) + \mu^2 = 9 + 25 = 34$.
