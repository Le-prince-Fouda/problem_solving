function findEvenIndex(arr) {
  //initial left sum is 0 and initial rigth sum is the sum of array's element 
    let left = 0
    let rigth = arr.reduce((a,b) => a+b, 0)  
  for(let i =0; i<arr.length; i++){
    //we remove to the previous right sum the value of the number in current array's index i
    rigth -= arr[i]
    //we compare the two sum
    if(left === rigth) return i
    //we calculate the next left sum with adding the value of the number in the current array's indexe
    //this will be used as the left sum in the next step
    left += arr[i]
  }
    return -1;
}