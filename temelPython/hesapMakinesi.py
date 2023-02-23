def topla(sayi1,sayi2):
    return sayi1+sayi2

def cikar(sayi1,sayi2):
    return sayi1-sayi2

def carp(sayi1,sayi2):
    return sayi1*sayi2

def bol(sayi1,sayi2):
    return sayi1/sayi2   

print("1 : Topla")
print("2 : Çıkar")
print("3 : Çarp")
print("4 : Böl")
cevap = input("Operasyon?")
sayi1 = int(input("Birinci sayıyı Giriniz= "))
sayi2 = int(input("İkinci sayıyı Giriniz= "))

if cevap=="1":
    toplam = topla(sayi1,sayi2)
    print(toplam)
elif cevap=="2":
    cikarma = cikar(sayi1,sayi2)
    print(cikarma)
elif cevap=="3":
    carpma = carp(sayi1,sayi2)
    print(carpma)
else:
    bolme = bol(sayi1,sayi2)
    print(bolme)
    

    
