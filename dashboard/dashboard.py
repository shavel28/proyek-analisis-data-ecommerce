import streamlit as st
import pandas as pd
import plotly.express as px
import os


# ============================================================
# KONFIGURASI HALAMAN
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

st.title("📊 E-Commerce Data Analytics Dashboard")

st.markdown(
    """
    Dashboard ini menyajikan hasil analisis data transaksi E-Commerce
    untuk memahami perkembangan penjualan dan kategori produk yang
    memberikan kontribusi terbesar terhadap nilai transaksi.
    """
)


# ============================================================
# SIDEBAR FILTER
# ============================================================

st.sidebar.header("Filter Data")


# Filter periode

min_date = df["order_purchase_timestamp"].min().date()
max_date = df["order_purchase_timestamp"].max().date()

date_range = st.sidebar.date_input(
    "Pilih Periode Transaksi",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)


# Filter kategori

categories = sorted(
    df["product_category_name_english"]
    .dropna()
    .unique()
)

selected_categories = st.sidebar.multiselect(
    "Pilih Kategori Produk",
    options=categories,
    default=categories
)


# ============================================================
# PROSES FILTER DATA
# ============================================================

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


# Filter kategori

filtered_df = filtered_df[
    filtered_df["product_category_name_english"]
    .isin(selected_categories)
]


# Jika tidak ada data

if filtered_df.empty:

    st.warning(
        "Tidak ada data yang tersedia berdasarkan filter yang dipilih."
    )

    st.stop()


# ============================================================
# KPI
# ============================================================

st.subheader("Ringkasan Data")


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
        "Total Pelanggan",
        f"{total_customers:,}"
    )


with col3:

    st.metric(
        "Total Nilai Transaksi",
        f"R$ {total_revenue:,.0f}"
    )


with col4:

    st.metric(
        "Rata-rata Nilai Pesanan",
        f"R$ {average_order_value:,.0f}"
    )


st.divider()


# ============================================================
# PERTANYAAN BISNIS 1
# ============================================================

st.header(
    "1. Perkembangan Nilai Transaksi dan Jumlah Pesanan"
)


st.write(
    """
    **Pertanyaan Bisnis:**

    Bagaimana perkembangan jumlah pesanan dan total nilai transaksi
    setiap bulan, serta bulan mana yang memiliki nilai transaksi tertinggi?
    """
)


# ============================================================
# ANALISIS BULANAN
# ============================================================

monthly = (
    filtered_df
    .groupby("month")
    .agg(
        total_orders=("order_id", "nunique"),
        total_revenue=("revenue", "sum")
    )
    .reset_index()
    .sort_values("month")
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
# INSIGHT PERTANYAAN BISNIS 1
# ============================================================

if not monthly.empty:

    highest_revenue_month = monthly.loc[
        monthly["total_revenue"].idxmax()
    ]

    highest_order_month = monthly.loc[
        monthly["total_orders"].idxmax()
    ]

    lowest_revenue_month = monthly.loc[
        monthly["total_revenue"].idxmin()
    ]

    st.success(
        f"""
### Insight

Nilai transaksi tertinggi terjadi pada **{highest_revenue_month['month']}**
dengan total nilai transaksi sebesar
**R$ {highest_revenue_month['total_revenue']:,.2f}**.

Jumlah pesanan tertinggi terjadi pada **{highest_order_month['month']}**
dengan total **{highest_order_month['total_orders']:,} pesanan**.

Sementara itu, nilai transaksi terendah terjadi pada
**{lowest_revenue_month['month']}** dengan total sebesar
**R$ {lowest_revenue_month['total_revenue']:,.2f}**.

Perbedaan antara bulan dengan jumlah pesanan tertinggi dan nilai transaksi
tertinggi menunjukkan bahwa banyaknya pesanan tidak selalu menghasilkan
nilai transaksi terbesar. Stakeholder dapat mengevaluasi kategori produk
dan pola pembelian pada periode dengan transaksi tertinggi untuk mengetahui
faktor yang mendorong peningkatan pendapatan.
"""
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
    **Pertanyaan Bisnis:**

    Kategori produk apa yang menghasilkan nilai transaksi terbesar
    dan berapa besar kontribusinya terhadap total nilai transaksi?
    """
)


# ============================================================
# ANALISIS KATEGORI PRODUK
# ============================================================

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


# Menghitung kontribusi

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


# ============================================================
# GRAFIK KATEGORI
# ============================================================

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
# TABEL TOP 10 KATEGORI
# ============================================================

st.subheader("Detail 10 Kategori Produk Teratas")

display_category = category.head(10).copy()

display_category["total_revenue"] = (
    display_category["total_revenue"]
    .round(2)
)

display_category["contribution"] = (
    display_category["contribution"]
    .round(2)
)

st.dataframe(
    display_category,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# INSIGHT PERTANYAAN BISNIS 2
# ============================================================

if not category.empty:

    top_category = category.iloc[0]

    second_category = category.iloc[1]

    st.success(
        f"""
### Insight

Kategori dengan nilai transaksi terbesar adalah
**{top_category['product_category_name_english']}**.

Kategori tersebut menghasilkan nilai transaksi sebesar
**R$ {top_category['total_revenue']:,.2f}** atau
**{top_category['contribution']:.2f}%** dari keseluruhan
nilai transaksi.

Kategori dengan nilai transaksi terbesar kedua adalah
**{second_category['product_category_name_english']}**
dengan nilai transaksi sebesar
**R$ {second_category['total_revenue']:,.2f}**.

Hasil ini menunjukkan bahwa kategori produk dengan kontribusi terbesar
memiliki peran penting terhadap pendapatan E-Commerce. Stakeholder dapat
memprioritaskan kategori tersebut dalam strategi promosi, pengelolaan stok,
dan pengembangan produk untuk mempertahankan atau meningkatkan pendapatan.
"""
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

st.divider()

st.markdown(
    """
    <div style="text-align: center; padding: 10px;">
        <p><b>E-Commerce Data Analytics Dashboard</b></p>
        </p>
        <p style="color: gray;">
            © 2026 Shava Selvia Ramadhani Subekti
        </p>
    </div>
    """,
    unsafe_allow_html=True
)