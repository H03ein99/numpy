# Using NumPy functions along rows and columns

import numpy as np


# ==================================================
# 2D Array
# ==================================================

A = np.array([
    [2, 9],
    [12, 6]
])

print(A)


# Shape of the array
# (2, 2) -> 2 rows and 2 columns
print("Shape: ", np.shape(A))


# Find the maximum value in the entire array
# Since no axis is specified, NumPy considers all elements.
print("max number: ", np.max(A))


# Find the maximum value along columns
#
# axis=0 means:
# Work DOWN the rows.
#
# Column 1: max(2, 12) = 12
# Column 2: max(9, 6)  = 9
#
# Result: [12, 9]
print("max number in columns: ", np.max(A, axis=0))


# Find the maximum value along rows
#
# axis=1 means:
# Work ACROSS the columns.
#
# Row 1: max(2, 9)  = 9
# Row 2: max(12, 6) = 12
#
# keepdims=True keeps the reduced dimension.
# Without keepdims -> shape (2,)
# With keepdims    -> shape (2, 1)
print(
    "max number rows: ",
    np.max(A, axis=1, keepdims=True),
    sep='\n'
)


# ==================================================
# Creating another 2D Array
# ==================================================

B = np.array([
    [0, 9],
    [11, -1]
])


# ==================================================
# Creating a 3D Array using stack()
# ==================================================

# Stack A and B together.
#
# A.shape -> (2, 2)
# B.shape -> (2, 2)
#
# C.shape -> (2, 2, 2)
#
# The first dimension tells us which matrix
# (A or B) we are looking at.
C = np.stack([A, B])

print(np.shape(C))


# ==================================================
# axis = 0
# ==================================================

# axis=0 means reduction along the first dimension.
#
# Here, we compare the corresponding elements
# between A and B.
#
# For example:
# max(2, 0)  -> 2
# max(9, 9)  -> 9
# max(12, 11) -> 12
# max(6, -1) -> 6
#
# keepdims=True preserves the axis.
print(
    "max with axis equal to zero:\n",
    np.max(C, axis=0, keepdims=True)
)

print(
    "shape of the result: ",
    np.shape(np.max(C, axis=0, keepdims=True))
)


# ==================================================
# axis = 1
# ==================================================

# axis=1 means reduction along the second dimension.
#
# For each matrix, calculate the maximum
# across its rows.
#
# keepdims=True keeps the reduced dimension.
print(
    "max with axis equal to one:\n",
    np.max(C, axis=1, keepdims=True)
)

print(
    "shape of the result: ",
    np.shape(np.max(C, axis=1, keepdims=True))
)


# ==================================================
# axis = 2
# ==================================================

# axis=2 means reduction along the third dimension.
#
# In our case, this means calculating the maximum
# across the columns of each row.
#
# keepdims=True keeps the reduced dimension.
print(
    "max with axis equal to two:\n",
    np.max(C, axis=2, keepdims=True)
)

print(
    "shape of the result: ",
    np.shape(np.max(C, axis=2, keepdims=True))
)