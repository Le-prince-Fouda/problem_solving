function XO(str) {
  //we set the text to lowercase and convert it to an array
  const str1 = str.toLowerCase().split("");
  //we save the number "x" and the number of "o" each in an array 
  const cardX = str1.filter(el => el === "x")
  const cardO = str1.filter(el => el === "o")
  //if the to table have the same length the we return true, th sting have same amount of "x"s and "o"s
  if(cardX.length === cardO.length){
    return true
  }
  return false
}