# ==========================================
# DAY 4 - PANDAS ADVANCED
# Topics:
# 1. loc
# 2. iloc
# 3. Filtering
# 4. Sorting
# 5. GroupBy
# 6. Merge
# 7. Concat
# 8. Value Counts
# 9. Unique
# 10. Apply
# 11. Map
# 12. Lambda
# 13. Replace
# ==========================================

import pandas as pd

students = {
    "ID":[101,102,103,104,105],
    "Name":["Amit","Priya","Rahul","Sneha","Karan"],
    "Age":[20,21,19,22,20],
    "Marks":[85,90,78,92,88],
    "City":["Pune","Mumbai","Pune","Delhi","Mumbai"]
}

df = pd.DataFrame(students)

print("="*60)
print("Original DataFrame")
print("="*60)
print(df)

# -------------------------------------------------

print("\nQuestion 1 : loc")
print(df.loc[0])

print("\nMultiple Rows")
print(df.loc[1:3])

# -------------------------------------------------

print("\nQuestion 2 : iloc")
print(df.iloc[2])

print("\nRows 1 to 3")
print(df.iloc[1:4])

# -------------------------------------------------

print("\nQuestion 3 : Filtering")

print(df[df["Marks"] > 85])

print("\nStudents from Pune")

print(df[df["City"]=="Pune"])

# -------------------------------------------------

print("\nQuestion 4 : Multiple Conditions")

print(df[(df["Marks"]>80) & (df["City"]=="Mumbai")])

# -------------------------------------------------

print("\nQuestion 5 : Sorting")

print(df.sort_values(by="Marks"))

print("\nDescending")

print(df.sort_values(by="Marks",ascending=False))

# -------------------------------------------------

print("\nQuestion 6 : GroupBy")

print(df.groupby("City")["Marks"].mean())

# -------------------------------------------------

print("\nQuestion 7 : Value Counts")

print(df["City"].value_counts())

# -------------------------------------------------

print("\nQuestion 8 : Unique")

print(df["City"].unique())

# -------------------------------------------------

print("\nQuestion 9 : Apply")

df["Bonus"] = df["Marks"].apply(lambda x: x+5)

print(df)

# -------------------------------------------------

print("\nQuestion 10 : Map")

grade = {
    85:"B",
    90:"A",
    78:"C",
    92:"A",
    88:"B"
}

df["Grade"] = df["Marks"].map(grade)

print(df)

# -------------------------------------------------

print("\nQuestion 11 : Lambda")

df["Age After 5 Years"] = df["Age"].apply(lambda x:x+5)

print(df)

# -------------------------------------------------

print("\nQuestion 12 : Replace")

df["City"] = df["City"].replace({
    "Pune":"PUNE",
    "Mumbai":"MUMBAI"
})

print(df)

# -------------------------------------------------

print("\nQuestion 13 : Merge")

department = pd.DataFrame({
    "ID":[101,102,103,104,105],
    "Department":["IT","HR","Finance","Marketing","Sales"]
})

merged_df = pd.merge(df,department,on="ID")

print(merged_df)

# -------------------------------------------------

print("\nQuestion 14 : Concat")

semester2 = pd.DataFrame({
    "ID":[106,107],
    "Name":["Neha","Rohan"],
    "Age":[21,20],
    "Marks":[81,76],
    "City":["Nagpur","Pune"],
    "Bonus":[86,81],
    "Grade":["B","C"],
    "Age After 5 Years":[26,25]
})

combined = pd.concat([df,semester2],ignore_index=True)

print(combined)

# -------------------------------------------------

print("\nQuestion 15 : Student Analysis")

print("Highest Marks :",df["Marks"].max())

print("Lowest Marks :",df["Marks"].min())

print("Average Marks :",df["Marks"].mean())

print("Total Students :",len(df))

print("Students Scoring Above Average")

print(df[df["Marks"]>df["Marks"].mean()])

print("\nDay 4 Completed Successfully")
