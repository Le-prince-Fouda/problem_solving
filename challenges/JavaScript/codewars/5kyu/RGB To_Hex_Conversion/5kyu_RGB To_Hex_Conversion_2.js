function rgb(r, g, b) {
  let result= ""
  let toHexDec = (decimal) => {
    //we check if "decimal" is a number between 0-255 (instead using several "if")
    let num = Math.min(255, Math.max(0, decimal))
    //we make sure that our convertion has 2 character, and is in upper case
    // if the conversion "toString(16)" return 1 character we complet our result with 0 in the begining
    return num.toString(16).padStart(2, 0).toUpperCase()
  }
   return result = result.concat(toHexDec(r), toHexDec(g), toHexDec(b))
}