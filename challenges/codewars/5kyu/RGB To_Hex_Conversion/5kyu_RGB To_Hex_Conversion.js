function rgb(r, g, b) {
  let result= ""
  // this function will convert the decimal number to hexadecimal character
    let convertion = (decimal) => {
        let hex = '', sentinel
        //an array with all the hexadecimal charachters
        let arr = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F",]
        let num = decimal
        //if the decimal is lower than 0 or greater than 255 we  rounded to the closest valid value.
        if(num < 0) num = 0
        if(num > 255) num = 255
        do{
            sentinel = num%16
            num = Math.floor(num/16)
            hex = arr[sentinel] + hex
              
        }while (num != 0)
        //if the result of the conversion "hex" don't have 2 character we add "0" befor
        //and we return our hexadecimal
        if(hex.length===1) return "0"+hex
        return hex
        
    }

   return result = result.concat(convertion(r), convertion(g), convertion(b))
}