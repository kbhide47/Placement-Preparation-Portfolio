# ==========================
# DAY 1 - NUMPY BASICS PRACTICE
# ==========================

import numpy as np

print("========== Question 1: Create Arrays ==========")

# 1D Array
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1)

# 2D Array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n2D Array:\n", arr2)

# 3D Array
arr3 = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
print("\n3D Array:\n", arr3)

# ----------------------------------------------------

print("\n========== Question 2: Shape ==========")
print("Shape of arr1:", arr1.shape)
print("Shape of arr2:", arr2.shape)
print("Shape of arr3:", arr3.shape)

# ----------------------------------------------------

print("\n========== Question 3: Number of Dimensions ==========")
print("arr1 ndim:", arr1.ndim)
print("arr2 ndim:", arr2.ndim)
print("arr3 ndim:", arr3.ndim)

# ----------------------------------------------------

print("\n========== Question 4: Size ==========")
print("arr1 size:", arr1.size)
print("arr2 size:", arr2.size)
print("arr3 size:", arr3.size)

# ----------------------------------------------------

print("\n========== Question 5: Data Type ==========")
print("arr1 dtype:", arr1.dtype)

float_arr = np.array([1.2, 2.3, 3.4])
print("float_arr dtype:", float_arr.dtype)

# ----------------------------------------------------

print("\n========== Question 6: Create Arrays Using NumPy Functions ==========")

zeros = np.zeros((2,3))
print("Zeros:\n", zeros)

ones = np.ones((3,2))
print("\nOnes:\n", ones)

identity = np.eye(4)
print("\nIdentity Matrix:\n", identity)

range_array = np.arange(1,11)
print("\nArange:", range_array)

linspace_array = np.linspace(0,100,5)
print("\nLinspace:", linspace_array)

# ----------------------------------------------------

print("\n========== Question 7: Reshape ==========")

arr = np.arange(1,13)

print("Original:")
print(arr)

reshaped = arr.reshape(3,4)

print("\nReshaped (3x4):")
print(reshaped)

# ----------------------------------------------------

print("\n========== Question 8: Flatten ==========")

flattened = reshaped.flatten()

print(flattened)

# ----------------------------------------------------

print("\n========== Question 9: Indexing ==========")

print("First element:", arr1[0])
print("Last element:", arr1[-1])

print("\nFirst row:", arr2[0])
print("Second row:", arr2[1])

print("Element (2nd row,3rd column):", arr2[1][2])

# ----------------------------------------------------

print("\n========== Question 10: Slicing ==========")

print(arr1[1:4])
print(arr1[:3])
print(arr1[2:])
print(arr1[::-1])

# ----------------------------------------------------

print("\n========== Question 11: Copy vs View ==========")

original = np.array([1,2,3,4])

copy_array = original.copy()
view_array = original.view()

original[0] = 100

print("Original:", original)
print("Copy:", copy_array)
print("View:", view_array)

# ----------------------------------------------------

print("\n========== Question 12: Array Conversion ==========")

list1 = [5,10,15,20]

numpy_array = np.array(list1)

print(numpy_array)

# ----------------------------------------------------

print("\n========== Question 13: Basic Mathematical Operations ==========")

a = np.array([1,2,3])

b = np.array([4,5,6])

print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)

# ----------------------------------------------------

print("\n========== Question 14: Array Attributes ==========")

print("Shape:", a.shape)
print("Size:", a.size)
print("Datatype:", a.dtype)
print("Dimensions:", a.ndim)

# ----------------------------------------------------

print("\n========== Question 15: Practice Exercise ==========")

marks = np.array([78,85,91,66,88])

print("Marks:", marks)

print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Total Marks:", np.sum(marks))

print("\n========== Day 1 Completed Successfully ==========")
