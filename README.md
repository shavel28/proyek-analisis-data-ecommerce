
# E-Commerce Data Analytics

## Deskripsi

Proyek ini merupakan proyek analisis data menggunakan E-Commerce Public Dataset.

Analisis dilakukan untuk memahami perkembangan transaksi dan performa kategori produk selama periode September 2016 hingga Agustus 2018.

Proses analisis mencakup:
- Data Gathering
- Data Assessing
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Explanatory Analysis
- Analisis lanjutan
- Dashboard interaktif menggunakan Streamlit

## Pertanyaan Bisnis

### Pertanyaan 1

Bagaimana perkembangan jumlah pesanan dan total nilai transaksi setiap bulan, dan bulan mana yang memiliki nilai transaksi tertinggi?

### Pertanyaan 2

Kategori produk apa yang menghasilkan nilai transaksi terbesar dan berapa besar kontribusinya terhadap total nilai transaksi?

## Dataset

Dataset yang digunakan adalah E-Commerce Public Dataset.

Dataset terdiri dari:
- customers_dataset.csv
- geolocation_dataset.csv
- order_items_dataset.csv
- order_payments_dataset.csv
- order_reviews_dataset.csv
- orders_dataset.csv
- product_category_name_translation.csv
- products_dataset.csv
- sellers_dataset.csv

## Tools dan Library

Proyek ini menggunakan:
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit

## Struktur Folder

```text
submission/
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
├── dashboard/
│   ├── main_data.csv
│   └── dashboard.py
│
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
