import numpy as np
import pandas as pd
import os
os.system('cls')
A = np.array([[1, 4, 5, 12, 14], 
    [-5, 8, 9, 0, 17],
    [-6, 7, 11, 19, 21]])

print(A[:2, :4])  # two rows, four columns
B=A[:,2]
print(B)  # all rows, second column

print(pd.Series(B))  