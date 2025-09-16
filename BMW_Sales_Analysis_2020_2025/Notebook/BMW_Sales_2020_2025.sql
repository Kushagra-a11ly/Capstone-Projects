USE hii;

-- 1. Select all records
SELECT * 
FROM bmw_sales_2020_2025;

-- 2. Select specific columns
SELECT Year, Month, Model, Revenue_USD
FROM bmw_sales_2020_2025;

-- 3. Count total records
SELECT COUNT(*) AS total_records
FROM bmw_sales_2020_2025;

-- 4. Find distinct car models
SELECT DISTINCT Model
FROM bmw_sales_2020_2025;

-- 5. Total units sold
SELECT SUM(Units_Sold) AS total_units_sold
FROM bmw_sales_2020_2025;

-- 6. Maximum revenue
SELECT MAX(Revenue_USD) AS max_revenue
FROM bmw_sales_2020_2025;

-- 7. Minimum cost
SELECT MIN(Cost_USD) AS min_cost
FROM bmw_sales_2020_2025;

-- 8. Average profit margin
SELECT AVG(Profit_Margin) AS avg_profit_margin
FROM bmw_sales_2020_2025;

-- 9. Records for a specific year (e.g., 2022)
SELECT *
FROM bmw_sales_2020_2025
WHERE Year = 2022;

-- 10. Records for a specific model (e.g., '3 Series')
SELECT *
FROM bmw_sales_2020_2025
WHERE Model = '3 Series';

-- 11. Total revenue by year
SELECT Year, SUM(Revenue_USD) AS total_revenue
FROM bmw_sales_2020_2025
GROUP BY Year
ORDER BY Year;

-- 12. Total units sold by region
SELECT Region, SUM(Units_Sold) AS total_units
FROM bmw_sales_2020_2025
GROUP BY Region;

-- 13. Average price of each model
SELECT Model, AVG(Avg_Price_USD) AS avg_price
FROM bmw_sales_2020_2025
GROUP BY Model;

-- 14. Count of records per country
SELECT Country, COUNT(*) AS total_records
FROM bmw_sales_2020_2025
GROUP BY Country;

-- 15. Revenue greater than 1,000,000 USD
SELECT *
FROM bmw_sales_2020_2025
WHERE Revenue_USD > 1000000;

-- Intermediate Level

-- 1. Total revenue by year
SELECT Year, SUM(Revenue_USD) AS total_revenue
FROM bmw_sales_2020_2025
GROUP BY Year
ORDER BY Year;

-- 2. Total units sold by model
SELECT Model, SUM(Units_Sold) AS total_units
FROM bmw_sales_2020_2025
GROUP BY Model
ORDER BY total_units DESC;

-- 3. Average profit margin by model
SELECT Model, AVG(Profit_Margin) AS avg_profit_margin
FROM bmw_sales_2020_2025
GROUP BY Model
ORDER BY avg_profit_margin DESC;

-- 4. Total revenue by region
SELECT Region, SUM(Revenue_USD) AS total_revenue
FROM bmw_sales_2020_2025
GROUP BY Region
ORDER BY total_revenue DESC;

-- 5. Total net profit by country
SELECT Country, SUM(Net_Profit_USD) AS total_net_profit
FROM bmw_sales_2020_2025
GROUP BY Country
ORDER BY total_net_profit DESC;

-- 6. Average cost and price by model
SELECT Model, AVG(Cost_USD) AS avg_cost, AVG(Avg_Price_USD) AS avg_price
FROM bmw_sales_2020_2025
GROUP BY Model;

-- 7. Units sold for each year and model
SELECT Year, Model, SUM(Units_Sold) AS total_units
FROM bmw_sales_2020_2025
GROUP BY Year, Model
ORDER BY Year, total_units DESC;

-- 8. Top 5 models by total revenue
SELECT Model, SUM(Revenue_USD) AS total_revenue
FROM bmw_sales_2020_2025
GROUP BY Model
ORDER BY total_revenue DESC
LIMIT 5;

-- 9. Total revenue by year and region
SELECT Year, Region, SUM(Revenue_USD) AS total_revenue
FROM bmw_sales_2020_2025
GROUP BY Year, Region
ORDER BY Year, total_revenue DESC;

-- 10. Average EBITDA margin by model
SELECT Model, AVG(EBITDA_Margin) AS avg_ebitda
FROM bmw_sales_2020_2025
GROUP BY Model
ORDER BY avg_ebitda DESC;

-- 11. Records with profit margin above 20%
SELECT *
FROM bmw_sales_2020_2025
WHERE Profit_Margin > 20
ORDER BY Profit_Margin DESC;

-- 12. Total operating expenses by year
SELECT Year, SUM(Operating_Expenses_USD) AS total_expenses
FROM bmw_sales_2020_2025
GROUP BY Year
ORDER BY Year;

-- 13. Average ROI by country
SELECT Country, AVG(ROI) AS avg_roi
FROM bmw_sales_2020_2025
GROUP BY Country
ORDER BY avg_roi DESC;

-- 14. Units sold by power type
SELECT Power, SUM(Units_Sold) AS total_units
FROM bmw_sales_2020_2025
GROUP BY Power
ORDER BY total_units DESC;

