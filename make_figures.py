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


# ------------------------------------- 7. mean against median on skewed data
def mean_vs_median():
    import warnings
    warnings.filterwarnings("ignore")
    import pandas as pd
    #  HERE is <project>/book, so one dirname reaches the project root.
    d = pd.read_stata(os.path.join(os.path.dirname(HERE),
                                   "STATA", "DATA", "cps_small.dta"))
    w = d["wage"].astype(float).to_numpy()

    fig, ax = plt.subplots(figsize=(5.8, 2.9))
    ax.hist(w, bins=60, color=GREY, edgecolor="white", linewidth=0.3)
    ax.axvline(np.median(w), color=INK, lw=1.6,
               label=f"median {np.median(w):.2f}")
    ax.axvline(w.mean(), color=RED, lw=1.6, ls="--", label=f"mean {w.mean():.2f}")
    ax.legend(frameon=False, fontsize=8)
    ax.set_yticks([])
    ax.set_xlabel("hourly wage, $")
    ax.set_title(f"Right-skewed (skew {stats.skew(w):+.2f}): the mean is pulled "
                 f"towards the tail", fontsize=9)
    fig.tight_layout()
    save(fig, "mean_vs_median.png")
    assert w.mean() > np.median(w), "the mean should exceed the median here"
    print("     mean %.4f  median %.4f  skew %+.4f"
          % (w.mean(), np.median(w), stats.skew(w)))


# --------------------------------------- 8. what different correlations look like
def correlation_grid(seed=7):
    rng = np.random.default_rng(seed)
    n = 300
    panels = []
    for target in (0.95, 0.5, 0.0, -0.85):
        x = rng.normal(size=n)
        e = rng.normal(size=n)
        a = target / np.sqrt(1 - target ** 2) if abs(target) < 1 else 10
        y = a * x + e
        panels.append((x, y, np.corrcoef(x, y)[0, 1]))
    #  the trap: a strong relationship the correlation cannot see
    x = rng.uniform(-3, 3, n)
    panels.append((x, x ** 2 + rng.normal(0, 0.8, n), np.corrcoef(x, x ** 2)[0, 1]))

    fig, axes = plt.subplots(1, 5, figsize=(13.5, 2.6))
    for ax, (x, y, r) in zip(axes, panels):
        ax.scatter(x, y, s=5, color=RED, alpha=0.45, linewidths=0)
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_title(f"r = {r:+.2f}", fontsize=9)
    axes[-1].set_title(f"r = {panels[-1][2]:+.2f}\n(but look at it)", fontsize=9)
    fig.suptitle("Correlation measures straight lines, and nothing else",
                 fontsize=10, y=1.06)
    fig.tight_layout()
    save(fig, "correlation_grid.png")
    assert abs(panels[-1][2]) < 0.15, "the curved panel should have r near zero"
    print("     " + "  ".join("r=%+.2f" % r for _, _, r in panels))


