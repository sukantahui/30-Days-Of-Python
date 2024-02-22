import mysql.connector
import pandas as pd


try:
  conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sukantahui",
    database="marigold"
  ) 
except:
  print("Unable to connect")

query = "SELECT * FROM agent_master"
df = pd.read_sql(query, conn)
conn.close()

df.to_csv('Test.csv')

