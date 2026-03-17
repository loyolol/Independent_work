# Задание №1. Факториал числа 

def factorial(n):
    """Рекурсивное вычисление факториала."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

try:
    num = int(input("Число: "))
    
    if num < 0:
        print("Факториал отрицательного числа не определен")
    else:
        result = factorial(num)
        print(f"Факториал: {result}")
        
except ValueError:
    print("Ошибка: введите целое число")