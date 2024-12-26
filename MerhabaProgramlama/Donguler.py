# Bir işlemin birden çok kez tekrarlanacağı durumda döngü kullanılır

# 1 ile 10 arasındaki sayıları yazdıralım
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# While Döngüsü
# 1 ile 10 arasındaki sayıları döngü ile yazdıralım
# döngü kendisine verilen koşul sağlandığı sürece
# (true olduğu sürece) indent'i çalıştırır.
sayac = 1
while sayac <= 10:
   print(sayac)
   sayac = sayac + 1
print("while dışı bölge")