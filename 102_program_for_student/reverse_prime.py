def is_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False        
    
def reverse(num):
    ans=0
    while num>0:
        r=num%10
        num=num//10
        ans=ans*10+r
    return int(ans)    

x=int(input("Enter start: "))
y=int(input("Enter end: "))

for i in range(x, y+1):
    if is_prime(i) and is_prime(reverse(i)):
        print(i, end=", ")

