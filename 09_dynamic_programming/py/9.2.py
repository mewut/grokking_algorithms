# Предположим, что вы собраетесь в турпоход. Емкость вашего рюкзака составляет 6 фунтов, и вы можете взять предметы из следующего списка. 
# У каждого предмета имеется стоимость; чем она выше, тем важнее предмет

# вода, 3 фунта, 10
# книга, 1 фунт, 3
# еда, 2 фунта, 9
# куртка, 2 фунта, 5
# камера, 1 фунт, 6

# Как выглядит оптимальный набор предметов для похода?

def knapsack(values, weights, names, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Заполняем таблицу dp
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    # Восстанавливаем список выбранных предметов
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(names[i-1])
            w -= weights[i-1]

    return dp[n][capacity], selected_items

# Итерируемся от конца таблицы dp к началу.
# Если значение в текущей ячейке dp[i][w] отличается от значения в предыдущей ячейке dp[i-1][w], это означает, что предмет был выбран.
# Добавляем название предмета в список selected_items и уменьшаем текущую вместимость w на вес выбранного предмета.

# Предметы: вода, книга, еда, куртка, камера
values = [10, 3, 9, 5, 6]
weights = [3, 1, 2, 2, 1]
names = ["вода", "книга", "еда", "куртка", "камера"]
capacity = 6

max_value, selected_items = knapsack(values, weights, names, capacity)
print(f"Оптимальный набор предметов для похода: {selected_items}")
