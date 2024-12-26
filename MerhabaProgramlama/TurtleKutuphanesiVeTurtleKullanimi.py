import turtle
ekran = turtle.Screen() # kaplumbapanın oluşacağı form ekranını açtık
kaplumbaa = turtle.Turtle()# turtle kütüphanesini değişkene attık
kaplumbaa.shape("turtle") # okun şekli kaplumbağa olsun

sayac = 0
kaplumbaa.speed(2)
kaplumbaa.color("green") # çizgi rengi
kaplumbaa.pensize(5) # çizgi büyüklüğü
kaplumbaa.fillcolor("yellow")
kaplumbaa.begin_fill()
while sayac < 4:
    kaplumbaa.forward(100)# 100 bitim ilerle
    kaplumbaa.left(90)# 90 derece sola dön
    sayac = sayac + 1
kaplumbaa.end_fill()
kaplumbaa.penup()
kaplumbaa.forward(120)
kaplumbaa.pendown()
sayac = 0
kaplumbaa.fillcolor("pink")
kaplumbaa.begin_fill()
while sayac < 4:
    kaplumbaa.forward(100)# 100 bitim ilerle
    kaplumbaa.left(90)# 90 derece sola dön
    sayac = sayac + 1
kaplumbaa.end_fill()




ekran.mainloop()# ekranın açık kalmasını sağladık

