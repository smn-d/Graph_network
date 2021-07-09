# SBM

## Stochastic block model: first steps

### a stochastic multigraph has nodes and relations

on a digraph, the adjacency matrix keeps track of the ties from a node to an other for a single relation

for multigraphs, the adjacency array is a vector of the adjacency matrix for all relations

the probability distribution X of a random adjacency array is called the stochastic multigraph

### stochastic block model requires more conditions

independence of the random vectors Xij
interchangeability of the nodes belonging to the same block

graphs obtained with functions from stochastic block models share their node distribution

A subset of a SBM is also one

## High level description

In an SBM, nodes are divided in different blocks.
Each block is characterized by the probability of its nodes to connect with other blocks' nodes and nodes of its own block.

The actual number of connections between nodes is random: usually drew from the poisson model.


