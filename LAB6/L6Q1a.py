def calculate(num1,op,num2):
    if(op=='+'):
        return num1+num2
    elif(op=='-'):
        return num1-num2
    elif(op=='*'):
        return num1*num2
    elif(op=='/'):
        return num1//num2
print(calculate(5,"/",4))