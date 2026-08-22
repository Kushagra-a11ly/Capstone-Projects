📊 Customer Shopping Behaviour – End-to-End Data Analytics Project

A small, relational-style retail sales dataset built in Excel, structured as a **star schema** — one fact table (`Orders`) surrounded by three dimension tables (`Customers`, `Products`, `Dates`). It's designed for practicing Excel formulas (VLOOKUP/INDEX-MATCH, PivotTables), Power BI data modeling, or SQL-style joins.

## Schema Overview

```
Customers ──┐
            │
Products ───┼──> Orders (fact table)
            │
Dates ──────┘
```

Each row in `Orders` links out to `Customers`, `Products`, and `Dates` via shared key columns, so the four sheets can be joined into a single analytical view.

---

## Sheet Details

### 1. `Customers`
Dimension table describing who placed each order.

| Column | Type | Description |
|---|---|---|
| `CustomerID` | Text (PK) | Unique customer identifier, e.g. `C001` |
| `CustomerName` | Text | Full name of the customer |
| `City` | Text | Customer's city (Pune, Mumbai, Nashik, Nagpur, Thane) |
| `Segment` | Text | Customer segment — `Consumer`, `Corporate`, or `Home Office` |

**Rows:** 8 customers.

### 2. `Products`
Dimension table describing what was sold.

| Column | Type | Description |
|---|---|---|
| `ProductID` | Text (PK) | Unique product identifier, e.g. `P001` |
| `ProductName` | Text | Product name (Laptop, Mouse, Office Chair, etc.) |
| `Category` | Text | High-level category — `Electronics` or `Furniture` |
| `SubCategory` | Text | More granular grouping (Computers, Accessories, Chairs, Tables, Storage, Office Equipment) |
| `UnitPrice` | Number (₹) | Standard unit price of the product |

**Rows:** 8 products across 2 categories.

### 3. `Orders`
The **fact table** — one row per order line.

| Column | Type | Description |
|---|---|---|
| `OrderID` | Text (PK) | Unique order identifier, e.g. `O001` |
| `OrderDate` | Date | Date the order was placed |
| `CustomerID` | Text (FK → Customers) | Links to the customer who placed the order |
| `ProductID` | Text (FK → Products) | Links to the product ordered |
| `Quantity` | Number | Units ordered |
| `Sales` | Number (₹) | Total sale value for the order line |
| `PaymentMode` | Text | `UPI`, `Card`, or `Cash` |

**Rows:** 16 orders, dated between 5-Jan-2026 and 21-Apr-2026.

### 4. `Dates`
Dimension/calendar table, one row per distinct order date, useful for time-intelligence formulas and Power BI date tables.

| Column | Type | Description |
|---|---|---|
| `Date` | Date | Calendar date (matches an `OrderDate` in `Orders`) |
| `Year` | Number | Calendar year (2026) |
| `Month` | Text | Month name (January–April) |
| `MonthNo` | Number | Month number (1–4) |
| `Quarter` | Text | Fiscal/calendar quarter (`Q1` or `Q2`) |

**Rows:** 16 dates covering Q1 and Q2 2026.

---

## Relationships

| From | Key | To |
|---|---|---|
| `Orders.CustomerID` | → | `Customers.CustomerID` |
| `Orders.ProductID` | → | `Products.ProductID` |
| `Orders.OrderDate` | → | `Dates.Date` |

These are one-to-many relationships (one customer/product/date can have many orders), which makes this dataset ready to load directly into Power BI or Excel's Data Model without further cleanup.

---

## At a Glance

- **Total orders:** 16
- **Date range:** 5-Jan-2026 to 21-Apr-2026 (Q1–Q2 2026)
- **Customers:** 8, spread across Pune, Mumbai, Nashik, Nagpur, and Thane
- **Products:** 8, across Electronics (Computers, Accessories, Office Equipment) and Furniture (Chairs, Tables, Storage)
- **Payment modes:** UPI, Card, Cash
- **Highest single sale:** ₹55,000 (Laptop, appears in 3 separate orders)

---

## Suggested Uses

- **Excel practice:** VLOOKUP/INDEX-MATCH to pull `CustomerName` or `ProductName` into the `Orders` sheet; PivotTables to summarize sales by city, category, or month.
- **Power BI / data modeling:** Import all four sheets and build relationships as described above to create a working star schema.
- **SQL practice:** Treat each sheet as a table and practice `JOIN`, `GROUP BY`, and aggregate queries (total sales by segment, by category, by payment mode, etc.).
- **Dashboarding:** Build a sales-by-month, sales-by-category, or top-customers dashboard using the relationships above.

---

## Notes

- All monetary values are in Indian Rupees (₹).
- `Sales` in the `Orders` sheet is an exact match of `Quantity × UnitPrice` for every order — verified across all 16 rows, with no discounts or discrepancies.
- The `Dates` sheet duplicates each order date from `Orders`; deduplicate it first if you need a true one-row-per-calendar-day date table.
Open the Power BI file to view the dashboard.
Review the Gamma-generated PPT for final insights and recommendations.
