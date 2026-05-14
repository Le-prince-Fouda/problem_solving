# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)  

![Category: Hash Table](https://img.shields.io/badge/Category-Hash%20Table-blue)
![Category: String](https://img.shields.io/badge/String-green)
![Category: Sliding Window](https://img.shields.io/badge/Sliding%20Window-red) 

![Language: Python](https://img.shields.io/badge/Language-Python-brightgreen)

## Description
The goal is to find the length of the longest substring without repeating characters in a given string `s`. A substring is a contiguous sequence of characters, so the solution must keep track of the current valid window while scanning the string.

## Algorithmic Approach
To solve this problem, I implemented a **Sliding Window** approach with a hash table to store the last seen index of each character.



1.  **Initialization**: Created a dictionary called `character` to store the latest index of each character, a `length` variable initialized to 0, and a `subStart` pointer initialized to 0 to represent the beginning of the current substring.
2.  **Process (Single Loop)**:
    * Iterate through the string with both the index and the current character.
    * If the current character already exists in the current window, move `subStart` to the position right after its previous occurrence.
    * Update the latest index of the current character in the `character` dictionary.
    * Update `length` using the maximum between the current result and the size of the active window.
3.  **Optimization**: This method is optimal because each character is processed once. The `subStart` pointer only moves forward, which avoids checking the same substring multiple times.

## Complexity Analysis
- **Time Complexity**: $O(n)$ - where $n$ is the length of the input string. We traverse the string once.
- **Space Complexity**: $O(k)$ - where $k$ is the number of unique characters stored in the dictionary. In the worst case, this can be $O(n)$.

## Execution Example
**Input:** `s = "abcabcbb"`

**Process:**
- Read `a`, `b`, and `c` to build the substring `"abc"`.
- When `a` appears again, move the start of the window after the previous `a`.
- Continue scanning while keeping only non-repeating characters inside the current window.

**Output:** `3` (the longest substring is `"abc"`)

---

## Implementation
```python
# The solution code is located in the longest_substring_without_repeating_characters.py file
```
