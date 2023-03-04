#list of prime number by function
def is_prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False     

start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))
for j in range(start,end+1):
    if is_prime(j):
        print(j,end=",")
