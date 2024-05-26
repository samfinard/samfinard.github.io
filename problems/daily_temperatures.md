## Daily Temperatures

Problem [[here]](https://leetcode.com/problems/daily-temperatures/description/)

**Statement:** Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

**Example:**

Input: temperatures = [6,9,2,4,8,1,3]

Output: [1,0,1,1,0,1,0]

**My Solution**
The naive solution is to check all elements to the right for every element, leading to an $O(n^2)$ solution. Can we do better?

For any given temperature we only care about temperatures to the right. 