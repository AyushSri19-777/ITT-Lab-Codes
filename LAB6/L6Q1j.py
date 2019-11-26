def shift(str,n):
    f=ord(str)
    if(f>=90):
        str=chr(65+(n-1))
    else:
    	str=chr(f+n)
    return str
str="ZOO"
w=""
for i in str:
    w=w+shift(i,3)
print(w)