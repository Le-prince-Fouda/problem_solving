# [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-blue)

![Category: Math](https://img.shields.io/badge/Category-Math-green)

![Language: Python](https://img.shields.io/badge/Language-Python-brightgreen)

## 📝 Description
The objective is to determine if an integer `x` is a palindrome. An integer is a palindrome when it reads the same backward as forward (e.g., 121 is, -121 is not).

## 💡 Algorithmic Approaches
I have implemented three different solutions to demonstrate different logic patterns and optimization levels.

### 1. Character-by-Character Comparison
- **Concept**: Convert to string and compare characters from both ends.
- **Logic**: Use an index to compare the $i$-th character with the $(n-1-i)$-th character.
- **Pros**: Demonstrates basic index logic.

### 2. String Comparison (Full Inversion)
- **Concept**: Convert the integer to a string and compare it with its reverse.
- **Logic**: If `str(x) == str(x)[::-1]`, it's a palindrome.
- **Pros**: Very clean and readable code.

### 3. Optimized Two-Pointers (Half-Scan)
- **Concept**: Similar to the second approach, but optimized for performance.
- **Logic**: We only iterate through **half of the string** ($n/2$). If the left half matches the mirrored right half, the number is a palindrome.
- **Optimization**: Reduces the number of comparisons by 50% compared to a full scan.



## 📊 Complexity Analysis (Optimized Version)
- **Time Complexity**: $O(n)$ – where $n$ is the number of digits in the integer. We traverse at most half of the string.
- **Space Complexity**: $O(n)$ – due to the string conversion which requires space proportional to the number of digits.

## 🚀 Execution Example
**Example 1:**
- **Input:** `x = 121`
- **Output:** `true`
- **Explanation:** 121 reads as 121 from both sides.

**Example 2:**
- **Input:** `x = -121`
- **Output:** `false`
- **Explanation:** From left to right: `-121`. From right to left: `121-`.

## 🛠️ Implementation
The repository contains three versions of the solution:
* `easy_palindrome1.py`: Full string comparison.
* `easy_palindrome2.py`: String inversion logic.
* `easy_palindrome3.py`: Optimized half-array iteration.

