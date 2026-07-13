# ==========================================================
# DAY 8 - EDA VISUALIZATION (MATPLOTLIB)
# Dataset: Titanic
# Topics:
# 1. Histogram
# 2. Bar Chart
# 3. Pie Chart
# 4. Scatter Plot
# 5. Box Plot
# 6. Line Plot
# 7. Horizontal Bar Chart
# 8. Survival Analysis
# 9. Passenger Class Analysis
# 10. Save Figures
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------

print("Loading Dataset...")

df = pd.read_csv("titanic.csv")

# ----------------------------------------------------------

print("\nQuestion 1 : Histogram of Age")

plt.figure(figsize=(8,5))
plt.hist(df["Age"].dropna(), bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("histogram_age.png")
plt.show()

# ----------------------------------------------------------

print("\nQuestion 2 : Bar Chart of Passenger Class")

pclass = df["Pclass"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(pclass.index.astype(str), pclass.values)
plt.title("Passenger Class Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.savefig("bar_pclass.png")
plt.show()

# ----------------------------------------------------------

print("\nQuestion 3 : Pie Chart of Gender")

gender = df["Sex"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(gender.values,
        labels=gender.index,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Gender Distribution")
plt.savefig("pie_gender.png")
plt.show()

# ----------------------------------------------------------

print("\nQuestion 4 : Scatter Plot")

plt.figure(figsize=(8,5))
plt.scatter(df["Age"], df["Fare"])
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.savefig("scatter_age_fare.png")
plt.show()

# ----------------------------------------------------------

print("\nQuestion 5 : Box Plot")

plt.figure(figsize=(6,5))
plt.boxplot(df["Fare"].dropna())
plt.title("Fare Boxplot")
plt.savefig("boxplot_fare.png")
plt.show()

# ----------------------------------------------------------

print("\nQuestion 6 : Line Plot")

fare = df["Fare"].head(20)

plt.figure(figsize=(8,5))
plt.plot(fare)
plt.title("Fare of First 20 Passengers")
plt.xlabel("Passenger")
plt.ylabel("Fare")
plt.savefig("line_fare.png")
plt.show()

# ----------------------------------------------------------

print("\nQuestion 7 : Horizontal Bar Chart")

city = df["Embarked"].value_counts()

plt.figure(figsize=(6,4))
plt.barh(city.index.astype(str), city.values)
plt.title("Embarked Distribution")
plt.xlabel("Passengers")
plt.savefig("horizontal_bar.png")
plt.show()

# ----------------------------------------------------------

print("\nQuestion 8 : Survival Count")

survival = df["Survived"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(["Not Survived","Survived"], survival.values)

plt.title("Survival Count")
plt.savefig("survival_bar.png")
plt.show()

# ----------------------------------------------------------

print("\nQuestion 9 : Passenger Class vs Survival")

survive_class = df.groupby("Pclass")["Survived"].sum()

plt.figure(figsize=(6,4))
plt.bar(survive_class.index.astype(str),
        survive_class.values)

plt.title("Survivors by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survivors")
plt.savefig("class_survival.png")
plt.show()

# ----------------------------------------------------------

print("\nQuestion 10 : Average Fare by Class")

avg_fare = df.groupby("Pclass")["Fare"].mean()

plt.figure(figsize=(6,4))
plt.bar(avg_fare.index.astype(str),
        avg_fare.values)

plt.title("Average Fare by Passenger Class")
plt.xlabel("Class")
plt.ylabel("Average Fare")
plt.savefig("avg_fare_class.png")
plt.show()

# ----------------------------------------------------------

print("\nQuestion 11 : Young vs Old Passengers")

young = len(df[df["Age"] < 30])
old = len(df[df["Age"] >= 30])

plt.figure(figsize=(6,4))
plt.bar(["Below 30","30 & Above"], [young, old])

plt.title("Age Group Distribution")
plt.savefig("age_group.png")
plt.show()

# ----------------------------------------------------------

print("\nQuestion 12 : Male vs Female Survival")

gender_survival = df.groupby("Sex")["Survived"].sum()

plt.figure(figsize=(6,4))
plt.bar(gender_survival.index,
        gender_survival.values)

plt.title("Survivors by Gender")
plt.savefig("gender_survival.png")
plt.show()

# ----------------------------------------------------------

print("\nQuestion 13 : Family Size")

family = df["SibSp"] + df["Parch"]

plt.figure(figsize=(8,5))
plt.hist(family, bins=8)

plt.title("Family Size Distribution")
plt.xlabel("Family Members")
plt.ylabel("Count")
plt.savefig("family_size.png")
plt.show()

# ----------------------------------------------------------

print("\nQuestion 14 : Highest Fare Passenger")

highest = df.loc[df["Fare"].idxmax()]

print(highest)

# ----------------------------------------------------------

print("\nQuestion 15 : Lowest Fare Passenger")

lowest = df.loc[df["Fare"].idxmin()]

print(lowest)

# ----------------------------------------------------------

print("\nQuestion 16 : Top 10 Highest Fare")

print(df.nlargest(10,"Fare"))

# ----------------------------------------------------------

print("\nQuestion 17 : Top 10 Lowest Fare")

print(df.nsmallest(10,"Fare"))

# ----------------------------------------------------------

print("\nQuestion 18 : Summary")

print(df.describe())

# ----------------------------------------------------------

print("\nQuestion 19 : Missing Values")

print(df.isnull().sum())

# ----------------------------------------------------------

print("\nQuestion 20 : Final Insights")

print("Average Age :", df["Age"].mean())
print("Average Fare :", df["Fare"].mean())
print("Highest Fare :", df["Fare"].max())
print("Survival Rate :", df["Survived"].mean()*100)

print("\nDay 8 Completed Successfully!")
