from huiDatabase import Database
from huiDatabase import People
from huiDatabase import Person
from random import randint
from dominate.tags import *
import pymongo
# importing ObjectId from bson library
from bson.objectid import ObjectId
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import random
import json
import os
import requests
import eel
import gevent.monkey
gevent.monkey.patch_all()

eel.init("web")
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["institution"]
customerCol = mydb["customers"]

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
def saveCustomer(customerData):
    data = dict(x.split("=") for x in customerData.split("&"))
    # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # mydb = myclient["institution"]
    # mycol = mydb["customers"]
    x = customerCol.insert_one(data)
    inserted_id = str(x.inserted_id)
    html = (h1('Customer')).render()
    t = table()  # Insert a table
    t.set_attribute('class', 'table table-striped')
    with t:
        with thead(cls="thead-dark"):
            with th():
                td('Name')
                td('Age')
        with tbody():
            for x in customerCol.find():
                with tr():
                    first = 0
                    for i in x:
                        with td(style="word-wrap: break-word;", halign="center", valign="top"):
                            if(first > 0):
                                a(str(x[i]))
                            first += 1
                    btn = button("Select")
                    btn.set_attribute(
                        'class', 'btn btn-primary select-cutomer')
                    btn.set_attribute('cust-id', x['_id'])
                    td(btn)
    html += t.render()

    return {"current_id": inserted_id, "return_html": html}

    # people.add_person(p1.get_person())
    # print(people.get_people())

@eel.expose
def getCustomerById(custId):
    myquery = { "id": ObjectId("62d0216f23b4f8b620f6fca5") }
    # customer = customerCol.find_one()
    customer = customerCol.find_one(ObjectId(custId))
    print(customer)
    return customer

@eel.expose
def saveToExcel():
    # df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
    #                index=['row 1', 'row 2'],
    #                columns=['col 1', 'col 2'])
    df1=pd.DataFrame(customerCol.find())
    df1.to_excel("output.xlsx",sheet_name='customers')  
   
    randomlist = []
    for i in range(1,random.randint(1,10)):
        n = random.randint(1,10)
        randomlist.append(n)
    s = pd.Series(randomlist)
    fig, ax = plt.subplots()
    s.plot.bar()
    fig.savefig('web/my_plot.png')
    html = h1(random.randint(1,10)).render()
    html += img(src="my_plot.png").render()
    return {"return_html": html}


@eel.expose
def showStudents():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["institution"]
    mycol = mydb["customers"]
    print(mydb.list_collection_names())
    mydict = {"name": "John", "address": "Highway 37"}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)


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
