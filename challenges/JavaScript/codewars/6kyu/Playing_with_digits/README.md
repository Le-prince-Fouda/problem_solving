# Playing with digits

## 📝 Subject

Some numbers have funny properties. For example:

89 --> 8<sup>1</sup> + 9<sup>2</sup> = 89 * 1

695 --> 6<sup>2</sup> + 9<sup>3</sup> + 5<sup>4</sup>= 1390 = 695 * 2

46288 --> 4<sup>3</sup> + 6<sup>4</sup>+ 2<sup>5</sup> + 8<sup>6</sup> + 8<sup>7</sup> = 2360688 = 46288 * 51

Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :
 a<sup>p</sup> + b<sup>p+1</sup> + c<sup>p+2</sup> + d<sup>p+3</sup> = n*k

If it is the case we will return k, if not return -1.

Note: n and p will always be strictly positive integers.

**Exemples :**

* n = 89; p = 1 ---> 1 since 8<sup>1</sup> + 9<sup>2</sup> = 89 * 1
* n = 92; p = 1 ---> -1 since there is no k such that 9<sup>1</sup> + 2<sup>2</sup>equals 92 * k
* n = 695; p = 2 ---> 2 since 6<sup>2</sup> + 9<sup>3</sup> + 5<sup>4</sup>= 1390 = 695 * 2
* n = 46288; p = 3 ---> 51 since 4<sup>3</sup> + 6<sup>4</sup>+ 2<sup>5</sup> + 8<sup>6</sup> + 8<sup>7</sup> = 2360688 = 46288 * 51

---

## 💡 My Solution

### Approche

1. we create an array that contain the diffrent figure of the number
2. we use Euclidean division by 10 and save the rest of each step of the division in an array
3. we sum the digit of n raised to consecutive power starting from p 
4. we divide this sum by our number n, if the result is an integer then we return this number k

---

## 🔗 Liens

* [Link to the Kata](https://www.codewars.com/kata/5552101f47fc5178b1000050).
* **Programming language:** Javascript
