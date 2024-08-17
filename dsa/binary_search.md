# Binary Search

## Problem

Given a sorted array $A$ and an object $t$, return the index of $A[t]$ - (or $-1$ if it's not in the array.)

### Pseudocode in words (intuitive explanation)

Naively, we can iterate through all $n \in A$ and get a solution $\in O(n)$. However, this is true for any array - we aren't exploiting the fact that $A$ is sorted.

Because $A$ is sorted, we know the smallest and largest element in $O(1)$ time by accessing the first and last element, respectively. If $t$ is smaller than the smallest object, or larger than the largest object, it cannot be inside the array. This is the core logic of Binary Search and takes full use of the array's sorted property.

Let $l=0, r=n-1$. Compare $t$ with $A[m]$ where $m = \left \lfloor{\dfrac{l+r}{2}}\right \rfloor$. If $t < A[m]$, $t$ must be on the left half so we change $r = m-1$. Otherwise, if $t > A[m]$, $t$ must be on the right half so we change $l = m+1$. In either case we keep iterating until one of two scenarios happen.

1. Either $t=A[m]$, at which point we return $m$.
2. If at any point $l > r$ we have searched all possible ranges of the array and can conclude $t \notin A$, at which point we return $-1$.

### Python Code

```python
def binary_search(arr, t):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1
```

*note: $l<r$ is incorrect because of the edge case where $n=1$?*

### Runtime / Space Analysis

With each iteration you divide the range of possible indices in half. By definition of log, you can divide an array of length $n$ by 2 a total of $\log_2(n)$ many times. With each iteration you are performing a comparison between $t$ and $A[m]$ which takes $O(1)$ time.
**Thus we have a final runtime of $O(\log n)$.**

For example, consider this example sequence of index ranges resulting from binary search.

- $0,\ldots,63$
- $0,\ldots,31$
- $0,\ldots,15$
- $7,\ldots,15$
- $11,\ldots,15$
- $11,\ldots,13$
- $12,\ldots,13$
- $13,\ldots,13$
  
Here $n=64$ and the number of iterations is $\log_2(64) = 8$

### Misc

**Why does the base in logarithms not matter in Big O notation?**

$O(\log_2(n)) = O(\log_k(n)) = O(\log n)$ for any real constant $k$ because of the Change of Base Formula, which says
$$\log_a(n) = \dfrac{\log_b(n)}{\log_b(a)}$$
Because $a, b$ are constants, we know $\log_b(a) = k$ where $k$ is a constant. Rewriting, we have
$$\log_a(n) = \dfrac{\log_b(n)}{k} \implies O(\log_a(n)) = O(\log_b(n)) = O(\log n)$$

### Why say 'objects' instead of just numbers?

1. Binary search uses a comparison system that checks whether $a<b, a==b, a>b$ (more formally, a [binary relation](https://en.wikipedia.org/wiki/Binary_relation)) which can be applied to any [totally ordered set](https://en.wikipedia.org/wiki/Total_order) and is not restricted to numbers.
2. In many cases it is possible to assign a unique ID number to each object in the set using a hash function, reducing the problem to an array of numbers. This becomes more difficult if objects are highly similar due to collisions.

### Related problems

1. Use binary search in a [sorted matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)

    This problem boils down to two steps.
    1. Figure out which row $t$ is in
    2. Use binary search on that row

    So this problem reduces to figuring out which row $t$ is in.

2. Search a [rotated sorted array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)
