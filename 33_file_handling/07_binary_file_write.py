import os
os.system('cls')
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta_binary.txt","wb")
str="Suparna is a good girl.\n"
f.write(str.encode())
f.write(b"The key function for working with files in Python is the open() function.\n")
f.close()

