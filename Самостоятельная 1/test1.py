# -------------------------------
# 1 Задание — Пузырьковая сортировка
# -------------------------------
def bubble_sort(arr):
    comparisons = 0
    swaps = 0

    n = len(arr)

    for i in range(n):
        for j in range(n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return arr, comparisons, swaps


print("Задание 1")

arr = [5, 1, 4, 2, 8]

print("Исходный массив:", arr)

sorted_arr, comp, sw = bubble_sort(arr.copy())

print("Отсортированный массив:", sorted_arr)
print("Количество сравнений:", comp)
print("Количество обменов:", sw)