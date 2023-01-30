# Formal Language

## Alphabet

### Definition

- A finite, non-empty set of symbols is called an alphabet.
- use $\Sigma$ or $\mathcal{A}$ to denote an alphabet.

### String

- A finite sequence of symbols from an alphabet is called a **string**.

#### Empty String

$\varepsilon$ is the empty string. Consists of no symbols.

#### Length

The length of a string s over an alphabet $\Sigma$ is denoted by $|s|$.

Denote by $\Sigma^n$ the set of all strings of length n over alphabet $\Sigma$.

Example:
If $\Sigma = \{a, b\}$, then 
$\Sigma^3 = \{aaa, aab, aba, abb, baa, bab, bba, bbb\}$
$\Sigma^0 = \{\varepsilon\}$

$\Sigma^*$ is the set of all strings over alphabet $\Sigma$.
$\Sigma^*$ = $\Sigma^0 \cup \Sigma^1 \cup \Sigma^2 \cup \Sigma^3 \cup ...$

**Note**: $\Sigma^*$ is not a finite set.

proof (by contradiction):
$$
\begin{aligned}
\text{Assume } \Sigma^* \text{ is finite.} \\
\text{Then there exists a length n such that } \Sigma^n \text{ is finite.} \\
and | \Sigma^n | = n \\
\text{But } \Sigma^n \text{ is a finite set, so } | \Sigma^n | \leq n \\


\end{aligned}
$$

### Language

A language is a set of strings over an alphabet $\Sigma$.

#### Let $\Sigma$ be an alphabet, if $L \subseteq \Sigma^*$, then $L$ is a language over $\Sigma$.

A language is any set of strings.

#### Example

- $\{a, b, ab, ba, aa, bb, aaa, bbb, aab, abb, bab, bba, aaaa, bbbb, ... \}$ is a language over alphabet $\Sigma = \{a, b\}$.
- $\{00, 111, 101\}$ is a language over alphabet $\Sigma = \{0, 1\}$.
- $\emptyset$ is a language over any alphabet.
- $\epsilon$ is a language over any alphabet.
- $\Sigma^*$ is a language over any alphabet $\Sigma$.

## Languages

### Relevance of language

- How do language pertain to real problems?
- Each language naturally provides yes/no questions.

### Membership Problem

Yes/No question about a language.

$$
\begin{aligned}
\text{The membership problem for a language } \\
\text{Given a string } w \in \Sigma^*\text{, is } w \in L \text{?} \\
\end{aligned}
$$

#### Examples

- Is the C program $w$ syntactically correct?
  The language is the set of all syntactically correct C programs.
  This is same asking if $w$ $\in$ L.
  L is the set of all syntactically correct C programs.

## Principle

$$
\begin{aligned}
\text{Languages are computations.} \\
\end{aligned}
$$