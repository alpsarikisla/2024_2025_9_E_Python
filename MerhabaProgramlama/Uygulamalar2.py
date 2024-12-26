# Konsoldan alınan sayı pozitif mi?
# metinselSayi = input("Lütfen sayı giriniz")
# sayi = int(metinselSayi)
# pozitifmi = sayi >= 0
# print("Pozitif mi = " + str(pozitifmi))

# ÖDEV 1
# konsoldan alınan 2 adet notun ortalamasını hesaplayınız?
# # 1 - Başla
# # 2 - konsoldan 1. notu al, türünü değiştir
# metinsel_not1 = input("Lütfen 1. notunuzu giriniz")
# not1 = int(metinsel_not1)
# # 3 - konsoldan 2. notu al, türünü değiştir
# not2 = int(input("Lütfen 2. notunuzu giriniz"))
# # 4 - alınan notları topla toplam değişkene at
# toplam = not1 + not2
# # 5 - toplamı 2 ye böl, ortalama değişkenine at
# ortalama = toplam / 2
# # 6 - ortalamayı yazdır
# print("Not Ortalamanız = " + str(ortalama))

# ÖDEV 2
# konsoldan isim soyad ve doğum yılı isteyiniz
# merhaba isim soyad yaşınız ... şeklinde yazdırın

# # 1 - Konsoldan isim iste değişkene at
# isim = input("Lütfen isminizi giriniz = ")
# # 2 - Konsoldan soyisim iste değişkene at
# soyisim = input("Lütfen soyisminizi giriniz = ")
# # 3 - Doğum yılı iste değişkene at, türünü değiştir
# dogumYili = int(input("Doğum yılınızı giriniz = "))
# # 4 - Doğum yılından yaşı hesapla değişkene at
# yas = 2024 - dogumYili
# # 5 - isim, soyisim, yaş değişkenlerini yazdır
# print("Merhaba " + isim + " " + soyisim + " yaşınız = " + str(yas))

# ÖDEV 3
# konsoldan alınan not1, not2, sözlü
# notlarının ortalamasını hesaplayınız.

# # 1 - Konsoldan 1. notu al, türünü değiştir, değişkene at
# metinselNot1 = input("Lütfen 1. notunuzu giriniz = ")
# not1 = int(metinselNot1)
# # 2 - Konsoldan 2. notu al, türünü değiştir, değişkene at
# not2 = int(input("Lütfen 2. notunuzu giriniz = "))
# # 3 - Konsoldan Sözlü notunu al, türünü değiştir, değişkene at
# sozlu = int(input("Lütfen sözlü notunuzu giriniz = "))
# # 4 - not1 sot2 ve sözlü değişkelerinin verilerini topla, toplam değişkenine at
# toplam = not1 + not2 + sozlu
# # 5 - toplam değişkeni 3'e bölerek ortamayı hesapla,ortalama değişkenine at
# ort = toplam / 3
# # 6 - ortalama değişkeninin verisini yazdır
# print("Not ortalamanız = " + str(ort))

# Ödev 4
# konsoldan alınan sayı çift ise true değilse false yazdırınız

# # 1 - Konsoldan sayı al, türünü değiştir değişkene at
# sayi = int(input("Lütfen sayı giriniz = "))
# # 2 - sayının 2'ye bölümünden kalanı hesapla değişkene at
# kalan = sayi % 2
# # 3 - kalan 0'a eşitmi değişkene at
# ciftMi = kalan == 0
# # 4 - sonuc değişkenini yazdır
# print("Girilen sayı çift mi = " + str(ciftMi))

# Ödev 5
# konsoldan alınan ürün fiyatının KDV dahil halini yazdırınız
kdvOrani = 0.20
# 1 - konsoldan ürünün fiyatını alalım türünü değiştirip değişkene atalım
fiyat = float(input("Lütfen ürün fiyatını giriniz = "))
# 2 - fiyatın kdv miktarını hesapla değişkene at
kdv = fiyat * kdvOrani
# 3 - kdv miktarı ile ürün fiyatını topla değişkene at
kdvDahil = fiyat + kdv
# 4 - kdv dahil fiyatı yazdır
print("Ka De Ve Dahil fiyat = " + str(kdvDahil))

# Ödev 6
# konsoldan alınan 3 ürünün fiyatını alıp
# Ara Toplam, KDV Tutarı, Genel toplam bilgilerini yazdırınız