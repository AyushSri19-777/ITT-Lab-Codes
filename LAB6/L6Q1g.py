a=['A','B','C','D','E','F']
def d2B(n):  
  
    if(n > 1):  
        d2B(n//2)        
    print(n%2,end=' ') 
def d2O(n):  
  
    if(n > 1):  
        d2O(n//8)        
    print(n%8,end=' ') 
def d2H(n):   
    if(n > 1):  
        d2H(n//16)        
    if(n<10):
        print(n,end=' ')
    else:
        print(a[n%16-10],end='')
print(d2B(7))
print(d2O(55))
print(d2H(20))
    
