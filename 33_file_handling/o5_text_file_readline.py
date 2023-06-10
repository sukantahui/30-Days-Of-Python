import os
os.system('cls')
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta.txt","r")
while True:
    k=f.readline()
    if not k:
        f.close()
        break
    list=k.split()
    # print(list)  
    max=""
    for i in list:
       if len(i)>len(max):
           max=i
    print(max)
f.close()