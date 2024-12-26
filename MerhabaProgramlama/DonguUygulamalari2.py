# Konsoldan 5 adet sayı alıp ortalamasını hesaplayınız


sayac = 0
toplam = 0
while sayac < 5:
    sayi = int(input("Lütfen bir sayi giriniz = "))
    toplam = toplam + sayi
    sayac += 1
ortalama = toplam / 5
print("Girilen sayıların ortalaması = " + str(ortalama))