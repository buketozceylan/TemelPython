sayilar = [1,2,3,4,5]

sayilarKare = list(map(lambda x: x**2,sayilar))

# for sayi in list:
#     listKare.append(sayi*sayi)

sayilarFiltreli = list(filter(lambda sayi : sayi>2,sayilar))
    
from functools import reduce

sayilarFaktoriyel = reduce(lambda x,y:x*y,sayilar)



print(sayilarFaktoriyel)
print(sayilarKare)
print(sayilarFiltreli)

