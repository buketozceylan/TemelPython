a = [[1,3,5],[2,4,1],[1,5,7]]
b = [[3,3,4],[2,4,1],[3,5,4]]

sonuc = [[0,0,0],[0,0,0],[0,0,0]]      

sonuc[0][0] = a[0][0]+b[0][0]
for i in range(len(a)):
    for j in range(len(b)):
        sonuc[i][j] = a[i][j]+b[i][j]
print(sonuc)