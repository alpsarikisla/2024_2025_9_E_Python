# 0 - 100 arasında kaç adet sayı var
# print(100)
# sayac = 0
# adet = 0
# while sayac < 100:
#     adet += 1
#     sayac += 1
# print(adet)

# 0 - 100 arasında 4' e bölünebilen kaç adet sayı var toplamları ne
#Programlamayı öğrenmek için çaba harcamalısınız.
# sayi = 0
# adet = 0
# toplam =0
# while sayi <= 100:
#     kalan = sayi % 4
#     if kalan == 0:
#         adet +=1
#         toplam += sayi
#     sayi += 1
# print("0 - 100 arasında 4'e bölünebilen " + str(adet) + " adet sayı vardır")
# print("Toplamları = " + str(toplam))



# konsoldanalınan 2 sayı arasında 4'e kalansız
# bölünebilen kaç sayı var toplamları ne
# baslangic = int(input("Lütfen başlangıç değeri giriniz = "))
# bitis = int(input("Lütfen bitiş değerini giriniz = "))
#
# sayi = baslangic
# adet = 0
# toplam = 0
#
# while sayi <= bitis:
#     if sayi % 4 == 0:
#         adet += 1
#         toplam += sayi
#     sayi += 1
# print(str(baslangic) + " ile " + str(bitis) + " arasında 4'e kalansız bölünebilen "
#       + str(adet) + " sayı vardır")
# print("toplamları = " + str(toplam))

#Konsoldan alınan pozitif sayıların ortalaması
#(önce kaç adet sayı alınamk istendiğini sor)

# adet = int(input("Kaç adet sayı gireceksiniz = "))
# sayac = 0
# toplam = 0
# pozitifadet = 0
#
# while sayac < adet:
#     sayi = int(input("Lütfen sayi giriniz = "))
#     if sayi > 0:
#         toplam += sayi
#         pozitifadet += 1
#     sayac += 1
#
# ortalama = toplam / pozitifadet
# print("Opzitif sayıların ortalaması = " + str(ortalama))

# Çarpım Tablosunun 3 ler basamağını aşağıdaki şekilde yazdırın
# 3 X 1 = 3
# 3 X 2 = 6

# sayac = 1
# while sayac <= 10:
#     carpim = sayac * 3
#     print("3 X " + str(sayac) + " = " + str(carpim))
#     sayac += 1


#Çarpım tablosunun kullanıcıdan alınan basamağını yazdırın
basamak = int(input("Lütfen basamak değerini yazdırınız = "))

sayac = 1
while sayac <= 10:
    carpim = sayac * basamak
    print(str(basamak) + " X " + str(sayac) + " = " + str(carpim))
    sayac+=1