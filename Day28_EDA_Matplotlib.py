# ==========================================================
# DAY 28 - EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_csv("titanic.csv")

# ----------------------------------------------------------
# Q1. Display first 5 rows.
# ----------------------------------------------------------

print(df.head())

# ----------------------------------------------------------
# Q2. Display dataset information.
# ----------------------------------------------------------

print(df.info())

# ----------------------------------------------------------
# Q3. Display statistical summary.
# ----------------------------------------------------------

print(df.describe())

# ----------------------------------------------------------
# Q4. Check missing values.
# ----------------------------------------------------------

print(df.isnull().sum())

# ----------------------------------------------------------
# Q5. Fill missing Age with median.
# ----------------------------------------------------------

df["Age"] = df["Age"].fillna(df["Age"].median())

# ----------------------------------------------------------
# Q6. Survival Count
# ----------------------------------------------------------

print(df["Survived"].value_counts())

plt.figure(figsize=(6,4))
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.show()

# ----------------------------------------------------------
# Q7. Passenger Class Distribution
# ----------------------------------------------------------

print(df["Pclass"].value_counts())

plt.figure(figsize=(6,4))
df["Pclass"].value_counts().plot(kind="bar")
plt.title("Passenger Class Distribution")
plt.xlabel("Class")
plt.ylabel("Passengers")
plt.show()

# ----------------------------------------------------------
# Q8. Gender Distribution
# ----------------------------------------------------------

print(df["Sex"].value_counts())

plt.figure(figsize=(6,4))
df["Sex"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# ----------------------------------------------------------
# Q9. Age Distribution
# ----------------------------------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# ----------------------------------------------------------
# Q10. Fare Distribution
# ----------------------------------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["Fare"], bins=20)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()

# ----------------------------------------------------------
# Q11. Average Age by Gender
# ----------------------------------------------------------

print(df.groupby("Sex")["Age"].mean())

# ----------------------------------------------------------
# Q12. Average Fare by Passenger Class
# ----------------------------------------------------------

print(df.groupby("Pclass")["Fare"].mean())

# ----------------------------------------------------------
# Q13. Survival by Gender
# ----------------------------------------------------------

print(df.groupby("Sex")["Survived"].mean())

# ----------------------------------------------------------
# Q14. Survival by Passenger Class
# ----------------------------------------------------------

print(df.groupby("Pclass")["Survived"].mean())

# ----------------------------------------------------------
# Q15. Top 10 Highest Fare Passengers
# ----------------------------------------------------------

print(df.sort_values(by="Fare", ascending=False).head(10))

# ----------------------------------------------------------
# Q16. Correlation Matrix
# ----------------------------------------------------------

print(df.corr(numeric_only=True))

# ----------------------------------------------------------
# Q17. Box Plot for Age
# ----------------------------------------------------------

plt.figure(figsize=(6,4))
plt.boxplot(df["Age"])
plt.title("Age Box Plot")
plt.show()

# ----------------------------------------------------------
# Q18. Box Plot for Fare
# ----------------------------------------------------------

plt.figure(figsize=(6,4))
plt.boxplot(df["Fare"])
plt.title("Fare Box Plot")
plt.show()

# ----------------------------------------------------------
# Q19. Scatter Plot (Age vs Fare)
# ----------------------------------------------------------

plt.figure(figsize=(7,5))
plt.scatter(df["Age"], df["Fare"])
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

# ----------------------------------------------------------
# Q20. Save Cleaned Dataset
# ----------------------------------------------------------

df.to_csv("titanic_cleaned.csv", index=False)

print("EDA Completed Successfully!")

# ==========================================================
# END OF DAY 28
# ==========================================================
