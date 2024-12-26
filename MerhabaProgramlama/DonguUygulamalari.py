# 0 ile 100 arasındaki sayıları yazdırınız
# sayac = 0
# while sayac <= 100:
#     print(sayac)
#     sayac = sayac + 1

# 100 ile 0 arasındaki sayıları yazdırınız
# sayac = 100
# while sayac >= 0:
#     print(sayac)
#     sayac = sayac - 1

# 0 dan kullanıcıdan alınan sayıya kadar olan sayıları yazdırınız
# sayac = 0
# sayi = int(input("Lütfen üst sınır giriniz"))
#
# while sayac <= sayi:
#     print(sayac)
#     sayac = sayac + 1

# 0 - 100 arasındaki çift sayıları yazdırınız
# sayac = 0
# while sayac <= 100:
#     kalan = sayac % 2
#     if kalan == 0:
#         print(sayac)
#     sayac = sayac + 1

# konsoldan alınan sayıdan 100 e kadar olan çift sayıları yazdırınız
# sayac = int(input("Başlangıç değerini giriniz = "))
# while sayac <= 100:
#     kalan = sayac % 2
#     if kalan == 0:
#         print(sayac)
#     sayac = sayac + 1

# konsoldan isim alıp 10 kere ismi yazdırın
# isim = input("isim giriniz = ")
# sayac = 0
# while sayac <= 10:
#     print(isim)
#     sayac = sayac + 1

# 0 - 100 arasında 3'e kalansız bölünebilen kaç adet sayı vardır
# sayac = 0
# adet = 0
# while sayac <= 100:
#     kalan = sayac % 3
#     if kalan == 0:
#         adet = adet + 1
#     sayac = sayac + 1
# print("0 ile 100 arasında 3'e kalansız bölünebilen " + str(adet) + " sayı vardır")

# konsoldan alınan sayı 0 ile 100 arasında mı?
alinan = float(input("Lütfen 0 - 100 arasında bir sayı giriniz = "))
if alinan >= 0 and alinan <= 100:
    print("Girilen sayı 0 -100 arasındadır")
else:
    print("Sana 0 -100 arasında demedik mi !!!")


