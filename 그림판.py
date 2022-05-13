from tkinter import *

def paint(event):
    x1, y1 = event.x-1, event.y-1
    x2, y2 = event.x+1, event.y+1
    canvas.create_oval(x1, y1, x2, y2, fill = pen_color, outline = pen_color, width = pen_size)

def blue():
    global pen_color
    pen_color = "blue"

def change_color(color):
    global pen_color
    pen_color = color

def size_up():
    global pen_size
    pen_size += 1

def size_down():
    global pen_size
    if pen_size > 1:
        pen_size -= 1
    
    

pen_color = "black"
pen_size = 1

window = Tk()
canvas = Canvas(window, width = 500, height = 500)
canvas.pack()
canvas.bind("<B1-Motion>", paint)

button_b = Button(window, text = "파랑", width = 5, bg = "lightblue", command = blue, font = ("나눔바른펜", 12))
button_b.place(x=0, y=0)

button_p = Button(window, text = "핑크", width = 5, bg = "pink", command = lambda : change_color("pink"), font = ("나눔바른펜", 12))
button_p.place(x=0, y=40)

button_r = Button(window, text = "빨강", width = 5, bg = "red", command = lambda : change_color("red"), font = ("나눔바른펜", 12))
button_r.place(x=0, y=80)

button_size_up = Button(window, text = "굵게", command = size_up, width = 5, font = ("나눔바른펜", 12))
button_size_up.place(x=0, y=120)

button_size_down = Button(window, text = "가늘게", command = size_down, width = 5, font = ("나눔바른펜", 12))
button_size_down.place(x=0, y=160)

button_e = Button(window, text = "지우기", command = lambda : canvas.delete("all"), width = 5, font = ("나눔바른펜", 12))
button_e.place(x=0, y=200)


window.mainloop()
