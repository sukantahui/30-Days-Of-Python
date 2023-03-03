#check a number prime or not
num=int(input("Enter a number: "))
count=0
for i in range(1,num+1):
    if(num%i==0):
       count+=1
if(count==2):       
    print("The given number is prime.")
else:
    print("The given number is not prime.")