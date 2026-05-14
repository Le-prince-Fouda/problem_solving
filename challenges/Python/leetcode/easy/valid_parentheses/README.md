# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-blue)

![Category: String](https://img.shields.io/badge/Category-String-green)
![Category: Stack](https://img.shields.io/badge/Category-Stack-lightblue)

![Language: Python](https://img.shields.io/badge/Language-Python-brightgreen)

## 📝 Description
Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, the goal is to determine if the input string is valid.

A string is valid if every opening bracket is closed by the same type of bracket and in the correct order.

## 💡 Algorithmic Approach
For this solution, I implemented a **Stack** approach to track the expected closing brackets.

1.  **Opening Bracket Detection**: Iterate through each character in the string.
2.  **Expected Closing Bracket**: When an opening bracket is found, push its corresponding closing bracket into the stack.
3.  **Closing Bracket Validation**: When a closing bracket is found, compare it with the last expected closing bracket.
4.  **Return**: If the closing bracket matches, remove it from the stack. Otherwise, return `False`.
5.  **Final Check**: At the end, the string is valid only if the stack is empty.



## 📊 Complexity Analysis
- **Time Complexity**: $O(n)$ – where $n$ is the number of characters in the string. Each character is processed once.
- **Space Complexity**: $O(n)$ – In the worst case, all characters are opening brackets and are stored in the stack.


## 🚀 Execution Example
**Input:** `s = "()[]{}"`

1. **First character**: `(` is an opening bracket.
   - Push the expected closing bracket `)` into the stack.
2. **Second character**: `)` is a closing bracket.
   - It matches the last expected closing bracket, so remove it from the stack.
3. **Continue validation**: The same logic is applied to `[]` and `{}`.
4. **Result**: The stack is empty, so the function returns `True`.

## 🛠️ Implementation
The solution is implemented in Python. It uses a stack to keep track of the expected closing brackets and validates the string in a single pass.
