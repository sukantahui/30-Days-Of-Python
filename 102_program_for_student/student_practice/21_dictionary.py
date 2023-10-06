import os
os.system('cls')
dic={"Name":"abc","Class":"V","Roll":23}
print(dic)
print(len(dic))
path=os.path.dirname(__file__)
f=open(path+"/dict_write.txt","wb")
f.write(dic.encode())
f.close()