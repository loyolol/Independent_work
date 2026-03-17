# Задание №3. Обработка событий мыши

import tkinter as tk
import random

def click_handler(event):
    x, y = event.x, event.y
    print(f"Координаты клика: x={x}, y={y}")
    
    # Случайный цвет
    color = f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}'
    
    # Рисуем круг
    r = 20
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline='black')

root = tk.Tk()
root.title("События мыши")
root.geometry("600x400")

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack()

canvas.bind("<Button-1>", click_handler)

root.mainloop()