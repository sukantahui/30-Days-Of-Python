import uuid

class Person:
  def __init__(self, name, age):
    temp = uuid.uuid1()
    self.id =temp.int
    self.name = name
    self.age = age

  def display(self):
    print("ID" , self.id)
    print("Name" , self.name)
    print("Age" , self.age)
  def get_person(self):
    return {"id": self.id, "name": self.name, "age": self.age}  
    


class People:
    person_list=list()

    def add_person(self, person):

        self.person_list.append(person)

    def get_people(self):
        return self.person_list     

