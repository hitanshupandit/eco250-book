# Chapter 2 — Centre: mean, median, mode

> **The question:** you have a column of numbers. Where is the middle?

## Five questions, before any formula

Faced with a new data set, there are five things worth asking, and I would rather
you memorised this list than most of the formulas that follow. Professor Leonard
opens his course with it and he is right to.

1. **Centre.** Where is the middle?
2. **Variation.** How spread out is it?
3. **Distribution.** What shape?
4. **Outliers.** Is anything far from the rest?
5. **Change over time.** Is the thing you measured drifting?

Every descriptive statistic you will learn answers one of those five. If you cannot
say which one a number is answering, you do not yet know what it is for. This
chapter is question 1; Chapter 3 is questions 2 and 4.

## Three centres

**The mean** is the balance point:

$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

Add everything up, divide by how many. It is the centre of mass: if the values were
weights on a ruler, the mean is where you would put your finger to balance it.

**The median** is the middle value once you have sorted. With an odd number of
observations it is the one in the middle; with an even number it is the average of
the two straddling the middle.

**The mode** is the value that occurs most often. That is genuinely all it is — the
word means *the most*. A data set can have one mode, several, or none.

## Why there are three

Because they fail differently, and knowing which one to reach for is the actual
skill.

The **mean** is the only one you can do algebra with. $E(aX + b) = aE(X) + b$ works
for means and has no counterpart for medians. That is why the entire rest of this
course — every standard error, every confidence interval, every test — is built on
the mean and not on the median. It is the workhorse, and it is not close.

But the mean feels every observation, including the one somebody typed wrong. That
is its weakness, and the next page is the weakness.

The **median** ignores the sizes of everything except the middle. That makes it
blind to outliers — which is a flaw when the outliers are real information, and a
virtue when they are not.

The **mode** is the only one that works on categorical data. You cannot average
"economics, biology, history". You can say which occurs most.

## Worked example — one number changes

A sample of five values:

$$\{3,\ 7,\ 7,\ 9,\ 14\}$$

**(a) Find the mean, median and mode.**

**(b) Now suppose the largest value was recorded wrongly — it should have been 44,
not 14. Which of the three move, and by how much?**

Try (b) in your head before reading on. You should be able to say which two do not
move without computing anything.

### Solution

**(a)** The mean:

$$\bar{x} = \frac{3 + 7 + 7 + 9 + 14}{5} = \frac{40}{5} = 8$$

Sorted, the values are $3,\ 7,\ \mathbf{7},\ 9,\ 14$. With $n = 5$ the middle one is
the third, so the **median is 7**.

The value 7 appears twice and nothing else repeats, so the **mode is 7**.

**(b)** With 44 in place of 14:

$$\bar{x} = \frac{3 + 7 + 7 + 9 + 44}{5} = \frac{70}{5} = 14$$

The mean has moved by **6**. The sorted values are now $3,\ 7,\ \mathbf{7},\ 9,\ 44$
— the middle one is still 7, so the **median has not moved at all**. Neither has the
mode.

One bad value dragged the mean most of the way towards itself. The median never
noticed.

> That is the entire argument for reporting both, and it is why you see *median*
> household income and never *mean* household income.

## What skew does

The relationship between mean and median tells you the shape.

- **Symmetric**: mean $\approx$ median.
- **Right-skewed** (a long tail of large values): **mean > median**. The tail pulls
  the balance point towards it; the counting point stays put.
- **Left-skewed**: **mean < median**.

This is not a rule to memorise so much as a consequence of what the two things are.
The mean is pulled by distance, the median only by counting.

Wages are the standard case, and it is worth seeing on real data rather than taking
my word for it. In the CPS extract we use in lab, 1,000 workers:

| | |
|---|---|
| Mean hourly wage | \$10.21 |
| Median hourly wage | \$8.79 |
| Skewness | $+1.95$ |

The mean sits nearly a dollar fifty above the median. A relatively small number of
very high earners — the largest in the file is \$60.19 — pull the average up while
leaving the middle person where she is. If you want to describe what a typical
worker earns, \$8.79 is the honest number. If you want to describe the total wage
bill divided by headcount, \$10.21 is. They answer different questions and neither
is wrong.

## In Stata

```stata
use "DATA/cps_small.dta", clear
summarize wage
summarize wage, detail
```

Plain `summarize` gives you the mean, the standard deviation, and the range.

`summarize, detail` gives you much more: the percentiles — and the 50th percentile
*is* the median — plus skewness and kurtosis, and the five largest and smallest
values, which is the fastest outlier check there is.

Stata has no `mode` in `summarize`, because the mode is nearly useless for
continuous data: with 1,000 wages measured to the cent, almost every value is
unique. If you need it for a categorical variable, use `tabulate` and read off the
biggest row.

```stata
tabulate educ
```

## What goes wrong

**Reporting the mean of a skewed variable without saying so.** Not wrong,
exactly, but it misleads, and in a report it will be read as "typical". Give both,
or give the median and say why.

**Forgetting to sort before taking the median.** The median is defined on sorted
data. By hand, this is the single most common slip.

**Taking the median of an even-sized sample as "one of the two middle values".** It
is their average, and the average need not be a value that appears in the data.

**Averaging a categorical variable.** Stata will do it. The result means nothing.

**Assuming the mode is unique.** It often is not, and "no mode" is a legitimate
answer when nothing repeats.

## Exercises

1. For $\{12,\ 15,\ 15,\ 18,\ 22,\ 24\}$ find the mean, median and mode.

2. A sample of seven houses sold for (in thousands): 180, 195, 210, 215, 230, 245,
   1,400. Compute the mean and the median. Which would you report in a newspaper
   story about house prices, and why?

3. A data set has mean 50 and median 62. What shape is it, and sketch roughly what
   the histogram looks like.

4. Nine students score a mean of 72 on a test. A tenth student joins with a score of
   92. What is the new mean? (Do it without recomputing the total from scratch if you
   can see how.)

5. Can the mean of a sample be a value that never appears in the sample? Can the
   median? Can the mode? Give an example or explain why not in each case.

### Answers

1. Sum is 106, so $\bar{x} = 106/6 = 17.67$. With $n = 6$ the median is the average
   of the 3rd and 4th: $(15 + 18)/2 = 16.5$. Mode is 15.

2. Sum is 2,675, so the mean is \$382,143. The median is the 4th of seven sorted
   values: \$215,000. Report the **median**. Six of the seven houses sold for between
   180 and 245; the mean describes none of them, and exists only because of one sale
   that is arguably a different market entirely.

3. Mean below median means **left-skewed** — a long tail running to the left. The
   bulk of the data sits at the high end with a few small values trailing off below.

4. The ten scores total $9(72) + 92 = 648 + 92 = 740$, so the new mean is 74. The
   shortcut: the new value is 20 above the old mean, and that surplus is shared over
   10 students, so the mean rises by $20/10 = 2$.

5. **Mean**: yes, routinely — the mean of $\{1, 2\}$ is 1.5. **Median**: yes, whenever
   $n$ is even and the two middle values differ. **Mode**: no, never — it is defined
   as a value that occurs, so it must be one of them.

---
