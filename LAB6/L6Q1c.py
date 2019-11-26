a=[[1,2],
   [1,1]]
b=[[3,2],
   [4,3]]
c=[[0,0],[0,0]]
m=n=2
for i in range(m):
    for j in range(m):
        for k in range(m):
            c[i][j] += a[i][k] * b[k][j]

for r in c:
   print(r)