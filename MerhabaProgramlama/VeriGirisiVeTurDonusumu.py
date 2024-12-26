# konsoldan alınan 2 sayıyı toplayınız
sayi1str = input("Lütfen 1. sayıyı giriniz = ")
sayi2str = input("Lütfen 2. sayıyı giriniz = ")
sayi1 = int(sayi1str)
sayi2 = int(sayi2str)
toplam = sayi1 + sayi2
print("Toplam = " + str(toplam))

fark = sayi1 - sayi2
print("Fark = " + str(fark))

carpim = sayi1 * sayi2
print("Çarpım = ")
print(carpim)

bolum = sayi1 / sayi2
print("Bolum = " + str(bolum))

mod = sayi1 % sayi2
print(sayi1str + " sayısının " + sayi2str + "' ye bölümünden kalan = " + str(mod))
