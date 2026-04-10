function digPow(n, p){
  //we create a table that contain the diffrent figure of the number
  //we use Euclidean division
  let number = []
  let euclidRest = 0;
  let sentinel = n
  while (sentinel!= 0){
    euclidRest = sentinel%10; //we save the rest oft the Euclidean division
    number.push(euclidRest); //we add the rest of the division in the table
    sentinel= Math.floor(sentinel/10);//we save all the figure of the number without the last
  }
  
  //we sum the digit of n raised to consecutive power starting from p
  //we use hier the revers of our table "number"
  let powerDigit = 0;
  
  number.reverse().forEach(element=> {
    powerDigit += Math.pow(element, p);//we do el^p
    p++
  })
  
  //we divide the sum by n and check if k is an integer, else we return -1
  const k = powerDigit/n;
  
  if(Number.isInteger(k)){
    return k
  }else{
    return -1
  }
}