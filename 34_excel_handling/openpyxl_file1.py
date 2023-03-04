# https://realpython.com/openpyxl-excel-spreadsheets-python/#getting-started-with-openpyxl
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"
print("test")

workbook.save(filename="hello_world.xlsx")