import os
os.system('cls')
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
web_techs = ['HTML', 'CSS', 'JS', 'React']

# countries.append(web_techs)
# print(countries)
# print (countries[-1][-1])
# print(web_techs[0])
# for i in web_techs:
#     # print(i,end=',')
#     countries.append(i)
countries.extend(web_techs)
countries.sort(reverse=True)
print(countries)