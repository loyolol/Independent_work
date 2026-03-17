# Задание №2. Числа Фибоначчи 

def fibonacci(n):
    """Рекурсивное вычисление n-го числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

try:
    n = int(input("Введите номер числа Фибоначчи: "))
    
    if n < 0:
        print("Номер числа должен быть неотрицательным")
    else:
        result = fibonacci(n)
        print(f"Число Фибоначчи: {result}")
        
except ValueError:
    print("Ошибка: введите целое число")