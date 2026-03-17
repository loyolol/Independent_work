# Задание №4. Рекурсивный обход массива

def print_array_recursive(arr, index=0):
    """Рекурсивный вывод элементов массива без использования циклов."""
    if index >= len(arr):
        return
    
    print(arr[index], end=" ")
    
    print_array_recursive(arr, index + 1)

input_str = input("Массив: ")
arr = list(map(int, input_str.split()))

print_array_recursive(arr)
print()  