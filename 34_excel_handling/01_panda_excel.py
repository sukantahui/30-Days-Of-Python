# https://www.dataquest.io/blog/reading-excel-file-python/
import pandas as pd
import os
print('Get current working directory : ',os.path.dirname(__file__))
df = pd.read_excel(os.path.dirname(__file__)+'\sample.xlsx',skiprows=range(3))

print(df)