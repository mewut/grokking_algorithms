function knapsack(values, weights, capacity) {
    const n = values.length;
    // Создаем таблицу dp размером (n+1) x (capacity+1) и инициализируем её нулями
    const dp = Array.from({ length: n + 1 }, () => Array(capacity + 1).fill(0));

    // Заполняем таблицу dp
    for (let i = 1; i <= n; i++) {
        for (let w = 1; w <= capacity; w++) {
            if (weights[i - 1] <= w) {
                // Если вес текущего предмета меньше или равен текущей вместимости
                dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]);
            } else {
                // Если вес текущего предмета больше текущей вместимости
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    // Возвращаем максимальную стоимость, которую можно унести
    return dp[n][capacity];
}

// Предметы: магнитофон, ноутбук, гитара, телефон, плеер
const values = [3000, 2000, 1500, 2000, 1000];
const weights = [4, 3, 1, 1, 1];
const capacity = 4;

const max_value = knapsack(values, weights, capacity);
console.log(`Максимальная стоимость, которую можно унести: ${max_value}`);
