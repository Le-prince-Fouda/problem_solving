# RGB To Hex Conversion

## 📝 Subject

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

**Exemples :**

* 255, 255, 255 --> "FFFFFF"
* 255, 255, 300 --> "FFFFFF"
* 0, 0, 0       --> "000000"
* 148, 0, 211   --> "9400D3"

---

## 💡 My Solution

    For this exercice i have write 2 solution with the same principle, but in the second solution "5kyu_RGB To_Hex_Conversion_2" i have try to use more natives functions like: **padStart, toString, Math.min and Math.max**

### Approche

1. i create a convertion function to execute it to each rgb elements
2. This function make sure that the value of rgb is between 0-255
3. the function convert the decimal number to hexadecimal character
4. at the end i return the result

---
## 🔗 Liens
* [Link to the Kata](https://www.codewars.com/kata/513e08acc600c94f01000001).
* **Programming language:** Javascript
