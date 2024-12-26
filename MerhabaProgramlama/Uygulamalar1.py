sayi = 10

# Ödev Sonuçlar true veya false olarak yazdırılacak
# sayı değişkeni içerisindeki veri pozitif mi?
pozitifMi = sayi > 0
print("Sayı pozitif mi = ")
print(pozitifMi)

# sayı değişkeni içerisindeki veri çift mi?
kalan = sayi % 2
ciftMi = kalan == 0
print("Sayı çift mi?")
print(ciftMi)

# sayı değişkeni içerisindeki veri 0 - 100 arasında mı?
sonuc = sayi > 0 and sayi < 100
print("Sayı değişkeni içerisindeki veri 0 - 100 arasında mı?")
print(sonuc)

# sayı değişkeni içerisindeki veri ondalık mi?
kalan2 = sayi % 1
ondalikMi = kalan2 == 0
print("Tamsayi Mı")
print(ondalikMi)
