# 👥 HR Employee Dataset

A synthetic HR dataset of **1,000 employees** across 6 departments and 5 Indian cities, provided in two versions: the **raw** file (with real-world data quality problems) and a **cleaned** file ready for analysis. It is well suited for practicing **data cleaning, Excel / SQL / Python analysis, attrition analysis, and dashboarding**.

---

## 📁 Repository Structure

```
.
├── hr_data.csv          # Raw data (1,002 rows, 13 columns) — messy, unprocessed
├── clean_hr_data.csv    # Cleaned data (1,000 rows, 14 columns) — analysis-ready
└── README.md
```

| File | Rows | Columns | Purpose |
|---|---:|---:|---|
| `hr_data.csv` | 1,002 | 13 | Original data with missing values, inconsistent labels, and duplicates |
| `clean_hr_data.csv` | 1,000 | 14 | Cleaned version with a new `Employment_Status` column |

---

## 📖 Data Dictionary

### Columns in both files

| Column | Type | Description | Example |
|---|---|---|---|
| `Employee_ID` | String | Employee identifier (`EMP1001`–`EMP2000`) | `EMP1001` |
| `First_Name` | String | Employee first name | `Priya` |
| `Last_Name` | String | Employee last name | `Patel` |
| `Gender` | String | Gender (`Male`, `Female`, `Unknown`) | `Female` |
| `Age` | Integer | Age in years (16–72) | `25` |
| `Department` | String | `Sales`, `Operations`, `Marketing`, `IT`, `Finance`, `HR` | `Operations` |
| `City` | String | `Mumbai`, `Pune`, `Surat`, `Ahmedabad`, `Delhi` | `Mumbai` |
| `Salary` | Integer | Salary amount (currency not specified; likely INR given locations) | `45000` |
| `Performance_Rating` | Float | Rating from 1 (lowest) to 5 (highest) | `5.0` |
| `Attendance_Percent` | Float | Attendance percentage (75–99) | `91.0` |
| `Joining_Date` | Date | Date of joining (`YYYY-MM-DD`), 2015–2024 | `2022-03-04` |
| `Exit_Date` | Date | Date of exit (`YYYY-MM-DD`); blank for active employees | `2023-10-18` |
| `Attrition` | String | `Yes` if employee left, `No` if still employed | `Yes` |

### Added in `clean_hr_data.csv` only

| Column | Type | Description |
|---|---|---|
| `Employment_Status` | String | `Exited` (Attrition = Yes) or `Active` (Attrition = No) |

---

## 🧹 Raw vs. Cleaned — What Changed

### Raw data issues (`hr_data.csv`)

| Issue | Count |
|---|---:|
| Missing `Gender` | 187 |
| Missing `Department` | 154 |
| Missing `City` | 183 |
| Missing `Performance_Rating` | 184 |
| Missing `Attendance_Percent` | 156 |
| Inconsistent gender labels (`M`, `F` vs. `Male`, `Female`) | 360 |
| Duplicate rows (exact copies) | 2 |
| Missing `Exit_Date` | 846 (expected — active employees) |

### Cleaning steps applied (`clean_hr_data.csv`)

> These steps were inferred by comparing the two files.

| Step | Detail |
|---|---|
| Removed duplicates | 2 exact duplicate rows dropped (1,002 → 1,000) |
| Standardised gender | `M` → `Male`, `F` → `Female` |
| Filled missing `Gender` | Filled with the most frequent value (`Male`) |
| Filled missing `Department` | Filled with the most frequent value (`Sales`) |
| Filled missing `City` | Filled with the most frequent value (`Mumbai`) |
| Filled missing `Performance_Rating` | Filled with the median (`3.0`) |
| Filled missing `Attendance_Percent` | Filled with the mean (`≈88.30`) |
| Added `Employment_Status` | Derived from `Attrition` |

---

## ⚠️ Known Limitations

The cleaned file is **not fully clean**. Check these before drawing conclusions:

| Issue | Where | Detail |
|---|---|---|
| **Negative salaries** | Both files | 127 rows have `Salary = -5000` (likely a placeholder/error) |
| **Salary outliers** | Both files | 132 rows at exactly `250000`, which looks like a cap or default value |
| **Underage employees** | Both files | 107 rows with `Age < 18` (minimum is 16) |
| **Duplicate Employee ID** | Both files | `EMP1100` appears twice for two different people (Neha Gupta, Suresh Kumar) |
| **Future exit dates** | Both files | 7 exit dates fall after Oct 2026 (latest: 2027-12-22) |
| **Imputation bias** | Clean file | Mode/median/mean fills inflate `Male`, `Sales`, `Mumbai`, and rating `3` (e.g. Sales jumps from 149 to 303 rows) |
| **Low value diversity** | Both files | `Attendance_Percent` and `Salary` take only a handful of distinct values, which suggests synthetic data |
| **Unknown gender** | Both files | 168 rows are labelled `Unknown`, kept as a separate category |

> 💡 **Tip:** Treat imputed values with caution in department-, city-, or gender-level analysis. Filtering them out or using the raw file's blanks may give more honest results.

---

## 📊 Quick Facts (Cleaned Data)

| Metric | Value |
|---|---|
| Total employees | 1,000 |
| Active / Exited | 844 / 156 |
| **Attrition rate** | **15.6%** |
| Joining date range | 2015-01-01 → 2024-12-22 |
| Avg. performance rating | 2.96 |
| Avg. attendance | 88.29% |

---

## 🚀 Getting Started

### Python (pandas)

```python
import pandas as pd

raw   = pd.read_csv("hr_data.csv", parse_dates=["Joining_Date", "Exit_Date"])
clean = pd.read_csv("clean_hr_data.csv", parse_dates=["Joining_Date", "Exit_Date"])

print(clean.shape)                                  # (1000, 14)
print(clean["Attrition"].value_counts(normalize=True))
print(clean.groupby("Department")["Salary"].mean())
```

### Excel

1. Open Excel → **Data → From Text/CSV** → select the file.
2. Convert to a Table with `Ctrl + T`.
3. Build Pivot Tables, e.g. **Attrition by Department** or **Average Salary by City**.

### SQL (example)

```sql
SELECT Department,
       COUNT(*) AS headcount,
       ROUND(100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS attrition_pct
FROM clean_hr_data
GROUP BY Department
ORDER BY attrition_pct DESC;
```

---

## 🎯 Suggested Analysis Ideas

- Attrition rate by department, city, gender, and age group
- Average tenure of exited vs. active employees (`Exit_Date − Joining_Date`)
- Relationship between performance rating, attendance, and attrition
- Salary distribution by department and performance rating
- **Cleaning challenge:** fix the remaining issues listed under *Known Limitations*
- Build an interactive HR dashboard (Excel slicers, Power BI, or Tableau)

---

## 📝 Notes

- All data appears **synthetic** and should not be treated as real employee information.
- Names, IDs, and values do not correspond to real individuals.
- Feel free to fork, clean further, and share your analysis.

---
