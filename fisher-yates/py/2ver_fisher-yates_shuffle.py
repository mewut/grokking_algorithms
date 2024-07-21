import random

list = ['element1', 'element2', 'element3', 'element4', 'element5']

def shuffle(array):
  for i in range(len(array) - 1, 0, -1):
    j = random.randint(0, i)
    array[i], array[j] = array[j], array[i]

shuffle(list)
print(list)
