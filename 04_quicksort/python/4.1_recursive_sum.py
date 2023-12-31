# Напишите код для функции sum:

def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([1, 2, 3, 4]))

# 1. Определить базовый случай. Как выглядит самый простой массив, который можно получить?
# Когда пишете рекурсивную функцию, в которой задействован массив, 
# базовым случаем часто оказывается пустой массив или массив из одного элемента.
# 2. Каждый рекурсивный вызов должен приближать к пустому масссиву. Как уменьшить размер задачи?

def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

print(sum([1, 2, 3, 4]))
