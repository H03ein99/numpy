# 1D and 2D Arrays
import numpy as np 

a1_1D = np.array([1,2,3,4,5]).reshape(1,-1)
print("Some samples for 1D and 2D Array using numpy\n===========================\na3_1D:\n\n", a1_1D)
print(type(a1_1D))
print("\nelements: ", a1_1D.size)
print("\nData Type: ", a1_1D.dtype)
print("\nDimension: ", a1_1D.ndim)
print(f"\nThis array uses {a1_1D.nbytes} bytes of memory")
print("\nShape: ", a1_1D.shape)

print(15*"-")

a2_1D = np.arange(-1,10, 2).reshape(-1,1)
print("\na3_1D:\n\n", a2_1D)
print("\nelements: ", a2_1D.size)
print("\nData Type: ", a2_1D.dtype)
print("\nDimension: ", a2_1D.ndim)
print(f"\nThis array uses {a2_1D.nbytes} bytes of memory")
print("\nShape: ", a2_1D.shape)

print(15*"-")


a3_1D = np.random.randint(0, 100, 7).reshape(1, -1)
print("\na3_1D:\n\n", a3_1D)
print("\nelements: ", a3_1D.size)
print("\nData Type: ", a3_1D.dtype)
print("\nDimension: ", a3_1D.ndim)
print(f"\nThis array uses {a3_1D.nbytes} bytes of memory")
print("\nShape: ", a3_1D.shape)
print(15*"-")

# Now lets make a fully randomed vector
number = np.random.randint(0, 21)
a4_1D=np.random.randint(-100, 100, number)
print("\na3_1D:\n\n", a4_1D)
print("\nelements: ", a4_1D.size)
print("\nData Type: ", a4_1D.dtype)
print("\nDimension: ", a4_1D.ndim)
print(f"\nThis array uses {a4_1D.nbytes} bytes of memory")
print("\nShape: ", a4_1D.shape)
print(15*"-")



a1_2D = np.random.randint(-100, 100, 16).reshape(4,-1)
print("\na3_1D:\n\n", a1_2D)
print("\nelements: ", a1_2D.size)
print("\nData Type: ", a1_2D.dtype)
print("\nDimension: ", a1_2D.ndim)
print(f"\nThis array uses {a1_2D.nbytes} bytes of memory")
print("\nShape: ", a1_2D.shape)