from email.mime import image
from random import randint
from time import sleep
from tkinter import Canvas, PhotoImage, Tk, mainloop

W = 600
H = 300
D = 20
GRAV = 2
FORCE = 20

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

class Bird:
    def __init__(self, c: Canvas) -> None:
        self.c = c
        self.image = PhotoImage(file='flappy.png')
        self.imageup = PhotoImage(file='flappy-up.png')
        self.imagedown = PhotoImage(file='flappy-down.png')
        self.obj = c.create_image(D // 2, D // 2, image=self.image)
        c.move(self.obj, 50, H // 2)
        self.speed = 0
    
    def move(self):
        self.c.move(self.obj, 0, -self.speed)
        self.speed -= GRAV
        if self.speed > 5: 
            self.c.itemconfig(self.obj, image = self.imageup)
        elif self.speed < -5: 
            self.c.itemconfig(self.obj, image = self.imagedown)
        else:
            self.c.itemconfig(self.obj, image = self.image)
        self.c.update()
    
    def flap(self, event):
        if event.keysym != 'space':
            return
        self.speed = FORCE
    
    def death(self, t: Tube):
        xf, yf = self.c.coords(self.obj)
        if yf > H:
            return True

        xx, yy, xt, yt = t.c.coords(t.top)
        xx, yy, xb, yb = t.c.coords(t.bottom)
        
        if (xf - D // 2 <= xt <= xf + D // 2 and yf - D // 2 <= yt <= yf + D // 2) or \
            (xf - D // 2 <= xb <= xf + D // 2 and yf - D // 2 <= yb <= yf + D // 2):
            return True
        return False
        

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
    run = not frank.death(tube)
    sleep(0.04)


mainloop()