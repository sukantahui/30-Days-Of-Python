
def is_dict(x):
    list=[]
    for key,values in x.items():
        if values>=250:
            list.append(key)
    return tuple(list)

        
my_dict={'ritaja':200,'Kinjal':225,'Mounita':202,'Tanu':300,'Suku':400,'Riddhi':250,'Mou':249,'Abhi':144,'Riya':298}
print('moni' in my_dict)
del my_dict['Mounita']
print(my_dict)
# y=is_dict(my_dict)
# print(y)
# for i in y:
#     print(i,my_dict[i])


# print(my_dict.keys())
# print(type(list(my_dict.keys())))
# print(type(my_dict.values()))
# print(my_dict.items())
# for key,values in my_dict.items():
#     print(key,values)

