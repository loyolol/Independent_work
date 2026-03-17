import time

# -------------------------------
# 2 Задание  — Сравнение алгоритмов
# -------------------------------
def selection_sort(arr):
    a = arr.copy()

    start = time.time()

    for i in range(len(a)):
        min_index = i

        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    end = time.time()

    return a, (end - start) * 1000


def insertion_sort(arr):
    a = arr.copy()

    start = time.time()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    end = time.time()

    return a, (end - start) * 1000


print("\nЗадание 2")

arr = [9, 3, 7, 1, 6]

sel_sorted, sel_time = selection_sort(arr)
ins_sorted, ins_time = insertion_sort(arr)

print("Сортировка выбором:", sel_sorted, f"(время: {sel_time:.4f} мс)")
print("Сортировка вставками:", ins_sorted, f"(время: {ins_time:.4f} мс)")
