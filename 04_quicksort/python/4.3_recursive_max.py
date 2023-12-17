# Найдите наибольшее число в списке

def max(list):                                             # Oбъявление функции max с аргументом list
    if len(list) == 2:                                     # Если длина списка равна 2, то возвращается большее из двух чисел в списке
        return list[0] if list[0] > list[1] else list[1]   # Возвращает list, если оно больше list[1], иначе возвращает list[1]
    sub_max = max(list[1:])                                # Здесь происходит рекурсивный вызов функции max для подсписка list[1:]
    return list[0] if list[0] > sub_max else sub_max       # Затем возвращается большее из list и sub_max


# можно еще так 
def max(arr):    
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

# или так
def max(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    else:
        max_num = max(list[1:])
        return list[0] if list[0] > max_num else max_num
    
