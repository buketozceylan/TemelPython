# -*- coding: utf-8 -*-

f = open("musteriler.txt",)
#print(f.read())
#for l in f:
 #   print(l)
#f.close()
#r Read default olarak bu vardır., a append(ekleme),w write(yeni oluştur), x create(yarat)


#fileToAppend = open("ogrenciler.txt","w")
#fileToAppend.write("Buket") #yanına ekler
#fileToAppend.write("\n")#enter demek
#fileToAppend.write("Sseelloo")
#fileToAppend.close()

#silmek için

import os

if os.path.exists("ogrenciler.txt"):#dosya var mı kontrol
    os.remove("ogrenciler.txt")
else:
    print("Yok")

os.rmdir()#bu da klasör silme




