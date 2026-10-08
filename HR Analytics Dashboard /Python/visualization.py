import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/clean_hr_data.csv")

# ==========================================
# 1. Employee count by Department
# ==========================================

df["Department"].value_counts().plot(kind="bar")
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.savefig("images/employee_department.png", dpi=300, bbox_inches="tight")
plt.show()

# ==========================================
# Chart 2: Employee Count by City
# ==========================================

city_count = df["City"].value_counts()
plt.figure(figsize=(10, 6))
city_count.plot(kind="barh")
plt.title("Employee Count by City")
plt.xlabel("Number of Employees")
plt.ylabel("City")
plt.savefig("images/employee_city.png", dpi=300, bbox_inches="tight")
plt.show()


# ==========================================
# Chart 3: Salary Distribution
# ==========================================

salary_analysis = df["Salary"]
plt.figure(figsize=(10, 6))
salary_analysis.plot(kind="hist")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Department")
plt.savefig("images/salary_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

# ==========================================
# Chart 4: Average Salary by Department
# ==========================================

salary_average = df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
salary_average.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.savefig("images/average_salary.png", dpi=300, bbox_inches="tight")
plt.show()

# ==========================================
# Chart 5: Gender Distribution
# ==========================================
gender_count = df["Gender"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(
    gender_count,
    labels=gender_count.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Gender Distribution")
plt.savefig("images/gender_distribution.png", dpi=300, bbox_inches="tight")
plt.show()


# ==========================================
# Chart 6: Department Performance
# ==========================================

department_performance = df.groupby("Department")["Performance_Rating"].mean()

plt.figure(figsize=(10,6))
department_performance.plot(kind="bar")

plt.title("Average Performance by Department")
plt.xlabel("Department")
plt.ylabel("Average Performance Rating")

plt.savefig("images/department_performance.png", dpi=300, bbox_inches="tight")
plt.show()

# ==========================================
# Chart 7: Department Attendance
# ==========================================

department_attendance = df.groupby("Department")["Attendance_Percent"].mean()

plt.figure(figsize=(10,6))
department_attendance.plot(kind="bar")

plt.title("Average Attendance by Department")
plt.xlabel("Department")
plt.ylabel("Attendance (%)")

plt.savefig("images/department_attendance.png", dpi=300, bbox_inches="tight")
plt.show()

# ==========================================
# Chart 8: Attrition Distribution
# ==========================================

plt.figure(figsize=(6,5))

sns.countplot(data=df, x="Attrition")

plt.title("Attrition Distribution")
plt.xlabel("Attrition")
plt.ylabel("Employee Count")

plt.savefig("images/attrition_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

# ==========================================
# Chart 9: Attrition by Department
# ==========================================

attrition_department = pd.crosstab(df["Department"], df["Attrition"])

attrition_department.plot(
    kind="bar",
    stacked=True,
    figsize=(10,6)
)

plt.title("Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Employee Count")
plt.legend(title="Attrition")

plt.savefig("images/attrition_department.png", dpi=300, bbox_inches="tight")
plt.show()

# ==========================================
# Chart 10: Correlation Heatmap
# ==========================================

correlation = df[
    [
        "Salary",
        "Age",
        "Attendance_Percent",
        "Performance_Rating"
    ]
].corr()

plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.savefig("images/correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()