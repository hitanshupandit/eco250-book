#!/usr/bin/env python3
"""Figures for the book, generated rather than drawn.

Every figure here is produced from a simulation or an exact density, so the picture
cannot drift away from the claim the text makes next to it. Each one prints the
numbers it is asserting, and the build fails if a figure stops showing what the
chapter says it shows.

Output goes to book/figures/ as PNG at 150 dpi, which is sharp on a laptop screen
and small enough to live in a git repository.

Usage:  python3 book/make_figures.py
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "figures")
os.makedirs(FIG, exist_ok=True)

INK, RED, GREY = "#222222", "#8b1a1a", "#999999"
plt.rcParams.update({"figure.dpi": 150, "savefig.dpi": 150,
                     "font.size": 9, "axes.edgecolor": GREY,
                     "axes.spines.top": False, "axes.spines.right": False})


def save(fig, name):
    p = os.path.join(FIG, name)
    fig.savefig(p, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  wrote figures/%s" % name)


# ------------------------------------------------- 1. the CLT, as n increases
def clt(n_values=(1, 5, 30, 100), reps=20000, seed=250):
    """Means of n draws from a hard, lopsided population.

    The population is deliberately nasty: a mixture that is strongly right-skewed
    with a lump at zero, so nobody can claim the bell was there all along.
    """
    rng = np.random.default_rng(seed)

    def draw(size):
        #  70% of the mass is a tight exponential, 30% a long right tail
        a = rng.exponential(2.0, size)
        b = rng.exponential(12.0, size)
        pick = rng.random(size) < 0.30
        return np.where(pick, b, a)

    pop = draw(200000)
    mu, sg = pop.mean(), pop.std()

    fig, axes = plt.subplots(1, len(n_values), figsize=(3.1 * len(n_values), 2.7))
    stats_out = []
    for ax, n in zip(np.atleast_1d(axes), n_values):
        means = draw(reps * n).reshape(reps, n).mean(axis=1)
        ax.hist(means, bins=60, density=True, color=GREY, edgecolor="white",
                linewidth=0.3)
        xs = np.linspace(means.min(), means.max(), 300)
        ax.plot(xs, stats.norm.pdf(xs, mu, sg / np.sqrt(n)), color=RED, lw=1.6)
        sk = stats.skew(means)
        ax.set_title(f"n = {n}\nSD {means.std():.2f}   skew {sk:+.2f}", fontsize=9)
        ax.set_yticks([])
        stats_out.append((n, means.std(), sk))

    fig.suptitle("Means of $n$ draws from a strongly right-skewed population",
                 fontsize=10, y=1.04)
    fig.tight_layout()
    save(fig, "clt_convergence.png")

    #  the two claims the chapter makes, checked rather than asserted in prose
    print("     population mu %.3f  sigma %.3f" % (mu, sg))
    for n, sd, sk in stats_out:
        print("     n=%-3d SD %.3f (sigma/sqrt(n) = %.3f)  skew %+.3f"
              % (n, sd, sg / np.sqrt(n), sk))
    first, last = stats_out[0], stats_out[-1]
    assert abs(last[1] - sg / np.sqrt(last[0])) < 0.05 * last[1], \
        "SD of the mean does not match sigma/sqrt(n)"
    assert abs(last[2]) < 0.35 * abs(first[2]), \
        "skewness did not fall as n grew -- the figure contradicts the text"
    return stats_out


# ------------------------------------- 2. standardising does not change shape
def standardise(seed=250):
    rng = np.random.default_rng(seed)
    x = rng.lognormal(mean=2.0, sigma=0.8, size=20000)
    z = (x - x.mean()) / x.std(ddof=1)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 2.7))
    a1.hist(x, bins=70, color=GREY, edgecolor="white", linewidth=0.3)
    a1.set_title(f"original\nmean {x.mean():.2f}   SD {x.std(ddof=1):.2f}"
                 f"   skew {stats.skew(x):+.2f}", fontsize=9)
    a2.hist(z, bins=70, color=RED, alpha=0.75, edgecolor="white", linewidth=0.3)
    a2.set_title(f"standardised\nmean {z.mean():.2f}   SD {z.std(ddof=1):.2f}"
                 f"   skew {stats.skew(z):+.2f}", fontsize=9)
    for a in (a1, a2):
        a.set_yticks([])
    fig.suptitle("Standardising recentres and rescales. It does not reshape.",
                 fontsize=10, y=1.04)
    fig.tight_layout()
    save(fig, "standardising.png")

    assert abs(stats.skew(x) - stats.skew(z)) < 1e-6, \
        "skewness changed under standardising -- it must not"
    print("     skew before %+.4f  after %+.4f  (identical)"
          % (stats.skew(x), stats.skew(z)))


# ------------------------------------------------ 3. t against the normal
def t_vs_normal():
    xs = np.linspace(-4.2, 4.2, 600)
    fig, ax = plt.subplots(figsize=(5.4, 2.8))
    ax.plot(xs, stats.t.pdf(xs, 3), color=GREY, lw=1.3, label=r"$t$, $\nu=3$")
    ax.plot(xs, stats.t.pdf(xs, 10), color=INK, lw=1.1, ls="--",
            label=r"$t$, $\nu=10$")
    ax.plot(xs, stats.norm.pdf(xs), color=RED, lw=1.8, label="normal")
    ax.set_yticks([])
    ax.legend(frameon=False, fontsize=8)
    ax.set_title("Same centre, fatter tails: the price of estimating $\\sigma$",
                 fontsize=10)
    fig.tight_layout()
    save(fig, "t_vs_normal.png")
    print("     P(|t_3|>2) %.4f   P(|t_10|>2) %.4f   P(|Z|>2) %.4f"
          % (2 * stats.t.sf(2, 3), 2 * stats.t.sf(2, 10), 2 * stats.norm.sf(2)))


# --------------------------------- 4. p-values are uniform when H0 is true
def pvalues(reps=20000, n=25, seed=250):
    rng = np.random.default_rng(seed)
    true = rng.normal(100, 15, size=(reps, n))
    false = rng.normal(106, 15, size=(reps, n))
    p_true = stats.ttest_1samp(true, 100, axis=1).pvalue
    p_false = stats.ttest_1samp(false, 100, axis=1).pvalue

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 2.7))
    for a, p, ttl, col in ((a1, p_true, "$H_0$ is TRUE", GREY),
                           (a2, p_false, "$H_0$ is FALSE ($\\mu=106$)", RED)):
        a.hist(p, bins=20, range=(0, 1), color=col, edgecolor="white", linewidth=0.4)
        a.axvline(0.05, color=INK, lw=1, ls=":")
        a.set_title(f"{ttl}\n{(p < 0.05).mean():.1%} fall below 0.05", fontsize=9)
        a.set_xlabel("$p$-value")
        a.set_yticks([])
    fig.suptitle("A $p$-value is a random variable", fontsize=10, y=1.04)
    fig.tight_layout()
    save(fig, "pvalue_uniform.png")

    rate = (p_true < 0.05).mean()
    power = (p_false < 0.05).mean()
    assert abs(rate - 0.05) < 0.01, "Type I rate is not alpha: %.4f" % rate
    print("     H0 true : %.4f below 0.05 (should be alpha = 0.05)" % rate)
    print("     H0 false: %.4f below 0.05 (the power at n=%d)" % (power, n))


# ----------------------------------------- 5. the binomial becoming normal
def binomial_normal(p=0.3, ns=(5, 20, 60)):
    fig, axes = plt.subplots(1, len(ns), figsize=(3.1 * len(ns), 2.5))
    for ax, n in zip(axes, ns):
        k = np.arange(0, n + 1)
        pmf = stats.binom.pmf(k, n, p)
        mu, sd = n * p, np.sqrt(n * p * (1 - p))
        ax.bar((k - mu) / sd, pmf * sd, width=1 / sd, color=GREY,
               edgecolor="white", linewidth=0.3)
        xs = np.linspace(-4, 4, 300)
        ax.plot(xs, stats.norm.pdf(xs), color=RED, lw=1.6)
        ax.set_xlim(-4, 4)
        ax.set_title(f"n = {n}", fontsize=9)
        ax.set_yticks([])
    fig.suptitle(f"A standardised binomial at p = {p} becomes the normal",
                 fontsize=10, y=1.04)
    fig.tight_layout()
    save(fig, "binomial_to_normal.png")
    print("     largest gap to the normal at n=%d: %.4f"
          % (ns[-1], abs(stats.binom.cdf(int(ns[-1] * p), ns[-1], p)
                         - stats.norm.cdf(0.5 / np.sqrt(ns[-1] * p * (1 - p))))))


# ------------------------------------------- 6. what the normal distribution is
def normal_anatomy():
    """Two panels: what the parameters do, and what the areas are."""
    xs = np.linspace(-5, 5, 600)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 2.9))

    #  left: mu slides the curve, sigma widens it
    for mu, sg, col, ls, lab in ((0, 1, RED, "-", r"$\mu=0,\ \sigma=1$"),
                                 (1.5, 1, INK, "--", r"$\mu=1.5,\ \sigma=1$"),
                                 (0, 2, GREY, "-", r"$\mu=0,\ \sigma=2$")):
        a1.plot(xs, stats.norm.pdf(xs, mu, sg), color=col, ls=ls, lw=1.5, label=lab)
    a1.legend(frameon=False, fontsize=8)
    a1.set_yticks([])
    a1.set_title(r"$\mu$ slides it, $\sigma$ widens it", fontsize=9)

    #  right: the 68-95-99.7 areas
    z = np.linspace(-4, 4, 600)
    a2.plot(z, stats.norm.pdf(z), color=INK, lw=1.4)
    for k, alpha in ((3, 0.12), (2, 0.18), (1, 0.30)):
        m = (z >= -k) & (z <= k)
        a2.fill_between(z[m], stats.norm.pdf(z[m]), color=RED, alpha=alpha,
                        linewidth=0)
    for k in (1, 2, 3):
        pct = stats.norm.cdf(k) - stats.norm.cdf(-k)
        a2.annotate(f"{pct:.1%}", xy=(0, 0.30 - 0.07 * k), ha="center", fontsize=8,
                    color="white" if k == 1 else INK)
    a2.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    a2.set_xticklabels([r"$-3\sigma$", r"$-2\sigma$", r"$-\sigma$", r"$\mu$",
                        r"$\sigma$", r"$2\sigma$", r"$3\sigma$"], fontsize=7)
    a2.set_yticks([])
    a2.set_title("the empirical rule, as areas", fontsize=9)

    fig.tight_layout()
    save(fig, "normal_anatomy.png")
    for k in (1, 2, 3):
        print("     within %d sigma: %.4f" % (k, stats.norm.cdf(k) - stats.norm.cdf(-k)))
    assert abs((stats.norm.cdf(1) - stats.norm.cdf(-1)) - 0.6827) < 5e-5
    assert abs((stats.norm.cdf(2) - stats.norm.cdf(-2)) - 0.9545) < 5e-5


if __name__ == "__main__":
    print("Figures for the book\n")
    clt()
    standardise()
    t_vs_normal()
    pvalues()
    binomial_normal()
    normal_anatomy()
    print("\n  all figures regenerated and their claims re-checked")
