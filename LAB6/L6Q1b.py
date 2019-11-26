a=[ [1,2,3]
   ,[1,1,4]
   ,[2,2,2]]
m=len(a)
b=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(m):
    for j in range(m):
        b[j][i]=a[i][j]
for r in b:
    print(r)