"""Publication figures for *The Geometry of Competent Contact*. The plotters
recompute belief geometry from analyses and read scalar results from the results
dict. Deterministic; no seed."""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from analyses import (
    N, NA, NB, STATES, prior, expect, modal_belief, fr_distance,
    value_task1, shannon_entropy, REWARD_ONLY_PLAN, COMPETENT_PLAN,
)

INK = "#1e1e2e"
MUTED = "#6c7086"
ACCENT = "#8839ef"
WARM = "#d20f39"
COOL = "#1e66f5"
GOOD = "#40a02b"


def _bare(ax):
    ax.spines[["top", "right"]].set_visible(False)


def plot_manifold(results, path):
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.4))
    m = results["manifold"]
    pv = results["probe_value"]

    # --- left: the world as a 2x3 grid and its two cross-cutting quotients ---
    axL.set_xlim(-0.6, 3.0)
    axL.set_ylim(-0.9, 2.2)
    axL.set_aspect("equal")
    axL.axis("off")
    for a in range(NA):
        for b in range(NB):
            x, y = a, b
            face = "#eff1f5" if not (a == 0) else "#e6e0f8"
            axL.add_patch(plt.Rectangle((x - 0.42, y - 0.42), 0.84, 0.84,
                                        fc=face, ec=MUTED, lw=1.0))
            axL.text(x, y, f"$w_{{{2*a+b}}}$\n$({a},{b})$", ha="center",
                     va="center", fontsize=8, color=INK)
    # task-1 reads columns (A), task-2 reads rows (B)
    for a in range(NA):
        axL.text(a, 1.75, f"$A={a}$", ha="center", fontsize=8, color=ACCENT)
    axL.text(1.0, 2.05, "task 1 reads the columns  ($g_1=A$)", ha="center",
             fontsize=8.5, color=ACCENT)
    for b in range(NB):
        axL.text(-0.55, b, f"$B={b}$", ha="center", va="center", fontsize=8, color=COOL)
    axL.text(-0.55, -0.78, "task 2 reads the rows ($g_2=B$)", ha="left",
             fontsize=8.5, color=COOL)
    # the two quotient-equal beliefs
    axL.annotate("", xy=(0, 1), xytext=(0, 0),
                 arrowprops=dict(arrowstyle="<->", color=WARM, lw=1.6))
    axL.text(0.12, 0.5, f"$d_{{FR}}={m['r_quotient_fr_distance']}$\n"
             f"same task-1 value {m['quotient_value_task1_b00']}\n"
             f"opposite on task 2", ha="left", va="center", fontsize=7.5, color=WARM,
             bbox=dict(facecolor="white", alpha=0.9, edgecolor="none", pad=1.5), zorder=6)
    axL.set_title("World-states and the two task partitions", fontsize=10, color=INK)

    # --- right: task-1 value vs A-probes; B-probe adds nothing ---
    v1 = pv["value_task1_vs_k_Aprobes"]
    ks = [0, 1, 2, 3]
    vals = [v1[f"k{k}"] for k in ks]
    axR.plot(ks, vals, "-o", color=ACCENT, lw=2.0, label="value after $k$ A-probes")
    axR.scatter([2], [pv["value_task1_after_AAB"]], color=COOL, s=70, zorder=5,
                marker="D", label="then a B-probe (no gain)")
    axR.annotate(f"B-probe marginal\ntask-1 value = "
                 f"{pv['value_task1_marginal_of_Bprobe']}",
                 (2, pv["value_task1_after_AAB"]), xytext=(1.15, 0.62),
                 fontsize=8, color=COOL,
                 arrowprops=dict(arrowstyle="->", color=COOL, lw=1.0))
    axR.set_xlabel("number of A-probes", fontsize=9)
    axR.set_ylabel("Bayes-optimal task-1 value", fontsize=9)
    axR.set_xticks(ks)
    axR.set_ylim(0.3, 1.02)
    axR.set_title("Task-1 value versus number of A-probes", fontsize=10, color=INK)
    axR.legend(fontsize=7.5, frameon=False, loc="lower right")
    _bare(axR)

    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def _rdm(plan):
    beliefs = [modal_belief(plan, w) for w in range(N)]
    M = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            M[i, j] = fr_distance(beliefs[i], beliefs[j])
    return M


