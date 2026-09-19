import numpy as np


# ==================================================
# Creating a 3D Array
# ==================================================

# Generate 20 random integers between -10 and 10
# and reshape them into a 3D array.
#
# Shape = (2, 2, 5)
#
# This means:
# 2 blocks
# 2 rows in each block
# 5 elements in each row
array_3D = np.random.randint(-10, 11, 20).reshape(2, 2, 5)

# Total number of elements
print("elements: ", array_3D.size)

# Data type of the elements
print("Data Type: ", array_3D.dtype)

# Number of dimensions
# A 3D array has ndim = 3
print("Dimension: ", array_3D.ndim)

# Total memory used by the array in bytes
print(f"This array uses {array_3D.nbytes} bytes of memory")

# Shape of the array
print("Shape: ", array_3D.shape)

# Display the entire 3D array
print(array_3D)

print(30 * "-")


# ==================================================
# Creating a Second 3D Array
# ==================================================

# Create another 3D array with exactly the same shape.
array_3D_2 = np.random.randint(-10, 11, 20).reshape(2, 2, 5)

# Total number of elements
print("elements: ", array_3D_2.size)

# Data type
print("Data Type: ", array_3D_2.dtype)

# Number of dimensions
print("Dimension: ", array_3D_2.ndim)

# Total memory usage
print(f"This array uses {array_3D_2.nbytes} bytes of memory")

# Shape
print("Shape: ", array_3D_2.shape)

# Display the second 3D array
print(array_3D_2)

print(30 * "-")


# ==================================================
# Creating a 4D Array using stack()
# ==================================================

# np.stack() combines multiple arrays by adding
# a NEW dimension.
#
# We have:
# array_3D.shape   -> (2, 2, 5)
# array_3D_2.shape -> (2, 2, 5)
#
# After stacking:
# array_4D.shape -> (2, 2, 2, 5)
#
# The first dimension (2) represents the two
# 3D arrays that we stacked together.
array_4D = np.stack([array_3D, array_3D_2])

# Total number of elements
print("elements: ", array_4D.size)

# Data type
print("Data Type: ", array_4D.dtype)

# Number of dimensions
# stack() added one dimension,
# so ndim changed from 3 to 4.
print("Dimension: ", array_4D.ndim)

# Total memory usage
print(f"This array uses {array_4D.nbytes} bytes of memory")

# Shape of the 4D array
print("Shape: ", array_4D.shape)

# Display the entire 4D array
print(array_4D)

print(30 * "-")