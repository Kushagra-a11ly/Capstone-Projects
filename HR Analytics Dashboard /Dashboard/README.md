# HR Executive Dashboard (Power BI)

An interactive, four-page Power BI report that gives HR leadership a single view of **headcount, attrition, performance, demographics and compensation** for a 999-employee workforce. The report is built on one cleaned employee table, 18 DAX measures, and a set of slicers and navigation buttons that let a viewer slice every page by Department, Gender, City and Joining Year.

---

## Table of Contents

1. [Project at a Glance](#1-project-at-a-glance)
2. [Business Questions Answered](#2-business-questions-answered)
3. [Report Pages](#3-report-pages)
4. [Data Source and Data Preparation (Power Query)](#4-data-source-and-data-preparation-power-query)
5. [Data Model](#5-data-model)
6. [DAX Measures and Calculated Columns](#6-dax-measures-and-calculated-columns)
7. [Data Dictionary](#7-data-dictionary)
8. [Snapshot of the Data](#8-snapshot-of-the-data)
9. [Key Insights](#9-key-insights)
10. [Data Quality Observations and Known Issues](#10-data-quality-observations-and-known-issues)
11. [How to Open and Refresh the Report](#11-how-to-open-and-refresh-the-report)
12. [Design Notes](#12-design-notes)
13. [Suggested Improvements](#13-suggested-improvements)
14. [Tech Stack](#14-tech-stack)

---

## 1. Project at a Glance

| Item | Detail |
|---|---|
| **File** | `HR_Executive_Dashboard.pbix` |
| **Tool** | Microsoft Power BI Desktop |
| **Pages** | 4 (canvas size 1280 x 720) |
| **Tables in model** | 1 fact table (`clean_hr_data`) plus 3 auto-generated date tables |
| **Rows** | 999 employees (one row per employee, deduplicated on `Employee_ID`) |
| **Measures** | 18 DAX measures |
| **Calculated columns** | 1 meaningful (`Salary_Category`) and 1 empty placeholder (`Column`) |
| **Visuals** | 55 visual containers across the 4 pages: 15 charts, 4 multi-card KPI visuals (19 KPI tiles), 16 slicers, 4 title text boxes and 16 navigation buttons |
| **Data load mode** | Import, from a local CSV file |
| **Theme** | Power BI built-in base theme `CY26SU05` |

---

## 2. Business Questions Answered

- How many employees do we have, how many are active, and how many have left?
- What is our attrition rate overall and by department?
- Which department has the strongest performance rating?
- How is performance spread across the 1 to 5 rating scale?
- How is the workforce distributed by age group, city and gender?
- How has hiring changed from year to year?
- What do we pay on average, by department, by city and by joining cohort?
- What are the highest, lowest, average and total salaries, and how many people fall into each salary band?

---

## 3. Report Pages

Every page has the same layout skeleton: a title banner at the top, four slicers (Department, Gender, City, Joining Year), a row of KPI cards, a row of charts, and a navigation bar of four buttons along the bottom.

### Page 1: HR Analytics Dashboard (Executive Overview)

The landing page. A one-glance summary of the whole workforce.

| Element | Type | Fields |
|---|---|---|
| KPI cards (7) | Card | Total Employees, Avg Salary, Exited, Active, Attrition Rate, Avg Rating, Avg Attendance |
| Employees by Department | Clustered bar | `Department` vs count of `Employee_ID` |
| *(untitled chart)* | Clustered column | `Department` vs `Active Employees` |
| Gender Distribution | Pie | `Gender` vs count of `Employee_ID` |

### Page 2: Performance & Attrition Analysis

| Element | Type | Fields |
|---|---|---|
| KPI cards (4) | Card | Average Rating, Attrition Rate, Exited Employees, Best Performing Department |
| Average Performance Rating by Department | Clustered column | `Department` vs `Average Rating` |
| Attrition by Department | Stacked column | `Department` vs `Active Employees` and `Exited Employees` |
| Salary Category Distribution | Donut | `Salary_Category` vs count of `Employee_ID` |
| Employee Performance Distribution | Clustered column | `Performance_Rating` vs count of `Employee_ID` |

### Page 3: Workforce Demographics

Subtitle on the page: *Employee Demographics, Diversity & Hiring Trends*.

| Element | Type | Fields |
|---|---|---|
| KPI cards (4) | Card | Average Age, Total Cities, Average Years of Service, Male : Female Ratio |
| Employees by Age Group | Clustered column | `Age_Group` vs count of `Employee_ID` |
| Employees by City | Clustered bar | `City` vs count of `Employee_ID` |
| Gender Distribution | Donut | `Gender` vs count of `Employee_ID` |
| Employees Joined by Year | Line | `Joining_Year` vs count of `Employee_ID` |

### Page 4: Salary & Workforce Insights

Subtitle on the page: *Compensation, Salary Analysis, Workforce Distribution*.

| Element | Type | Fields |
|---|---|---|
| KPI cards (4) | Card | Highest Salary, Lowest Salary, Average Salary, Total Salary |
| Average Salary by Department | Clustered bar | `Department` vs `Average_Salary` |
| Salary Category Distribution | Donut | `Salary_Category` vs count of `Employee_ID` |
| Average Salary by City | Clustered bar | `City` vs `Average_Salary` |
| Average Salary Trend by Joining Year | Line | `Joining_Year` vs `Average_Salary` |

### Slicers (all pages)

| Slicer | Field |
|---|---|
| Department | `clean_hr_data[Department]` |
| Gender | `clean_hr_data[Gender]` |
| City | `clean_hr_data[City]` |
| Joining Year | `Joining_Date` date hierarchy, Year level |

### Navigation

Each page has four buttons labelled **Home**, **Performance**, **Demographics** and **Salary**, implemented as page-navigation buttons. See [Known Issues](#10-data-quality-observations-and-known-issues) for two buttons that point to the wrong page.

---

## 4. Data Source and Data Preparation (Power Query)

**Source:** a single CSV file, `clean_hr_data.csv`, loaded with `Csv.Document` (comma delimited, 14 columns, Windows-1252 encoding). The path is a hard-coded absolute path on the author's machine (see [How to Open and Refresh](#11-how-to-open-and-refresh-the-report)).

**Raw columns (14):** `Employee_ID`, `First_Name`, `Last_Name`, `Gender`, `Age`, `Department`, `City`, `Salary`, `Performance_Rating`, `Attendance_Percent`, `Joining_Date`, `Exit_Date`, `Attrition`, `Employment_Status`.

### Transformation steps

| # | Step | Purpose |
|---|---|---|
| 1 | Promote headers, set data types | Text for IDs and categories; whole numbers for `Age`, `Salary`, `Performance_Rating`; decimal for `Attendance_Percent`; dates for `Joining_Date` and `Exit_Date` |
| 2 | Build `Salary_Clean` | `if [Salary] < 0 then 0 else [Salary]`. Negative salaries are replaced with 0. The original `Salary` column is then removed |
| 3 | Round `Attendance_Percent` | Rounded to 2 decimal places |
| 4 | Build `Full_Name` | `First_Name & " " & Last_Name`, then drop the two source columns |
| 5 | Remove duplicates | `Table.Distinct` on `Employee_ID` |
| 6 | Build `Age_Group` | 25 or under = **Young**, 26 to 35 = **Adult**, 36 to 45 = **Mid Age**, over 45 = **Senior** |
| 7 | Build `Joining_Year` | `Date.Year([Joining_Date])` |
| 8 | Build `Years_of_Service` | `Duration.TotalDays(today - [Joining_Date]) / 365`, rounded down to a whole number |
| 9 | Column reordering and cleanup | A first version of `Salary_Category` (below 50,000 / up to 80,000 / above) is created and then removed at the end of the query, because the model uses a DAX version instead |

---

## 5. Data Model

- **Star schema?** No. The model is a single flat fact table, `clean_hr_data`, with no user-defined relationships. The diagram view shows only that one table.
- **Auto date/time:** Power BI created three hidden date tables (one `DateTableTemplate` and two `LocalDateTable` tables), each with `Date`, `Year`, `MonthNo`, `Month`, `QuarterNo`, `Quarter` and `Day`. They support the date hierarchies on `Joining_Date` and `Exit_Date`, including the Joining Year slicer.
- **Storage:** Import mode. The data is stored inside the `.pbix`.

---

## 6. DAX Measures and Calculated Columns

### Measures

| Measure | DAX | Meaning |
|---|---|---|
| **Total Employees** | `COUNT(clean_hr_data[Employee_ID])` | Headcount in current filter context |
| **Active Employees** | `CALCULATE(COUNT(clean_hr_data[Employee_ID]), clean_hr_data[Employment_Status] = "Active")` | Employees still employed |
| **Exited Employees** | `CALCULATE(COUNT(clean_hr_data[Employee_ID]), clean_hr_data[Employment_Status] = "Exited")` | Employees who have left |
| **Attrition Rate** | `DIVIDE([Exited Employees], [Total Employees])` | Share of employees who have exited |
| **Average_Salary** | `AVERAGE(clean_hr_data[Salary_Clean])` | Mean salary, zero-salary rows included |
| **Total Salary** | `SUM(clean_hr_data[Salary_Clean])` | Sum of all salaries |
| **Highest Salary** | `CALCULATE(MAX(clean_hr_data[Salary_Clean]), clean_hr_data[Salary_Clean] > 0)` | Maximum salary, zeros excluded |
| **Lowest Salary** | `CALCULATE(MIN(clean_hr_data[Salary_Clean]), clean_hr_data[Salary_Clean] > 0)` | Minimum salary, zeros excluded |
| **Average Rating** | `ROUND(AVERAGE(clean_hr_data[Performance_Rating]), 1)` | Mean rating on the 1 to 5 scale |
| **Average Attendance** | `AVERAGE(clean_hr_data[Attendance_Percent])` | Mean attendance on a 0 to 100 scale |
| **Average Attendance %** | `DIVIDE(AVERAGE(clean_hr_data[Attendance_Percent]), 100)` | Same value as a 0 to 1 fraction, used by the overview card so it can be formatted as a percentage |
| **Average Age** | `AVERAGE(clean_hr_data[Age])` | Mean age |
| **Average Years of Service** | `AVERAGE(clean_hr_data[Years_of_Service])` | Mean tenure in whole years |
| **Total Cities** | `DISTINCTCOUNT(clean_hr_data[City])` | Number of work locations |
| **Male Employees** | `CALCULATE(COUNT(clean_hr_data[Employee_ID]), clean_hr_data[Gender] = "Male")` | Helper for the ratio |
| **Female Employees** | `CALCULATE(COUNT(clean_hr_data[Employee_ID]), clean_hr_data[Gender] = "Female")` | Helper for the ratio |
| **Male : Female Ratio** | see below | Text such as `1.52 : 1` |
| **Best Performing Department** | see below | Department with the highest average rating, with the value in brackets |

```dax
Male : Female Ratio =
VAR MaleCount = [Male Employees]
VAR FemaleCount = [Female Employees]
RETURN
    FORMAT(DIVIDE(MaleCount, FemaleCount), "0.00") & " : 1"
```

```dax
Best Performing Department =
VAR DeptTable =
    ADDCOLUMNS(
        VALUES(clean_hr_data[Department]),
        "AvgRating", CALCULATE(AVERAGE(clean_hr_data[Performance_Rating]))
    )
VAR TopDept =
    TOPN(1, DeptTable, [AvgRating], DESC)
RETURN
    CONCATENATEX(
        TopDept,
        clean_hr_data[Department] & " (" & FORMAT([AvgRating], "0.00") & ")"
    )
```

### Calculated columns

```dax
Salary_Category =
SWITCH(
    TRUE(),
    clean_hr_data[Salary_Clean] >= 90000, "High",
    clean_hr_data[Salary_Clean] >= 60000, "Medium",
    "Low"
)
```

| Band | Rule |
|---|---|
| High | Salary of 90,000 or more |
| Medium | 60,000 to 89,999 |
| Low | Under 60,000 (includes the zero-salary rows) |

A second calculated column named `Column` exists with no expression and holds only blanks. It is not used by any visual (see Known Issues).

---

## 7. Data Dictionary

Final columns in `clean_hr_data` (18):

| Column | Type | Description |
|---|---|---|
| `Employee_ID` | Text | Unique employee identifier (`EMP1007` style) |
| `Full_Name` | Text | First and last name combined |
| `Gender` | Text | Male, Female or Unknown |
| `Age` | Whole number | Age in years (range 16 to 72) |
| `Department` | Text | Finance, HR, IT, Marketing, Operations, Sales |
| `City` | Text | Ahmedabad, Delhi, Mumbai, Pune, Surat |
| `Performance_Rating` | Whole number | 1 (lowest) to 5 (highest) |
| `Attendance_Percent` | Decimal | Attendance, 75 to 99, rounded to 2 decimals |
| `Joining_Date` | Date | Date of joining (2015 to 2024) |
| `Joining_Year` | Whole number | Year extracted from `Joining_Date` |
| `Exit_Date` | Date | Date of leaving; blank for active employees |
| `Attrition` | Text | Yes or No |
| `Employment_Status` | Text | Active or Exited (matches `Attrition` on every row) |
| `Age_Group` | Text | Young, Adult, Mid Age, Senior |
| `Salary_Clean` | Whole number | Cleaned salary; negatives set to 0 |
| `Years_of_Service` | Whole number | Whole years since joining, as of the last refresh |
| `Salary_Category` | Text | High, Medium or Low (DAX column) |
| `Column` | Whole number | Empty placeholder column |

---

## 8. Snapshot of the Data

Values below were computed from the data stored in the file and match what the measures return with no slicers applied.

### Headline KPIs

| KPI | Value |
|---|---|
| Total employees | 999 |
| Active employees | 843 |
| Exited employees | 156 |
| Attrition rate | 15.6% |
| Average salary (zeros included) | 79,540 |
| Average salary (non-zero only) | 91,124 |
| Highest salary | 250,000 |
| Lowest salary (non-zero) | 35,000 |
| Total salary | 79,460,000 |
| Average performance rating | 3.0 |
| Average attendance | 88.3% |
| Average age | 37.9 |
| Average years of service | 6.2 |
| Cities | 5 |
| Male : Female ratio | 1.52 : 1 (501 male, 330 female, 168 Unknown) |

### By department

| Department | Employees | Avg rating | Attrition rate | Avg salary |
|---|---|---|---|---|
| Sales | 303 | 2.93 | 14.2% | 81,551 |
| Operations | 145 | 3.11 | 18.6% | 80,759 |
| Marketing | 141 | 2.88 | 15.6% | 87,447 |
| IT | 140 | 2.98 | 16.4% | 74,036 |
| Finance | 137 | 2.86 | 15.3% | 76,314 |
| HR | 133 | 3.02 | 15.0% | 74,361 |

### Other distributions

| Dimension | Breakdown |
|---|---|
| Performance rating | 1: 183, 2: 156, 3: 335, 4: 170, 5: 155 |
| Age group | Young 331, Adult 236, Senior 236, Mid Age 196 |
| City | Mumbai 359, Pune 177, Surat 166, Ahmedabad 155, Delhi 142 |
| Salary category | Low 496, High 260, Medium 243 |
| Joining year | 2015: 114, 2016: 94, 2017: 88, 2018: 129, 2019: 100, 2020: 96, 2021: 87, 2022: 94, 2023: 105, 2024: 92 |

---

## 9. Key Insights

These observations describe the stored data snapshot and are a starting point for discussion, not conclusions.

- **Attrition is about 1 in 6.** 156 of 999 employees (15.6%) have exited. Operations has the highest rate (18.6%) and Sales the lowest (14.2%), though the spread is only about four points.
- **Operations rates best on performance** (3.11), with HR second (3.02). Finance has the lowest average (2.86). All departments sit close to the middle of the scale.
- **Performance is centred on 3.** 335 employees (34%) are rated 3, and the two extremes are similar in size (183 rated 1, 155 rated 5).
- **Sales is the largest department** at 303 people, roughly twice the size of any other department.
- **Mumbai holds over a third of the workforce** (359 of 999).
- **The workforce skews young.** 331 employees are in the Young band (25 or under), the largest age group.
- **Hiring peaked in 2018** (129 joiners) and was lowest in 2021 (87).
- **Marketing pays the highest average salary** (87,447) and IT the lowest (74,036). By city, Pune is highest (85,989) and Delhi lowest (70,387).
- **Pay by joining cohort is uneven.** The 2017 cohort has the highest average salary (90,284); the 2021 cohort the lowest (73,736).

---

## 10. Data Quality Observations and Known Issues

### Data observations

| # | Observation | Impact |
|---|---|---|
| 1 | **127 employees have a salary of 0.** These were negative values in the source, replaced with 0 in Power Query | Pulls `Average_Salary` down (79,540 versus 91,124 for non-zero rows) and inflates the Low salary band. `Highest` and `Lowest Salary` exclude zeros but `Average` and `Total` include them, so the cards are not on the same basis |
| 2 | **107 employees are under 18** (minimum age 16) | Unusual for a workforce; likely a source data problem. Inflates the Young group and lowers average age |
| 3 | **168 employees have Gender = "Unknown"** | Excluded from the Male : Female ratio, but included in the Gender pie and donut charts |
| 4 | **7 exit dates are later than the date of this analysis** (latest is December 2027) | Future-dated exits; worth confirming against the source |
| 5 | **`Attrition` and `Employment_Status` carry the same information** | Redundant. The measures use `Employment_Status` |
| 6 | **Attrition rate is cumulative**, not a period rate: all exits divided by all employees ever on record | Not comparable to an annual attrition percentage |
| 7 | **`Years_of_Service` depends on the refresh date** because it uses the current date | Values change each time the report is refreshed |

### Known issues in the report build

| # | Issue | Suggested fix |
|---|---|---|
| 1 | On **Page 1**, the **Home** button navigates to the *Salary & Workforce Insights* page instead of staying on (or pointing to) the overview | Re-point the button, or set no action since it is the current page |
| 2 | On **Page 4**, the **Salary** button navigates to *Performance & Attrition Analysis* instead of the current page | Re-point the button, or set no action |
| 3 | On **Page 1**, the clustered column chart showing Active Employees by Department **has no title** | Add a title such as "Active Employees by Department" |
| 4 | Pages 2 and 4 both use the same chart emoji in their page names, which makes the page tabs look alike | Use distinct icons, e.g. a money bag for Salary |
| 5 | **`Salary_Category` is defined twice with different thresholds**: Power Query used 50,000 / 80,000, the DAX column uses 60,000 / 90,000. Only the DAX version survives | Keep one definition and document the thresholds on the report |
| 6 | **Empty calculated column `Column`** | Delete it |
| 7 | **Hard-coded local file path** for the data source | Use a Power BI parameter (see below) |
| 8 | **Two attendance measures** (`Average Attendance` on a 0 to 100 scale and `Average Attendance %` on a 0 to 1 scale) | Keep one and format it as a percentage |

---

## 11. How to Open and Refresh the Report

**Requirements:** Power BI Desktop (current release; the file was last saved with the CY26SU05 theme and query settings version 2.155).

1. Open `HR_Executive_Dashboard.pbix` in Power BI Desktop. The report displays immediately from the data stored inside the file.
2. To refresh, the CSV must exist at the path stored in the query. On any other machine the refresh will fail until you repoint it:
   - **Home > Transform data > Data source settings > Change Source**, or
   - open **Transform data**, select the `clean_hr_data` query, and edit the file path in the **Source** step.
3. Click **Refresh**. `Years_of_Service` will recalculate against today's date.

**Recommended:** replace the absolute path with a parameter (**Home > Transform data > Manage parameters**, e.g. `DataFolder`) so the project is portable.

### Suggested repository layout

```
HR-Executive-Dashboard/
├── HR_Executive_Dashboard.pbix
├── data/
│   └── clean_hr_data.csv
├── screenshots/
│   ├── 01_overview.png
│   ├── 02_performance_attrition.png
│   ├── 03_demographics.png
│   └── 04_salary.png
└── README.md
```

---

## 12. Design Notes

- **Canvas:** 1280 x 720 on all four pages, with a consistent header, slicer row, KPI row, chart row and navigation bar.
- **Navigation:** emoji-labelled buttons with a hover colour change.
- **Interaction:** the report keeps Power BI's default setting where drill actions filter the other visuals on the page, and each page has its own set of the four slicers.
- **Theme:** the built-in Power BI base theme (`CY26SU05`), with its standard blue, navy and orange data colours.
- **Assets:** the file embeds a set of small image resources (people, money bag, hourglass, star rating, pin, bank and similar icons). No standalone image visuals appear in the page layout, so these may be leftovers from earlier design iterations and could be removed to shrink the file.

---

## 13. Suggested Improvements

- Fix the two navigation buttons and add the missing chart title (see Known Issues).
- Decide how to treat zero-salary and under-18 records (exclude, flag, or correct at source) and show the rule on the report.
- Add a **period-based attrition rate** (for example exits per year divided by average headcount) and an **exit-year trend** chart using `Exit_Date`.
- Add **attrition by tenure band** and **attrition by performance rating** to show who is leaving.
- Add a proper **Date table** and relate it to `Joining_Date` and `Exit_Date` instead of relying on auto date/time.
- Add **tooltips** and **drill-through** pages (for example department detail).
- Add **conditional formatting** on the KPI cards (for example attrition above a target).
- Move the file path into a **parameter** and consider a scheduled refresh in the Power BI Service.
- Add an **RLS** (row-level security) role if the report is shared with department heads, since it contains salary data.

---

## 14. Tech Stack

| Layer | Tool |
|---|---|
| Source data | CSV (`clean_hr_data.csv`) |
| Data preparation | Power Query (M) |
| Modelling and calculations | Data Analysis Expressions (DAX) |
| Visualisation | Power BI Desktop |

---

*Author: add your name, LinkedIn and GitHub links here.*