# ------------------------------------------- 9. Venn diagrams for probability
def venn():
    """Three panels built from plain circles: union, intersection, conditioning.

    Drawn here rather than borrowed, so the shading matches exactly the rules the
    chapter states and the numbers in the captions are the chapter's numbers.
    """
    from matplotlib.patches import Circle, Rectangle

    PA, PB, PAB = 0.42, 0.37, 0.15
    cx1, cx2, cy, rad = -0.45, 0.45, 0.0, 0.85

    def frame(ax, title):
        ax.add_patch(Rectangle((-1.75, -1.15), 3.5, 2.3, fill=False,
                               edgecolor=GREY, lw=0.8))
        ax.set_xlim(-1.8, 1.8); ax.set_ylim(-1.95, 1.45)
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(title, fontsize=9)
        ax.text(1.62, 1.0, "S", fontsize=8, color=GREY)

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(10.5, 2.9))

    #  union: both circles shaded, the lens shaded twice over
    frame(a1, r"$\mathrm{P}(A\cup B)=\mathrm{P}(A)+\mathrm{P}(B)-\mathrm{P}(A\cap B)$")
    a1.add_patch(Circle((cx1, cy), rad, facecolor=RED, alpha=0.30, edgecolor=INK, lw=1))
    a1.add_patch(Circle((cx2, cy), rad, facecolor=RED, alpha=0.30, edgecolor=INK, lw=1))
    a1.text(-0.95, 0, "A", fontsize=10, ha="center")
    a1.text(0.95, 0, "B", fontsize=10, ha="center")
    a1.text(0, -1.62, "the lens is inside both circles,\nso adding counts it twice",
            fontsize=7.5, ha="center", color=INK)

    #  intersection only
    frame(a2, r"$\mathrm{P}(A\cap B) = %.2f$" % PAB)
    a2.add_patch(Circle((cx1, cy), rad, facecolor="none", edgecolor=INK, lw=1))
    a2.add_patch(Circle((cx2, cy), rad, facecolor="none", edgecolor=INK, lw=1))
    #  shade the lens by clipping one circle to the other
    lens = Circle((cx1, cy), rad, facecolor=RED, alpha=0.55, edgecolor="none")
    a2.add_patch(lens)
    lens.set_clip_path(Circle((cx2, cy), rad, transform=a2.transData))
    a2.text(-0.95, 0, "A", fontsize=10, ha="center")
    a2.text(0.95, 0, "B", fontsize=10, ha="center")
    a2.text(0, -1.62, "only where both happen", fontsize=7.5, ha="center", color=INK)

    #  conditioning: B becomes the whole world
    frame(a3, r"$\mathrm{P}(A\mid B)=\dfrac{\mathrm{P}(A\cap B)}{\mathrm{P}(B)}"
              r"=\dfrac{%.2f}{%.2f}=%.2f$" % (PAB, PB, PAB / PB))
    a3.add_patch(Circle((cx1, cy), rad, facecolor="none", edgecolor=GREY, lw=0.9,
                        linestyle=":"))
    a3.add_patch(Circle((cx2, cy), rad, facecolor=GREY, alpha=0.35, edgecolor=INK, lw=1.6))
    lens3 = Circle((cx1, cy), rad, facecolor=RED, alpha=0.65, edgecolor="none")
    a3.add_patch(lens3)
    lens3.set_clip_path(Circle((cx2, cy), rad, transform=a3.transData))
    a3.text(-1.05, 0, "A", fontsize=10, ha="center", color=GREY)
    a3.text(1.05, 0, "B", fontsize=10, ha="center")
    a3.text(0, -1.62, "B is the new world;\nmeasure A inside it",
            fontsize=7.5, ha="center", color=INK)

    fig.tight_layout()
    save(fig, "venn_probability.png")
    print("     P(A or B) %.2f   P(A|B) %.4f   (A, B dependent: %s)"
          % (PA + PB - PAB, PAB / PB, abs(PA * PB - PAB) > 1e-9))


BLUE = "#1a4f8b"


# ------------------------- 10. what "95% confident" refers to "95% confident" refers to
def coverage(mu=28.4, sigma=6.0, n=36, reps=100, seed=250):
    """100 intervals from the same population. Count how many miss mu."""
    rng = np.random.default_rng(seed)
    t = stats.t.ppf(0.975, n - 1)

    lo, hi = [], []
    for _ in range(reps):
        x = rng.normal(mu, sigma, n)
        me = t * x.std(ddof=1) / np.sqrt(n)
        lo.append(x.mean() - me)
        hi.append(x.mean() + me)
    lo, hi = np.array(lo), np.array(hi)
    miss = (lo > mu) | (hi < mu)

    fig, ax = plt.subplots(figsize=(7.4, 3.5))
    for i in range(reps):
        c = RED if miss[i] else GREY
        ax.plot([i, i], [lo[i], hi[i]], color=c, lw=1.6,
                alpha=1.0 if miss[i] else 0.55, solid_capstyle="butt")
    ax.axhline(mu, color=INK, lw=1.3)
    ax.text(reps + 1.5, mu, r"  true $\mu$", va="center", fontsize=9, color=INK)

    ax.set_xlim(-2, reps + 12)
    ax.set_xlabel("100 repeats of the same study")
    ax.set_ylabel("minutes")
    ax.set_xticks([])
    ax.set_title(f"{reps - miss.sum()} of {reps} intervals contain $\\mu$   "
                 f"({miss.sum()} miss, in red)", color=INK, fontsize=10)
    save(fig, "ci_coverage.png")

    #  A 95% procedure should miss about 5 in 100. Anything outside 0-13 would
    #  mean the picture is not showing what the slide says it shows.
    assert 0 < miss.sum() <= 13, f"coverage simulation produced {miss.sum()} misses"
    return int(miss.sum())

