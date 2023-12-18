// Найдите наибольшее число в списке

function max(arr) {
    if (arr.length === 2) {
        return arr[0] > arr[1] ? arr[0] : arr[1];
    }
    const sub_max = max(arr.slice(1));
    return arr[0] > sub_max ? arr[0] : sub_max;
}

console.log(max([6, 7, 8, 9, 10])); // 10
console.log(max([6, 7, 8, 9, 10, 11])); // 11

// можно еще так
function max(arr) {
    if (arr.length === 0) {
        return 0;
    }
    if (arr.length === 1) {
        return arr[0];
    }
    if (arr.length === 2) {
        return arr[0] > arr[1] ? arr[0] : arr[1];
    }
    const sub_max = max(arr.slice(1));
    return arr[0] > sub_max ? arr[0] : sub_max;
}

console.log(max([6, 7, 8, 9, 10])); // 10
console.log(max([6, 7, 8, 9, 10, 11])); // 11

// так
function max(list) {
    if (list.length === 0) {
        return null;
    }
    if (list.length === 1) {
        return list[0];
    }
    const max_num = max(list.slice(1));
    return list[0] > max_num ? list[0] : max_num;
}

console.log(max([6, 7, 8, 9, 10])); // 10
console.log(max([6, 7, 8, 9, 10, 11])); // 11