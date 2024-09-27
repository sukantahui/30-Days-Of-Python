import numpy as np

# Create a 2x2 NumPy array (matrix)
matrix = np.array([[4, 7], [2, 6]])

# Print the original matrix
print("Matrix:")
print(matrix)

# Calculate the determinant using np.linalg.det()
determinant = np.linalg.det(matrix)

# Print the determinant
print("\nDeterminant of the matrix:")
print(determinant)
