# 1. Выбрать опорный элемент.
# 2. Разделить массив на два подмассива: элементы, меньшие опорного, и элементы, большие опорного.
# 3. Ракурсивно применить быструю сортировку к двум подмассивам.


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([10, 5, 2, 3]))

# [2, 3, 5, 10]