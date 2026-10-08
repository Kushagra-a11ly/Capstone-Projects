import pandas as pd

# Read Dataset
df = pd.read_csv("data/hr_data.csv")

print("=" * 50)
print("HR ANALYTICS DATA EXPLORATION")
print("=" * 50)

# Shape
print("\n1. Shape")
print(df.shape)

# Columns
print("\n2. Columns")
print(df.columns)

# Data Types
print("\n3. Data Types")
print(df.dtypes)

# Information
print("\n4. Dataset Information")
df.info()

# Statistics
print("\n5. Statistical Summary")
print(df.describe(include="all"))

# by using include="all" in describe() method, we can get the statistical summary of all columns, including categorical columns.

# Missing Values
print("\n6. Missing Values")
print(df.isnull())

# its returns a DataFrame of the same shape as df, with True for missing values and False for non-missing values. We can also use the sum() method to get the count of missing values in each column.
print(df.isnull().sum())

# Duplicate Rows
print("\n7. Duplicate Rows")
print(df.duplicated())

# its returns a Series of the same length as df, with True for duplicate rows and False for non-duplicate rows. We can also use the sum() method to get the count of duplicate rows.
print("\nCount of Duplicate Rows:")
print(df.duplicated().sum())

# it will check the mode value of the Gender by using mode() method and fill the missing values of the Gender column with the mode value by using fillna() method. The mode() method returns the most frequent value in the column, and we can access it by using [0] index. The fillna() method replaces the missing values with the specified value.
print(df["Gender"].mode())

# Fill Missing Values in Gender Column with Mode Value by using fillna() method. The mode() method returns the most frequent value in the column, and we can access it by using [0] index. The fillna() method replaces the missing values with the specified value.
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])

# finally, we can check the missing values again to confirm that the missing values in the Department column have been filled with the mode value.
print("Department", df["Department"].mode())
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])

print(df["City"].mode())
df["City"] = df["City"].fillna(df["City"].mode()[0])

# print(df["Performance_Rating"].mean())
mean_rating = round(df["Performance_Rating"].mean(),1)
# print(mean_rating)
df["Performance_Rating"] = df["Performance_Rating"].fillna(mean_rating)


df["Attendance_Percent"] = df["Attendance_Percent"].fillna(
    df["Attendance_Percent"].mean()
)


df["Exit_Date"] = pd.to_datetime(df["Exit_Date"])

df["Employment_Status"] = df["Exit_Date"].apply(lambda x: "Active" if pd.isnull(x) else "Exited")
print(df.isnull().sum())

print(df["Department"])

df.drop_duplicates(inplace=True)
print(df.duplicated().sum())

df.to_csv("data/clean_hr_data.csv", index=False)

# Data Cleaning
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])
df["Exit_Date"] = pd.to_datetime(df["Exit_Date"])

# Verify Data Types
print("\nData Types After Cleaning:")
print(df.dtypes)

# Convert Gender to String
df["Gender"] = df["Gender"].replace({
    "M": "Male",
    "F": "Female"
})

# Save Clean Dataset
df.to_csv("data/clean_hr_data.csv", index=False)

print("✅ Cleaned dataset saved successfully.")