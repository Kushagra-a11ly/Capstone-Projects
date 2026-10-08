import pandas as pd
from numpy import mean
def employee_overview(df):
    print("=" * 50)
    print("HR ANALYTICS - EDA")
    print("=" * 50)
    print("Total Employees:", len(df))
    print("Total Departments:", df["Department"].nunique())
    print("Total Cities:", df["City"].nunique())
    print("Employment Status Distribution:",df["Employment_Status"].value_counts())
    print("Department Distribution:",df["Department"].value_counts())

def salary_analysis(df):
    print("=" * 50)
    print("SALARY ANALYSIS")
    print("=" * 50)
    print("Total Employees:", len(df))
    print("Total Departments:", df["Department"].nunique())
    print("Total Cities:", df["City"].nunique())
    print(df["Employment_Status"].value_counts())
    print(df["Department"].value_counts())
    print(df["Gender"].value_counts())
    print(df["Gender"].value_counts(normalize=True))
    print(df["Age"].describe())
    print(df["Age"].value_counts())
    average_salary = df["Salary"].mean()
    print("Highest Salary:", df["Salary"].max())
    print("Lowest Salary:", df["Salary"].min())
    print("Average Salary:", df["Salary"].mean())
    print("Median Salary:", df["Salary"].median())
    print("Top 10 Highest Salaries:")
    print(df["Salary"].nlargest(10))
    print(df.nlargest(10, "Salary")[["Employee_ID", "First_Name", "Last_Name", "Salary"]])
    print(df.nsmallest(10, "Salary")[["Employee_ID", "First_Name", "Last_Name", "Salary"]])
    print(df.groupby("Department")["Salary"].mean())
    print(df.groupby("City")["Salary"].mean())
    print(df.groupby("Department")["Salary"].mean().sort_values(ascending=False).head(1))
    print(df.groupby("Department")["Salary"].mean().idxmax())
    print(df.groupby("City")["Salary"].mean().sort_values(ascending=False).head(1))
    print(df.groupby("City")["Salary"].mean().idxmax())


def age_analysis(df):
    print(df["Age"].describe())
    print(df["Age"].value_counts())
    print(df["Age"].value_counts(normalize=True))
    print("Youngest Employee:",df[df["Age"] < 30])
    print("Oldest Employee:",df[df["Age"] > 50])
    print("Average Age:", df["Age"].mean())
    print("Count employee in each age group:",df["Age"].value_counts())

    df["Age_Group"] = pd.cut(
        df["Age"],
        bins=[20, 30, 40, 50, float("inf")],
        labels=["20-30", "31-40", "41-50", "51+"],
        right=True,
        include_lowest=True
    )
    # df["Age_Group2"] = df["Age"].apply(lambda x: "20-30" if 20 <= x < 30 else "31-40" if 30 <= x < 40 else "41-50" if 40 <= x < 50 else "51+")

def gender_analysis(df):
    print("=" * 50)
    print("GENDER ANALYSIS")
    print("=" * 50)
    print(df["Gender"].value_counts())
    # # Find the gender percentage.
    print(df["Gender"].value_counts(normalize=True) * 100)
    print(df.groupby("Gender")["Salary"].mean())
    print(df.groupby("Gender")["Performance_Rating"].mean())
    
    
def performanceRating_alalysis(df):    
    print("=" * 50)
    print("PERFORMANCE RATING ANALYSIS")
    print("=" * 50)
    print(df["Performance_Rating"].mean())
    print(df.groupby("Department")["Performance_Rating"].mean())
    high_performers = df["Performance_Rating"].max()
    print(df[df["Performance_Rating"] == high_performers][
            ["First_Name", "Last_Name", "Department", "Performance_Rating"]
        ])
    print(df["Performance_Rating"].value_counts())
    print(df.groupby("Performance_Rating")["Salary"].mean())

def attendance_analysis(df):
    print("=" * 50)
    print("ATTENDANCE ANALYSIS")
    print("=" * 50)
    print(df["Attendance_Percent"].mean())
    print(df.groupby("Department")["Attendance_Percent"].mean())
    print(df[df["Attendance_Percent"] < 80][["First_Name", "Last_Name", "Department", "Attendance_Percent"]])
    print(df[df["Attendance_Percent"] > 95][["First_Name", "Last_Name", "Department", "Attendance_Percent"]])
    print(df.columns)
    attendance = df.groupby("Department")["Attendance_Percent"].mean()
    print(attendance)
    print(attendance.idxmax())   # Department name
    print(attendance.max())      # Highest average attendance

def attrition_analysis(df):
    print("=" * 50)
    print("ATTEITION ANALYSIS")
    print("=" * 50)
    print(df["Employment_Status"].value_counts())
    print(df["Attrition"].value_counts(normalize=True) * 100)
    print(df.groupby("Department")["Attrition"].value_counts())
    print(df.groupby("City")["Attrition"].value_counts())
    print(df.groupby("Employment_Status")["Salary"].mean())
    
    
