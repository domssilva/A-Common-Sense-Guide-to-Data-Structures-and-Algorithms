# Graphs

[William Fiset - Graph Theory Introduction](https://www.youtube.com/watch?v=eQA-m22wjTQ&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=2)

* node = vertex
* link = edge
* connected vertices are called **adjacent**

## Representing graphs

The most popular and convenient representation of a graph, whether directed or undirected, weighted or unweighted, is an adjacency matrix.

* adjacency matrix
    * lookup is O(1)
    * requires O(v**2) space
* adjacency list
    * efficient edge iteration
    * edge weight lookup O(E)
* edge list
    * efficient edge iteration
    * edge weight lookup O(E)