# Задание №5. Управление объектом с клавиатуры

import tkinter as tk

def move(event):
    global x, y
    step = 10
    size = 50
    
    if event.keysym == 'Up' and y - step > 0:
        y -= step
    elif event.keysym == 'Down' and y + size + step < 400:
        y += step
    elif event.keysym == 'Left' and x - step > 0:
        x -= step
    elif event.keysym == 'Right' and x + size + step < 600:
        x += step
    
    canvas.coords(player, x, y, x + size, y + size)

root = tk.Tk()
root.title("Управление с клавиатуры")
root.geometry("600x400")

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack()

x, y = 100, 100
size = 50
player = canvas.create_rectangle(x, y, x + size, y + size, fill='green')

root.bind("<KeyPress>", move)
root.focus_set()

root.mainloop()