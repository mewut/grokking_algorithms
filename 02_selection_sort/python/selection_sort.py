# функция для поиска наименьшего элемента массива

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

print(findSmallest([5, 3, 6, 2, 10]))

# ответ 3


# на основе функции выше можно написать функцию сортировки выбором:

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))

# ответ [2, 3, 5, 6, 10]
