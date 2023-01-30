# Finite Automata

- A state captures a description of the process at one particular point moment in time.
- States can change via **transitions** in response to various *events*, *stimuli*, or *inputs*.

$$
\begin{aligned}
\text{Example:} \\
\text{Consider first a light switch.} \\
\text{At any given moment, the light switch is either in the} \\
\text{on position or the off position.} \\

\end{aligned}
$$

## Drawing Finite Automata

- A finite automaton is a directed graph with two kinds of nodes:
  - **States** (vertices)
  - **Transitions** (edges)
  - On each transition, there is a label that indicates the input symbol that causes the transition to occur.
  - Usually, we need a single state as the **start state** and some states as the **accepting states**, which are the states the automaton requires to be in for the automaton to accept the input string.

$$
\begin{aligned}
\text{Definition:} \\
\text{A deterministic finite automaton (DFA)} \\
\text{is a 5-tuple } M = (Q, \Sigma, \delta, q_0, F) \\
\text{where:} \\
\text{Q is a finite set of states,} \\
\Sigma\text{ is a finite input alphabet,} \\
\delta: Q \times \Sigma \rightarrow Q \text{ is the transition function,} \\
q_0 \in Q \text{ is the start state,} \\
F \subseteq Q \text{ is the set of accepting states.} \\
\end{aligned}
$$

## Acceptance

- A DFA accepts a string if and only if there is a sequence of transitions from the start state to an accepting state that consumes the input string.
- The DFA accepts the string if the final state is an accepting state, and
- The DFA does not accept the string if the final state is not an accepting state.

### Proof

Let M be a DFA and $L(M)$ be the language accepted by M.

Let $R = \{w\}$ be the set of all strings that M accepts. where $w = a_1a_2 \cdots a_n$ be a string over the alphabet $\Sigma$ that M accepts.

We need to show that $R = L(M)$.
