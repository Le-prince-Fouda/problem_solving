/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    const str = String(x)
    const sizee = str.length
    let j= sizee - 1
    for( let i =0; i<Math.floor(sizee/2); i++){
        if(str[i] != str[j]){
            return false
        }
        j -= 1
    }
    return true
    
};