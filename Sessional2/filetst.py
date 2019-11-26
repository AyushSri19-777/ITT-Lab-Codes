f=open("names.txt","r")
g=open("lname.txt","w")
#h=open("count.txt","w")
k=0
c=0
b=[]
for line in f:
    s=str(line)
    a=s.split()
    b.append(a[1])
b.sort()
k=sorted(b,reverse=True)
for i in b:
    g.write(i+"\n")
    if i[0]== 'P':
        c=c+1;
c=str(c)
g.write("The count is : "+c+"\n")
for i in k:
    g.write(i+"\n")

f.close()
g.close()
    
    
