# 1D and 2D Arrays
import numpy as np


# ==================================================
# 1D and 2D Arrays in NumPy
# ==================================================

# Create a 1D array and reshape it into a row vector.
# Original shape: (5,)
# New shape: (1, 5)
#
# Important:
# Technically, after reshape this is a 2D array,
# not a true 1D array.
a1_1D = np.array([1, 2, 3, 4, 5]).reshape(1, -1)

print("Some samples for 1D and 2D Array using numpy\n===========================\na1_1D:\n\n", a1_1D)

# Check the type of the object
print(type(a1_1D))

# Number of elements in the array
print("\nelements: ", a1_1D.size)

# Data type of the elements
print("\nData Type: ", a1_1D.dtype)

# Number of dimensions
# Here ndim = 2 because the array has rows and columns
print("\nDimension: ", a1_1D.ndim)

# Total memory used by the array in bytes
print(f"\nThis array uses {a1_1D.nbytes} bytes of memory")

# Shape of the array
# (1, 5) means 1 row and 5 columns
print("\nShape: ", a1_1D.shape)


print(15 * "-")


# --------------------------------------------------
# Creating an array using np.arange()
# --------------------------------------------------

# np.arange(start, stop, step)
#
# Generates:
# -1, 1, 3, 5, 7, 9
#
# Then reshape(-1, 1) converts it into a column vector.
# -1 tells NumPy to automatically calculate the number of rows.
a2_1D = np.arange(-1, 10, 2).reshape(-1, 1)

print("\na2_1D:\n\n", a2_1D)

# Number of elements
print("\nelements: ", a2_1D.size)

# Data type
print("\nData Type: ", a2_1D.dtype)

# Number of dimensions
print("\nDimension: ", a2_1D.ndim)

# Memory usage in bytes
print(f"\nThis array uses {a2_1D.nbytes} bytes of memory")

# Shape
# (6, 1) means 6 rows and 1 column
print("\nShape: ", a2_1D.shape)


print(15 * "-")


# --------------------------------------------------
# Creating a random array
# --------------------------------------------------

# Generate 7 random integers between 0 and 99.
#
# reshape(1, -1) converts the array into a row vector.
# Since there are 7 elements, the final shape is (1, 7).
a3_1D = np.random.randint(0, 100, 7).reshape(1, -1)

print("\na3_1D:\n\n", a3_1D)

# Number of elements
print("\nelements: ", a3_1D.size)

# Data type
print("\nData Type: ", a3_1D.dtype)

# Number of dimensions
print("\nDimension: ", a3_1D.ndim)

# Memory usage
print(f"\nThis array uses {a3_1D.nbytes} bytes of memory")

# Shape
print("\nShape: ", a3_1D.shape)


print(15 * "-")


# --------------------------------------------------
# Creating a completely random-length vector
# --------------------------------------------------

# First, randomly choose how many elements
# the array should contain.
#
# randint(0, 21) can generate a number from 0 to 20.
number = np.random.randint(0, 21)

# Create an array containing 'number' random integers
# between -100 and 99.
a4_1D = np.random.randint(-100, 100, number)

print("\na4_1D:\n\n", a4_1D)

# Number of elements
print("\nelements: ", a4_1D.size)

# Data type
print("\nData Type: ", a4_1D.dtype)

# Number of dimensions
# Unlike the previous examples, this is actually a 1D array
# because we did not reshape it.
print("\nDimension: ", a4_1D.ndim)

# Memory usage
print(f"\nThis array uses {a4_1D.nbytes} bytes of memory")

# Shape
# The shape is (number_of_elements,)
print("\nShape: ", a4_1D.shape)


print(15 * "-")


# ==================================================
# 2D Array
# ==================================================

# Generate 16 random integers between -100 and 99.
#
# reshape(4, -1):
# - 4 -> number of rows
# - -1 -> NumPy automatically calculates the columns
#
# Since there are 16 elements:
# 16 / 4 = 4
#
# Therefore, the final shape is (4, 4).
a1_2D = np.random.randint(-100, 100, 16).reshape(4, -1)

print("\na1_2D:\n\n", a1_2D)

# Total number of elements
print("\nelements: ", a1_2D.size)

# Data type
print("\nData Type: ", a1_2D.dtype)

# Number of dimensions
# A matrix has 2 dimensions: rows and columns
print("\nDimension: ", a1_2D.ndim)

# Total memory used
print(f"\nThis array uses {a1_2D.nbytes} bytes of memory")

# Shape
# (4, 4) -> 4 rows and 4 columns
print("\nShape: ", a1_2D.shape)