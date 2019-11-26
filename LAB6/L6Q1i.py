f=0
a=[1,2,3,4,5,4,3,2,1]
j=len(a)//2
l=len(a)-1
for i in range(j):
    if(a[i]!=a[l-i]):
        f=1
        break
if(f==1):
    print("Not Palindrome")
else:
    print("palindrome")
