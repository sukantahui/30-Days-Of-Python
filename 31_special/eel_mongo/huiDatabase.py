import uuid
import pickle


class Database:
    data = {"students": []}

    def getData(self):
        file = open("database.dat", 'rb')
        self.data = pickle.load(file)
        file.close()
        return self.data

    def updateStudent(self, student):
        temp = uuid.uuid1()
        x={"id": temp.int}
        x.update(student)
        tempStudents = self.data["students"]
        tempStudents.append(x)
        self.data["students"] = tempStudents
        file = open("database.dat", 'wb')
        pickle.dump(self.data, file)
        file.close()


class Person:
    def __init__(self, name, age):
        temp = uuid.uuid1()
        self.id = temp.int
        self.name = name
        self.age = age

    def display(self):
        print("ID", self.id)
        print("Name", self.name)
        print("Age", self.age)

    def get_person(self):
        return {"name": self.name, "age": self.age}


class People:
    person_list = list()

    def add_person(self, person):

        self.person_list.append(person)

    def get_people(self):
        return self.person_list
