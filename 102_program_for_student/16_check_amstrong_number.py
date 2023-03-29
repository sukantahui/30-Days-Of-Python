#check amstrong number
import os
os.system('cls')
def is_amstrong(num):
    temp=num
    count=0
    sum=0
    num1=num
    while num>0:
        num=num//10
        count+=1
    while num1>0:
        r=num1%10
        sum=sum+(pow(r,count))
        num1=num1//10
    if temp==sum: 
       return True 
    else:
        return False
    
num=int(input("Enter a number: "))
if is_amstrong(num):
    print("The given number is amstrong number.")
    