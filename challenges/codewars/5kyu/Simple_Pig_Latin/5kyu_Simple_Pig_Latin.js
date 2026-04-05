function pigIt(str){
  let arr = str.split(" ")
  let str1 = arr.map((el) => {
    //we use a RegEx to exclud ponctuation character
    if(!/\p{P}/u.test(el)){
      el += el[0] + "ay"
      el = el.replace(el[0], '')
    }
    return el
  }).join(" ")
  return str1
}