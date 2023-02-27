# Python3 code to select
# data from excel
import xlwings as xw
import pandas as pd
 
xw.App(visible=False)

# Specifying a sheet
ws = xw.Book("sample.xlsx").sheets['Sheet1']
 
# Selecting data from
# a single cell
v1 = ws.range("B1:f7").value
v2 = ws.range("F5").value
print("Result:", v1, v2)


num_col = ws.range('B1').end('right').column
num_row = ws.range('B1').end('down').row

# print(num_col, num_row)

content_list = ws.range((2,1),(num_row,num_col)).value
# print(content_list)