from random import shuffle
import os
import tomli
import msvcrt

def getch():
        return msvcrt.getch().decode()
# print("Enter your choice")
# x=getch()

mylist = ['','A', 'B' ,'C', 'D']
e_list = enumerate(mylist,start=65)
print(list(e_list))

for count,value in  enumerate(mylist,start=65):
        print(count)

print(mylist.index('C'))

# questions = [
#     {
#         'question': 'Who developed Python Programming Language?',
#         'options': ['Wick van Rossum','Rasmus Lerdorf','Guido van Rossum','Niene Stom'],
#         'answer': [3],
#         'subject': 'Python',
#         'topic': 'General'
#     }
# ]

# k=questions[0]['options']
# shuffle(k)
# file_path=os.path.dirname(__file__)
# print(file_path)


# with open(file_path+"/"+"mcq.toml", mode="rb") as toml_file:
#     mcqs = tomli.load(toml_file)
# print(mcqs)

# for count, value in enumerate(k,start=1):
#     print(count, end=". ")
#     print(value)
