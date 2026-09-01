import streamlit as st
import pandas as pd
import plotly.express as px
import os


# ============================================================
# KONFIGURASI
# ============================================================

st.set_page_config(
    page_title="E-Commerce Data Analytics",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "main_data.csv"
    )

    df = pd.read_csv(file_path)

    df["order_purchase_timestamp"] = pd.to_datetime(
        df["order_purchase_timestamp"],
        errors="coerce"
    )

    return df


df = load_data()


# ============================================================
# JUDUL DASHBOARD
# ============================================================

st.title("E-Commerce Data Analytics Dashboard")

st.markdown(
    """
    Dashboard ini menyajikan analisis performa transaksi
    dan kategori produk berdasarkan E-Commerce Public Dataset.
    """
)


# ============================================================
# FILTER PERIODE
# ============================================================

st.sidebar.header("Filter Data")

min_date = df["order_purchase_timestamp"].min().date()
max_date = df["order_purchase_timestamp"].max().date()

date_range = st.sidebar.date_input(
    "Periode Transaksi",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:

    start_date = pd.Timestamp(date_range[0])

    end_date = (
        pd.Timestamp(date_range[1])
        + pd.Timedelta(days=1)
    )

    filtered_df = df[
        (df["order_purchase_timestamp"] >= start_date)
        &
        (df["order_purchase_timestamp"] < end_date)
    ].copy()

else:

    filtered_df = df.copy()


# ============================================================
# KPI
# ============================================================

total_orders = filtered_df["order_id"].nunique()

total_customers = filtered_df["customer_id"].nunique()

total_revenue = filtered_df["revenue"].sum()

average_order_value = (
    total_revenue / total_orders
    if total_orders > 0
    else 0
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Pesanan",
        f"{total_orders:,}"
    )

with col2:
    st.metric(
        "Total Customer",
        f"{total_customers:,}"
    )

with col3:
    st.metric(
        "Total Nilai Transaksi",
        f"R$ {total_revenue:,.0f}"
    )

with col4:
    st.metric(
        "Rata-rata Transaksi",
        f"R$ {average_order_value:,.0f}"
    )


st.divider()


# ============================================================
# PERTANYAAN BISNIS 1
# ============================================================

st.header(
    "1. Perkembangan Nilai Transaksi dan Pesanan"
)

st.write(
    """
    Bagaimana perkembangan jumlah pesanan dan total nilai
    transaksi setiap bulan, dan bulan mana yang memiliki
    nilai transaksi tertinggi?
    """
)


monthly = (
    filtered_df
    .groupby("month")
    .agg(
        total_orders=("order_id", "nunique"),
        total_revenue=("revenue", "sum")
    )
    .reset_index()
)


# ============================================================
# GRAFIK NILAI TRANSAKSI
# ============================================================

fig_revenue = px.line(
    monthly,
    x="month",
    y="total_revenue",
    markers=True,
    title="Perkembangan Total Nilai Transaksi per Bulan"
)

fig_revenue.update_layout(
    xaxis_title="Bulan",
    yaxis_title="Total Nilai Transaksi (R$)"
)

st.plotly_chart(
    fig_revenue,
    use_container_width=True
)


# ============================================================
# GRAFIK JUMLAH PESANAN
# ============================================================

fig_orders = px.line(
    monthly,
    x="month",
    y="total_orders",
    markers=True,
    title="Perkembangan Jumlah Pesanan per Bulan"
)

fig_orders.update_layout(
    xaxis_title="Bulan",
    yaxis_title="Jumlah Pesanan"
)

st.plotly_chart(
    fig_orders,
    use_container_width=True
)


# ============================================================
# BULAN DENGAN NILAI TRANSAKSI TERTINGGI
# ============================================================

if not monthly.empty:

    highest_month = monthly.loc[
        monthly["total_revenue"].idxmax()
    ]

    st.success(
        f"Bulan dengan nilai transaksi tertinggi adalah "
        f"**{highest_month['month']}** dengan total "
        f"**R$ {highest_month['total_revenue']:,.2f}**."
    )


st.divider()


# ============================================================
# PERTANYAAN BISNIS 2
# ============================================================

st.header(
    "2. Kategori Produk dengan Nilai Transaksi Terbesar"
)

st.write(
    """
    Kategori produk apa yang menghasilkan nilai transaksi
    terbesar dan berapa besar kontribusinya terhadap total
    nilai transaksi?
    """
)


category = (
    filtered_df
    .groupby("product_category_name_english")
    .agg(
        total_revenue=("revenue", "sum"),
        total_orders=("order_id", "nunique")
    )
    .reset_index()
    .sort_values(
        "total_revenue",
        ascending=False
    )
)


category["contribution"] = (
    category["total_revenue"]
    / category["total_revenue"].sum()
    * 100
)


# ============================================================
# TOP 10 KATEGORI
# ============================================================

top10 = (
    category
    .head(10)
    .sort_values(
        "total_revenue",
        ascending=True
    )
)


fig_category = px.bar(
    top10,
    x="total_revenue",
    y="product_category_name_english",
    orientation="h",
    title="10 Kategori Produk dengan Nilai Transaksi Terbesar"
)

fig_category.update_layout(
    xaxis_title="Total Nilai Transaksi (R$)",
    yaxis_title="Kategori Produk"
)

st.plotly_chart(
    fig_category,
    use_container_width=True
)


# ============================================================
# KATEGORI DENGAN NILAI TRANSAKSI TERTINGGI
# ============================================================

if not category.empty:

    top_category = category.iloc[0]

    st.success(
        f"Kategori dengan nilai transaksi terbesar adalah "
        f"**{top_category['product_category_name_english']}** "
        f"dengan nilai transaksi sebesar "
        f"**R$ {top_category['total_revenue']:,.2f}**, "
        f"atau **{top_category['contribution']:.2f}%** "
        f"dari total nilai transaksi."
    )


st.divider()


# ============================================================
# DATA TRANSAKSI
# ============================================================

st.header("Data Transaksi")

display_columns = [
    "order_id",
    "customer_id",
    "order_purchase_timestamp",
    "product_id",
    "product_category_name_english",
    "price",
    "freight_value",
    "revenue",
    "month"
]

st.dataframe(
    filtered_df[display_columns]
    .sort_values(
        "order_purchase_timestamp",
        ascending=False
    ),
    use_container_width=True,
    hide_index=True
)


# ============================================================
# FOOTER
# ============================================================

st.caption(
    "E-Commerce Data Analytics | Proyek Analisis Data Dicoding"
)