from tkinter import filedialog
import tkinter as tk
import openpyxl
import os

root = tk.Tk()
root.withdraw()

folder = filedialog.askdirectory()

for f in os.listdir(folder):
    print(f)
    path = os.path.join(folder,f)
    print(path)
    # wb = openpyxl.load_workbook(path)
    # ws = wb.active
    # v = ws['A1']
    # print(v.value)