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


sql = "select agent_id,short_name from agent_master where show_in_commission = %s and agent_category_id= %s"
mycursor.execute(sql,(0,2,))
for x in mycursor:
    print(x)

