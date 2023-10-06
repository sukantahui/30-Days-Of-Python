import os
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta.txt","r")
doc=f.read()
print(doc)
f.close()