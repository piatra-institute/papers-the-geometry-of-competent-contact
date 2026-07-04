# Brief

Written before drafting. See the workspace docs (run `papers docs`): research-pipeline.md §1.

## Question

Reinforcement learning scores a policy by a scalar, J(π) = E[R]. Is that scalar the right object for competence, or is an agent's competent contact with its world better read as the geometry of how its actions transform its belief over world-states?

## Claim

Competence is not scalar. An agent's belief over hidden world-states is a sufficient statistic for control (Åström 1965; Kaelbling, Littman & Cassandra 1998) and lives on the probability simplex, whose only metric invariant under sufficient statistics is Fisher-Rao (Chentsov 1982; Ay et al. 2017). Competent contact is the geometry of how the agent's actions move its belief on this manifold: the contraction of the uncertainty set, the Fisher-Rao length of the belief trajectory, and the task-relevant separability the terminal belief keeps between world-states. The central, provable point is that a scalar return is a quotient of this geometry. If reward depends on the world only through a partition g, the expected return depends on the belief only through its pushforward g_*b, so two beliefs arbitrarily far apart in Fisher-Rao distance can be reward-identical. A reward-only policy therefore resolves only the reward-relevant quotient; a competent-contact policy (infomax on the full world, in the Blackwell/Lindley sense) resolves the world. The two can attain identical single-task return while the competent one alone transfers zero-shot to a task the reward never mentioned. The simulation makes this exact on a small active-perception POMDP.

## Kind

formal-model (ships a simulation). `has_simulation: true`, `claims_target: results.json`.

## Cornerstone literature

- Belief-state / POMDP: Åström (1965), Kaelbling, Littman & Cassandra (1998); Sutton & Barto (2018) for J(π)=E[R].
- Information geometry: Rao (1945), Chentsov (1982), Amari & Nagaoka (2000), Ay, Jost, Lê & Schwachhöfer (2017).
- Value of information / experiments: Blackwell (1953), Lindley (1956); Itti & Baldi (2009), Gottlieb et al. (2013) for active sensing as information gain; Cover & Thomas (2006), Shannon (1948).
- Intrinsic drives and active inference: Klyubin, Polani & Nehaniv (2005) empowerment; Tishby & Polani (2011); Friston et al. (2015) epistemic value.
- Representational geometry: Kriegeskorte, Mur & Bandettini (2008), Kriegeskorte & Kievit (2013).
- Perception as competent world-contact: Gibson (1979), Merleau-Ponty (1945/2012), Dreyfus (2002) on maximal grip, O'Regan & Noë (2001), Uexküll (1934/2010) Umwelt.
