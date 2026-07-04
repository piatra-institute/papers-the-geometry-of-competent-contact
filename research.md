# Research

Findings, tiered by source proximity. See the workspace docs (`papers docs`): research-pipeline.md §2.
T1 primary · T2 authoritative secondary · T3 reference · T4 general web (leads only).
Every claim in the paper rests on a T1/T2 source. All bibliographic details below verified against publisher pages / DOIs / Project Euclid / official journal archives.

## The scalar objective and the belief-state

- [T2] Sutton & Barto (2018), *Reinforcement Learning: An Introduction* (2nd ed.), MIT Press — the RL objective is the expected return, a scalar (their Ch. 3). "J(π)" is policy-gradient convention, not their exact symbol; used as a formalization, not quoted as theirs.
- [T1] Åström (1965), *J. Math. Anal. Appl.* 10(1), 174–205, doi:10.1016/0022-247X(65)90154-X — the posterior over hidden states is a sufficient statistic for optimal control in a partially observed Markov process. Origin cite for the belief-state. (Åström appends "I" to his own title; a Part II followed in 1969.)
- [T1] Kaelbling, Littman & Cassandra (1998), *Artificial Intelligence* 101(1–2), 99–134, doi:10.1016/S0004-3702(98)00023-X — the POMDP as a belief-state MDP; the belief lives on the simplex and actions are maps on it.

## The forced geometry of the simplex

- [T1] Rao (1945), *Bull. Calcutta Math. Soc.* 37, 81–91 — Fisher information read as a Riemannian metric on a family of distributions (pages 81–91, not 81–89).
- [T1] Chentsov (1982), *Statistical Decision Rules and Optimal Inference*, TMM 53, AMS (Russian original 1972) — on a finite sample space the Fisher-Rao metric is, up to scale, the unique metric invariant under Markov morphisms (sufficient statistics).
- [T1] Amari & Nagaoka (2000), *Methods of Information Geometry*, TMM 191, AMS/OUP — the map p ↦ 2√p carries the simplex isometrically onto a radius-2 sphere; geodesic distance d(p,q)=2·arccos(Σ√(p_i q_i)); constant curvature 1/4.
- [T1] Ay, Jost, Lê & Schwachhöfer (2017), *Information Geometry*, Ergebnisse 64, Springer, doi:10.1007/978-3-319-56478-4 — the general-manifold extension of the Chentsov uniqueness result (invariance of the Fisher metric / Amari-Chentsov tensor beyond finite sample spaces). Cited for the general statement; no pinpoint theorem number verified.

## Value of information and the comparison of experiments

- [T1] Blackwell (1953), *Ann. Math. Stat.* 24(2), 265–272, doi:10.1214/aoms/1177729032 — one experiment is sufficient for (more informative than) another iff it is weakly preferred in every decision problem for every loss. The partial order used for "sufficiency for the world vs sufficiency for the task."
- [T1] Lindley (1956), *Ann. Math. Stat.* 27(4), 986–1005, doi:10.1214/aoms/1177728069 — expected information of an experiment as the expected reduction in Shannon entropy of the posterior. The infomax objective the competent-contact policy uses.
- [T1] Itti & Baldi (2009), *Vision Research* 49(10), 1295–1306, doi:10.1016/j.visres.2008.09.007 — Bayesian surprise = KL divergence from prior to posterior; the information-theoretic measure of a belief's movement under an observation.
- [T2] Gottlieb, Oudeyer, Lopes & Baranes (2013), *Trends Cogn. Sci.* 17(11), 585–593, doi:10.1016/j.tics.2013.09.001 — review tying active sensing / curiosity to information gain.
- [T2] Cover & Thomas (2006), *Elements of Information Theory* (2nd ed.), Wiley — mutual information, KL, channel capacity currency.
- [T1] Shannon (1948), *Bell System Technical Journal* 27(3), 379–423; 27(4), 623–656 — channel capacity (used for empowerment).

## Intrinsic drives and active inference (neighbors to distinguish)

- [T1] Klyubin, Polani & Nehaniv (2005), "Empowerment: A universal agent-centric measure of control," *Proc. 2005 IEEE CEC* vol. 1, 128–135, doi:10.1109/CEC.2005.1554676 — empowerment = channel capacity of the action→sensor channel. The canonical definitional cite (the ECAL "All else being equal be empowered" paper is the maxim framing). Distinguished from competent contact: empowerment measures controllability of the sensory future, not resolution of world-structure.
- [T2] Tishby & Polani (2011), "Information theory of decisions and actions," in *Perception-Action Cycle*, 601–636, Springer, doi:10.1007/978-1-4419-1452-1_19 — information-theoretic formulation of the perception-action cycle.
- [T1] Friston, Rigoli, Ognibene, Mathys, Fitzgerald & Pezzulo (2015), *Cognitive Neuroscience* 6(4), 187–214, doi:10.1080/17588928.2015.1020053 — expected free energy carries an epistemic (information-gain) term that drives uncertainty-reducing action. (Pages 187–214, not 187–224.)

## Representational geometry

- [T1] Kriegeskorte, Mur & Bandettini (2008), *Frontiers in Systems Neuroscience* 2, 4, doi:10.3389/neuro.06.004.2008 — representational similarity analysis; the representational dissimilarity matrix. (Article number 4; third author rendered "P. A.")
- [T2] Kriegeskorte & Kievit (2013), *Trends Cogn. Sci.* 17(8), 401–412, doi:10.1016/j.tics.2013.06.007 — representational geometry; task-relevant separability of representations.

## Perception as competent world-contact

- [T1] Gibson (1979), *The Ecological Approach to Visual Perception*, Houghton Mifflin — affordances; perception as active pickup of information, not passive reception.
- [T1] Merleau-Ponty (1945/2012), *Phenomenology of Perception* (Landes, Trans.), Routledge — perception tends toward an optimal hold, the body "geared into" the world.
- [T1] Dreyfus (2002), *Phenomenology and the Cognitive Sciences* 1(4), 367–383, doi:10.1023/A:1021351606209 — glosses Merleau-Ponty as "maximal grip," the body's tendency to reduce perceptual disequilibrium toward an optimal grip. IMPORTANT: "maximal grip" is Dreyfus's phrase, not verbatim Merleau-Ponty; attributed accordingly.
- [T1] O'Regan & Noë (2001), *Behavioral and Brain Sciences* 24(5), 939–1031 (target article 939–973) — seeing as the exercise of mastery of sensorimotor contingencies.
- [T1] Uexküll (1934/2010), *A Foray into the Worlds of Animals and Humans* (O'Neil, Trans.), Univ. of Minnesota Press — the Umwelt; each agent inhabits a world carved by its own functional cycles. Grounds the Umwelt-relativity of the belief manifold.

## Notes for drafting

- The reward-is-a-quotient proposition is elementary (a one-line marginalization) but load-bearing; state it as a proposition, prove it, exhibit it in the sim (two beliefs at FR distance π, reward-identical for task 1, opposite for task 2).
- Do NOT overclaim the simulation. The policies are hand-specified to isolate the phenomenon (both take the same 2-probe A-budget; only the competent one also probes B). The exact, robust fact carrying the argument is that a B-probe has exactly zero task-1 value, so no task-1 maximizer takes one.
- Numbers are facts about the construction, not measurements. State stipulations (channel hit rates q_A=0.8, q_B=0.85; probe cost 0.05) plainly.
