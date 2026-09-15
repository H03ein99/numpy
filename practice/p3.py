import numpy as np

# Generate a random 3D Array using numpy
array_3D = np.random.randint(-10, 11, 20).reshape(2,2,5)
print("elements: ", array_3D.size)
print("Data Type: ", array_3D.dtype)
print("Dimension: ", array_3D.ndim)
print(f"This array uses {array_3D.nbytes} bytes of memory")
print("Shape: ", array_3D.shape)
print(array_3D)
print(30*"-")

#Generate a Second random 3D Array
array_3D_2 = np.random.randint(-10, 11, 20).reshape(2,2,5)
print("elements: ", array_3D_2.size)
print("Data Type: ", array_3D_2.dtype)
print("Dimension: ", array_3D_2.ndim)
print(f"This array uses {array_3D_2.nbytes} bytes of memory")
print("Shape: ", array_3D_2.shape)
print(array_3D_2)
print(30*"-")
#Now lets use stack() method to create a 4D Array
array_4D = np.stack([array_3D, array_3D_2])
print("elements: ", array_4D.size)
print("Data Type: ", array_4D.dtype)
print("Dimension: ", array_4D.ndim)
print(f"This array uses {array_4D.nbytes} bytes of memory")
print("Shape: ", array_4D.shape)
print(array_4D)
print(30*"-")