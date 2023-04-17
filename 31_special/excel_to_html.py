import pandas as pd
df =pd.read_excel('fake_data_list.xlsx')
html=df.to_html('test.html')