# Dizi (Array) Nedir?
# Bir veya daha çok verinin
# belirli bir "index" numarası ile bir arada tutulmasını
# sağlayan yapıya dizi(array) denir.
# Amacı veri kümesi oluşturmaktır.
# python programlama dilinde dizi oluşturmanın
# önemli bir özelliği ise farklı veri türlerini bir arada
# tutabilmekteyiz.

# 5 adet sayı bilgisini tutalım
# s1 = 45
# s2 = 70
# s3 = -57
# s4 = 88
# s5 = 9

# 5 adet sayı bilgisini dizide tutalım
sayilar = [45,70,-57,88,9]
print(sayilar[0])
# sayılar dizisinin 0. index numarasındaki veriyi yazdıralım

# sayılar dizisinin tüm elemanlarını yazdıralım
print("Dizi Elemanları")
indexno = 0
while indexno < 5:
    print(sayilar[indexno])
    indexno += 1

print("for ile dizi elemanları")
for sayi in sayilar:
    print(sayi)
# sayilar dizisi içindeki her verinin adı sayi olsun
# dizi elemanlarının tümünü yazdır
