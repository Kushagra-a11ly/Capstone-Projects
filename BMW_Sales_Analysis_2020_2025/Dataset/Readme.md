📂 Dataset – BMW Sales Analysis (2020–2025)

This folder contains the dataset(s) used in the BMW Sales Analysis (2020–2025) project.  
 📑 Files
- BMW_Sales_2020_2025.csv
  Raw dataset containing BMW sales records from 2020 to 2025.  
 📊 Dataset Overview

 🧹 Data Notes
- Dataset is in CSV format (comma-separated values).  
- Null/missing values may exist → handled during preprocessing.  
- Currency is in **USD** for uniform comparison.  
The dataset includes sales details of BMW cars across multiple **years, regions, and models**.  

Key Columns:
- `Year` → Year of sales (2020–2025)  
- `Month` → Month of sales (1–12)  
- `Model` → BMW car model sold  
- `Type` → Vehicle type (e.g., SUV, Sedan, Coupe)  
- `Power` → Engine power specification  
- `Region` → Global sales region (e.g., Europe, Asia, North America)  
- `Country` → Country where the sale occurred  
- `Units_Sold` → Number of cars sold  
- `Avg_Price_USD` → Average selling price per unit (USD)  
- `Revenue_USD` → Total sales revenue (USD)  
- `Cost_USD` → Total cost incurred (USD)  
- `Profit_USD` → Profit before expenses (USD)  
- `Profit_Margin` → Profit margin percentage  
- `Gross_Margin` → Gross margin percentage  
- `Operating_Expenses_USD` → Operating expenses (USD)  
- `Net_Profit_USD` → Final net profit (USD)  
- `ROI` → Return on Investment (%)  
- `EBITDA_Margin` → Earnings Before Interest, Taxes, Depreciation, and Amortization margin  
  
  df = pd.read_csv("Dataset/BMW_Sales_2020_2025.csv")
  print(df.head())
