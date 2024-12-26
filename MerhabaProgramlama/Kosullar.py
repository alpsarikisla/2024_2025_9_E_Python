# Koşullar
# Koşullar programlamada akış kontrol sistemi olarak kullanılır
# Koşul kontrolü MUTLAKA Bool(Boolean) veriler üzerinden yapılır
# koşul true verilerde işlemi gerçekleştirir. false verilerde atlar

# konsoldan alınan veri pozitif ise sayı pozitiftir yazdıralım
# sayi = int(input("Lütfen bir sayı giriniz = "))
#
# pozitifMi = sayi > 0
#
# if pozitifMi == True:
#     print("Girilen Sayı pozitiftir")

#if ve else kullanımı
# konsoldan alınan veri;
# pozitif ise sayı pozitiftir
# değil ise sayı negatiftir yazdıralım

# sayi = int(input("Lütfen bir sayı giriniz = "))
# if sayi >= 0:
#     print("Sayı pozitiftir")
# else:
#     print("Sayı Negatiftir")
# # if ile belirtilen koşul true sonuç üretir ise if'in indenti çalışır
# # false sonuç üretir ise if'in indentini atlar ve else'in indentini çalıştırırı
# # if ve else birlikte kullanıldığında ya if yada else'ten bir mutlaka çalışacaktır

# sayi = float(input("Lütfen bir sayı giriniz = "))
# if sayi == 0:
#     print("Sayı Nötr'dür")
# if sayi < 0:
#     print("Sayı Negatiftir")
# if sayi > 0:
#     print("Sayı Pozitiftir")

# konsoldan alınan sayı
# 20 - 40 1. aralık
# 50 - 70 2. aralık
# 60 - 80 3. aralık

sayi = float(input("Lütfen bir sayı giriniz = "))
if sayi > 20 and sayi < 40:
    print("sayı 1. aralıkta")
elif sayi > 50 and sayi < 70:# üstteki değilse eğer
    print("sayı 2. aralıkta")
elif sayi > 60 and sayi < 80:# üstteki değilse eğer
    print("sayı 3. aralıkta")
else:# yukarıdakilerin hiçbiri değilse
    print("Girilen sayı tanımlı aralıklarda değildir")

# else sadece kendinden önceki if'e bağlıdır


