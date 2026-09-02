````md
# E-Commerce Data Analytics Dashboard

## Project Description

This project is an end-to-end data analysis project using the Brazilian E-Commerce Public Dataset.

The project analyzes E-Commerce transaction data to understand sales performance, monthly transaction trends, and product category contributions to total transaction value.

The complete analysis process includes:

- Data Gathering
- Data Assessing
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Conclusion

The analysis results are presented through an interactive dashboard built using Streamlit.

---

## Business Questions

This project focuses on answering the following business questions:

1. How do the number of orders and total transaction value develop each month, and which month has the highest transaction value?

2. Which product category generates the largest transaction value, and how much does it contribute to the total transaction value?

---

## Dataset

This project uses the Brazilian E-Commerce Public Dataset provided for the Dicoding data analysis project.

The dataset contains information about:

- Customers
- Orders
- Order items
- Order payments
- Order reviews
- Products
- Sellers
- Geolocation
- Product category translations

The datasets are processed and combined to support the E-Commerce transaction analysis.

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
````

### Project Structure Explanation

* `dashboard/dashboard.py`
  Contains the source code for the interactive Streamlit dashboard.

* `dashboard/main_data.csv`
  Contains the processed data used by the Streamlit dashboard.

* `data/`
  Contains the original datasets used during the data analysis process.

* `notebook.ipynb`
  Contains the complete data analysis process, including data gathering, assessing, cleaning, exploratory data analysis, visualization, and conclusions.

* `requirements.txt`
  Contains the list of Python libraries required to run this project.

* `url.txt`
  Contains the link to the deployed Streamlit dashboard.

* `README.md`
  Contains project documentation and instructions for running the project.

---

## Streamlit Dashboard

The interactive dashboard can be accessed online through the following link:

### [Open E-Commerce Data Analytics Dashboard](https://ecommerce-data-analytics-shava.streamlit.app/)

> Replace the URL above with your actual Streamlit deployment URL.

The dashboard provides visualizations related to:

* Monthly order trends
* Monthly transaction value
* Sales performance
* Product category performance
* Product category contribution to total transaction value

---

# Installation Guide

Follow the instructions below to run this project on your local computer.

## Prerequisites

Before running this project, make sure the following software is installed:

* Python
* Git
* pip

You can check your Python version by running:

```bash
python --version
```

---

# 1. Clone the Repository

Clone this repository to your local computer using Git:

```bash
git clone https://github.com/shavel28/proyek-analisis-data-ecommerce.git
```

Move into the project directory:

```bash
cd proyek-analisis-data-ecommerce
```

---

# 2. Setup Virtual Environment

It is recommended to use a virtual environment to isolate the project dependencies.

Create a virtual environment using:

```bash
python -m venv venv
```

This command will create a folder named `venv` containing the virtual environment.

---

# 3. Activate Virtual Environment

Activate the virtual environment based on the terminal you are using.

## Windows Command Prompt

```bash
venv\Scripts\activate
```

## Git Bash

```bash
source venv/Scripts/activate
```

## PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

After successfully activating the virtual environment, the terminal should display something similar to:

```text
(venv)
```

---

# 4. Install Required Libraries

Install all required Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This command will automatically install all dependencies required by the project.

The main libraries used in this project include:

* pandas
* numpy
* matplotlib
* plotly
* streamlit

The complete list and version of the required libraries can be found in:

```text
requirements.txt
```

Using `requirements.txt` is recommended to ensure that all required dependencies are installed correctly.

---

# 5. Run the Streamlit Dashboard

Make sure that the virtual environment is still active.

Run the dashboard using the following command:

```bash
streamlit run dashboard/dashboard.py
```

After running the command, Streamlit will start the application.

The terminal will display information similar to:

```text
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

Open the Local URL in your browser:

```text
http://localhost:8501
```

The E-Commerce Data Analytics Dashboard will then be displayed.

---

# How to Use the Dashboard

After successfully running the dashboard, users can explore the available visualizations and analysis results.

## Monthly Sales Analysis

This section displays information about:

* Number of orders each month
* Total transaction value each month
* Monthly transaction trends
* Sales performance over time

Users can use this information to understand how E-Commerce transactions change from month to month.

---

## Product Category Analysis

This section displays information about product category performance.

Users can view:

* Product categories with high sales performance
* Categories with the largest transaction value
* Comparison between product categories
* Contribution of product categories to total transaction value

---

## Data Visualization

The dashboard presents the analysis results using interactive visualizations.

The visualizations help users understand:

* Sales trends
* Order trends
* Transaction value
* Product category performance

---

# Analysis Process

## 1. Data Gathering

The datasets used in this project are collected from the Brazilian E-Commerce Public Dataset.

Several datasets are used to obtain complete information about E-Commerce transactions.

The main datasets include:

* Orders dataset
* Order items dataset
* Products dataset
* Product category translation dataset

---

## 2. Data Assessing

The datasets are examined to identify potential data quality issues.

The assessment process includes:

* Checking dataset structure
* Checking data types
* Checking missing values
* Checking duplicated data
* Identifying inconsistent values

---

## 3. Data Cleaning

After identifying potential data quality issues, the datasets are cleaned before analysis.

The cleaning process includes:

* Handling missing values
* Removing duplicate data
* Converting data types
* Preparing transaction data for analysis

---

## 4. Exploratory Data Analysis

The exploratory data analysis is divided into several sections based on the purpose of the analysis.

### Sales Data Overview

Provides general information about the processed sales data, including:

* Number of transactions
* Number of orders
* Number of customers
* Analysis period

### Sales Value Distribution

Analyzes the distribution of transaction values using:

* Descriptive statistics
* Histogram
* Boxplot

### Product Category Analysis

Analyzes product categories to identify categories with the highest number of purchased items.

### Numerical Variable Analysis

Analyzes the relationship between numerical variables:

* Price
* Freight value
* Sales value

The relationship between variables is visualized using a correlation heatmap.

### Monthly Sales Analysis

Analyzes:

* Number of orders per month
* Total transaction value per month
* Monthly transaction trends
* Sales performance over time

### Product Category Contribution Analysis

Analyzes product categories based on:

* Total orders
* Total transaction value
* Contribution percentage to total transaction value

---

# Dashboard Features

The Streamlit dashboard provides the following features:

* Monthly order visualization
* Monthly transaction value visualization
* Sales trend analysis
* Product category performance analysis
* Product category contribution analysis
* Interactive data visualization
* Business insights based on the analysis results

---

# Requirements

The required Python libraries are listed in:

```text
requirements.txt
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Do not install each library manually unless necessary. Installing directly from `requirements.txt` ensures that the required dependencies for the project are installed together.

---

# Complete Commands

For easier setup, the complete commands to run this project are:

```bash
git clone https://github.com/shavel28/proyek-analisis-data-ecommerce.git

cd proyek-analisis-data-ecommerce

python -m venv venv
```

Activate the virtual environment.

For Windows CMD:

```bash
venv\Scripts\activate
```

For Git Bash:

```bash
source venv/Scripts/activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit dashboard:

```bash
streamlit run dashboard/dashboard.py
```

Open the dashboard in your browser using:

```text
http://localhost:8501
```

---

# Author

**Shava Selvia Ramadhani Subekti**

Dicoding Username: **shavel28**

Project Submission for:

**Belajar Fundamental Analisis Data**

Dicoding Academy

````

URL Streamlit : https://ecommerce-data-analytics-shava.streamlit.app/

