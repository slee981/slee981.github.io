---
title: "Networks (Part I) - Notation"
author: Stephen Lee
layout: post

categories: [Networks]
tags: [Networks]
toc: true
katex: true
---

## Audience 

I assume you know what a network is, some areas where they appear (e.g. social media connection graphs, airline routes, supply chain logistics, etc.), and are familiar with or curious about formalizing these relationships mathematically. 

Consider this post more of a "cheatsheet" rather than a tutorial. This draws heavily from the textbook "Social and Economic Networks" by Matthew O. Jackson, although the notation is fairly standard and similar to what you'd see in a book on algorithms. 

## Overview

Causal inference on network structures is notoriously difficult. This is due (at least in part) to the complicated web of interactions, and the resulting spillovers (i.e. externalities) violate assumptions for the "potential outcomes" approach to inference ([click for more]({% post_url 2021-07-13-what-is-potential-outcomes %})). For example, suppose you are studying a supply chain fulfilment network, and are wondering which facility or facilities, if upgraded, would improve the network's capacity the most. Because of the interconnected routing decisions, the answer is not at all obvious. 

This post will (hopefully) kick off a series of posts that explore how to measure and analyze network structures. 

## Setup and Definitions

Consider the following network graph.

<img src="{{ 'assets/images/networks/network-simple.svg' | relative_url }}" alt="scatter" width="150"/>

### Nodes 

Let $$N = \{1, ..., n\}$$ be a set of **nodes** in a network. These nodes (also called vertices) could be individuals, companies, fulfilment centers, or nearly any other object. A node is the basic unit of analysis, and the main focus is on the relationships between these nodes. 

### Edges 

Nodes are connected by **edges**. Edges can represent a friendship between two people, a link between webpages, and so on. Importantly, edges can be either **directed** or **undirected**. In a directed network, the order matters, and relationships are not necessarily reciprocal - so some webpage A can link to webpage B, but webpage B might not link to webpage A. By contrast, in an undirected network these relationships are symmetric. 

Additionally, edges may be **weighted** or **unweighted**. An unweighted edge represents a simple binary connection, whereas a weighted edge may represent some magnitude of the relationship, for example, the amount of money traded between two banks. 

### Network Graphs

Given a network, there are multiple ways to express it, and which one you choose depends on your use case. For most of what follows, I will focus on the matrix representation, as it naturally lends itself to matrix algebra, which will be useful later on. However, where there are very few edges relative to the number of nodes (i.e. the network is *sparce*), a matrix will likely not be a very efficient way of storing or processing the information. 

#### Matrix Notation 

The figure above shows an undirected network graph with four (4) nodes and three unweighted edges. We can represent this graph, $$g$$, in matrix form as follows: 

$$
g = \begin{bmatrix}
0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\ 
1 & 0 & 0 & 0
\end{bmatrix} 
$$

By convention, the edge connecting node 1 to node 4 is represented by a "1" in the first row, fourth column. Similarly, the edge representing the connection from node 4 back to node 1 is captured by a "1" in the fourth row, first column. Note also that in this case, "self-edges" are denoted as "0" i.e. we don't count an edge from a node back to itself. This choice is unimportant for this example, but may matter depending on your specific use case. 

The figure below shows a directed network with weighted eges. For example, we can imagine this as a group of friends settling a bet. 

<img src="{{ 'assets/images/networks/network-weighted-directed.svg' | relative_url }}" alt="scatter" width="150"/>

Similar to the first graph, we can represent this in matrix form as follows. 

$$
g = \begin{bmatrix}
    0 & 0 & 0 & 9 \\
    8 & 0 & 7 & 0 \\
    0 & 0 & 0 & 0 \\ 
    0 & 0 & 0 & 0
\end{bmatrix} 
$$

#### Other Notation

The following notations are often used in computational settings when implementing algorithms on graphs (e.g. depth-first search). Since that falls outside the scope of this post, I will only briefly mention their representations for my own future reference. 

##### Adjacency List 

One popular form of describing graphs for computation problems is via "adjacency lists". Here we represent each edge from node $$i$$ to node $$j$$ as a list (oftentime a linked list) that stems from the source node. For example, our original unweighted and undirected graph could have the following form: 

```python
# example with Python3 syntax
graph = {
    1: [2, 4], 
    2: [1, 3], 
    3: [2], 
    4: [1]
}
```

##### List of Edges 

Similar to the adjacency list, another way of describing a network is simply as a list of edges, so to again use the first network above, this representation would be: 

```python 
# note Python uses an exclusive stop value
# in the "range" function
nodes = list(range(1, 5)) 
edges = [
    (1, 2), (1, 4), 
    (2, 1), (2, 3), 
    (3, 2), 
    (4, 1)
]

graph = (nodes, edges)
```

## Conclusion 

I plan to use these definitions and notation in future posts. 
