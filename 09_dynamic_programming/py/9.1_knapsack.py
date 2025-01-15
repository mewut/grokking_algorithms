# Вы вор с рюкзаком, в который помещается 4 фунта веса.
# Вы можете украсть: магнитофон, ноутбук, гитара, телефон, плеер.

# магнитофон (вес 4 фунта, цена 3000), 
# ноутбук (вес 3 фунта, цена 2000), 
# гитара (вес 1 фунт, цена 1500), 
# телефон (вес 1 фунт, цена 2000)
# плеер (вес 1 фунт, цена 1000)

# Какую максимальную стоимость можно унести в рюкзаке?

# Решение через динамическое программирование


def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Предметы: магнитофон, ноутбук, гитара, телефон, плеер
values = [3000, 2000, 1500, 2000, 1000]
weights = [4, 3, 1, 1, 1]
capacity = 4

max_value = knapsack(values, weights, capacity)
print(f"Максимальная стоимость, которую можно унести: {max_value}")


# Создаем таблицу dp, где dp[i][w] - максимальная стоимость, которую можно получить, используя первые i предметов и рюкзак вместимостью w. 
# Таблица заполняется, используя рекуррентное соотношение для задачи о рюкзаке.
# И на бумаге в виде обычной таблицы выглядит проще...

# Объяснение: клетка таблицы - это cell. i - это строка, j - это столбец.
# cell[i][j] = максимум от (1. предыдущий максимум (значение в cell[i-1][j]) или 2. стоимость текущего элемента + стоимость оставшегося пространства (cell[i-1][j - вес предмета]) )
# применяя эту формулу к каждой ячейке таблицы, получится таблица dp
