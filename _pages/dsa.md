---
layout: archive
title: "DSA"
permalink: /dsa/
author_profile: true
---

# Homepage

Problems I've solved [[here]](/problems/homepage.md)

## Primary Sources

1. Basic Algorithms Spring 2023 [[notes]](https://masdranif.notion.site/Basic-Algorithms-Spring-23-0fdc855b62e94371884c19aca4354412)
2. **CLRS** - amazing definitions, especially Greedy, Dynamic Programming, Hashing, Graphs, and advanced topics.
3. MIT 6.006 - especially first 8 lectures for data structures. Watch videos, read lecture notes, recitation notes, do practice problems, and attempt pset problems. Quiz/exam problems are challenging.
4. MIT 6.046 - hashing and advanced topics.
5. Cracking the coding interview - great practice problems
6. 50 Algorithms Every Programmer Should Know - interesting anecdotes but not essential for learning

### Abstract Data Type

An abstract data type is different from the particular form of the data structure itself. ADT's are defined by a set of operations whereas data structures are a specific implementation of an ADT.

| ADT | Data Structure |
| -----| --------------------- |
| List | Array, Linked List, Doubly Linked List|
| Set | Hash Set, Binary Search Tree|
| Map (dictionary) | Hash Map, Red-Black Tree|
| Stack| Array, Linked List|
| Queue | Array, Linked List, Circular Buffer, Dequeue|
| Priority Queue | Heap, Binary Heap, Fibonacci Heap|
| Graph | Adjacency List, Adjacency Matrix, Edge List|
| Tree | Binary Tree, Binary Search Tree, AVL Tree, Red-Black Tree|
| Heap | Binary Heap, Fibonacci Heap|
| Bloom Filter | Bit Array|

Note that ADT's can be implemented by other ADT's - for example, a priority queue can be implemented using a heap.

## The Basics

- Types of running time ($O, \Theta, \Omega$, worst case, best case, amortized, expected)
- Sums, recurrence relation, logarithm rules, basic probability
- primitive data types, floating point

- Caches, locality
- Program stack/dynamic memory allocation
  - Pointers in C/C++ Playlist [[here]](https://www.youtube.com/playlist?list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_)
  - Pointers and dynamic memory - stack vs. heap video ([[here]](https://www.youtube.com/watch?v=_8-ht2AKyH4&ab_channel=mycodeschool))
  
### Sorting/Searching

[Binary Search](binary_search.md)

- Ternary search
- Interpolate search
- Other search?

- Bubble sort
- Insertion sort
- Selection sort
- Merge sort
  - Decision tree - **proof of $O(n \log n)$ optimality for comparison based algorithms**
  - application when you can't store array in memory
- Quick sort
  - Quick select with probabilistic time analysis
- Heap sort

- Radix sort *not comparison based*

- Timsort

### Linear Data structures

- [Array](array.md)
- [Stack](stack.md)
- Queue, dequeue
- Priority queue
- Linked List
- Matrix *and conversion to array*
  - adjacency list/matrix

### Non linear data structures

- [Hash function](hash_function.md) which leads to hash tables and hash sets.
- Heap

- #### Graphs

  - **Tree (BST)**

### Graphs - Advanced

- Search
  - Unweighted graphs (BFS, DFS)
  - Weighted graphs (Dijkstra, Floyd-Warshall, APSP/SP, negative cycles)

### Brute Force/Backtracking

### Greedy

### Dynamic Programming

- Rod cutting

## Advanced

### DS

- Trie
- Disjoint Set (Union, Find)
- **Tree extensions**
  - AVL, B-Tree, Red-Black
  - Merkle trees
- Authenticated DS
- Segment Tree

### Substring

- KMP
- Rabin-Karp

### Optimization

### Number Theory

- Generating primes

### Geometry

- Shortest pair of points in $R^2$ and $R^3$
- Convex hull

### Randomized algorithms

#### Algorithmic time complexity (P vs. NP)
