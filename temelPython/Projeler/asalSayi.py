sayi=int(input("Sayı Giriniz"))
i=1

asal=0
for x in range(2,sayi):
    i=i+1
    if sayi%x==0:
        asal=asal+1
if asal==0:
    print("Sayınız Asaldır")
else:
    print("Sayınız Asal Değildir.")
 



