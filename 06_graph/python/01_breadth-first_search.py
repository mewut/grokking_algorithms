from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'                           # это проверка на продавца манго. Если последняя буква имени - "m", то это продавец


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    search_queue = deque()                           # создание новой очереди
    search_queue += graph["you"]                     # добавление элементов в очередь. graph["you"] вернет список "alice", "bob", "claire"
    searched = []                                    # создание нового списка для хранения посещенных элементов (кого мы уже проверили на продавцов манго)
    while search_queue:
        person = search_queue.popleft()              # извлечение элемента из очереди
        if not person in searched:                   # элемент проверяется только в том случае, если его нет в списке проверенных
            if person_is_seller(person):             # Проверяем, является ли этот человек продавцом манго
               print(person + " is a mango seller!") # да, является
               return True
            else:
                search_queue += graph[person]        # а если нет, то все его элементы добавляем в очередь
                searched.append(person)
    return False                                     # если функция зашла сюда, то продавцов манго вообще нет в графе

search("you")

# Время выполнения составляет как минимум О(количество ребер графа)
# Добавление одного элемента в очередь выполняется за постоянное время: O(1)
# Выполнение операции для каждого элемента потребует суммарного времени O(количество вершин в графе)
# Поиск в ширину выполняется за время О(количество вершин + количество ребер): O(V + E), т.е. линейно. 
# Это означает, что алгоритм работает эффективно даже для больших графов.