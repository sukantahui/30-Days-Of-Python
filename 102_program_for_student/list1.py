import random

#print(random.random())

def randNumBetween( s, e) :
    return int(random.random()*(e-s+1))+10



lst1=[]
lst2=[]
lst3=[]
len=20
while len!=0 :
    lst1.append(randNumBetween(10,30))
    lst2.append(randNumBetween(10,30))
    len-=1

print("List1 : ",lst1)
print("List2 : ",lst2)

for i in lst1 :
    if i not in lst2:
        lst3.append(i)

for i in lst2 :
    if i not in lst1:
        lst3.append(i)   

print("Elents not common : ",lst3)             

#print(randNumBetween(10,500))
