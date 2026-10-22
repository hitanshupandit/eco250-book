# Multiple choice: chance

Chapters 5 to 7. Twenty questions, one answer each.

**These are hard on purpose.** Most take more than one step, and every wrong option is the number you get by making one specific mistake — dividing by $n$ instead of $n-1$, forgetting a square root, using $\sigma$ where $\sigma/\sqrt{n}$ belongs, inverting a conditional.

So if you pick a wrong answer, the key tells you **which mistake you made**, which is more use than the letter.

---

**1.** A plant takes 55\% of parts from A (4\% defective) and 45\% from B (10\% defective). A part fails inspection. The probability it came from B is closest to

(A) 0.450   (B) 0.672   (C) 0.100   (D) 0.328

**2.** $\mathrm{P}(A) = 0.6$, $\mathrm{P}(B) = 0.5$, $\mathrm{P}(A \cup B) = 0.8$. Then $\mathrm{P}(A \cap B)$ is

(A) 0.1   (B) 0.2   (C) 1.1   (D) 0.3

**3.** For those same events, $\mathrm{P}(A \mid B)$ is

(A) 0.60   (B) 0.375   (C) 0.50   (D) 0.30

**4.** Given those numbers, $A$ and $B$ are

(A) mutually exclusive   (B) dependent   (C) independent   (D) complementary

**5.** A test is 95\% sensitive and 90\% specific for a condition affecting 2\% of people. The probability that a positive result is correct is closest to

(A) 0.950   (B) 0.900   (C) 0.020   (D) 0.162

**6.** Eight components each work independently with probability 0.9. The probability that at least one fails is closest to

(A) 0.570   (B) 0.100   (C) 0.430   (D) 0.800

**7.** Events $A$ and $B$ are mutually exclusive, with $\mathrm{P}(A) = 0.3$ and $\mathrm{P}(B) = 0.4$. Then $\mathrm{P}(A \mid B)$ is

(A) 0.12   (B) 0.30   (C) 0   (D) 0.75

**8.** For $x = 1, 2, 3$ with probabilities $0.5, 0.3, 0.2$, $V(X)$ is

(A) 0.78   (B) 0.61   (C) 1.70   (D) 2.90

**9.** For that same variable, $E(X^2)$ equals

(A) 3.5   (B) 2.89   (C) 1.70   (D) 0.61

**10.** If $E(X) = 10$, $V(X) = 4$, then $\mathrm{SD}(3X + 5)$ is

(A) 12   (B) 36   (C) 6   (D) 41

**11.** Two assets have $V(X) = 9$, $V(Y) = 16$, $\rho = -0.5$. The variance of their total is

(A) 25   (B) 13   (C) 37   (D) 7

**12.** A bag has 4 red and 6 blue. Two are drawn without replacement. The probability both are red is

(A) 4/25   (B) 1/6   (C) 8/45   (D) 2/15

**13.** $\mathrm{P}(A) = 0.4$ and $\mathrm{P}(B \mid A) = 0.25$. Then $\mathrm{P}(A \cap B)$ is

(A) 0.65   (B) 0.16   (C) 0.10   (D) 0.625

**14.** From the information in the previous question, $\mathrm{P}(B)$ is

(A) 0.10   (B) not determinable   (C) 0.25   (D) 0.625

**15.** A random variable has $E(X) = 0$ and $V(X) = 0$. Then $X$

(A) is impossible   (B) is uniform   (C) has an undefined distribution   (D) is a constant equal to 0

**16.** Which statement is true?

(A) mutually exclusive events with positive probability are always dependent   (B) mutually exclusive events are always independent   (C) independent events are always mutually exclusive   (D) independence and mutual exclusivity are the same

**17.** A fair coin is tossed 6 times and lands heads every time. The probability the next toss is heads is

(A) less than 0.5   (B) greater than 0.5   (C) cannot be determined   (D) 0.5

**18.** $E(X) = 5$ and $E(Y) = 3$, and $X$ and $Y$ are dependent. Then $E(X + Y)$ is

(A) 8   (B) 8 only if they are independent   (C) cannot be determined   (D) 15

**19.** A probability distribution lists $0.3, 0.3, 0.3$ for three outcomes. It is

(A) valid   (B) invalid, because the probabilities sum to 0.9   (C) invalid, because they are equal   (D) valid only if a fourth outcome exists

**20.** $\mathrm{P}(\text{rain} \mid \text{clouds})$ compared with $\mathrm{P}(\text{clouds} \mid \text{rain})$ is

(A) larger   (B) equal   (C) smaller   (D) unrelated

---

## Answers

**1. B** — $\mathrm{P}(D) = 0.067$, then $(0.45)(0.10)/0.067$. **0.450** is the prior — the answer if you ignore the evidence; **0.100** is the likelihood, a different conditional entirely.

**2. D** — Rearrange the addition rule: $0.6 + 0.5 - 0.8$. **1.1** adds instead of subtracting.

**3. A** — $0.3/0.5$. **0.375** inverts the conditional and computes $\mathrm{P}(B \mid A) = 0.3/0.8$ using the wrong denominator.

**4. C** — $\mathrm{P}(A\mid B) = 0.6 = \mathrm{P}(A)$. Equivalently $0.6 \times 0.5 = 0.3$, matching the joint probability.

**5. D** — $\mathrm{P}(+) = (0.02)(0.95) + (0.98)(0.10) = 0.117$, so $0.019/0.117$. **0.950** is the sensitivity — a different conditional, and the error this question exists to catch.

**6. A** — $1 - 0.9^8$. **0.430** computes $0.9^8$ itself, which is the probability that *none* fails.

**7. C** — If $B$ happened, $A$ cannot have. **0.12** multiplies them as though they were independent — which mutually exclusive events never are.

**8. B** — $E(X) = 1.7$ and $E(X^2) = 3.5$, so $3.5 - 2.89$. **1.70** is the mean; **2.90** is $[E(X)]^2$.

**9. A** — $1(0.5) + 4(0.3) + 9(0.2)$. **2.89** is $[E(X)]^2$, and the gap between them is the variance.

**10. C** — $|a|\sigma = 3 \times 2$. **36** is the *variance* $a^2V(X)$; **41** has added the constant, which affects the mean and not the spread.

**11. B** — $\mathrm{COV} = -0.5(3)(4) = -6$, so $9+16+2(-6)$. **25** forgets the covariance; negative correlation is what makes the total *less* volatile than the parts.

**12. D** — $\frac{4}{10} \times \frac{3}{9}$. **4/25** is $(4/10)^2$, which treats the draws as independent — they are not, because the first draw changes the bag.

**13. C** — $\mathrm{P}(A)\mathrm{P}(B\mid A)$. **0.625** divides instead of multiplying.

**14. B** — You have only the route to $B$ through $A$. You would also need $\mathrm{P}(B \mid A^c)$ to complete the total probability.

**15. D** — Zero variance means no spread at all, so the variable never departs from its mean.

**16. A** — They are near-opposites: knowing one mutually exclusive event occurred tells you the other definitely did not.

**17. D** — The tosses are independent; the coin has no memory. Expecting a tail is the gambler's fallacy.

**18. A** — Expectation is linear whether or not the variables are independent. It is the *variance* that needs the covariance term.

**19. B** — They must sum to exactly 1. Checking this before computing anything is often worth a mark.

**20. C** — It almost always rains from cloud, so the second is near 1; cloudy days often stay dry, so the first is well below it.
