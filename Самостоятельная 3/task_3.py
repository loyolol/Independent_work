# Задание №3. Сумма цифр числа 

def sum_of_digits(n):
    """Рекурсивное вычисление суммы цифр числа."""

    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

try:
    num = int(input("Число: "))
    
    result = sum_of_digits(abs(num))
    print(f"Сумма цифр: {result}")
    
except ValueError:
    print("Ошибка: введите целое число")