-- 15. Month-wise total units sold in 2023
SELECT Month, SUM(Units_Sold) AS total_units
FROM bmw_sales_2020_2025
WHERE Year = 2023
GROUP BY Month
ORDER BY FIELD(Month, 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');

-- Advanced Level
-- 1. Year-over-year revenue growth
SELECT Year,
       SUM(Revenue_USD) AS total_revenue,
       LAG(SUM(Revenue_USD)) OVER (ORDER BY Year) AS prev_year_revenue,
       ROUND(
           (SUM(Revenue_USD) - LAG(SUM(Revenue_USD)) OVER (ORDER BY Year)) 
           / LAG(SUM(Revenue_USD)) OVER (ORDER BY Year) * 100, 2
       ) AS revenue_growth_pct
FROM bmw_sales_2020_2025
GROUP BY Year
ORDER BY Year;

-- 2. Top-selling model each year
SELECT Year, Model, Units_Sold
FROM (
    SELECT Year, Model, SUM(Units_Sold) AS Units_Sold,
           ROW_NUMBER() OVER (PARTITION BY Year ORDER BY SUM(Units_Sold) DESC) AS rn
    FROM bmw_sales_2020_2025
    GROUP BY Year, Model
) AS ranked
WHERE rn = 1;

-- 3. Cumulative revenue over the years
SELECT Year,
       SUM(Revenue_USD) AS yearly_revenue,
       SUM(SUM(Revenue_USD)) OVER (ORDER BY Year) AS cumulative_revenue
FROM bmw_sales_2020_2025
GROUP BY Year
ORDER BY Year;

-- 4. Average profit margin per region with ranking
SELECT Region, AVG(Profit_Margin) AS avg_profit_margin,
       RANK() OVER (ORDER BY AVG(Profit_Margin) DESC) AS rank_region
FROM bmw_sales_2020_2025
GROUP BY Region
ORDER BY rank_region;

-- 5. Model with highest net profit in each region
SELECT Region, Model, Net_Profit_USD
FROM (
    SELECT Region, Model, SUM(Net_Profit_USD) AS Net_Profit_USD,
           ROW_NUMBER() OVER (PARTITION BY Region ORDER BY SUM(Net_Profit_USD) DESC) AS rn
    FROM bmw_sales_2020_2025
    GROUP BY Region, Model
) AS ranked
WHERE rn = 1;

-- 6. Month-over-month revenue growth in 2023
SELECT Month,
       SUM(Revenue_USD) AS monthly_revenue,
       LAG(SUM(Revenue_USD)) OVER (ORDER BY FIELD(Month, 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')) AS prev_month,
       ROUND(
           (SUM(Revenue_USD) - LAG(SUM(Revenue_USD)) OVER (ORDER BY FIELD(Month, 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))) 
           / LAG(SUM(Revenue_USD)) OVER (ORDER BY FIELD(Month, 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')) * 100, 2
       ) AS revenue_growth_pct
FROM bmw_sales_2020_2025
WHERE Year = 2023
GROUP BY Month
ORDER BY FIELD(Month, 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');

-- 7. Models with ROI above average
SELECT Model, ROI
FROM bmw_sales_2020_2025
WHERE ROI > (SELECT AVG(ROI) FROM bmw_sales_2020_2025)
ORDER BY ROI DESC;

-- 8. Top 3 models by revenue in each year
SELECT Year, Model, SUM(Revenue_USD) AS total_revenue
FROM (
    SELECT Year, Model, SUM(Revenue_USD) AS SUM_Revenue_USD,
           ROW_NUMBER() OVER (PARTITION BY Year ORDER BY SUM(Revenue_USD) DESC) AS rn
    FROM bmw_sales_2020_2025
    GROUP BY Year, Model
) AS ranked
WHERE rn <= 3
GROUP BY Year, Model
ORDER BY Year, total_revenue DESC;

-- 9. Total revenue and average profit margin by region and power type
SELECT Region, Power,
       SUM(Revenue_USD) AS total_revenue,
       AVG(Profit_Margin) AS avg_profit_margin
FROM bmw_sales_2020_2025
GROUP BY Region, Power
ORDER BY Region, Power;


-- 10. Top 5 countries by cumulative net profit
SELECT Country, SUM(Net_Profit_USD) AS total_net_profit
FROM bmw_sales_2020_2025
GROUP BY Country
ORDER BY total_net_profit DESC
LIMIT 5;

-- 11. Difference between revenue and cost per model
SELECT Model,
       SUM(Revenue_USD) - SUM(Cost_USD) AS revenue_minus_cost
FROM bmw_sales_2020_2025
GROUP BY Model
ORDER BY revenue_minus_cost DESC;

-- 12. Average monthly units sold per model
SELECT Model, AVG(Units_Sold) AS avg_units_per_month
FROM bmw_sales_2020_2025
GROUP BY Model
ORDER BY avg_units_per_month DESC;

-- 13. Models with highest EBITDA margin each year
SELECT Year, Model, EBITDA_Margin
FROM (
    SELECT Year, Model, AVG(EBITDA_Margin) AS EBITDA_Margin,
           ROW_NUMBER() OVER (PARTITION BY Year ORDER BY AVG(EBITDA_Margin) DESC) AS rn
    FROM bmw_sales_2020_2025
    GROUP BY Year, Model
) AS ranked
WHERE rn = 1;

-- 14. Average profit margin per year and region
SELECT Year, Region, AVG(Profit_Margin) AS avg_profit_margin
FROM bmw_sales_2020_2025
GROUP BY Year, Region
ORDER BY Year, avg_profit_margin DESC;

-- 15. Models whose revenue is greater than overall average
SELECT Model, SUM(Revenue_USD) AS total_revenue
FROM bmw_sales_2020_2025
GROUP BY Model
HAVING SUM(Revenue_USD) > (SELECT AVG(Revenue_USD) FROM bmw_sales_2020_2025)
ORDER BY total_revenue DESC;

