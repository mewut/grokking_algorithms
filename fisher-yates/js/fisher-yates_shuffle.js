// перемешивание элементов массива

const list = ['element1', 'element2', 'element3', 'element4', 'element5'];

function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

shuffle(list);

console.log(list)
