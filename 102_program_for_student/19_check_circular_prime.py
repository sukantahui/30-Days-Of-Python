#check circular prime.py
import math
def is_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
    
    
def no_digit(num):
    count=0
    while num>0:
        num=num//10
        count+=1;
    return count


def get_combination(num):
    values=[num]
    length=no_digit(num)
    x=length-1
    while x>0:
        r=num%10
        num//=10
        num=r*(10**(length-1))+num
        x-=1
        values.append(num)
    return values



def is_circular_prime(num):
    for i in get_combination(num):
        if is_prime(i)==False:
           return False
    return True


circular_primes=[]
for i in range(11,9999):
    if is_circular_prime(i):
        circular_primes.append(i)
print(circular_primes)