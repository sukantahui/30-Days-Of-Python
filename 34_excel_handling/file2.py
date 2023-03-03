# https://morioh.com/p/6cd71f4e3bd4?f=5d9fed1343803f11f5bcd541

import pandas as pd
import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Reference
import string

excel_file = pd.read_excel('supermarket_sales.xlsx')
excel_file[['Gender', 'Product line', 'Total']]

report_table = excel_file.pivot_table(index='Gender',columns='Product line',values='Total',aggfunc='sum').round(0)

report_table.to_excel('report_2021.xlsx',sheet_name='Report',startrow=4)