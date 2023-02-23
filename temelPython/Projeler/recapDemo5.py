import sys

Liste = [7,'bukish',0,3,'6']


for x in Liste:
    try:
        print("sayı:"+str(x))
        sonuc = 1/int(x)
        print("Sonuc:"+str(sonuc))
    except:
        print(str(x)+" hesaplanamadı :(")
        print(sys.exc_info())











