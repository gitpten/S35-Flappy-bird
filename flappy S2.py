from random import randint
from time import sleep
from tkinter import Canvas, Tk, mainloop

W = 600
H = 300
D = 20
GRAV = 2
FORCE = 20

class Bird:
    def __init__(self, c: Canvas) -> None:
        self.c = c
        self.obj = c.create_oval(0, 0, D, D, fill='yellow')
        c.move(self.obj, 50, H // 2)
        self.speed = 0
    
    def move(self):
        self.c.move(self.obj, 0, -self.speed)
        self.speed -= GRAV
        self.c.update()
    
    def flap(self, event):
        if event.keysym != 'space':
            return
        self.speed = FORCE

class Tube:
    def __init__(self, c: Canvas) -> None:
        self.c = c
        self.top = c.create_rectangle(0, 0, 0, 0, fill='green2')
        self.bottom = c.create_rectangle(0, 0, 0, 0, fill='green2')
        self.space = 150
        self.place()
    
    def place(self):
        y = randint(50, H - 50)
        x = W * 1.1
        self.c.coords(self.top, x, 0, x + D, y - self.space / 2)
        self.c.coords(self.bottom, x, H, x + D, y + self.space / 2)
    
    def move(self, speed):
        self.c.move(self.top, -speed, 0)
        self.c.move(self.bottom, -speed, 0)
        x, y, xx, yy = self.c.coords(self.top)
        if x < 0:
            self.place()
        

tk = Tk()
c = Canvas(tk, width=W, height=H, bg='lightblue')
c.pack()
frank = Bird(c)
tube = Tube(c)
run = True
speed = 10

c.bind_all("<Key>", frank.flap)

while run:
    frank.move()
    tube.move(speed)
    sleep(0.04)



mainloop()