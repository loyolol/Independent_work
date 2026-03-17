# Задание №1. Создание графического окна

import tkinter as tk

root = tk.Tk()
root.title("Мое первое графическое окно")
root.geometry("600x400")
root.resizable(False, False)

root.mainloop()