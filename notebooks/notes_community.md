# Network Science 
# Chapter 9: Community

- [Network Science](#network-science)
- [Chapter 9: Community](#chapter-9-community)
  - [intro](#intro)
    - [Hypothesis 1 :](#hypothesis-1-)
  - [community basics](#community-basics)
    - [Hypothesis 2:](#hypothesis-2)
    - [community as a complete subgraph / clique:](#community-as-a-complete-subgraph--clique)
    - [strong and weak communities](#strong-and-weak-communities)
    - [community number](#community-number)
  - [Hierarchical clustering](#hierarchical-clustering)
    - [agglomerative procedure: Ravasz Algorithm](#agglomerative-procedure-ravasz-algorithm)
    - [divisive procedure: girvan-newman](#divisive-procedure-girvan-newman)
    - [hierarchy in real networks](#hierarchy-in-real-networks)
  - [Modularity](#modularity)
    - [hypothesis 3:](#hypothesis-3)
    - [hypothesis 4](#hypothesis-4)
    - [greedy algorithm](#greedy-algorithm)
    - [limitation](#limitation)
  - [overlapping communities](#overlapping-communities)
    - [clique percolation](#clique-percolation)
    - [link clustering](#link-clustering)

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

weak communities allow exceptions: certain nodes do not necessarily connect to the community nodes more than to other communities' nodes

### community number

simplest problem: graph bisection, which divides the network into two distinct subgraphs, with the minimum number of links between the two subgraphs

could answer it with brute force, exploring all possible divisions of the network into 2 graphs and picking the best one. however its too costly.


community dector differ from graph partitioning: 
the number and size of community is not predefined but is uncovered from the network 

its impossible to explore all subgraphs as the number of network partitions grows exponentially with N increasing

## Hierarchical clustering

brute force algorithms evoked earlier have exponential runtime.

 algorithms with a polynomial number of computations with N^x are required to find communities in large networks 

once a similarity matrix xij transcribing the distance between nodes of the network is obtained, agglomerative and divisive algorithms can be used to find communities.
they revolved around the generation of dendrograms, hierarchical trees.

### agglomerative procedure: Ravasz Algorithm

two nodes are similar when most their common neighbours account to most of their degree. 

group of nodes with high similarity are put in groups

ravasz uses average link to evaluate group similarity, averaging xij for all pairs belonging to the 2 distinct communities

(single link uses the smallest xij between two nodes belonging each to a different community, and complete link the xij maximum.)


starting from single nodes forming their own communities, ravasz regroups communities with highest similarity first, iteratively ending up with a single community.

the process is tracked by a dendrogram tree, which needs to be cut relevantly 

ravasz's complexity: O(N$^2$)

### divisive procedure: girvan-newman

xij is now centrality, being higher when i and j belong to different communities

link betweenness is a measure of centrality defined by the number of shortest path between all nodes going through i and j.

links with highest centrality are  removed one by one 

a dendrogram of the progressive link removal is obtained and needs to be cut


### hierarchy in real networks

two problems arise:
communities are seen as subgraphs of a larger one in the dendrogram, is it just the product of our algorithms ? 

in a scale free network (few nodes have exponential number of links)
are the communities identified as subgraphs independent if they are always linked by a hub ? 

scale free network 
https://www.futurelearn.com/info/courses/complexity-and-uncertainty/0/steps/1855


a scale free hierarchical network composed of small communities forming increasingly larger ones is built.

the higher a node's degree, the smaller its clustering coefficient


> Any cut of the dendrogram offers a potentially valid partition 

however for large networks a visual separation is not possible.

## Modularity 

### hypothesis 3:
randomly wired networks don't have communities

to evaluate the strength of a community we can compare its deviation to a randomly formed network: its modularity

The modularity Mc of a community compares the quality of the links Lc between its node Aij to the one of the network randomly rewired pij 

a simple formula based on the number of links Lc between a community nodes and their total degree

the modularity can be extended to the whole graph by summing over all communities


modularity can be used to cut the dendrogram of hierarchical clustering algorithms 

### hypothesis 4

the optimal community structure has the maximum modularity 

as there is often too many partitions to inspect, bruteforce is not an options

### greedy algorithm 

starting with single community nodes, merge the communities with highest modularity difference for the whole network until all are merged into a single community.
keeping the partition with highest modularity 

the algorithm can further be used to find subcommunities, treating each community as its own network.

### limitation

increasing modularity can force merge small communities, needing only a single link between two otherwise distinct communities. This happens with small communities, when both have a small total node degree, below a certain threshold: $\sqrt{2L}$


It can be hard to distinguish the best partition using the max modularity. 
Merging communities together can lead to small modularity change.

The modularity function has a high plateau instead of a clear peak.
which explain why algorithm can quickly find a partition with a modularity close to the max


## overlapping communities 

some nodes must belong to different communities simultaneously

this means that communities could overlap in some node instead of being strictly separated

### clique percolation 

the algorithm identifies communities as adjacent k-cliques (they are when they share k-1 nodes)
two k-clique that do not reach belong to different communities

nodes that belong to k-cliques belonging to different communities allow them to overlap 

however, when studying random networks, in sufficiently dense ones large k-cliques naturally emerge

### link clustering