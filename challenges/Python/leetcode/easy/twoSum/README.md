# twoSum

## 📝 Subject

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Examples :**

1. Example 1:
    * Input: nums = [2,7,11,15], target = 9
    * Output: [0,1]
    * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
2. Example 2:
    * Input: nums = [3,2,4], target = 6
    * Output: [1,2]
3. Example 3:
    * Input: nums = [3,3], target = 6
    * Output: [0,1]

---

## 💡 My Solution

### Approach

1. subtract the current element's value from the target value
2. search for the result in the rest of the array

---

## 🔗 Liens

* [Link to the Exercise](https://leetcode.com/problems/two-sum/).

* **Programming language:** Python

 **Complexity:** O(n<sup>2</sup>) with n the number of recipe's property
