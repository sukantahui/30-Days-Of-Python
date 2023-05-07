list1=[2,45,24,1,6,3]
# x=list1[1]
# list1.remove(list1[2])
# print(list1)
# # list1.pop()
# print(list1.remove(3))
# print(list1.pop(4))
# print(list1)
# del list1[2]
# # print(list1)
# del list1
# # print(list1)
# list1.clear()
# print(list1)
# list2=list1
# print(list2)
# print(id(list1))
# print(id(list2))
# print(id(list1)==id(list2))
# list3=list1.copy()
# print(list3)
# print(id(list3)==id(list1))
# list1.pop()
# print(list1)
# print(list2)
# print(list3)

list2=[23,65,7,8,9,24]
# list3=list1+list2
# print(list3)
list3=[]
list3.extend(list1)
list3.extend(list2)
print(list3)
print(list3.count(24))
