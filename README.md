# E-Commerce Data Analytics Dashboard

## Project Description

This project analyzes E-Commerce transaction data to understand transaction trends and identify product categories that contribute the most to the total transaction value.

The analysis uses the E-Commerce Public Dataset and includes several stages:

- Data Gathering
- Data Assessing
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Conclusion

The results of the analysis are presented through an interactive dashboard built using Streamlit.

---

## Dashboard

The interactive dashboard can be accessed through the following link:

🔗 **Streamlit Dashboard:**  
https://ecommerce-data-analytics.streamlit.app/

---

## Business Questions

1. How do the number of orders and total transaction value develop each month, and which month has the highest transaction value?

2. Which product category generates the largest transaction value, and how much does it contribute to the total transaction value?

---

## Project Structure

```text
submission/
│
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
│
├── data/
│   ├── customers_dataset.csv
│   ├── geolocation_dataset.csv
│   ├── order_items_dataset.csv
│   ├── order_payments_dataset.csv
│   ├── order_reviews_dataset.csv
│   ├── orders_dataset.csv
│   ├── product_category_name_translation.csv
│   ├── products_dataset.csv
│   └── sellers_dataset.csv
│
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt