# Practice: chance

Chapters 5 to 7 — the probability rules, conditional probability and Bayes, random variables.

Fifteen problems. Work them with the solutions covered — reading a worked answer and producing one are different skills, and only the second is any use with a clock running.

Keep **four decimal places** unless a question says otherwise.

---

**1.** Events $A$ and $B$ have $\mathrm{P}(A) = 0.48$,
$\mathrm{P}(B) = 0.36$ and $\mathrm{P}(A \cap B) = 0.18$.

(a) Find $\mathrm{P}(A \cup B)$.
(b) Find the probability neither occurs.
(c) Find $\mathrm{P}(A \mid B)$.
(d) Are $A$ and $B$ independent?

**2.** A courier classifies 700 deliveries by outcome and customer type:

| | New | Existing | Total |
|---|---|---|---|
| On time | 210 | 330 | 540 |
| Late | 90 | 70 | 160 |
| Total | 300 | 400 | 700 |

(a) $\mathrm{P}(\text{on time})$?
(b) $\mathrm{P}(\text{on time and new})$?
(c) $\mathrm{P}(\text{on time} \mid \text{new})$?
(d) Are "on time" and "new customer" independent?

**3.** A manufacturer sources from three plants. Ashford supplies 45\% with a 4\% defect
rate; Benton 35\% with 6\%; Calder 20\% with 9\%.

(a) What fraction of all units are defective?
(b) A defective unit is found. Which plant most probably made it?
(c) Calder supplies the least. Why is it still a serious suspect?

**4.** A screening test is 97% sensitive and 94% specific. The
condition affects 0.5% of the population. You test positive.

(a) What fraction of all tests come back positive?
(b) What is the probability you actually have the condition?
(c) Explain the result to someone who expected about 97\%.

**5.** A machine produces items independently, each defective with probability 0.03.
Eight are drawn.

(a) Find the probability none is defective.
(b) Find the probability at least one is.
(c) Why is the complement the efficient route?

**6.** Explain, without formulas, why two mutually exclusive events with non-zero
probability can never be independent.

**7.** A random variable $X$ has this distribution:

| $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $\mathrm{P}(X=x)$ | 0.08 | 0.22 | 0.34 | 0.26 | 0.1 |

(a) Verify it is valid.
(b) Find $E(X)$.
(c) Find $V(X)$ and $\sigma$.

**8.** Using the variable above, a firm's daily cost is $C = 35X + 120$.

(a) Find $E(C)$.
(b) Find $V(C)$ and $\sigma_C$.
(c) Fixed costs rise to 200. What changes?

**9.** $\mathrm{P}(A) = 0.35$ and $\mathrm{P}(B \mid A) = 0.70$.

(a) Find $\mathrm{P}(A \cap B)$.
(b) Can you find $\mathrm{P}(B)$? Explain.
(c) What one further piece of information would let you?

**10.** Explain the difference between $\mathrm{P}(A \mid B)$ and $\mathrm{P}(B \mid A)$,
using an example of your own, and say why confusing them matters.

**11.** $E(X) = 12$ and $E(X^2) = 169$.

(a) Find $V(X)$ and $\sigma$.
(b) Find $V(4X - 7)$.
(c) Find $E(4X - 7)$.

**12.** Of 240 applicants, 150 have a degree, 90 have relevant experience, and 60 have
both.

(a) How many have neither?
(b) What is the probability a random applicant has a degree or experience?
(c) Are "degree" and "experience" independent?

**13.** A distribution has $\mathrm{P}(X=1) = 0.3$, $\mathrm{P}(X=2) = 0.45$ and
$\mathrm{P}(X=3) = k$.

(a) Find $k$.
(b) Find $E(X)$.
(c) Find $V(X)$.

**14.** Two assets have $V(X) = 81$, $V(Y) = 144$ and correlation $\rho = 0.5$.

(a) Find $\text{COV}(X,Y)$.
(b) Find $V(X+Y)$.
(c) What would $V(X+Y)$ be if the assets were uncorrelated, and what is the lesson?

**15.** A student writes: "the probability of drawing two aces from a deck is
$(4/52)^2$."

(a) What has gone wrong?
(b) Give the correct calculation.
(c) When would the student's version be right?

---

# Solutions

**1.** (a) $0.48 + 0.36 - 0.18 = 0.66$.
(b) $1 - 0.66 = 0.34$.
(c) $0.18/0.36 = 0.50$.
(d) $\mathrm{P}(A)\mathrm{P}(B) = 0.48 \times 0.36 =
0.1728$, which is **not** 0.18. Not independent. (Equivalently
$\mathrm{P}(A \mid B) = 0.50 \neq 0.48$.)

**2.** (a) $540/700 = 0.7714$.
(b) $210/700 = 0.3000$.
(c) Shrink to the new-customer column: $210/300 = 0.70$.
(d) $\mathrm{P}(\text{on time}) = 0.7714$ but
$\mathrm{P}(\text{on time} \mid \text{new}) = 0.70$. Knowing the
customer is new changes the probability, so **not independent** — new customers are
served late more often.

**3.** (a) $(0.45)(0.04) + (0.35)(0.06) + (0.20)(0.09) = 0.018 + 0.021 + 0.018
= 0.0570$.
(b) Posteriors: Ashford $0.3158$, Benton
$0.3684$, Calder $0.3158$. **Benton** is the
most likely source.
(c) Because what matters is share **times** rate. Calder's 9\% defect rate on a 20\%
share produces as many defects as Ashford's 4\% on 45\% — its small share is offset by
the worst quality.

**4.** (a) $(0.005)(0.97) + (0.995)(0.06)
= 0.00485 + 0.05970
= 0.0646$.
(b) $0.00485/0.0646 = 0.0751$ — about
**7.5%**.
(c) The healthy group is roughly 200 times larger than the sick group, so even a
6% false-positive rate on it produces far more positives than a
97% true-positive rate on the tiny sick group. The test is good; the
**base rate** does the damage. A positive is a reason for a second, more specific
test — not a diagnosis.

**5.** (a) $(0.97)^8 = 0.7837$.
(b) $1 - 0.7837 = 0.2163$.
(c) "At least one" covers the eight separate cases $X = 1, \ldots, 8$, each needing its
own term. Its complement is the single case $X = 0$.

**6.** If they are mutually exclusive and you learn one happened, you know immediately
that the other did not — its probability collapses to zero. Learning something that
changes the other's probability that drastically is the exact opposite of
"tells you nothing", which is what independence requires.

**7.** (a) All five lie in $[0,1]$ and sum to 1.00.
(b) $E(X) = 2.08$.
(c) $E(X^2) = 5.52$, so $V(X) = 5.52 - 2.08^2
= 1.1936$ and $\sigma = 1.0925$.

**8.** (a) $35(2.08) + 120 = 192.80$.
(b) $V(C) = 35^2(1.1936) = 1462.16$, so
$\sigma_C = 38.2382$.
(c) $E(C)$ rises by 80 to $272.80$. $V(C)$ does **not** change — a
constant shifts the distribution without stretching it.

**9.** (a) $\mathrm{P}(A \cap B) = (0.35)(0.70) = 0.245$.
(b) No. $\mathrm{P}(B)$ needs both routes to $B$, and you have only the one through $A$.
(c) $\mathrm{P}(B \mid A^c)$ — then
$\mathrm{P}(B) = 0.245 + (0.65)\mathrm{P}(B \mid A^c)$.

**10.** Any sound example. One: the probability that a road is wet given that it rained is
near 1; the probability that it rained given that the road is wet is much lower, because
sprinklers, street cleaning and burst pipes also wet roads. The two conditionings ask
about different reference groups — rainy occasions versus wet-road occasions — and the
sizes of those groups drive the answers apart. Confusing them is the error behind
misreading medical tests and forensic evidence.

**11.** (a) $V(X) = 169 - 144 = 25$, so $\sigma = 5$.
(b) $V(4X-7) = 4^2(25) = 400$.
(c) $E(4X-7) = 4(12) - 7 = 41$.

**12.** (a) Degree or experience $= 150 + 90 - 60 = 180$, so $240 - 180 = 60$ have neither.
(b) $180/240 = 0.75$.
(c) $\mathrm{P}(D) = 150/240 = 0.625$ and $\mathrm{P}(E) = 90/240 = 0.375$, so
$\mathrm{P}(D)\mathrm{P}(E) = 0.2344$. But $\mathrm{P}(D \cap E) = 60/240 = 0.25$. Not
equal, so **not independent**.

**13.** (a) $k = 1 - 0.3 - 0.45 = 0.25$.
(b) $E(X) = 1(0.3) + 2(0.45) + 3(0.25) = 0.3 + 0.9 + 0.75 = 1.95$.
(c) $E(X^2) = 1(0.3) + 4(0.45) + 9(0.25) = 0.3 + 1.8 + 2.25 = 4.35$, so
$V(X) = 4.35 - 1.95^2 = 4.35 - 3.8025 = 0.5475$.

**14.** (a) $\text{COV} = \rho\sigma_x\sigma_y = 0.5(9)(12) = 54$.
(b) $81 + 144 + 2(54) = 333$.
(c) Uncorrelated it would be $81 + 144 = 225$. Positive correlation adds 108 to the
variance of the total for no extra return — which is the case for diversifying into
assets that do not move together.

**15.** (a) They multiplied as if the draws were independent. Without replacement the
second draw's probability depends on the first.
(b) $\mathrm{P} = \frac{4}{52} \times \frac{3}{51} = \frac{12}{2652} = 0.0045$.
(c) If the first card were **replaced** and the deck reshuffled, the draws would be
independent and $(4/52)^2 = 0.0059$ would be correct.

---
