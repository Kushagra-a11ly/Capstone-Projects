📂 Dataset – BMW Sales Analysis (2020–2025)

This folder contains the dataset(s) used in the BMW Sales Analysis (2020–2025) project.  
 📑 Files
- BMW_Sales_2020_2025.csv
  Raw dataset containing BMW sales records from 2020 to 2025.  
 📊 Dataset Overview
The dataset includes sales details of BMW cars across multiple years, regions, and models.  
Key Columns:
- `Year` → Year of sales (2020–2025)  
- `Month` → Month of sales (1–12)  
- `Model` → BMW car model sold  
- `Country` → Country where the sale occurred  
- `Units_Sold` → Number of cars sold  
- `Revenue_USD` → Revenue generated in USD  
- `Net_Profit_USD` → Profit earned in USD  
 🧹 Data Notes
- Dataset is in **CSV format** (comma-separated values).  
- Null/missing values may exist → handled during preprocessing.  
- Currency is in **USD** for uniform comparison.  

  
  df = pd.read_csv("Dataset/BMW_Sales_2020_2025.csv")
  print(df.head())
