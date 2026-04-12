# Palindrome

## 📝 Subject

Given an integer x, return true if x is a palindrome, and false otherwise.

**Examples :**

1. Example 1:
   * Input: x = 121
   * Output: true
   * Explanation: 121 reads as 121 from left to right and from right to left.
2. Example 2:
   * Input: x = -121
   * Output: false
   * Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
3. Example 3:
   * Input: x = 10
   * Output: false
   * Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

---

## 💡 My Solution

### Approach

1.  first code (easy_palindrome1)
   * convert the int into a string 
   * compare each character on the right side with the corresponding character (same position) on the left site of the string
   * when comparing,we return false if two character don't match (we don't have a palindrome)

2. second code (easy_palindrome2)
   * convert the int into a string 
   * store the inverse of this string in another string
   * if the two are the same, than we have a palindrome

3. the third code (easy_palindrome3)
   * This code is the same as the first one (easy_palindrome1), but here we don’t iterate through the entire array; we only look at half of it. 
   * If the elements in the left half are identical to each of the elements in the right half of the array, then we have a palindrome.
---

## 🔗 Liens

* [Link to the Exercise](https://leetcode.com/problems/palindrome-number/submissions/1976522868/).

* **Programming language:** Python

*  **Complexity:** O(n)

