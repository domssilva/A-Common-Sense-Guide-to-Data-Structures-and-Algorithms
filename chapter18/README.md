# Graphs

[William Fiset - Graph Theory Introduction](https://www.youtube.com/watch?v=eQA-m22wjTQ&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=2)

* node = vertex
* link = edge
* connected vertices are called **adjacent**

## Representing graphs

The most popular and convenient representation of a graph, whether directed or undirected, weighted or unweighted, is the adjacency list.

* adjacency matrix
    * lookup is O(1)
    * requires O(v**2) space
* adjacency list
    * efficient edge iteration
    * edge weight lookup O(E)
* edge list
    * efficient edge iteration
    * edge weight lookup O(E)

The adjacency list is a "hybrid" between an adjacency matrix and an edge list.
There are different ways of actually implementing the adjacency list

* hash table: associates each vertex with an array of adjacent vertices
* singly linked list: each vertex points to a linked list of the neighboring vertices
* object oriented approach: each Vertex is an object containing a list of references of the neighboring vertices