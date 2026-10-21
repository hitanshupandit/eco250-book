# Chapter 1 — What statistics is for

> **The question:** you cannot measure everyone. What can you honestly claim anyway?

## The gap the whole subject lives in

Suppose you want to know the average weekly study time of Bates students. There are
about 1,800 of them. You could, in principle, ask all 1,800 — and then you would
not need statistics at all. You would have the answer.

You will not do that. You will ask 200, and you will get a number, and that number
will not be the one you wanted. It will be close, probably. But *probably* and
*close* are doing a lot of work in that sentence, and the whole of this course is
the effort to say exactly how much.

That gap — between the 200 you measured and the 1,800 you care about — is where
statistics lives. Not in the arithmetic. The arithmetic is easy and a computer does
it. The difficulty is knowing what the arithmetic entitles you to say.

## Population and sample

The **population** is every element you care about. The **sample** is the subset you
actually measured.

Two things follow immediately, and students who keep them straight have an easier
term than students who do not.

A number describing a population is a **parameter**. A number describing a sample is
a **statistic**. They get different letters, and the letters are not decoration:

| Quantity | Parameter (population) | Statistic (sample) |
|---|---|---|
| Mean | $\mu$ | $\bar{x}$ |
| Standard deviation | $\sigma$ | $s$ |
| Variance | $\sigma^2$ | $s^2$ |
| Proportion | $p$ | $\hat{p}$ |
| Size | $N$ | $n$ |

**Greek letters are truths you will never see. Roman letters are what you computed.**

And the asymmetry that everything later depends on:

> $\mu$ is a fixed number. It does not move. You do not know it.
>
> $\bar{x}$ moves. Draw a different sample and you get a different one.

That second line looks obvious and is not. It takes until Chapter 12 to use
properly, and most of the confusion students have in the second half of the course
is a failure to believe it early enough. The sample mean is not an approximation
with a mistake attached. It is a *random quantity with a distribution of its own*,
and that distribution is the thing we will eventually learn to describe.

## What kind of data is it?

Before any formula, ask what you are holding.

**Categorical** data are labels: class year, major, country. Numbers used as labels
are still labels — a zip code is categorical, and averaging zip codes produces
nothing.

**Quantitative** data are counts or measurements, and they come in two kinds that
matter later:

- **Discrete** — you can list the possible values, usually counts. Number of
  siblings, defects in a batch, heads in ten coin flips.
- **Continuous** — the values fill an interval. Time, weight, price.

Hold onto that distinction. In Chapter 7 it decides whether you add probabilities
or find an area, and in Chapter 9 it produces the fact that unsettles people most:
for a continuous variable, the probability of any *exact* value is zero.

There is also a hierarchy of how much structure a measurement carries — nominal,
ordinal, interval, ratio — which matters mainly for knowing what operations are
legitimate. You cannot average a nominal variable. You can order an ordinal one but
not subtract it meaningfully: the gap between "fair" and "good" on a survey is not
a quantity.

## Where the sample came from

Everything that follows assumes the sample is related to the population in a way
you can describe. So how you drew it is not an administrative detail. It is the
load-bearing assumption.

Four designs, and you should be able to tell them apart.

**Simple random sampling** is the benchmark. Every member of the population, and
every *group* of the same size, has an equal chance of selection. Nearly all the
theory in this course assumes this, which is worth remembering when you read
someone else's study.

**Systematic sampling** puts the population in some order, picks a random starting
point, and takes every $k$th element. It is random because you did not choose who —
you chose a rule, and the rule chose for you.

**Stratified sampling** splits the population into layers by a characteristic you
care about — class year, region, sex — and then draws a random sample *inside each
layer*. The word *strata* means layers, as in the strato*sphere*, and that is the
whole mnemonic. (I took that one from Professor Leonard, and it has never failed a
student yet.) You stratify to guarantee that every subgroup appears: with pure
random sampling you could, by bad luck, draw almost no first-years.

**Cluster sampling** splits the population into groups *regardless* of
characteristic — city blocks, zip codes, households — picks some groups at random,
and measures everyone in the ones it picked. You do it to save money.

Stratified and cluster get confused every single year, so:

