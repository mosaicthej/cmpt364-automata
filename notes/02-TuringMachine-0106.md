# Turing Machine

## Introduction

A Turing Machine:

- Starts with input encoded on a tape.
- Has finite number of **states**. At each time step, the machine is in some particular state.

At each step, the machine can:

### Based on

1. The current state
2. Current symbol under the head

### Do

1. Switch to a new state
2. Change symbol under the head
3. Move the head left or right

### Turing-Completeness

Anything that can be translated into a Turing Machine can be computed by a Turing Machine.

## Mathematical Model

### Models in this course

- finite automata
- regular expressions
- context-free grammars

For each model, describe mathematically:

- we can give a precise definition of what it means to be a computation
- we can determine what computations are possible
- we can determine what computations are impossible
- the relationship to other models
- we can see how we compute with the model

## Algorithm

### Wang Tiles

For sure can work: One type tile with 4 same colors.
For sure not work: One type tile with 4 different colors.

However, this is not an algorithm because it does not describe how to solve the problem.

Wang Tile is actually undecidable. The worst time complexity is at infinity.

## Math Preliminaries

### Set Theory

### Graph Theory
