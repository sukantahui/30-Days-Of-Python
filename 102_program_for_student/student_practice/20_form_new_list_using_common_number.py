#Form new list using common number from another two list
import os
import random
os.system('cls')


list1=[]
for i in range(random.randrange(21,31)):
    x=random.randrange(10,100)
    if x not in list1:
        list1.append(x)
        
print(len(list1))
print(list1)

list2=[]
while True:
    x=random.randrange(2,101)
    if x not in list2:
        list2.append(x)
    if(len(list2))==30:
        break
        
print(len(list2))
print(list)

print()
list3=[]
list3=[i for i in list2 if i not in list1 ]
for i in list1:
    if i not in list3:
        list3.append(i)

print(len(list3))
list3.sort()
print(list3)
print(list3[-1])
max=list3[0]
for i in list3:
    if max<i:
        max=i
print(max)
