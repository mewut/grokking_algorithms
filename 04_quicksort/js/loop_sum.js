function sum(array) {
    let total = 0;
    for (let i = 0; i < array.length; i++) {
      total += array[i];
    }
    return total;
  }
  
  console.log(sum([1, 2, 3, 4])); // 10
  