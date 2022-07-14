import eel
import requests
import os
import json
import pickle
import uuid
import pymongo
from random import randint
from huiDatabase import Person
from huiDatabase import People
from huiDatabase import Database

eel.init("web")

people = People()
database = Database()


def write():
    file = open("binary.dat", 'wb')
    x = {"students": [{"name": "Abcd", "age": 23},
                      {"name": "Zxcv", "age": 18}]}
    pickle.dump(x, file)
    file.close()


def read():
    file = open("binary.dat", 'rb')
    x = pickle.load(file)
    file.close()
    print(x['students'][0])


@eel.expose
def savePerson(name, age):
    p1 = Person(name, age)
    database.updateStudent(p1.get_person())

    # people.add_person(p1.get_person())
    # print(people.get_people())


@eel.expose
def showStudents():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    print(myclient.list_database_names())
    print("Showing database")
    print(database.getData())


@eel.expose
def sum(num1, num2):
    write()
    return int(num1)+int(num2)


@eel.expose
def sub(num1, num2):
    read()
    return int(num1)-int(num2)


@eel.expose
def mul(num1, num2):
    return int(num1)*int(num2)


@eel.expose
def div(num1, num2):
    return float(num1)/float(num2)


@eel.expose
def mod(num1, num2):
    return int(num1) % int(num2)


# Start the index.html file
eel.start("index.html")
