studentsSet={"Buket","Zülfiye","Agah"}
print(studentsSet)

for student in studentsSet:
    print(student)
    
print("buket" in studentsSet)
if "Buket" in studentsSet:
    print("Listede var")
studentsSet.add("Ali")
studentsSet.update(["Görkem","İrfan"])
print(studentsSet)
#2kere çıkarmaya çalışırsan hata veriyo
studentsSet.remove("Agah")
#bunda vermiyo
studentsSet.discard("Agah")

#random elemanı silmeye yarıyor
x=studentsSet.pop()
print(studentsSet)

#bütün seti silmeye yarıyo
x=studentsSet.clear()

#komple seti silme
del 