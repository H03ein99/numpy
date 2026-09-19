# Some useful functions from NumPy
import numpy as np

# Generate an array containing 4 random integers between 1 and 10
arr = np.random.randint(1, 11, 4)
print("Array:", arr)


# --------------------------------------------------
# Element-wise mathematical functions
# These functions are applied to every element
# of the array separately.
# --------------------------------------------------

# Absolute value
# Converts negative values to positive values
# Example: -5 -> 5
print("abs: ", np.abs(arr))


# Square root
# Calculates the square root of every element
print("sqrt: ", np.sqrt(arr))


# Natural logarithm (ln)
# Calculates the natural logarithm of every element
print("log: ", np.log(arr))


# Power
# Raises every element to the specified power
# Here, every element is squared
print("Square: ", np.power(arr, 2))


# --------------------------------------------------
# Aggregation functions
# These functions combine multiple elements
# and usually return a single value.
# --------------------------------------------------

# Maximum value in the array
print("Max: ", np.max(arr))

# Index of the maximum value
print("Max index: ", np.argmax(arr))


# Minimum value in the array
print("Min: ", np.min(arr))

# Index of the minimum value
print("Min index: ", np.argmin(arr))


# Sum of all elements
print("Sum: ", np.sum(arr))


# Arithmetic mean (average) of the elements
print("Mean: ", np.mean(arr))


# Median
# Returns the middle value after sorting the array
print("Median: ", np.median(arr))


# Standard deviation (std) and variance (var)
# std measures the amount of spread around the mean
# var is the square of the standard deviation
print(f"std is {np.std(arr)} and var is {np.var(arr)}")


# Cumulative sum
# Each element contains the sum of all previous elements
# Example: [1, 2, 3] -> [1, 3, 6]
print("CumSum: ", np.cumsum(arr))


# Product
# Multiplies all elements together
print("Product: ", np.prod(arr))


# --------------------------------------------------
# Quantile and Percentile
# --------------------------------------------------

# Quantile
# q=0.9 means the 90th percentile
# q must be between 0 and 1
print("Quantile: ", np.quantile(arr, q=0.9))


# Percentile
# Uses a percentage between 0 and 100
# q=90 means the 90th percentile
print("Percentile: ", np.percentile(arr, q=90))


# --------------------------------------------------
# Handling NaN values
# --------------------------------------------------

# Create an array containing NaN (Not a Number)
arr2 = np.array([
    [1, 2, np.nan],
    [3, 4, np.nan]
])

print(arr2)


# Regular NumPy functions do not ignore NaN values.
# If even one NaN exists, the result can become NaN.
print("Wrong way to sum: ", np.sum(arr2))


# NaN-aware functions ignore NaN values
# Therefore, only 1 + 2 + 3 + 4 is calculated.
print("Sum: ", np.nansum(arr2))