def plot_policies(results, path):
    fig, axs = plt.subplots(1, 3, figsize=(12.5, 4.2),
                            gridspec_kw={"width_ratios": [1.1, 1, 1]})
    po = results["policies"]

    # --- left: the scalar is blind (task-1 return equal; geometry differs) ---
    axL = axs[0]
    groups = ["task-1\nvalue", "terminal\nentropy", "FR path\nfrom prior"]
    ro = [po["reward_only"]["exp_value_task1"], po["reward_only"]["exp_entropy"],
          po["reward_only"]["exp_fr_from_prior"]]
    co = [po["competent"]["exp_value_task1"], po["competent"]["exp_entropy"],
          po["competent"]["exp_fr_from_prior"]]
    x = np.arange(3); w = 0.36
    axL.bar(x - w / 2, ro, w, label="reward-only", color=WARM)
    axL.bar(x + w / 2, co, w, label="competent contact", color=COOL)
    for xi, (a, b) in enumerate(zip(ro, co)):
        axL.text(xi - w / 2, a + 0.02, f"{a}", ha="center", fontsize=7.5, color=INK)
        axL.text(xi + w / 2, b + 0.02, f"{b}", ha="center", fontsize=7.5, color=INK)
    axL.set_xticks(x); axL.set_xticklabels(groups, fontsize=8.5)
    axL.set_title("Task-1 value, entropy, and path length", fontsize=10, color=INK)
    axL.legend(fontsize=8, frameon=False, loc="upper left")
    _bare(axL)

    # --- middle + right: the two representational dissimilarity matrices ---
    Mro = _rdm(REWARD_ONLY_PLAN)
    Mco = _rdm(COMPETENT_PLAN)
    vmax = max(Mro.max(), Mco.max())
    labels = [f"$w_{{{i}}}$" for i in range(N)]
    for ax, M, title, mn in [
        (axs[1], Mro, f"RDM, reward-only policy\n(min sep {po['reward_only_min_separation']})", po["reward_only_min_separation"]),
        (axs[2], Mco, f"RDM, competent-contact policy\n(min sep {po['competent_min_separation']})", po["competent_min_separation"]),
    ]:
        im = ax.imshow(M, cmap="magma", vmin=0, vmax=vmax)
        ax.set_xticks(range(N)); ax.set_xticklabels(labels, fontsize=7)
        ax.set_yticks(range(N)); ax.set_yticklabels(labels, fontsize=7)
        ax.set_title(title, fontsize=9.5, color=INK)
        cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        cb.set_label("Fisher-Rao distance", fontsize=7.5)
        cb.ax.tick_params(labelsize=6.5)

    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_transfer(results, path):
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.2))
    tr = results["transfer"]

    # --- left: zero-shot task-2 value, reward-only at chance ---
    names = ["reward-only", "competent\ncontact"]
    vals = [tr["reward_only_zeroshot_task2"], tr["competent_zeroshot_task2"]]
    bars = axL.bar(names, vals, color=[WARM, COOL], width=0.5)
    axL.axhline(tr["chance_task2"], color=MUTED, ls=(0, (4, 3)), lw=1.2)
    axL.text(0.5, tr["chance_task2"] + 0.015, f"chance {tr['chance_task2']}",
             fontsize=8, color=MUTED, ha="center")
    for b, v in zip(bars, vals):
        axL.text(b.get_x() + b.get_width() / 2, v + 0.01, f"{v}",
                 ha="center", fontsize=9, color=INK)
    axL.set_ylabel("zero-shot task-2 value", fontsize=9)
    axL.set_ylim(0, 1.02)
    axL.set_title(f"Zero-shot task-2 value (gap {tr['transfer_gap']})",
                  fontsize=9.5, color=INK)
    _bare(axL)

    # --- right: value over the two-task family ---
    names2 = ["reward-only", "competent\ncontact"]
    fam = [tr["reward_only_family_value"], tr["competent_family_value"]]
    bars2 = axR.bar(names2, fam, color=[WARM, COOL], width=0.5)
    for b, v in zip(bars2, fam):
        axR.text(b.get_x() + b.get_width() / 2, v + 0.01, f"{v}",
                 ha="center", fontsize=9, color=INK)
    axR.set_ylabel("expected value, task drawn from {A, B}", fontsize=9)
    axR.set_ylim(0, 1.02)
    axR.set_title("Expected value over the two-task family", fontsize=9.5, color=INK)
    _bare(axR)

    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
