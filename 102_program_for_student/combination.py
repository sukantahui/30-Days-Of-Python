def factorial(num):
    ans=1
    while num>0:
        ans*=num
        num-=1
    return ans 

n=int(input("Enter value of N: "))
r=int(input("Enter value of R: "))
ans=factorial(n)/(factorial(n-r)*factorial(r))
print("Answer is ",ans) 
