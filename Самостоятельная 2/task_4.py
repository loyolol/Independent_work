# Задание №4. Бинарный поиск с подсчётом шагов

def binary_search_with_steps(arr, target):
    """Бинарный поиск. Возвращает индекс и количество шагов."""
    left = 0
    right = len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, steps

input_str = input("Введите отсортированный массив чисел через пробел: ")
arr = list(map(int, input_str.split()))

target = int(input("Введите искомое число: "))

index, steps = binary_search_with_steps(arr, target)

if index != -1:
    print("Элемент найден.")
    print(f"Количество шагов: {steps}")
else:
    print("Элемент не найден.")
    print(f"Количество шагов: {steps}")