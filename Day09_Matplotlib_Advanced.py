# ==========================================================
# DAY 9 - MATPLOTLIB ADVANCED
# Topics:
# 1. Line Plot
# 2. Multiple Line Plot
# 3. Marker Styles
# 4. Line Styles
# 5. Colors
# 6. Grid
# 7. Legend
# 8. Figure Size
# 9. Bar Plot
# 10. Horizontal Bar Plot
# 11. Histogram
# 12. Pie Chart
# 13. Scatter Plot
# 14. Box Plot
# 15. Save Figure
# ==========================================================

import matplotlib.pyplot as plt

# -----------------------------------------------------

months = ["Jan","Feb","Mar","Apr","May","Jun"]

sales = [120,180,150,220,280,300]

profit = [20,40,30,60,80,95]

# -----------------------------------------------------

print("Question 1 : Basic Line Plot")

plt.figure(figsize=(8,5))

plt.plot(months,sales)

plt.title("Monthly Sales")

plt.xlabel("Months")

plt.ylabel("Sales")

plt.show()

# -----------------------------------------------------

print("Question 2 : Multiple Line Plot")

plt.figure(figsize=(8,5))

plt.plot(months,sales,label="Sales")

plt.plot(months,profit,label="Profit")

plt.legend()

plt.title("Sales vs Profit")

plt.show()

# -----------------------------------------------------

print("Question 3 : Marker")

plt.figure(figsize=(8,5))

plt.plot(months,sales,marker="o")

plt.title("Sales with Markers")

plt.show()

# -----------------------------------------------------

print("Question 4 : Line Style")

plt.figure(figsize=(8,5))

plt.plot(months,sales,linestyle="--")

plt.title("Dashed Line")

plt.show()

# -----------------------------------------------------

print("Question 5 : Line Width")

plt.figure(figsize=(8,5))

plt.plot(months,sales,linewidth=3)

plt.title("Thick Line")

plt.show()

# -----------------------------------------------------

print("Question 6 : Grid")

plt.figure(figsize=(8,5))

plt.plot(months,sales)

plt.grid(True)

plt.title("Grid Example")

plt.show()

# -----------------------------------------------------

print("Question 7 : Bar Chart")

plt.figure(figsize=(8,5))

plt.bar(months,sales)

plt.title("Monthly Sales")

plt.show()

# -----------------------------------------------------

print("Question 8 : Horizontal Bar Chart")

plt.figure(figsize=(8,5))

plt.barh(months,sales)

plt.title("Horizontal Bar Chart")

plt.show()

# -----------------------------------------------------

print("Question 9 : Histogram")

marks=[65,70,80,90,88,75,68,92,84,77,81,73]

plt.figure(figsize=(8,5))

plt.hist(marks,bins=5)

plt.title("Marks Distribution")

plt.show()

# -----------------------------------------------------

print("Question 10 : Pie Chart")

department=["IT","HR","Finance","Sales"]

employees=[40,20,15,25]

plt.figure(figsize=(6,6))

plt.pie(employees,
        labels=department,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Department Distribution")

plt.show()

# -----------------------------------------------------

print("Question 11 : Scatter Plot")

age=[20,22,24,26,28,30]

salary=[25000,30000,35000,45000,55000,65000]

plt.figure(figsize=(8,5))

plt.scatter(age,salary)

plt.title("Age vs Salary")

plt.xlabel("Age")

plt.ylabel("Salary")

plt.show()

# -----------------------------------------------------

print("Question 12 : Box Plot")

plt.figure(figsize=(6,5))

plt.boxplot(salary)

plt.title("Salary Distribution")

plt.show()

# -----------------------------------------------------

print("Question 13 : Save Figure")

plt.figure(figsize=(8,5))

plt.plot(months,sales)

plt.title("Monthly Sales")

plt.savefig("monthly_sales.png")

plt.show()

# -----------------------------------------------------

print("Question 14 : Maximum Sales")

print(max(sales))

# -----------------------------------------------------

print("Question 15 : Minimum Profit")

print(min(profit))

print("\nDay 9 Completed Successfully!")
