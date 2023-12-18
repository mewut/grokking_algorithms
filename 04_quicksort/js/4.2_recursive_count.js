// Напишите рекурсивную функцию для подсчета элементов в списке

function count(list) {
    if (list.length === 0) {
      return 0;
    }
    return 1 + count(list.slice(1));
  }
  