import os
os.system('cls')
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta.txt","r")
max=len(f.readline())

for i in f:
    if len(f.readline())>max:
        max=len(f.readline())
        maxline=f.readline()
print(max)
print(maxline)
f.close()