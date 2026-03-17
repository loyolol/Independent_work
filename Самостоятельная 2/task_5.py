# Задание №5. Поиск студента по фамилии в списке

students = [
    ("Иванов", "Пётр", "ИС-21"),
    ("Сидоров", "Алексей", "ИС-22"),
    ("Петров", "Иван", "ИС-21")
]

search_surname = input("Введите фамилию для поиска: ").strip().lower()

found = []
for surname, name, group in students:
    if surname.lower() == search_surname:
        found.append((surname, name, group))

if found:
    print("Найден студент:")
    for s in found:
        print(f"{s[0]} {s[1]} {s[2]}")
else:
    print("Студент с такой фамилией не найден.")