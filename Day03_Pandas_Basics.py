# ==========================================
# DAY 3 - PANDAS BASICS
# Topics:
# 1. Import Pandas
# 2. Series
# 3. DataFrame
# 4. Read CSV
# 5. Head()
# 6. Tail()
# 7. Shape
# 8. Columns
# 9. Info()
# 10. Describe()
# 11. Selecting Columns
# 12. Selecting Rows
# 13. Add Column
# 14. Drop Column
# 15. Rename Column
# ==========================================

import pandas as pd

print("="*60)
print("Question 1: Create a Series")
print("="*60)

marks = pd.Series([85, 90, 78, 92, 88])

print(marks)

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 2: Create a DataFrame")
print("="*60)

students = {
    "Name":["Amit","Priya","Rahul","Sneha","Karan"],
    "Age":[20,21,19,22,20],
    "Marks":[85,90,78,92,88],
    "City":["Pune","Mumbai","Delhi","Nagpur","Nashik"]
}

df = pd.DataFrame(students)

print(df)

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 3: Save DataFrame as CSV")
print("="*60)

df.to_csv("students.csv", index=False)

print("students.csv created successfully!")

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 4: Read CSV")
print("="*60)

data = pd.read_csv("students.csv")

print(data)

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 5: Head()")
print("="*60)

print(data.head())

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 6: Tail()")
print("="*60)

print(data.tail())

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 7: Shape")
print("="*60)

print("Shape:", data.shape)

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 8: Columns")
print("="*60)

print(data.columns)

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 9: Info()")
print("="*60)

print(data.info())

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 10: Describe()")
print("="*60)

print(data.describe())

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 11: Select One Column")
print("="*60)

print(data["Name"])

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 12: Select Multiple Columns")
print("="*60)

print(data[["Name","Marks"]])

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 13: Select First Row")
print("="*60)

print(data.iloc[0])

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 14: Select First Three Rows")
print("="*60)

print(data.iloc[:3])

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 15: Add New Column")
print("="*60)

data["Result"] = ["Pass","Pass","Pass","Pass","Pass"]

print(data)

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 16: Drop Column")
print("="*60)

new_data = data.drop(columns=["Result"])

print(new_data)

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 17: Rename Column")
print("="*60)

new_data.rename(columns={"Marks":"Score"}, inplace=True)

print(new_data)

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 18: Data Types")
print("="*60)

print(new_data.dtypes)

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 19: Index")
print("="*60)

print(new_data.index)

# ----------------------------------------------------

print("\n" + "="*60)
print("Question 20: Student Summary")
print("="*60)

print("Total Students:", len(new_data))
print("Average Marks:", new_data["Score"].mean())
print("Highest Marks:", new_data["Score"].max())
print("Lowest Marks:", new_data["Score"].min())

print("\n✅ Day 3 Completed Successfully!")
