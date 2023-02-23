ogrenciler = ["Bukish","Sseelloo","Hazimazi","satranc31"]

fileToAppend = open("ogrenciler.txt","a")
for i in ogrenciler:
    fileToAppend.write(i)
    fileToAppend.write("\n")

fileToAppend.close()
