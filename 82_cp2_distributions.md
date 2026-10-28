# Practice: Continuous distributions

Chapter 9 — uniform, normal and exponential. 12 multiple choice and 8 worked questions, all with solutions.

These are the Checkpoint 2 practice questions for this topic. Work them with the answers covered.

---

## Multiple choice

**1.** A form takes between 8 and 32 minutes to process, any duration equally likely. The mean and standard deviation are

(A) 20 and 6.9282   (B) 20 and 12.0   (C) 12.0 and 6.9282   (D) 20 and 9.7980

**2.** For that same form, the probability it takes less than 17 minutes is

(A) 0.6250   (B) 0.2500   (C) 0.3750   (D) 0.7083

**3.** For that same form, the probability it takes between 12 and 24 minutes is

(A) 0.3750   (B) 0.2500   (C) 0.5000   (D) 0.6667

**4.** Time between arrivals at a counter is exponential with mean 6 minutes. The probability of waiting more than 9 minutes is

(A) 0.2231   (B) 0.7769   (C) 0.1500   (D) 0.6667

**5.** For those same arrivals, the standard deviation of the waiting time is

(A) 2.4495 minutes   (B) 36 minutes   (C) 6 minutes   (D) 1 minute

**6.** Monthly electricity use is normal with mean 340 kWh and standard deviation 45. The fraction of households using more than 400 kWh is

(A) 0.9088   (B) 0.1824   (C) 0.5000   (D) 0.0912

**7.** For those same households, the fraction using between 280 and 400 kWh is

(A) 0.8176   (B) 0.9088   (C) 0.0912   (D) 0.6827

**8.** The utility wants to contact the heaviest-using 2.5% of households. The threshold is closest to

(A) 414.02   (B) 251.80   (C) 397.67   (D) 428.20

**9.** Packed cartons weigh normally with mean 500 g and standard deviation 8 g. The fraction below 486 g is closest to

(A) 0.9599   (B) 0.0500   (C) 0.1587   (D) 0.0401

**10.** For those same cartons, 90% weigh more than

(A) 510.25   (B) 489.75   (C) 486.84   (D) 484.32

**11.** Exam scores are normal with mean 68, standard deviation 12. A student scores 86. Their $z$-score and rough percentile are

(A) 1.50 and the 85th   (B) 1.50 and the 93rd   (C) 18.0 and the 93rd   (D) 0.67 and the 75th

**12.** Component lifetimes are normal with mean 1{,}200 hours, standard deviation 150. A warranty is set so that only 5% fail within it. The warranty is

(A) 953.27   (B) 906.01   (C) 1446.73   (D) 1007.77

## Worked questions

**1.** Monthly spend is normal with $\mu = 340$, $\sigma = 45$. **(a)** Find the fraction above 400. **(b)** Find the fraction between 280 and 400. **(c)** Find the 90th percentile.

**2.** Processing times are uniform on $[8, 32]$ minutes. Find the mean, the standard deviation, and $\mathrm{P}(12 < X < 24)$.

**3.** Time between faults is exponential with mean 6 days. **(a)** Find $\mathrm{P}(X > 9)$. **(b)** Find $\mathrm{P}(X < 3)$. **(c)** State the standard deviation.

**4.** A student writes $\mathrm{P}(X = 40) = 0.02$ for a continuous variable. Explain what is wrong and what they probably meant.

**5.** Scores are normal with $\mu = 68$, $\sigma = 12$. A scholarship goes to the top 5%. Find the cut-off, and state the $z$ you used.

**6.** Explain why standardising a skewed variable does not make it normal.

**7.** $X \sim N(340, 45^2)$. Find the interquartile range.

**8.** Lab 5 standardised a right-skewed wage variable and found the minimum and maximum $z$ unchanged in rank. Explain what standardising did and did not do, and why a histogram of $z$ still looked skewed.

---

## Answers — multiple choice

**1. A** — Midpoint, and $(b-a)/\sqrt{12}$. **12.0** is half the range, which is not a standard deviation.

**2. C** — The fraction of the interval below 17: $9/24$. **0.6250** is the complement.

**3. C** — $12/24$ of the interval.

**4. A** — $e^{-9/6}$. **0.7769** is the complement.

**5. C** — For an exponential the standard deviation equals the mean — unusual, and worth remembering.

**6. D** — $z = 1.3333$, then the upper tail. **0.9088** is the area to the left.

**7. A** — Subtract the two cumulative areas. The first distractor forgets the lower tail.

**8. D** — $z = 1.959964$. The first distractor uses the one-tailed 5% value.

**9. D** — $z = -1.7500$, lower tail.

**10. B** — 90% above means 10% below, so $z = -1.2816$. The first distractor finds the value 90% lie *below*.

**11. B** — $z = (86-68)/12$, and $\Phi(1.5) = 0.9332$. **18.0** is the raw gap, not standardised.

**12. A** — 5% below means $z = -1.6449$. The second distractor goes the wrong way and would cover 95% of failures.


## Answers — worked questions

**1.** (a) $z = 1.3333$, so $0.0912$. (b) $0.8176$. (c) $z = 1.281552$, so $340 + 1.281552(45) = 397.67$.

**2.** $\mu = 20$; $\sigma = 6.9282$; $\mathrm{P} = 12/24 = 0.5000$.

**3.** (a) $e^{-1.5} = 0.2231$. (b) $1 - e^{-0.5} = 0.3935$. (c) 6 days — for an exponential, $\sigma = \mu$.

**4.** For a continuous variable the probability of any exact value is zero. They have most likely computed the density at 40 — a height, not a probability — or they meant an interval such as $\mathrm{P}(39.5 < X < 40.5)$.

**5.** $z = 1.644854$, so $68 + 1.644854(12) = 87.74$.

**6.** Standardising subtracts a constant and divides by a constant. Both are linear operations: they move the centre to 0 and the spread to 1, but they cannot reorder or reshape the values, so the skewness is unchanged.

**7.** $Q_1$ and $Q_3$ are at $z = \mp 0.6745$, so $Q_3 - Q_1 = 2(0.6745)(45) = 60.70$.

**8.** It subtracted the mean and divided by $s$, moving the centre to 0 and the spread to 1. Both are linear, so no value can overtake another and the shape is preserved exactly — the skewness is identical before and after. Standardising is not a route to normality.