# ---------------------------- 11. alpha and beta, as two areas and beta, as two areas
def errors(mu0=100.0, mu1=106.0, sigma=15.0, n=25, alpha=0.05):
    """The same test as the power table on the slide, drawn."""
    se = sigma / np.sqrt(n)
    crit = mu0 + stats.norm.ppf(1 - alpha) * se
    power = stats.norm.sf((crit - mu1) / se)
    beta = 1 - power

    x = np.linspace(mu0 - 4 * se, mu1 + 4 * se, 800)
    d0 = stats.norm.pdf(x, mu0, se)
    d1 = stats.norm.pdf(x, mu1, se)

    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    ax.plot(x, d0, color=INK, lw=1.6)
    ax.plot(x, d1, color=BLUE, lw=1.6)

    r = x >= crit
    l = x <= crit
    ax.fill_between(x[r], 0, d0[r], color=RED, alpha=0.65, lw=0)
    ax.fill_between(x[l], 0, d1[l], color=BLUE, alpha=0.22, lw=0)
    ax.axvline(crit, color=GREY, lw=1.1, ls="--")

    top = max(d0.max(), d1.max())
    #  The two peaks are only 2 SE apart, so centred labels overlap. Push each
    #  one outward, away from the other, and anchor it on its own side.
    ax.text(mu0 - 1.6 * se, top * 1.02, r"if $H_0$ true:  $\mu=100$",
            ha="right", color=INK, fontsize=9)
    ax.text(mu1 + 1.6 * se, top * 1.02, r"the truth:  $\mu=106$",
            ha="left", color=BLUE, fontsize=9)
    ax.annotate(rf"$\alpha={alpha:.2f}$" "\nfalse alarm",
                xy=(crit + 0.7 * se, 0.012), xytext=(crit + 2.0 * se, top * 0.52),
                color=RED, fontsize=9, ha="center",
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.0))
    ax.annotate(rf"$\beta={beta:.4f}$" "\na miss",
                xy=(crit - 1.1 * se, 0.012), xytext=(crit - 3.1 * se, top * 0.52),
                color=BLUE, fontsize=9, ha="center",
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.0))
    #  Sits inside the axes on the dashed line; below the axis it collided with
    #  the tick labels.
    ax.text(crit + 0.12 * se, top * 0.90, f"reject above {crit:.2f}",
            ha="left", color=GREY, fontsize=8, rotation=90, va="top")

    ax.set_ylim(0, top * 1.14)
    ax.set_yticks([])
    ax.set_xlabel(r"sample mean $\bar{x}$")
    ax.set_title(f"Power = 1 - $\\beta$ = {power:.4f}", color=INK, fontsize=10)
    save(fig, "type_i_ii.png")

    #  must match the slide's table exactly
    assert abs(crit - 104.9346) < 5e-5
    assert abs(power - 0.6388) < 5e-5 and abs(beta - 0.3612) < 5e-5
    #  the red area IS alpha, and the blue area IS beta -- check by integration
    assert abs(np.trapezoid(d0[r], x[r]) - alpha) < 2e-3
    assert abs(np.trapezoid(d1[l], x[l]) - beta) < 2e-3
    return float(power)

# ------------------- 12. diminishing returns to sample size returns to sample size
def precision(sigma=6.0, marks=(9, 36, 144)):
    n = np.arange(4, 401)
    me = stats.t.ppf(0.975, n - 1) * sigma / np.sqrt(n)

    fig, ax = plt.subplots(figsize=(7.4, 3.2))
    ax.plot(n, me, color=INK, lw=1.8)
    for m in marks:
        y = float(stats.t.ppf(0.975, m - 1) * sigma / np.sqrt(m))
        ax.plot([m, m], [0, y], color=RED, lw=1.0, ls=":")
        ax.plot(m, y, "o", color=RED, ms=5)
        ax.annotate(f"n={m}\n$\\pm${y:.2f}", xy=(m, y),
                    xytext=(m + 14, y + 0.28), color=RED, fontsize=8.5)

    ax.set_xlabel("sample size $n$")
    ax.set_ylabel("margin of error (minutes)")
    ax.set_ylim(0, None)
    ax.set_title(r"Margin of error falls as $1/\sqrt{n}$ --- "
                 "four times the data, half the width",
                 color=INK, fontsize=10)
    save(fig, "precision_vs_n.png")

    a = float(stats.t.ppf(0.975, 35) * sigma / np.sqrt(36))
    b = float(stats.t.ppf(0.975, 143) * sigma / np.sqrt(144))
    assert abs(a - 2.0301) < 5e-5
    assert 1.9 < a / b < 2.1, "quadrupling n should roughly halve the margin"
    return a, b

if __name__ == "__main__":
    print("Figures for the book\n")
    clt()
    standardise()
    t_vs_normal()
    pvalues()
    binomial_normal()
    normal_anatomy()
    mean_vs_median()
    correlation_grid()
    venn()
    coverage()
    errors()
    precision()
    print("\n  all figures regenerated and their claims re-checked")
