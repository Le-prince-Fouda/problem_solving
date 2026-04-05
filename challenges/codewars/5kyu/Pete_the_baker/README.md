# Pete, the baker

## 📝 Subject

Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

**Exemples :**

* // must return 2
    * cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200}); 
*  // must return 0
    * cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000}); 

---

## 💡 My Solution

### Approche

1. i use the loop **for in** and the methode **hasOwnProperty()** to check if the two objects has the same property (ingrdient)
2. if one of the recipe ingredient is not available, we cannot bake a cake
3. for each ingredient we divide the available quantity by this that we must use in the recipe.
4. we return the smallest of the array **numbers**

---

## 🔗 Liens

* [Link to the Kata](https://www.codewars.com/kata/525c65e51bf619685c000059).

* **Programming language:** Javascript

 **Complexity:** O(n) with n the number of recipe'sproperty
