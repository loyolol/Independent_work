# Задание №2. Рисование простых фигур

import tkinter as tk

root = tk.Tk()
root.title("Рисование фигур")
root.geometry("600x400")

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack()

# Прямоугольник
canvas.create_rectangle(50, 50, 200, 150, fill='blue', outline='red', width=3)

# Круг (овал)
canvas.create_oval(300, 50, 450, 150, fill='yellow', outline='green', width=3)

root.mainloop()