function sumTwoSmallestNumbers(numbers) { 
  //we use the sort() function to sort the array (this is equivalent to an insertion sort)
  numbers.sort((a,b) => a-b)
  // we ad the two first element of the sorted array
 return  numbers[0] + numbers[1]
  
}