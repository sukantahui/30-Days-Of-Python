#check amstrong number
import os
os.system('cls')
def is_amstrong(num):
    n=num
    count=0
    reverse=0
    num1=num
    while num>0:
        num=num//10
        count+=1
    while num1>0:
        r=num1%10
        reverse=reverse+(pow(r,count))
        num1=num1//10
    if n==reverse: 
       return True 
    else:
        return False
    
num=int(input("Enter a number: "))
if is_amstrong(num):
    print("amstrong")
    