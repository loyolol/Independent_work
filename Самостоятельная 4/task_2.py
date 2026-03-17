# Задание №2. Эвристика для задачи о рюкзаке

capacity = 10
items = [
    (5, 10),
    (4, 40),
    (6, 30)
]

ratios = []
for i, (weight, value) in enumerate(items):
    ratio = value / weight
    ratios.append((i, weight, value, ratio))

ratios.sort(key=lambda x: x[3], reverse=True)

selected = []
total_weight = 0
total_value = 0

for i, weight, value, _ in ratios:
    if total_weight + weight <= capacity:
        selected.append(i + 1)
        total_weight += weight
        total_value += value

print("Выбраны предметы:", ", ".join(map(str, selected)))
print(f"Итоговая ценность: {total_value}")