| | Stratified | Cluster |
|---|---|---|
| Groups formed by | a characteristic, chosen deliberately | convenience — geography, cost |
| Each group is | internally similar, different from the others | a miniature of the whole |
| You sample | *within* every group | *whole* groups, chosen at random |
| You do it to | make sure every subgroup appears | save money and travel |

The quick test: **did the grouping use a characteristic you cared about?** If yes,
stratified. If the groups are just whoever happened to be nearby, cluster.

## Two kinds of error, and only one is your fault

**Sampling error** is $\bar{x} - \mu$: the difference between your sample and the
population, arising purely because you took a sample. Your 200 students are not the
1,800 and were never going to be. This error is random, unavoidable, and — crucially
— it *shrinks as $n$ grows*. Chapter 12 will tell you exactly how fast.

**Non-sampling error** is everything else. A mistyped number. A leading question. The
people who did not reply. This error is often systematic, frequently invisible, and
it does **not** shrink as $n$ grows.

> A bigger sample fixes the first and does nothing at all for the second.

That sentence is most of what goes wrong with statistics in public life. A survey of
a million people who all opted in is still a survey of people who opt in, and its
margin of error — computed honestly, reported honestly — is answering a question
nobody asked.

## In Stata

Two commands, and the habit of starting with them.

```stata
use "DATA/cps_small.dta", clear
describe
summarize wage
```

`describe` tells you what is in the file: how many observations, how many variables,
what each one is called and what it holds. `summarize` gives you the count, mean,
standard deviation, minimum and maximum.

Run both before you do anything else, every time. Most of the errors I see in
submitted work are not statistical errors — they are someone computing a careful
answer about a variable that turned out to have 685 missing values, which
`summarize` would have shown in its first column.

## What goes wrong

**Mixing Greek and Roman.** Writing $\sigma$ when you computed $s$ is not a typo,
because the two behave differently and the formulas that use them differ. This costs
more marks across the term than any other single thing.

**Treating a convenience sample as random.** The people who answered are not a random
sample of the people you asked, and the people you asked are not a random sample of
anybody. Say so.

**Thinking more data fixes bias.** See above. It does not.

**Averaging labels.** If the variable is categorical, the mean is a number with no
meaning. Stata will compute it cheerfully.

## Exercises

1. For each, say whether it is a population or a sample, and name the parameter or
   statistic involved.
   (a) The mean GPA of the 23 students in this section.
   (b) The mean GPA of 23 students surveyed in Commons, used to describe the college.

2. Classify as categorical, discrete quantitative, or continuous quantitative:
   student ID number; number of courses taken; time spent on a problem set; letter
   grade; credit hours earned.

3. A researcher wants to estimate mean household income in Maine. Describe how she
   would do it (a) by stratified sampling and (b) by cluster sampling, and say which
   you would choose and why.

4. A website runs a poll and gets 2.4 million responses. The reported margin of
   error is $\pm 0.06$ percentage points. In one sentence, what is wrong?

5. A sample of 200 Bates students gives a mean study time of 14.2 hours a week.
   Which of the following is $\mu$, which is $\bar{x}$, and which is neither?
   (a) 14.2 (b) the true mean over all 1,800 students (c) 200.

### Answers

1. (a) Population — all 23 are the group of interest, so 
   the mean is $\mu$. (b) Sample — the 23 stand in for the college, so the mean is
   $\bar{x}$. Notice the *same 23 people* can be either. It depends entirely on what
   you claim they represent.

2. Categorical: student ID (a label, despite being numeric), letter grade (ordinal).
   Discrete: number of courses, credit hours. Continuous: time spent.

3. (a) Split Maine into counties, or into income bands if known, and draw a random
   sample within each so that every region is represented. (b) Split the state into
   census blocks, pick a random set of blocks, and survey every household in those
   blocks. Cluster is far cheaper because the interviewer travels to a few places
   instead of everywhere; stratified is more precise. Chapter 12 shows precisely how
   much precision clustering costs.

4. The margin of error measures sampling error only. The respondents selected
   themselves, so the dominant error here is non-sampling, and 2.4 million does
   nothing about it. The stated $\pm 0.06$ is arithmetically correct and practically
   meaningless.

5. (a) $\bar{x}$. (b) $\mu$. (c) neither — that is $n$.

---
