# Задание №4. Движение объекта

import tkinter as tk

def move_square():
    global x_pos
    if x_pos + square_size < 600:  # Проверка на выход за границу
        x_pos += 5
        canvas.coords(square, x_pos, y_pos, x_pos + square_size, y_pos + square_size)
        root.after(50, move_square)

root = tk.Tk()
root.title("Движение объекта")
root.geometry("600x400")

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack()

square_size = 50
x_pos = 10
y_pos = 175

square = canvas.create_rectangle(x_pos, y_pos, x_pos + square_size, y_pos + square_size, fill='red')

root.after(50, move_square)
root.mainloop()