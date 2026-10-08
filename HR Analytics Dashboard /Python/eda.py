from numpy import mean
import pandas as pd
from utils import *

df = pd.read_csv("data/clean_hr_data.csv")

employee_overview(df)
salary_analysis(df)
age_analysis(df)
gender_analysis(df)
performanceRating_alalysis(df)
attendance_analysis(df)
attrition_analysis(df)
department_analysis(df)
city_analysis(df)
advanced_analysis(df)
business_insights(df)
