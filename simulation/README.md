# Simulation — The Geometry of Competent Contact

Four exact, deterministic studies behind the paper. No random seed: every expectation is computed by enumerating observation outcomes with their predictive probabilities, so the numbers are exact facts about the construction.

```bash
cd simulation
uv run run_all.py      # writes output/results.json and output/figures/*.png
```

Every decimal cited in the paper is a key in `output/results.json` (the `papers claims` gate checks the paper's prose decimals against it).

## The world

A static active-perception POMDP. The hidden world-state is a pair `w = (A, B)` of two independent attributes, `A` in {0,1,2} and `B` in {0,1}, giving `N = 6` states on the belief simplex `Delta^5`. The agent holds a belief `b` over `w` and acts by choosing probes: an A-probe reports `A` through a confusion channel (correct with probability `q_A = 0.8`), a B-probe reports `B` (correct with probability `q_B = 0.85`). Each probe outcome updates the belief by Bayes' rule, a map on the simplex. Task 1's reward depends on `w` only through `A`; task 2's only through `B`. The two tasks are cross-cutting quotients of one world.

## The geometry

Chentsov's theorem forces the Fisher-Rao metric on the belief simplex; the map `b -> 2*sqrt(b)` is an isometry onto a radius-2 sphere, geodesic distance `d(b,b') = 2*arccos(sum_i sqrt(b_i b'_i))`, constant curvature 1/4. This holds in every dimension, so it applies to the belief over the 6 states.

## What it computes

`analyses.py`

- **`study_manifold`** — the self-test and the quotient proposition. `gaussian_curvature` (Brioschi formula, numerical partials) fed the Fisher metric on a 3-state marginal simplex returns 0.25 with maximum deviation 0.0, certifying the machinery. Two beliefs concentrated on `(0,0)` and `(0,1)` sit at Fisher-Rao distance 3.14 (the diameter, disjoint support), share task-1 value 1.0, and take opposite task-2 decisions (cross-value 0.0).
- **`study_probe_value`** — task-1 value against the number of A-probes (diminishing returns); the marginal task-1 value of a B-probe is 0.0. Mutual information: an A-probe carries 0.4596 nats about `A` and 0.0 about `B`.
- **`study_policies`** — the reward-only policy (2 A-probes) and the competent-contact policy (2 A-probes + 2 B-probes) attain the identical task-1 value 0.8 (gap 0.0), yet differ in geometry: terminal entropy 1.0945 vs 0.679 nats, Fisher-Rao path from the prior 1.282 vs 1.6161. The representational dissimilarity matrix (Fisher-Rao distances between terminal beliefs indexed by the true world-state) has minimum off-diagonal separation 0.0 for the reward-only policy (B-twins collapse) against 2.4429 for the competent policy. Net of a 0.05 per-probe cost, the reward-only policy nets 0.7 on task 1 against the competent policy's 0.6.
- **`study_transfer`** — zero-shot task-2 value (no further probing): reward-only 0.5 (chance), competent 0.85, transfer gap 0.35. Over a task family drawing reward from either attribute: 0.65 vs 0.825.

`figures.py` (pure plotters, recompute belief geometry and read scalars from the results dict)

- `output/figures/manifold.png` — the world as a 2x3 grid with its two cross-cutting quotients, and task-1 value vs number of A-probes.
- `output/figures/policies.png` — equal task-1 return with different geometry, and the two representational dissimilarity matrices side by side.
- `output/figures/transfer.png` — zero-shot task-2 value and competence over the task family.

## Status

Complete. The geometry is not stipulated: the Fisher-Rao metric is forced by Chentsov's theorem and the curvature self-test recovers the known value exactly. The reward-is-a-quotient proposition needs no tuning. The policies are hand-specified to isolate the phenomenon (both take the same 2-probe A-budget; only the competent one also probes B); the exact fact carrying the argument is that a B-probe has zero task-1 value. Dependencies: `numpy` and `matplotlib` (see `pyproject.toml`).
