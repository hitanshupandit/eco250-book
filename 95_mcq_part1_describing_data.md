# Multiple choice: describing data

Chapters 1 to 4. Twenty questions, one answer each.

**These are hard on purpose.** Most take more than one step, and every wrong option is the number you get by making one specific mistake — dividing by $n$ instead of $n-1$, forgetting a square root, using $\sigma$ where $\sigma/\sqrt{n}$ belongs, inverting a conditional.

So if you pick a wrong answer, the key tells you **which mistake you made**, which is more use than the letter.

---

**1.** A sample of 12 values has $\sum x = 180$ and $\sum x^2 = 3000$. The sample standard deviation is closest to

(A) 4.77   (B) 5.00   (C) 5.22   (D) 27.27

**2.** Group A has 20 students averaging 68; group B has 30 averaging 78. The combined mean is

(A) 74.0   (B) 71.0   (C) 73.0   (D) 76.0

**3.** Fifteen values average 62. One value of 80 is removed. The new mean is closest to

(A) 58.80   (B) 61.80   (C) 63.29   (D) 60.71

**4.** $V(X) = 16$, $V(Y) = 25$ and the correlation is $0.6$. Then $V(X+Y)$ is

(A) 41   (B) 65   (C) 53   (D) 77

**5.** Student P scores 78 where the class mean is 70 and $s = 5$. Student Q scores 88 where the mean is 82 and $s = 4$. Relative to their classes,

(A) Q did better   (B) P did better   (C) they are identical   (D) cannot be compared

**6.** Every value of $x$ is doubled and every value of $y$ is tripled. The correlation $r$ is

(A) multiplied by 6   (B) multiplied by 2   (C) halved   (D) unchanged

**7.** A data set has $\bar x = 50$, $s = 10$. Every value is replaced by $3x - 20$. The new mean and standard deviation are

(A) 130 and 10   (B) 130 and 30   (C) 150 and 30   (D) 130 and 90

**8.** Bell-shaped data has mean 200 and $s = 25$. Roughly what percentage lies between 150 and 250?

(A) 68\%   (B) 99.7\%   (C) 95\%   (D) 50\%

**9.** For a sample, $\sum(x - \bar x)$ always equals

(A) $n\bar x$   (B) $s^2$   (C) it depends on the data   (D) 0

**10.** A scatterplot shows points tightly following a downward curve. The correlation is most likely

(A) close to $-1$   (B) moderately negative, but $r$ understates the relationship   (C) close to 0 because it is curved   (D) close to $+1$

**11.** Which pair of changes would leave the coefficient of variation unchanged?

(A) adding 4 to every value   (B) subtracting the mean from every value   (C) multiplying every value by 4   (D) squaring every value

**12.** Incomes in a town have mean \$62,000 and median \$48,000. A reporter writes that the typical resident earns \$62,000. The error is that

(A) the mean is inflated by a few very high incomes   (B) the median is the wrong statistic here   (C) the sample must be biased   (D) the mean and median should be averaged

**13.** $s_{xy} = 18$, $s_x^2 = 36$, $s_y^2 = 25$. Then $r$ is

(A) 0.72   (B) 0.60   (C) 0.02   (D) 0.36

**14.** A seventh value is added to the six values 4, 7, 9, 11, 14, 20, and the median does not change. That value could be

(A) 4   (B) 25   (C) 10   (D) any value at all

**15.** Two variables are strongly correlated. A third variable causes both. This is

(A) a confounded relationship   (B) reverse causation   (C) a sampling error   (D) a non-linear relationship

**16.** Removing the largest value from a right-skewed sample will

(A) lower the median more than the mean   (B) lower both equally   (C) leave the mean unchanged   (D) lower the mean more than the median

**17.** A variable is measured in dollars. Its variance is reported as 400. The units of that 400 are

(A) squared dollars   (B) dollars   (C) dollars per observation   (D) it has no units

**18.** Which is true of the interquartile range?

(A) it uses every observation   (B) it equals $2s$ for bell-shaped data   (C) it cannot be computed for skewed data   (D) it ignores the most extreme quarter at each end

**19.** A sample has $n = 5$ and deviations from the mean of $-4, -1, 0, 2$ and one unknown. The missing deviation is

(A) $-3$   (B) 0   (C) 3   (D) cannot be determined

**20.** Standardising a data set and then computing its skewness gives

(A) zero   (B) the same skewness as before   (C) a skewness of 1   (D) an undefined value

---

## Answers

**1. C** — $\sum(x-\bar x)^2 = 3000 - 180^2/12 = 300$, then divide by $n-1 = 11$ and take the root. **5.00** is what you get dividing by $n$; **27.27** is the variance, not the standard deviation.

**2. A** — A weighted mean: $(20 \times 68 + 30 \times 78)/50$. **73.0** is the unweighted average of 68 and 78, which ignores that B is the larger group.

**3. D** — Total was $15 \times 62 = 930$; remove 80 and divide by 14. **63.29** comes from adding 80 rather than removing it.

**4. B** — You must convert: $\mathrm{COV} = \rho\sigma_x\sigma_y = 0.6(4)(5) = 12$, then $16+25+2(12)$. **41** forgets the covariance term entirely; **53** uses $\rho$ in place of the covariance.

**5. A** — $z_P = 1.6$ and $z_Q = 1.5$ — so in fact **P** is further above. Choosing Q means comparing raw gaps, 8 against 6, instead of standardising.

**6. D** — The scale factors cancel between the numerator and $s_x s_y$. **Multiplied by 6** is what happens to the *covariance*.

**7. B** — $E(aX+b) = a\bar x + b$ and $\mathrm{SD}(aX+b) = |a|s$. **130 and 90** squares the multiplier, which is the rule for the *variance*, not the standard deviation.

**8. C** — 150 and 250 are $\mu \pm 2\sigma$. **68\%** is the one-sigma band, which is the answer if you forget to divide the gap of 50 by $\sigma = 25$.

**9. D** — The mean is the balance point, so positive and negative deviations cancel exactly. This is a free check on any deviation table.

**10. B** — $r$ measures *linear* association. A tight downward curve gives a clearly negative $r$, but one that understates how predictable $y$ actually is.

**11. C** — CV is $s/\bar x$, and multiplying scales both. **Adding 4** changes the mean but not $s$, so the ratio moves.

**12. A** — Right-skewed data pulls the mean towards the tail. The median is the better description of a typical resident.

**13. B** — $r = 18/(6 \times 5)$ — note you were given the **variances**, so take roots first. **0.02** divides by the variances instead of the standard deviations.

**14. C** — The median of the six is $(9+11)/2 = 10$. With seven values the median is the fourth, so it stays 10 only if the new value is exactly 10.

**15. A** — The classic third-variable case — ice cream sales and drowning, both driven by summer.

**16. D** — The mean uses the size of every observation; the median only its rank.

**17. A** — Which is exactly why we report $\sigma = \$20$ instead.

**18. D** — That insensitivity is precisely why it pairs with the median.

**19. C** — Deviations must sum to zero, so the fifth is $+3$. This is the free check from question 9, used in reverse.

**20. B** — Standardising shifts and rescales but does not reshape. **Zero** is what you would get only if standardising made things normal — it does not.
