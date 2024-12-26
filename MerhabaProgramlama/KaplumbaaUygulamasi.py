import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.speed(500)
n=36
h=0

i = 0
while   i <= 460:
    c= colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    t.color(c)
    t.left(145)
    i+=1
    j = 0
    while j < 5:
        t.forward(300)
        t.left(150)
        j+=1
s.mainloop()