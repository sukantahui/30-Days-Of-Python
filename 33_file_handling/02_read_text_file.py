import os
os.system('cls')
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta.txt","r")
# f.seek(6)
doc=f.read(6)[-1]
print(doc)
f.close()