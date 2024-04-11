import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sukantahui",
  database="marigold"
) 

mycursor = mydb.cursor()
# data=mycursor.execute('select * from agent_master')
# # print(mycursor.fetchall())

# for x in mycursor:
#   print(x) 


sql = "select * from agent_master"
mycursor.execute(sql)
num_fields = len(mycursor.description)
print(num_fields)
field_names = [i[0] for i in mycursor.description]
print(field_names)