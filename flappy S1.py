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

tk = Tk()
c = Canvas(tk, width=W, height=H, bg='lightblue')
c.pack()
frank = Bird(c)
c.bind_all("<Key>", frank.flap)
run = True

while run:
    frank.move()
    sleep(0.04)



mainloop()