# Dizileri Birleştirme
liste1 = [1,2,3,4,5]
liste2 = [6,7,8,10]
liste3 = liste1 + liste2
print(liste3)
for eleman in  liste3:
    print(eleman)

#Diziye Eleman Dahil Etme
sehirler = ["Ankara","Istanbul","İzmir"]
sehirler = sehirler + ["Eskişehir"]
print(sehirler)

# Veri Değiştirme
sayilar = [1,2,3,4,5,6]
sayilar[2] = "Murtaza"
print(sayilar)

for sayi in sayilar:
    if sayi == "Murtaza":
        break
    else:
        print(sayi)
