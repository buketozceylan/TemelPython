# -*- coding: utf-8 -*-
ogrenci1="Bukiş"
ogrenci2="Zülfiş"
ogrenci3="Agah"

ogrenciler=["Bukiş","Zülfiş","Agah"]
ogrenciler.append("Ahmet")
ogrenciler.remove("Bukiş")
ogrenciler[0]="Veli"
print(ogrenciler)
#list constructor
sehirler=list(("Ankara","İstanbul"))
print(sehirler)

print(len(sehirler))

#diğer fonksiyonlar
#print(sehirler.clear())
print(sehirler.count("Ankara"))
print("Ankara Index'i="+str(sehirler.index("Ankara")))
sehirler.pop(1)
sehirler.insert(0,"İstanbul")
print(sehirler.reverse())
print(sehirler)

sehirler2=sehirler
sehirler2[0]="İzmir"
sehirler3=sehirler.copy()
print(sehirler3)

sehirler.extend(sehirler3)
sehirler.sort()
sehirler.reverse()
print(sehirler)












