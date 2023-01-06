# Automata and Formal Languages

## Introduction

read the syllabus.

## What is Computation?

Computations occurs everywhere. (e.g. in the brain, in the computer, in the universe)

### Definition: *Information Processing*

Changing(*processing*) of information in any manner detectable by an observer. A process which describes everything happens(*changes*) in the universe. Falling of a rock (change in position), printing a letter (change in the state of the paper), etc.

### Definition: *Algorithm*

Many different vague and informal definitions of algorithm.

An ordered sequence of effective instructions (and terminates?)

## Turing Machines

- Starts with input encoded on a tape.
- Has finite number of **states**. At each time step, the machine is in some particular state.

At each step, the machine can:

### Based on

1. The current state
2. The current symbol under the head

### Do

1. Switch to a new state
2. Change the symbol under the head
3. Move the head left or right

### Church-Turing Thesis

Any algorithm can be implemented by a Turing machine. (Turing machine is universal)

