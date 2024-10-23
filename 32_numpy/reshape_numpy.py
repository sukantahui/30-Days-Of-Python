#Write a Python program to reshape a 2-dimensional NumPy array.
import numpy as np

# Create a 2D NumPy array (2 rows, 3 columns)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Print the original array
print("Original Array (2x3):")
print(array_2d)

# Reshape the array to a new shape (3 rows, 2 columns)
reshaped_array = array_2d.reshape(3, 2)

# Print the reshaped array
print("\nReshaped Array (3x2):")
print(reshaped_array)

