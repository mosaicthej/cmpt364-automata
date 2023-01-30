# Pattern Matching

We can view pattern matching as an instance of DFA, which it accepts a string if and only if there is a sequence of transitions from the start state to an accepting state that consumes the input string.

## Example

Consider the following DFA that accepts only strings {"coffee", "coille"}

```svg

```

## Variations on Finite Automata

### With output

Can have output more than just accepting or rejecting a string.

#### Moore Machine

$$
\begin{aligned}
\text{Definition:} \\
\text{A Moore machine is a 5-tuple } M = (Q, \Sigma, \Delta, \delta, \lambda, q_0)\\
\text{where:} \\
Q, \Sigma, \delta, q_0 \text{ are as in a DFA} \\
\end{aligned}
$$