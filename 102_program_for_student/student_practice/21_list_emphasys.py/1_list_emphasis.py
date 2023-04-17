import os
import random
os.system('cls')

# x=random.random()
def randbetween(s,e):
    return(int(random.random()*(e-s+1))+10)



start=int(input("Enter the starting number"))
end=int(input("Enter ending number"))
list1=[]
count=0
while True:
    x=randbetween(start,end)
    print(x)
    if x not in list1:
        list1.append(x)
    count+=1
    if count==10:
        break
print(list1)