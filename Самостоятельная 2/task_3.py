# Задание №3. Бинарный поиск в отсортированном массиве

def binary_search(arr, target):
    """Бинарный поиск. Возвращает индекс элемента или -1, если не найден."""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

input_str = input("Введите отсортированный массив чисел через пробел: ")
arr = list(map(int, input_str.split()))

target = int(input("Введите искомое число: "))

index = binary_search(arr, target)

if index != -1:
    print(f"Элемент найден на позиции: {index}")
else:
    print("Элемент не найден")