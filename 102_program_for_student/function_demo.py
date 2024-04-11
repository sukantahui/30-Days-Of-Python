import random

def rand_between(start,end):
    return (int)(random.random()*(end-start+1)+start)

list1=[]
list2=[]
for i in range(50):
    list1.append(rand_between(20,40))

for i in range(50):
    list2.append(rand_between(30,60))    
print(list1)    
print(list2)   

list3= list1[-4:]+list2[:4]
print(list3)