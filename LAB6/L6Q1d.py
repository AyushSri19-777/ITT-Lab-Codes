a=[[1,2,3],[1,1,1]]
b=[[1,1,1],[1,2,3]]
c=[[0,0,0],[0,0,0]]
m=len(a)
n=len(a[0])
for i in range(m):
    for j in range(n):
        c[i][j]=a[i][j]+b[i][j]
for r in c:
	print(r)