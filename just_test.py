op1=int(input("enter a number!"))
op2=int(input("enter a number!"))

operator=input("Enter your operation out of +, -, *, /")

def calci():
    if(operator=='+'):
        res=op1+op2
        return res
    elif(operator=='-'):
        res=op1-op2
        return res
    elif(operator=='*'):
        res=op1*op2
        return res
    elif(operator=='/'):
        res=op1/op2
        return res
    else:
        print("enter correct operator")

print(f"the result is {calci()}")

