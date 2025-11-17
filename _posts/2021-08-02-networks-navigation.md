---
title: "Networks (Part II) - Navigation"
author: Stephen Lee
layout: post

categories: [Networks]
tags: [Networks]
toc: true
katex: true
---

Note, this is a cross post from an older blog, Sparking Correlation, which I no longer use. 

## Audience 

This is part II in a series about making economic inferences on network structures. The notation is covered in [part I]({% post_url 2021-07-14-networks-notation %}).

## Overview

In the previous post I described the basic notations for representing network graphs. Here, I will introduce some definitions that relate to navigating in a graph. This is a key building block for more complicated analyses in a network. 

## Definitions 

Consider the following network graph.

<img src="{{ 'assets/images/networks/network-simple.svg' | relative_url }}" alt="scatter" width="150"/>

The figure above shows an undirected network graph with four (4) nodes and three unweighted edges. We can represent this graph, $$g$$, in matrix form as follows: 

$$
g = \begin{bmatrix}
0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\ 
1 & 0 & 0 & 0
\end{bmatrix} 
$$

Note, this is illustrative to provide a concrete example to reference. All the definitions below apply to both weighted and unweighted, directed and undirected graphs. 

### Paths 

A path from node $$i$$ to node $$j$$ in graph $$g$$ is a sequence that begins at node $$i$$ and follows available edges until arriving at node $$j$$. 

Formally, a **path** in network $$g$$ between nodes $$i$$ and $$j$$ is a sequence of edges $$(n_1, n_2) \rightarrow (n_2, n_3) \rightarrow ... \rightarrow (n_{K-1}, n_K)$$ where each edge $$(n_{k-1}, n_k) \in g$$, $$n_1 = i$$ and $$n_K = j$$, and each node $$n_1, ..., n_K$$ are distinct. Note that the destination node along one edge becomes the starting node for the next edge.

Using the graph in the figure above, there is only one possible path from node $$1$$ to node $$3$$, namely $$\{(1, 2) \rightarrow (2, 3)\}$$. 

### Walk 

A **walk** is a path that doesn't require distinct nodes i.e. an edge can lead to a node that has already been visited. In this sense, a walk will, in general, be less restrictive. 

### Cycles 

A **cycle** is a walk that starts and ends at the same node without visiting any other node more than once. In the definition of path above, we simply let $$n_1 = n_K = i = j$$. 

### Geodesic 

A **geodesic** between nodes $$i$$ and $$j$$ is the shortest path between those nodes. 

### Degree 

The **degree** of a node is the number of links that involve the node. For directed graphs, this can be referenced as an in-degree and an out-degree, depending on if the edge ends with or starts from that node. 

In our example above, nodes $$1$$ and $$2$$ both have degree two (2), while nodes $$3$$ and $$4$$ have degree one (1). 

### Component

Finally, what if there is a node $$j$$ that cannot be reached after starting from some other node $$i$$? In this case, we say that those nodes are in separate components.

More formally, a given network $$g$$ is **connected** if there exists a path between any two nodes i.e. you can start at any node in the network and find a path to reach any other node in the network. 

Similarly, a **component** of a network $$g$$ is a subnetwork $$g' \subseteq g$$ where 1) $$g'$$ is connected and 2) if a node $$i$$ is in $$g'$$ and the edge $$(i, j) \in g$$ (i.e. the edge exists in the larger graph) then the node $$j$$ and edge $$(i, j)$$ must both also be in $$g'$$. In other words, a component is a maximally connected subgraph. The graph below shows a network with two connected components. 

<img src="{{ 'assets/images/networks/network-component.svg' | relative_url }}" alt="scatter" width="150"/>

### Conclusion 

This post focused on definitions that relate to navigating in a network i.e. how to think about moving from one node to another. 

One very natural extension are algorithms for actually navigating these graphs. This includes things like depth-first and breadth-first searches, among other. I suspect I'll make a post about these at some point, but until then, I very much recommend [this textbook](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf), which is currently available for free as a PDF online. 

## Resources 
- "Social and Economic Networks" by M. O. Jackson
- "Algorithms" by S. Dasgupta, C. H. Papadimitriou, and U. V. Vazirani

