import os
os.system('cls')
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta.txt","r")
for x in f:
    list=x.split()
    max=""
    for i in list:
        if len(i)>len(max):
            max=i
    print(max)
f.close()