def department_analysis(df):
    print("=" * 50)
    print("DEPARTMENT ANALYSIS")
    print("=" * 50)
    department_counts = df["Department"].value_counts()
    print(department_counts)
    print(department_counts.idxmax())
    print(department_counts.max())
    print(department_counts.idxmin())
    print(department_counts.min())
    print(df.groupby("Department")["Age"].mean())
    highest_paid = df.loc[df.groupby("Department")["Salary"].idxmax()]
    print(highest_paid[["Department", "First_Name", "Last_Name", "Salary"]])
    lowest_paid = df.loc[df.groupby("Department")["Salary"].idxmin()]
    print(lowest_paid[["Department", "First_Name", "Last_Name", "Salary"]])
        
def city_analysis(df):
    print("=" * 50)
    print("CITY ANALYSIS")
    print("=" * 50)
    count_city = df.groupby("City")["Employee_ID"].count()
    print(count_city.idxmax())
    print(count_city.max())
    print(count_city.idxmin())
    print(count_city.min())
    print(df.groupby("City")["Salary"].mean())
    print(df.groupby("City")
        ["Attendance_Percent"].mean())
    print(df.groupby("City")["Performance_Rating"].mean())
    print(df.groupby("City")["Age"].mean())
    
def advanced_analysis(df):
    print("=" * 50)
    print("ADVANCED ANALYSIS")
    print("=" * 50)
    average_salary = df["Salary"].mean()
    print(df.loc[df["Salary"] > average_salary][["First_Name", "Last_Name", "Department", "Salary"]])
    lowest_salary = df.loc[df["Salary"] < average_salary]
    print(lowest_salary[["First_Name", "Last_Name", "Department", "Salary"]])
    department_average_salary = df.groupby("Department")["Salary"].transform(mean)
    print(df.loc[df["Salary"] > department_average_salary][["First_Name", "Last_Name", "Department", "Salary"]])
    company_avg_attendance = df["Attendance_Percent"].mean()
    print(df.loc[df["Attendance_Percent"] < company_avg_attendance][["First_Name", "Last_Name", "Department", "Attendance_Percent"]])
    Performance_Rating_average = df["Performance_Rating"].mean()
    print(df.loc[df["Performance_Rating"] > Performance_Rating_average][["First_Name", "Last_Name", "Department", "Performance_Rating"]])
    department_average_salary1 = df.groupby("Department")["Salary"].mean()
    print(department_average_salary1.nlargest(5))
    print(department_average_salary1.nsmallest(5))
    coleration = df[["Attendance_Percent","Performance_Rating"]].corr()
    print(coleration)
    average_age = df["Age"].mean()
    print(df.loc[df["Age"] > average_age][["First_Name", "Last_Name", "Department", "Age"]])
    print(df.loc[df["Age"] < average_age][["First_Name", "Last_Name", "Department", "Age"]])
    df["Salary_Rank"] = df["Salary"].rank(method="dense", ascending=False)
    print(
        df[["First_Name", "Last_Name", "Department", "Salary", "Salary_Rank"]]
    )
    
def business_insights(df):
    print("=" * 50)
    print("BUSINESS INSIGHTS")
    print("=" * 50)
    # # Which department should receive more hiring?
    # # HR department has less number of employees so it should receive more hiring
    # # Which department has the highest salary expenditure?
    # # Sales department has the highest salary expenditure with value of 24540000
    # # Which city has the most employees?
    # # Mumbai city has the most employees with value of 359
    # # Which department has the best performance?
    # # Operations department has best performance with value 3.110345
    # # Which department has the lowest attendance?
    # # Marketing department have lowest attendance 87.600839
    # # Is higher salary associated with better performance?
    # # Is higher salary associated with better performance?
    # # No, higher salary is not associated with better performance
    # # Which department has the highest attrition?
    # # Operations departemnt have the highest attrition 18.620690
    # attrition_rate = df.groupby("Department")["Attrition"].value_counts(normalize=True) * 100
    # print(attrition_rate.loc[:, "Yes"])
    # # Which age group has the highest attrition?
    # # 30 age group have the highest attrition 26
    # attrition_age = df.groupby("Age")["Attrition"].value_counts()
    # print(attrition_age.loc[:,"Yes"])
    # # Which gender has the highest average salary?
    # # Female gender have the highest average salary
    # print(df.groupby("Gender")["Salary"].mean())
    
    # # Write 10 business insights from your analysis.
    # Write 10 business insights from your analysis.
    # -> Hr deparment have less employees than other departments
    # -> depend on rating salary is distributed
    # -> depend on rating performance is distributed
    # -> depend on rating attrition is distributed
    # -> depend on rating average working hours is distributed
    # -> depend on rating average monthly working hours is distributed
    # -> depend on rating average monthly income is distributed
    # -> depend on rating average monthly income is distributed
    # -> Gender is not related to attrition
    # -> Age is not related to attrition
    # -> Gender is not related to salary

