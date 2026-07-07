# ==========================================
# DAY 2 - NUMPY ADVANCED PRACTICE
# Topics:
# Broadcasting
# Boolean Indexing
# Fancy Indexing
# Aggregation
# Axis
# Random Module
# Sorting
# Searching
# Unique
# Concatenate
# Stack
# Split
# Where
# ==========================================

import numpy as np

print("=" * 60)
print("Question 1: Broadcasting")
print("=" * 60)

arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)
print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 2: Boolean Indexing")
print("=" * 60)

marks = np.array([45, 67, 89, 23, 90, 55, 72])

print("Marks:", marks)
print("Marks > 60:", marks[marks > 60])
print("Marks < 50:", marks[marks < 50])

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 3: Fancy Indexing")
print("=" * 60)

numbers = np.array([10,20,30,40,50,60,70])

print(numbers[[0,2,4]])
print(numbers[[1,3,5]])

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 4: Aggregation Functions")
print("=" * 60)

salary = np.array([25000,40000,55000,70000,90000])

print("Sum:", np.sum(salary))
print("Mean:", np.mean(salary))
print("Median:", np.median(salary))
print("Maximum:", np.max(salary))
print("Minimum:", np.min(salary))
print("Standard Deviation:", np.std(salary))
print("Variance:", np.var(salary))

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 5: Axis Operations")
print("=" * 60)

matrix = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(matrix)

print("\nRow-wise Sum:")
print(np.sum(matrix, axis=1))

print("\nColumn-wise Sum:")
print(np.sum(matrix, axis=0))

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 6: Random Module")
print("=" * 60)

print("Random Integers")
print(np.random.randint(1,100,10))

print("\nRandom Float Numbers")
print(np.random.rand(5))

print("\nRandom Normal Distribution")
print(np.random.randn(5))

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 7: Sorting")
print("=" * 60)

arr = np.array([45,12,89,23,67,10])

print("Original:", arr)
print("Sorted:", np.sort(arr))

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 8: Searching")
print("=" * 60)

numbers = np.array([5,10,15,20,25,30])

print("Index of 20:")
print(np.where(numbers == 20))

print("Numbers > 15")
print(np.where(numbers > 15))

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 9: Unique Values")
print("=" * 60)

arr = np.array([1,2,3,4,2,3,1,5,6,6])

print("Original:", arr)
print("Unique:", np.unique(arr))

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 10: Concatenate")
print("=" * 60)

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.concatenate((a,b)))

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 11: Vertical Stack")
print("=" * 60)

print(np.vstack((a,b)))

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 12: Horizontal Stack")
print("=" * 60)

print(np.hstack((a,b)))

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 13: Split Array")
print("=" * 60)

arr = np.arange(1,13)

print(arr)

split = np.split(arr,3)

print(split)

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 14: Employee Salary Analysis")
print("=" * 60)

salary = np.array([25000,35000,42000,50000,62000,75000,82000])

print("Salaries:", salary)

print("Average Salary:", np.mean(salary))
print("Highest Salary:", np.max(salary))
print("Lowest Salary:", np.min(salary))

print("Salary > 50000")
print(salary[salary > 50000])

print("Salary < 40000")
print(salary[salary < 40000])

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 15: Matrix Operations")
print("=" * 60)

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print("Matrix A")
print(A)

print("Matrix B")
print(B)

print("Addition")
print(A+B)

print("Subtraction")
print(A-B)

print("Element-wise Multiplication")
print(A*B)

print("Matrix Multiplication")
print(np.dot(A,B))

# --------------------------------------------------

print("\n" + "=" * 60)
print("Question 16: Practice Challenge")
print("=" * 60)

sales = np.array([120,150,180,90,300,250,100])

print("Sales:", sales)

print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))

print("Sales Greater Than Average:")
print(sales[sales > np.mean(sales)])

print("Sorted Sales:")
print(np.sort(sales))

print("\n✅ Day 2 Completed Successfully!")
