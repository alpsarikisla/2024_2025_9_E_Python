# Konsoldan Çokgen kaç kenarlı diye sorulacak
# Girilen kenar sayısına göre çokgen çizdirilecek
import turtle
ekran = turtle.Screen()
ok = turtle.Turtle()

print("Çizdirmek istediğiniz çokgenin")
kenarsayi = int(input("kenar sayısını yazınız = "))
print("1) Kırmızı")
print("2) Yeşil")
print("3) Mavi")
secilenrenk = input("Seçtiğiniz rengin kodunu giriniz = ")
if secilenrenk == "1":
    ok.color("red")
elif secilenrenk == "2":
    ok.color("green")
elif secilenrenk == "3":
    ok.color("blue")

aci = 360 / kenarsayi
sayac = 0
while sayac < kenarsayi:
    sayac = sayac + 1
    ok.forward(50)
    ok.left(aci)
ekran.mainloop()