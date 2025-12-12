# UrbanMart Sales Dashboard – Mini Project (Python + Streamlit)

## 📌 Project Overview
This mini‑project is designed for MAIB students to practice core Python programming and beginner‑level data analytics.  
You will build:

- A Python console script (`urbanmart_analysis.py`) for basic data exploration  
- A Streamlit web dashboard (`app.py`) for interactive retail insights  
- A CSV dataset (`urbanmart_sales.csv`) representing UrbanMart’s daily transactions  

The goal is to help UrbanMart’s management understand:

- Which product categories perform best  
- How sales vary across stores and days  
- Who their most valuable customers are  

---

## 🎯 Learning Objectives
By completing this project, you will practice:

### ✅ Python Fundamentals
- Variables, data types, operators  
- Lists, tuples, dictionaries  
- Loops and conditionals  
- Functions with parameters and return values  
- File handling (CSV reading)  
- Basic error handling (try/except)

### ✅ Data Analysis
- Using pandas for data manipulation  
- Creating new columns  
- Grouping and summarizing data  
- Preparing data for visualization  

### ✅ Dashboard Development (Streamlit)
- Sidebar filters  
- KPIs and metrics  
- Bar charts, line charts, tables  
- Interactive filtering  

---

## 📂 Project Structure

---

## 📝 Part 1 – Console Analysis (`urbanmart_analysis.py`)

Your script should:

### ✅ Load the CSV file  
Using either:
- Python’s built‑in csv module  
- pandas.read_csv()  

### ✅ Perform sanity checks  
- Total number of rows  
- Unique store IDs  
- Date range  

### ✅ Use Python data structures  
- List of product categories  
- Dictionary mapping store_id → store_location  
- Manual count of Online vs In‑store transactions  

### ✅ Implement a CLI menu  
Options:
1. Total revenue  
2. Revenue by store  
3. Top 5 products  
4. Exit  

Includes error handling for:
- Missing file  
- Invalid menu choice  

---

## 📊 Part 2 – KPI Functions

Implement functions such as:

- compute_total_revenue(df)  
- compute_revenue_by_store(df)  
- compute_top_n_products(df, n=5)  

---

## 📈 Part 3 – Data Preparation

Add new columns:

- line_revenue = quantity * unit_price - discount_applied  
- day_of_week extracted from the date  

Prepare summary tables:

- Revenue by category  
- Revenue by store  
- Revenue by channel  
- Top customers  

Optional:  
A filter_data() function for date, store, and channel filtering.

---

## 🌐 Part 4 – Streamlit Dashboard (`app.py`)

Your dashboard must include:

### ✅ Sidebar Filters
- Date range  
- Store location  
- Channel  
- Product category  

### ✅ KPIs
- Total revenue  
- Total transactions  
- Average revenue per transaction  
- Unique customers  

### ✅ Visualizations
- Revenue by category  
- Revenue by store  
- Daily revenue trend  
- Top 5 products  
- Top 5 customers  

### ✅ Raw Data Preview
st.dataframe(df_filtered.head(20))

---

## 📁 Dataset Description (`urbanmart_sales.csv`)

Each row represents one product in one bill.

Columns include:

- transaction_id, bill_id, date  
- store_id, store_location  
- customer_id, customer_segment  
- product_id, product_category, product_name  
- quantity, unit_price, discount_applied  
- payment_method, channel  

---

## 🧠 Reflection Questions

1. Which store location generates the highest revenue overall?  
2. Does online or in‑store channel generate more revenue in your filtered view?  
3. Which 3 product categories contribute the most revenue?  
4. What additional filter or feature would make this dashboard more useful for management?  

---

## 🚀 How to Run the Project

### 1. Install dependencies