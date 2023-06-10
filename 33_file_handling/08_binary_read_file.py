import os
os.system('cls')
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta_binary.txt","rb")
str=f.read()
print(str.decode())
f.close()
