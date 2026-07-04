"""Orchestrator: reproduces every number and figure in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/. Every numeric value cited in the
paper is a key in the JSON file. All four studies are deterministic: expectations
are computed by enumerating observation outcomes with their predictive
probabilities, so there is no sampling and no seed.
"""
from __future__ import annotations

import json
from pathlib import Path

from analyses import run
from figures import plot_manifold, plot_policies, plot_transfer

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_manifold(results, str(OUT / "figures" / "manifold.png"))
    plot_policies(results, str(OUT / "figures" / "policies.png"))
    plot_transfer(results, str(OUT / "figures" / "transfer.png"))

    m, pv, po, tr = (results["manifold"], results["probe_value"],
                     results["policies"], results["transfer"])
    print(f"manifold: curvature self-test {m['curvature_mean']} "
          f"(expected 0.25, max dev {m['curvature_max_abs_dev_from_quarter']}); "
          f"quotient beliefs at FR distance {m['quotient_fr_distance']}, "
          f"task-1 value {m['quotient_value_task1_b00']}={m['quotient_value_task1_b01']}, "
          f"task-2 decisions {m['quotient_task2_decision_b00']} vs "
          f"{m['quotient_task2_decision_b01']} (cross-value {m['quotient_task2_cross_value']})")
    print(f"probe:    B-probe marginal task-1 value {pv['value_task1_marginal_of_Bprobe']}; "
          f"I(A-probe;A)={pv['mi_Aprobe_about_A_nats']} nats, about B={pv['mi_Aprobe_about_B_nats']}")
    print(f"policies: task-1 return reward-only {po['reward_only']['exp_value_task1']} "
          f"= competent {po['competent']['exp_value_task1']} (gap {po['task1_return_gap']}); "
          f"entropy {po['reward_only']['exp_entropy']} vs {po['competent']['exp_entropy']}; "
          f"min separation {po['reward_only_min_separation']} vs {po['competent_min_separation']}")
    print(f"transfer: zero-shot task-2 reward-only {tr['reward_only_zeroshot_task2']} "
          f"(chance {tr['chance_task2']}) vs competent {tr['competent_zeroshot_task2']}; "
          f"gap {tr['transfer_gap']}")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
