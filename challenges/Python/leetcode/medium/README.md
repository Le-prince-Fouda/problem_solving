# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)  
![Category: Linked List](https://img.shields.io/badge/Category-Linked%20List-blue)
![Category: Math](https://img.shields.io/badge/Math-green)
![Category: Recursion](https://img.shields.io/badge/Recursion-red) 

## 📝 Description
The goal is to sum two non-negative integers represented as **linked lists**. Each node contains a single digit, and the digits are stored in reverse order. The result should also be returned as a linked list.

## 💡 Algorithmic Approach
To solve this problem, I implemented a **Elementary Addition Simulation** with carry management.



1.  **Initialization**: Created a dummy node called `myLinkedList` to serve as the starting point for the result list, and a `carry` variable initialized to 0.
2.  **Process (Single Loop)**: 
    * Iterate through both lists as long as there are remaining nodes or a non-zero carry.
    * In each iteration, sum the values of the current nodes (if they exist) and the carry.
    * Extract the new digit for the result using `add % 10` and update the carry using `add // 10`.
    * Move the pointers for both input lists and the result list forward.
3.  **Optimization**: This method is optimal because it only requires a single pass through the lists. The use of a `dummy node` simplifies the insertion logic at the beginning, avoiding special conditions for the first node.

## 📊 Complexity Analysis
- **Time Complexity**: $O(\max(m, n))$ – where $m$ and $n$ are the lengths of the two input lists. We traverse each list at most once.
- **Space Complexity**: $O(\max(m, n))$ – Since we create a new linked list to store the result. The length of the new list is at most $\max(m, n) + 1$.

## 🚀 Execution Example
**Input:** `l1 = [2, 4, 3]` (represents 342)
`l2 = [5, 6, 4]` (represents 465)

**Calculation:**
- $2 + 5 = 7$
- $4 + 6 = 10$ (write $0$, carry $1$)
- $3 + 4 + 1 = 8$

**Output:** `[7, 0, 8]` (represents 807)

---

## 🛠️ Implementation
```python
# The solution code is located in the Add_Two_Numbers.py file