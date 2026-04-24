# [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-blue)


![Category: Hash%20Table](https://img.shields.io/badge/Category-Hash%20Table-lightblue)
![Category: Math](https://img.shields.io/badge/Math-green)
![Category: String](https://img.shields.io/badge/String-lightgrey)

![Language: Python](https://img.shields.io/badge/Language-Python-brightgreen)

## 📝 Description
The goal is to convert a Roman numeral string into its corresponding integer value. Roman numerals are represented by seven symbols (`I`, `V`, `X`, `L`, `C`, `D`, `M`) and generally follow an additive rule, except for specific subtractive cases (like `IV` for 4 or `CM` for 900).

| Symbol | Value |
|:-------|------:|
| I      |     1 |
| V      |     5 |
| X      |    10 |
| L      |    50 |
| C      |   100 |
| D      |   500 |
| M      |  1000 |

## 💡 Algorithmic Approach
To solve this efficiently, I used a **Single-Pass Greedy Scan** with look-ahead logic.

1.  **Mapping**: I used a Hash Map (Dictionary in Python) to store the integer value of each Roman symbol for $O(1)$ lookup.
2.  **Logic**:
    * Iterate through the string from left to right.
    * **The Comparison Rule**: For each character, compare its value to the value of the *next* character.
    * **Subtraction**: If the current value is **less** than the next value (e.g., `I` before `V`), it means we are in a subtractive case. We subtract the current value from the total.
    * **Addition**: Otherwise, we simply add the current value to the total.
3.  **Edge Case**: The last character is always added since there is no "next" character to trigger a subtraction.



## 📊 Complexity Analysis
- **Time Complexity**: $O(n)$ – where $n$ is the length of the input string. We traverse the string exactly once.
- **Space Complexity**: $O(1)$ – The Hash Map used for symbols has a fixed size (7 elements), which does not grow with the input size.

## 🚀 Execution Example
**Example: `s = "MCMXCIV"`**

| Step | Char | Next | Value | Action | Total |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | M | C | 1000 | 1000 > 100 → Add | 1000 |
| 2 | C | M | 100 | 100 < 1000 → **Subtract** | 900 |
| 3 | M | X | 1000 | 1000 > 10 → Add | 1900 |
| 4 | X | C | 10 | 10 < 100 → **Subtract** | 1890 |
| 5 | C | I | 100 | 100 > 1 → Add | 1990 |
| 6 | I | V | 1 | 1 < 5 → **Subtract** | 1989 |
| 7 | V | - | 5 | Last char → Add | **1994** |

## 🛠️ Implementation
The solution is implemented in Python, using a dictionary for optimal symbol-to-value conversion.
