# Equal Sides Of An Array

## 📝 Subject

You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.

If there is no index that would make this happen, return -1.

**Exemples :**

* {1,2,3,4,3,2,1} => 3
* {1,100,50,-51,1,1} => 1
* {20,10,-80,10,10,15,35} => 0

---

## 💡 My Solution

### Approche

1. initial left sum is 0 and initial rigth sum is the sum of array's element 
2. for each step, we remove to the previous right sum the value of the number in current array's index i
3. we compare the two sum
4. if it not equal, we calculate the next left sum with adding the value of the number in the current array's indexe. these for the next step.

---
## 🔗 Liens
* [Link to the Kata](https://www.codewars.com/kata/5679aa472b8f57fb8c000047).
* **Programming language:** Javascript
