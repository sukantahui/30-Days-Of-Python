# HCF calculation
num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
while num1>0:
    r=num2%num1
    num2=num1
    num1=r
print("The HCF of the given numbers ",num2)