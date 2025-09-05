Employee Attrition Dataset

📌 Objective
This dataset is designed to explore the factors that contribute to employee attrition. It helps address questions such as:
How does travel frequency impact retention across departments?
Does monthly income differ by education level when comparing employees who stay versus those who leave?
The dataset is synthetic (created by IBM data scientists) and mimics real-world HR data patterns.

📂 Dataset Description

Each row corresponds to an individual employee, containing demographic details, job-related attributes, satisfaction ratings, and compensation metrics. The target variable indicates whether the employee has left the company (Attrition) or not.

📖 Data Dictionary

Age → Age of the employee
Attrition → Whether the employee left the company (Yes/No)
BusinessTravel → Frequency of business travel
DailyRate → Employee’s daily wage rate
Department → Department of work (e.g., Sales, R&D, HR)
DistanceFromHome → Distance from home to office

Education →
1 = Less than College
2 = College Graduate
3 = Bachelor’s Degree
4 = Master’s Degree
5 = Doctorate

EducationField → Field of study (e.g., Life Sciences, Medical, Marketing)
EmployeeCount → Headcount (constant = 1 for each record)
EmployeeNumber → Unique employee ID

EnvironmentSatisfaction →
1 = Unsatisfied
2 = Neutral
3 = Satisfied
4 = Highly Satisfied

Gender → Male/Female
HourlyRate → Hourly wage
JobInvolvement →
1 = Low Commitment
2 = Moderate Commitment
3 = High Commitment
4 = Very High Commitment
JobLevel → Level of the job position
JobRole → Specific job designation (e.g., Sales Executive, Manager)

JobSatisfaction →
1 = Dissatisfied
2 = Somewhat Satisfied
3 = Satisfied
4 = Extremely Satisfied

MaritalStatus → Employee’s marital status
MonthlyIncome → Monthly salary
MonthlyRate → Monthly rate of pay
NumCompaniesWorked → Number of companies previously worked for
Over18 → Whether employee is over 18 (constant = Yes)
OverTime → Works overtime (Yes/No)
PercentSalaryHike → Percentage increase in salary during last appraisal
PerformanceRating →
1 = Poor
2 = Fair
3 = Excellent
4 = Outstanding

RelationshipSatisfaction →
1 = Unhappy
2 = Moderate
3 = Happy
4 = Very Happy

StandardHours → Standard working hours (constant = 80)
StockOptionLevel → Level of stock options awarded
TotalWorkingYears → Total years of work experience
TrainingTimesLastYear → Number of training sessions attended last year

WorkLifeBalance →
1 = Poor
2 = Good
3 = Better than Average
4 = Excellent

YearsAtCompany → Years spent in the current company
YearsInCurrentRole → Years in the current role
YearsSinceLastPromotion → Years since last promotion
YearsWithCurrManager → Years with the current manager

🎯 Possible Use Cases
Predicting employee attrition using classification models
Exploring satisfaction and compensation patterns across roles

Building HR dashboards for attrition insights

Identifying high-risk groups for turnover
