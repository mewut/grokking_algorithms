// Предположим, что вы собраетесь в турпоход. Емкость вашего рюкзака составляет 6 фунтов, и вы можете взять предметы из следующего списка. 
// У каждого предмета имеется стоимость; чем она выше, тем важнее предмет
// вода, 3 фунта, 10
// книга, 1 фунт, 3
// еда, 2 фунта, 9
// куртка, 2 фунта, 5
// камера, 1 фунт, 6
// Как выглядит оптимальный набор предметов для похода?

function knapsack(values, weights, names, capacity) {
    const n = values.length;
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

    const selected_items = [];
    let w = capacity;
    for (let i = n; i > 0; i--) {
        if (dp[i][w] !== dp[i - 1][w]) {
            selected_items.push(names[i - 1]);
            w -= weights[i - 1];
        }
    }

    return { maxValue: dp[n][capacity], selectedItems: selected_items };
}

// Предметы: вода, книга, еда, куртка, камера
const values = [10, 3, 9, 5, 6];
const weights = [3, 1, 2, 2, 1];
const names = ["вода", "книга", "еда", "куртка", "камера"];
const capacity = 6;

const result = knapsack(values, weights, names, capacity);
console.log(`Оптимальный набор предметов для похода: ${result.selectedItems.join(', ')}`);
