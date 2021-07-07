# Network Science 
# Chapter 9: Community

  - [intro](#intro)
    - [Hypothesis 1 :](#hypothesis-1-)
  - [community basics](#community-basics)
    - [Hypothesis 2:](#hypothesis-2)
    - [community as a complete subgraph / clique:](#community-as-a-complete-subgraph--clique)
    - [strong and weak communities](#strong-and-weak-communities)
    - [community number](#community-number)
  - [Hierarchical clustering](#hierarchical-clustering)

## intro 

community: group of nodes more likely connecting to each other

### Hypothesis 1 : 
the community structure of a network can be uniquely identified by its adjacency matrix Aij 
(for a network with N nodes, it contains N rows and N columns, with Aij = 1 if a link from j to i exists)

## community basics

### Hypothesis 2:
connectedness: members of a community must be reached through other members
density: members of a community have higher probability to be linked to each other than other community nodes

h2 still allows multiple definitions of a community

### community as a complete subgraph / clique:
all nodes are connected to each other, the community is a compete subgraph

this definition misses legitimate communities 

### strong and weak communities

taking a subgraph of the network, they use the internal and external degrees of each node to assign their community.

strong: for each node the internal degree is superior to the external one

weak: the total internal degree of the community is superior to the total external one

weak communities allow exeptions: certain nodes do not necesarely connect to the community nodes more than to other communities' nodes

### community number

simplest problem: graph bisection, which divideds the network into two distinct subgraphs, with the minimum number of links between the two subgraphs

could answer it with brute force, exploring all possible divisions of the network into 2 graphs and picking the best one. however its too costly.


community dector differ from graph partitioning: 
the number and size of community is not predefined but is uncovered from the network 

its impossible to explore all subgraphs as the number of network partitions grows expotionally with N increasing

## Hierarchical clustering

brute force algorithms evoked earlier have exponential runtime.

 algorithms with a polynomial number of computations with N^x are required to find communities in large networks 

once a similarity matrix xij transcribing the distance between nodes of the network is obtained, agglomerative and divisive algorithms can be used to find communities.
they revolved around the generation of dendograms, hierarchical trees.

### agglomerative procedure: Ravasz Algorithm

two nodes are similar when most their common neighbours account to most of their degree. 

group of nodes with high similarity are put in groups

ravasz uses average link to evaluate group similarity, averaging xij for all pairs belonging to the 2 distinct communities

(single link uses the smallest xij between two nodes belonging each to a different community, and complete link the xij maximum.)


starting from single nodes forming their own communities, ravasz regroups communities with highest similarity first, iteratively ending up with a single community.

the process is tracked by a dendrogram tree, which needs to be cut relevantly 

ravasz's complexity: O(N$^2$)

