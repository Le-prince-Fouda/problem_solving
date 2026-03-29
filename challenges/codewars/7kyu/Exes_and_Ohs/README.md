# Exes and Ohs

# 📝 Subject

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

**Exemples :**

* XO("ooxx") => true
* XO("xooxx") => false
* XO("ooxXm") => true
* XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
* XO("zzoo") => false

---

## 💡 My Solution

### Approche

1. i set the text to lowercase to make sure that the function is not case-sensitive
2. i convert the text to an array
3. i save the number of "x" and the number of "o" each in an array
4. if the two array have the same length then we return true (the sting have same amount of "x"s and "o"s)

---
## 🔗 Liens
* [Link to the Kata](https://www.codewars.com/kata/55908aad6620c066bc00002aL).
* **Programming language:** Javascript
