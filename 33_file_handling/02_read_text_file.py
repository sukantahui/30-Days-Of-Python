import os
os.system('cls')
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta.txt","r")
while True:
    line=f.readline()
    if not line:
        break
    print(line.strip())
f.close()