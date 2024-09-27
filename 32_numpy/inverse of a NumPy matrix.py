import numpy as np

# Define a matrix
matrix = np.array([[4, 7], 
                   [2, 6]])

# Calculate the inverse of the matrix
try:
    inverse = np.linalg.inv(matrix)
    print("The inverse of the matrix is:")
    print(inverse)
except np.linalg.LinAlgError:
    print("The matrix is singular and does not have an inverse.")
