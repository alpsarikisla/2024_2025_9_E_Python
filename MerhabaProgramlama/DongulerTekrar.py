# Indent(Girinti) pyton programlama dilinde koşula bağlı yapıcalak
# olan işlemleri temsil eder.(Indent Önemli!!!!!)

#sayi değişkeni içerisine 5 değerini attık
# sayi = 5
#
# if sayi > 0:
#     print("Sayı 0 dan büyük. Pozitif")
# else:
#     print("Sayı 0 dan küçük. Negatif")
# print("Koşula bağlı değilim")

# sayi = 0
#
# while sayi < 5:
#     print(sayi)
#     sayi += 1

# devam etmek istiyor musunuz? e/h
# h girilene kadar isim soran program yazdıralım...

# secenek = "e"
# while secenek == "e":
#     isim = input("Lütfen isim giriniz = ")
#     secenek = input("Devam etmek istiyor musunuz? (e/h) ")

# Murtaza ismi girilene kadar isim alalım
# isim = ""
# while isim != "murtaza":
#     isim = input("İsminizi giriniz = ")
# print("Sen gelme murtaza!!!")

# negatif sayı girilene kadar girilen sayıların toplamı
# sayi = 0
# toplam = 0
# while sayi >= 0:
#     sayi = int(input("Lütfen pozitif sayı giriniz = "))
#     toplam += sayi
# print("Negatif sayı girdin ben gidiyom!!!")
# print("Girilen sayıların toplamı = " + str(toplam))

# 0 - 10 arasındaki sayıları yazdırınız
# sayi = 0
# while sayi <= 10:
#     print(sayi)
#     sayi += 1


# for sayi in range(10):
#     print(sayi)

# #ÖDEV 1
# # negatif sayı girilene kadar girilen sayıların ortalaması
# sayi = 0
# toplam = 0
# adet = 0
#
# while sayi >= 0:
#     sayi = int(input("Lütfen pozitif sayı giriniz = "))
#     toplam += sayi
#     adet += 1
#
# print("Negatif sayı girildi. İşlem sonlandırıldı.")
# ortalama = toplam / adet
# print("Girilen pozitif sayıların ortalaması = " + str(ortalama))

#ÖDEV 2
# kontrole devam edilsin mi e/h şeklinde sorarak
# konsoldan alınan sayıların tek mi çift mi olduğunu yazdırın

secenek = "e"

while secenek == "e":
    sayi = int(input("Sayı giriniz = "))
    kalan = sayi % 2
    if kalan == 0:
        print("Sayı Çift")
    else:
        print("Sayı tek")
    secenek = input("Sayı girmeye devam edilsin mi? e/h ")
print("Görüşmek Üzere")

#ÖDEV 3
#Konsoldan alınan sayının faktöriyelini hesaplayıp yazdırın

#ÖDEV 4
# fibonacci serisini 25 sayısına kadar yazdırınız
# kendinden önceki 2 sayının toplamı olacak şekilde sıralanan seriye
# fibonacci serisi denir
# 1 1 2 3 5 8 13 21







