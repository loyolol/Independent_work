# -------------------------------
# 3 Задание — Оптимизированный пузырь
# -------------------------------
def optimized_bubble(arr):
    a = arr.copy()
    n = len(a)
    passes = 0

    for i in range(n):
        swapped = False
        passes += 1

        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        if not swapped:
            print("Массив уже отсортирован.")
            break

    return passes


print("\nЗадание 3")

arr = [1, 2, 3, 4, 5]

passes = optimized_bubble(arr)

print("Количество проходов:", passes)