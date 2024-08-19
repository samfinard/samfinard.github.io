---
layout: archive
title: "Data Structures & Algorithms"
permalink: /dsa/
author_profile: true
---

### Sources used [[here]](../dsa/sources.md)

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
  - Pointers in C/C++ [[playlist]](https://www.youtube.com/playlist?list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_)
  - Pointers and dynamic memory - stack vs. heap [[video]](https://www.youtube.com/watch?v=_8-ht2AKyH4&ab_channel=mycodeschool)
  
### Sorting/Searching

- [Binary Search](../dsa/binary_search.md)
- Ternary/Interpolate search?
- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
  - Decision tree - **proof of $O(n \log n)$ optimality for comparison based algorithms**
  - Application - when you can't store array in memory
- Quick Sort
  - Quick select with probabilistic time analysis
- Heap Sort
- Radix Sort
  - not comparison based
- Timsort
  - Python's default sorting algorithm - derived from merge sort and insertion sort.

## Data Structures

### Linear Data structures

- [Array](../dsa/array.md)
- [Stack](../dsa/stack.md)
- Queue, dequeue
- Priority queue
- Linked List
- Matrix *and conversion to array*
  - adjacency list/matrix

### Non linear data structures

- [Hash function](../dsa/hash_function.md) which leads to hash tables and hash sets.
- Heap
- Graphs
  - Tree (BST)
  - **Search**
    - Unweighted graphs (BFS, DFS)
    - Weighted graphs (Dijkstra, Floyd-Warshall, APSP/SP, negative cycles)

## Fundamental Algorithmic Paradigms

### Divide and Conquer

### Brute Force/Backtracking

### Greedy

### Dynamic Programming

- Rod cutting
- 0/1 knapsack
- Subset sum
- Longest common subsequence
- Edit distance
- Matrix multiplication

## Advanced

### Data Structures

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

### Geometry

- Shortest pair of points in $R^2$ and $R^3$
- Convex hull

### Number Theory

- Generating primes

### Algorithmic time complexity (P vs. NP)

## Advanced Algorithmic Paradigms

### Optimization

### Randomized algorithms

### Branch and Bound

### Approximation Algorithms

### Network Flow Algorithms
