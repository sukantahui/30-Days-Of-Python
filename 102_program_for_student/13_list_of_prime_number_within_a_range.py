#list of prime number within a range
start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))
for j in range(start,end+1):
    count=0
    for i in range(1,j+1):
        if j%i==0:
            count+=1
    if(count==2):       
        print(i,end=",")
