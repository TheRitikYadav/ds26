import numpy as np

# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# Array shape
print("Shape of 2D Array:", array_2d.shape)

# Array data type
print("Data type of 1D Array:", array_1d.dtype)

# Creating an array of zeros
zeros_array = np.zeros((2, 3))
print("Array of Zeros:\n", zeros_array)

# Creating an array of ones
ones_array = np.ones((2, 3))
print("Array of Ones:\n", ones_array)

# Creating an array with a range of values
range_array = np.arange(0, 10, 2)
print("Array with Range:", range_array)

# Reshaping an array
reshaped_array = np.arange(6).reshape((2, 3))
print("Reshaped Array:\n", reshaped_array)

# Basic array operations
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
print("Array Addition:", array_a + array_b)
print("Array Multiplication:", array_a * array_b)

# Statistical operations
print("Mean of Array A:", np.mean(array_a))
print("Sum of Array B:", np.sum(array_b))