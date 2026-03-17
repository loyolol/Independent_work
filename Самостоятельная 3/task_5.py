# Задание №5. Степень числа 

def power(base, exponent):
    """Рекурсивное вычисление степени числа."""
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    
    return base * power(base, exponent - 1)

try:
    base = float(input("Число: "))
    exponent = int(input("Степень: "))
    
    result = power(base, exponent)
    print(f"Результат: {result}")
    
except ValueError:
    print("Ошибка: введите корректные числа")