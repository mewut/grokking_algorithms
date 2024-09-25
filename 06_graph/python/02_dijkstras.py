# graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# costs
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)

# Время выполнения алгоритма составляет O((V+E)logV), где V — количество вершин, а E — количество рёбер.

# Основной цикл:

# Пока есть вершины с минимальной стоимостью:
# Для текущей вершины рассмотрим всех соседей.
# Если путь через текущую вершину до соседа короче, чем текущий кратчайший путь до соседа, обновим стоимость и родителя соседа.
# После этого добавим текущую вершину в список обработанных.
# Цикл продолжается.
