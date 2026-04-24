# [1. Two Sum](https://leetcode.com/problems/two-sum/)

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-blue)

![Category: Array](https://img.shields.io/badge/Category-Array-green)
![Category: Hash%20Table](https://img.shields.io/badge/Hash%20Table-lightblue)

![Language: Python](https://img.shields.io/badge/Language-Python-brightgreen)

## 📝 Description
Given an array of integers `nums` and an integer `target`, the goal is to find the indices of the two numbers that add up to the target. Each input has exactly one solution, and the same element cannot be used twice.

## 💡 Algorithmic Approach
For this solution, I implemented a **Brute Force** approach using nested iterations.

1.  **Outer Loop**: Iterate through each element `nums[i]` in the array.
2.  **Target Calculation**: For each element, calculate the required value to reach the target: `complement = target - nums[i]`.
3.  **Inner Loop (Search)**: Scan the remainder of the array to find if the `complement` exists.
4.  **Return**: Once the complement is found at index `j`, return the pair `[i, j]`.



## 📊 Complexity Analysis
- **Time Complexity**: $O(n^2)$ – where $n$ is the number of elements in the array. In the worst case, we compare every possible pair of numbers.
- **Space Complexity**: $O(1)$ – No additional data structures are used; the search is performed directly within the input array.


## 🚀 Execution Example
**Input:** `nums = [2, 7, 11, 15]`, `target = 9`

1. **First iteration (i=0)**: `nums[0] = 2`. 
   - `complement = 9 - 2 = 7`.
2. **Inner search**: Does `7` exist in the rest of the array?
   - Yes, at index `1`.
3. **Result**: `[0, 1]`.

## 🛠️ Implementation
The solution is implemented in Python. It focuses on the fundamental logic of exhaustive search to guarantee finding the unique solution.