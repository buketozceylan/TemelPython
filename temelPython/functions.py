def selamVer():
    print("Merhaba " + isim)

isim=input("İsim=")    
selamVer()

def alan(a,b):
    return a*b/2
a=int(input("a değerini giriniz= "))
b=int(input("b değerini giriniz= "))

print(alan(a,b))


alan2 = lambda a,b : a*b/2
