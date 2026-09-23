# The Geometry of Competent Contact

What a Scalar Return Cannot See in an Agent's Grip on the World.

Reinforcement learning scores a policy by a single number, the expected return $J(\pi)=\mathbb{E}[R]$, and treats everything an agent does as a means to that scalar. In competent action, such as a hand turning a cup to read its shape or a robot tapping a surface to tell metal from plastic, what improves is the agent's grip on the world: the way its uncertainty about hidden states collapses into task-relevant structure. The agent's belief over world-states is a sufficient statistic for control and lies on the probability simplex, where Chentsov's theorem singles out the Fisher-Rao metric, so the movement of belief has a determined geometry. Competent contact is measured on that geometry by the contraction of uncertainty, the Fisher-Rao length of the belief trajectory, and the separation the terminal belief keeps between world-states. If reward depends on the world only through a partition $g$, the expected return depends on the belief only through its pushforward $g_\ast b$, so two beliefs at the maximal Fisher-Rao distance $\pi$ can be reward-identical. In an exactly solvable active-perception POMDP, a reward-only policy and a competent-contact policy attain the same single-task return of 0.8 but leave terminal entropies of 1.09 and 0.68 nats; world-states differing only in the reward-irrelevant attribute collapse to Fisher-Rao distance 0.0 under the reward-only policy, while the competent policy keeps all six at least 2.44 apart. On a second task the first reward never mentioned, the reward-only agent scores at chance, 0.5, and the competent agent 0.85, a gap of 0.35 invisible to the single-task return.

## Contents

- `paper/PAPER.md` — the paper (6 sections + references).
- `simulation/` — four exact, deterministic studies: the Fisher-Rao curvature self-test, the reward-is-a-quotient proposition, the reward-only vs competent-contact policy comparison, and zero-shot transfer. Every numeric claim in the paper is a key in `simulation/output/results.json`.
- `brief.md`, `research.md`, `sources.md`, `audit.md` — the working memory (scope, tiered findings, frozen bibliography, build log).

## Reproduce

```bash
cd simulation
uv run run_all.py          # writes output/results.json and output/figures/*.png
```

Deterministic: expectations are computed by enumerating observation outcomes with their predictive probabilities, so there is no sampling and no seed. Dependencies are `numpy` and `matplotlib` (see `simulation/pyproject.toml`).

## Build

```bash
uv run build.py          # -> paper/PAPER.pdf  (vendored canonical recipe)
```

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run `papers build the-geometry-of-competent-contact`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace docs for the research and writing pipelines.
