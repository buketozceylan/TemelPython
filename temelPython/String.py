#substring
mesaj = "Merhaba Dünya"
print(mesaj[2:5])
yeniMesaj=mesaj[2:]
print(yeniMesaj)

#len fonksiyonu
print(len(mesaj))
yeniMesaj2=mesaj[len(mesaj)-3:len(mesaj)]
print(yeniMesaj2)

#lower and upper
print(mesaj.upper())
print(mesaj.lower())

#replace
print(mesaj.replace("ü","u"))
print(mesaj.replace("a", "e"))

#split
bilgi="Bukiş Özceylan 22 İzmir"
print(bilgi.split())
print(bilgi.split("i"))

#input
ad=input("Adınız=")
sayi1=input("Sayı Giriniz=")
sayi2=input("Sayı Giriniz=")
sayi3=input("Sayı Giriniz=")
print(int(sayi1)*int(sayi2))












