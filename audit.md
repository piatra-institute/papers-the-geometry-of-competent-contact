# Audit

Dated log of editorial passes and verification runs. Newest first. See the workspace docs (run `papers docs`): writing-pipeline.md §7.

## 2026-07-04 — initial full build

Scope: first complete build from the seed chat. Wrote the simulation, the paper, and all provenance docs; brought the paper to a clean `check => PASS`.

Thesis: reinforcement learning scores a policy by a scalar, J(π)=E[R], but competent contact with a world is the geometry of how an agent's actions transform its belief over hidden world-states, an object on the Fisher-Rao simplex. The load-bearing result is the reward-is-a-quotient proposition: if reward factors through a partition g of the world, the Bayes value depends on the belief only through the pushforward g_*b, so beliefs at the maximal Fisher-Rao distance π can be reward-identical, and the return is blind to the belief's finer geometry. That discarded geometry is what transfers to a new task.

Distilled from the seed's sprawl (fuzzy geometry, polycomputation, Levin/Hoel, sheaf-gluing/"epiplexity") to the single most defensible core: perception as active geometrical reduction of belief-uncertainty, formalized rigorously with belief-state POMDP + information geometry + Blackwell/value-of-information, and grounded in the phenomenology of competent world-contact (Gibson, Merleau-Ponty/Dreyfus grip, O'Regan & Noë, Uexküll). The seed's polycomputation/observer-relativity survives only as the bounded, defensible §6 point: the belief manifold is over the agent's own hypothesis space (Umwelt-relativity), stated as a positive claim, not sheaf overreach.

Changes:

- simulation/: three modules (analyses.py + figures.py + run_all.py), numpy + matplotlib(Agg), `uv run run_all.py` -> output/results.json + 3 figures. Four exact, deterministic studies (no seed; expectations computed by enumerating observation outcomes with predictive weights): manifold (Fisher-Rao curvature self-test returns 0.25, max dev 0.0; the quotient proposition exhibited at FR distance 3.14); probe_value (B-probe marginal task-1 value 0.0; I(A-probe;A)=0.4596 nats, about B = 0.0); policies (reward-only vs competent-contact, equal task-1 value 0.8, entropy 1.0945 vs 0.679, FR path 1.282 vs 1.6161, RDM min separation 0.0 vs 2.4429); transfer (zero-shot task-2 0.5 vs 0.85, gap 0.35; family value 0.65 vs 0.825; net-of-cost task-1 0.7 vs 0.6).
- paper/PAPER.md: 6 sections. The Return and the Grip; The Belief Simplex Is the Arena (Åström/Kaelbling belief-state, Chentsov/Rao/Amari-Nagaoka/Ay geometry, curvature self-test); Reward Is a Quotient (Proposition 1 + proof, Blackwell); Two Policies the Return Cannot Tell Apart (Lindley/Itti&Baldi infomax, Kriegeskorte RDM); What the Discarded Geometry Was Worth (transfer, empowerment/active-inference distinctions); Contact Is Always with a Carved World (Uexküll Umwelt-relativity, folded limits, substantive close). No ceremonial "what the model cannot do" closer.
- metadata.yaml: title/header/date "July 2026", has_simulation true, claims_target results.json, abstract filled, status built.
- brief.md, research.md (tiered T1/T2, all bib fields verified via subagent against DOIs/Project Euclid/publisher pages), sources.md (23 frozen entries), README.md, simulation/README.md.

Citation verification (subagent pass, 2026-07-04): all 23 sources verified real with exact fields. Corrections applied: "maximal grip" attributed to Dreyfus (2002) glossing Merleau-Ponty, not to Merleau-Ponty directly; empowerment cited to the IEEE CEC 2005 paper (pp. 128-135); Kriegeskorte, Mur & Bandettini rendered "P. A." and article number 4; O'Regan & Noë target-article pages 939-973; Rao 81-91; Friston et al. 187-214.

Verification:

- voice: 0 errors, 3 review-candidate warns (two negate-pivot and one inline-contrastive, all the reward-vs-geometry contrast the paper develops; legitimate). Advisories: "exactly" reduced 8 -> 1; rhythm 11% short (sd 17), one residual long-run flag that is the raw-LaTeX proof block read as a single sentence by the splitter (artifact), not a real monotony.
- refs: 22 cited / 22 bib / 0 missing / 0 unused. (Åström is gate-invisible on both sides due to the leading Å; real and correctly attributed.)
- claims: 23 decimal claims, 0 without a matching simulation value.
- build: 10 pages, 3 figures embedded, Proposition/Proof (amsthm) render with QED box, diacritics (Åström, Noë, Lê, Uexküll) and math render, 0 missing-character warnings.
- check => PASS.

Notes / deferred:

- The policies are hand-specified to isolate the phenomenon (shared 2-probe A-budget; competent adds 2 B-probes), not derived as optima; stated plainly in §6. The exact robust fact carrying the argument is the B-probe's zero task-1 value, independent of the probe counts.
- Numbers are facts about the construction (channel hit rates q_A=0.8, q_B=0.85; probe cost 0.05), not measurements or forecasts.
- Status is `built`, not `published`: sync + page.tsx + git repo creation left to the maintainer.
