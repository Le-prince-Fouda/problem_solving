function cakes(recipe, available) {
  let number = []
  for (let el in recipe ){
    if (available.hasOwnProperty(el)){
      number.push(Math.floor(available[el]/recipe[el]))
    }else{
      return 0
    }
  }
  
  return Math.min(...number)
}