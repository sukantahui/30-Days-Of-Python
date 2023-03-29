#check automorphic number
def is_automorphic(num):
    temp=num**2
    count=0
    while num>0:
        count+=1
        num//=10
        temp1=temp%(10**count)
    return temp1
        
        
num=int(input("Enter a number: "))
n=num
if n==is_automorphic(num):
    print("The given number is automorphic number.")
