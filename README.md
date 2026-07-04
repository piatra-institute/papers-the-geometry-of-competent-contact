# The Geometry of Competent Contact

Reinforcement learning scores a policy by a scalar, the expected return $J(\pi)=\mathbb{E}[R]$. This paper argues that an agent's competent contact with its world is not that scalar but the geometry of how its actions transform its belief over hidden world-states, an object living on the probability simplex under the Fisher-Rao metric that Chentsov's theorem singles out. The central result is a quotient: if reward depends on the world only through a partition $g$, the expected return depends on the belief only through its pushforward $g_\ast b$, so two beliefs at the maximal Fisher-Rao distance can be reward-identical, and the return is blind to everything the belief resolves within a reward-class. On a small active-perception POMDP a reward-only policy and a competent-contact policy attain the identical single-task return while leaving beliefs of very different geometry, and the geometry the return discarded is exactly what lets the competent agent transfer zero-shot to a task the reward never mentioned.

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

Requires `pandoc` and `xelatex` on PATH. From the workspace you can also run
`papers build the-geometry-of-competent-contact`.

Part of [piatra-papers](https://github.com/piatra-institute). See the workspace
docs for the research and writing pipelines.
