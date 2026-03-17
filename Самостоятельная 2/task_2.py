# Задание №2. Поиск всех вхождений

def linear_search_all(arr, target):
    """Возвращает список индексов всех вхождений target."""
    indices = []
    for i, val in enumerate(arr):
        if val == target:
            indices.append(i)
    return indices

input_str = input("Введите массив чисел через пробел: ")
arr = list(map(int, input_str.split()))

target = int(input("Введите искомое число: "))

indices = linear_search_all(arr, target)

if indices:
    print("Элемент найден на позициях:", *indices)
else:
    print("Элемент не найден")