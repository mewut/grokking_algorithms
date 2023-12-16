# Напишите рекурсивную функцию для подсчета элементов в списке

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

