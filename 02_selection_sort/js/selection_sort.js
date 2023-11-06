// Функция для поиска наименьшего элемента массива

function findSmallest(arr) {
    let smallest = arr[0];
    let smallestIndex = 0;
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < smallest) {
            smallest = arr[i];
            smallestIndex = i;
        }
    }
    return smallestIndex;
}

console.log(findSmallest([5, 3, 6, 2, 10])); 

// ответ 3

// На основе функции выше можно написать функцию сортировки выбором

function selectionSort(arr) {
    let newArr = [];
    const length = arr.length;
    for (let i = 0; i < length; i++) {
        let smallest = findSmallest(arr);
        newArr.push(arr.splice(smallest, 1)[0]);
    }
    return newArr;
}

console.log(selectionSort([5, 3, 6, 2, 10])); 

// [2, 3, 5, 6, 10]
