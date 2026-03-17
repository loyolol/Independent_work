# Задание №1. Линейный поиск 

def linear_search_first(arr, target):
    """Возвращает индекс первого вхождения target или -1, если элемент не найден."""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


input_str = input("Введите массив чисел через пробел: ")
arr = list(map(int, input_str.split()))

target = int(input("Введите искомое число: "))

index = linear_search_first(arr, target)

if index != -1:
    print(f"Элемент найден на позиции: {index}")
else:
    print("Элемент не найден")