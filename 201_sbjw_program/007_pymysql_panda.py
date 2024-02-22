from sqlalchemy import create_engine
import pandas as pd

# replace <user>, <password>, <host>, and <port> with your MySQL credentials
engine = create_engine('mysql+pymysql://root:sukantahui@localhost:3306/marigold')
sql_df = pd.read_sql("SELECT * FROM agent_master", con=engine) 
  
print(sql_df) 


