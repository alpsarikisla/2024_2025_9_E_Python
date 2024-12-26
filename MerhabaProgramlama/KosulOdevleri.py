# Koşul Ödevleri
# konsoldan alınan sayı tek mi çift mi?

# konsoldan alınan sayı 0 - 100 arasında mı?

# konsoldan doğum yılını alınız.
# yaş 15 ten büyük ise yaş değeri uygun
# değil ise yaş değeri uygun değildir yazınız

# konsoldan alınan not1 not2 sözlü notunun ortalaması
# 50 den büyük ise geçtin değil ise kaldın yazılsın

# konsoldan alınan 3 ürünün fiyatı 1.000TL üstünde ise
# 50 TL indirim uygulayın
fiyat1 = float(input("Lütfen 1. ürünün fiyatını giriniz"))
fiyat2 = float(input("Lütfen 2. ürünün fiyatını giriniz"))
fiyat3 = float(input("Lütfen 3. Ürünün fiyatını giriniz"))

toplam = fiyat1 + fiyat2 + fiyat3
if toplam >= 1000:
    toplam = toplam - 50

print("Toplam Fiyat = " + str(toplam) + " TL")

# Konsoldan yaşadığınız şehri isteyin
# girilen şehir ankara ise başkentte yaşıyorsun yazın
# eskişehir ise eseses kikiki eski eski es yazın

