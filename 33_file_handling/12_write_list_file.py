import pickle
import os
os.system('cls')
list=[1,3,4,5,"a quick brown fox",(23,4,56,6)]
# print(list)
path=os.path.dirname(__file__)
f=open(path+"/test_list.txt","wb")
pickle.dump(list,f)
f.close()
f=open(path+"/test_list.txt","rb")
x=pickle.load(f)

print(x)
f.close()