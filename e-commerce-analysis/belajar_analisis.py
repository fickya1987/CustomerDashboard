import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
 
filtered_customer = pd.read_csv("C:/Users/chint/Documents/GitHub/CustomerDashboard/e-commerce-analysis/E-commerce-public-dataset/E-Commerce Public Dataset/filtered_customer.csv")
merge_customer = pd.read_csv("C:/Users/chint/Documents/GitHub/CustomerDashboard/e-commerce-analysis/E-commerce-public-dataset/E-Commerce Public Dataset/merge_customer.csv")
rfm_data = pd.read_csv("C:/Users/chint/Documents/GitHub/CustomerDashboard/e-commerce-analysis/E-commerce-public-dataset/E-Commerce Public Dataset/rfm_data.csv")

top_5_city_key = filtered_customer["customer_city"].value_counts().nlargest(5).index.tolist()
top_5_city_value = filtered_customer["customer_city"].value_counts().nlargest(5).tolist()
bottom_5_city_key = filtered_customer["customer_city"].value_counts().tail(5).index.tolist()
bottom_5_city_value = filtered_customer["customer_city"].value_counts().tail(5).tolist()
repeater_key = filtered_customer['status'].value_counts().index.tolist()
repeater_value = filtered_customer['status'].value_counts().tolist()
top_5_general_key = merge_customer["product_category_name_english"].value_counts().nlargest(5).index.tolist()
top_5_general_value = merge_customer["product_category_name_english"].value_counts().nlargest(5).tolist()
bottom_5_general_key = merge_customer["product_category_name_english"].value_counts().tail(5).index.tolist()
bottom_5_general_value = merge_customer["product_category_name_english"].value_counts().tail(5).tolist()
top_5_repeater_key = merge_customer["product_category_name_english"].value_counts().nlargest(5).index.tolist()
top_5_repeater_value = merge_customer["product_category_name_english"].value_counts().nlargest(5).tolist()

st.title('Analisis Data E-Commerce')
st.header("Customer Behaviour")
st.subheader("Kota dengan Jumlah Pembeli Terbesar & Terkecil")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(65, 20))

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x=top_5_city_key, y=top_5_city_value, palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel('Nama Kota', fontsize=30)
ax[0].set_title('Top 5 - Kota dengan Jumlah Pembeli Terbesar', loc="center", fontsize=60)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(x=bottom_5_city_key, y=bottom_5_city_value, palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[0].set_xlabel('Nama Kota', fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title('Bottom 5 - Kota dengan Jumlah Pembeli Terkecil', loc="center", fontsize=60)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)

with st.expander("See Explanation"):
    st.write(
        """Pembeli terbesar pada platform E-Commerce ini berasal dari Sao Paulo, 
        diikuti dengan Rio de Janeiro, Belo Horizonte, Brasilia, dan Curitiba.
        """
    )

st.subheader("Repeat Customer")
fig1, ax1 = plt.subplots()
ax1.pie(repeater_value, labels=repeater_key, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=180)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

with st.expander("See Explanation"):
    st.write(
        """Jumlah Pembeli Repeater masih tergolong kecil, 3.1% dari keseluruhan pembeli yang ada.
        """
    )

st.subheader("Produk yang Paling Diminati")

fig2, ax2 = plt.subplots(nrows=1, ncols=2, figsize=(65, 20))

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x=top_5_general_key, y=top_5_general_value, palette=colors, ax=ax2[0])
ax2[0].set_ylabel(None)
ax2[0].set_xlabel('Nama Produk', fontsize=30)
ax2[0].set_title('Top 5 - Produk yang Diminati secara Umum', loc="center", fontsize=60)
ax2[0].tick_params(axis='y', labelsize=35)
ax2[0].tick_params(axis='x', labelsize=30)

sns.barplot(x=top_5_repeater_key, y=top_5_repeater_value, palette=colors, ax=ax2[1])
ax2[1].set_ylabel(None)
ax2[0].set_xlabel('Nama Produk', fontsize=30)
ax2[1].invert_xaxis()
ax2[1].yaxis.set_label_position("right")
ax2[1].yaxis.tick_right()
ax2[1].set_title('Bottom 5 - Produk yang Diminati oleh Repeater', loc="center", fontsize=60)
ax2[1].tick_params(axis='y', labelsize=35)
ax2[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig2)

with st.expander("See Explanation"):
    st.write(
        """Produk yang diminati oleh pembeli secara umum dengan pembeli repeater sama, 
        yakni Bed Bath Table, Health Beauty, Sports Leisure, Furniture Decor, dan 
        Computers Aceccories.
        """
    )

st.subheader("Produk yang Sedikit Diminati")
fig3, ax3 = plt.subplots(figsize=(20,10))

sns.barplot(y= bottom_5_general_value, x= bottom_5_general_key, palette=colors)
ax3.set_title("Produk Kurang Diminati", loc="center", fontsize=15)
ax3.set_ylabel("Jumlah Terjual")
ax3.set_xlabel("Nama Produk")
st.pyplot(fig3)

with st.expander("See Explanation"):
    st.write(
        """Sedangkan produk yang sedikit diminati adalah arts and craftmanship, cds dvds musicals, 
        la cuisine, fashion childern clothes, dan security and services. Penjualan barang ini dapat 
        ditingkatkan dengan paket bundling yang dipadukan dengan produk yang laris terjual.
        """
    )

st.subheader("Pelanggan Terbaik berdasarkan RFM Parameters (customer_unique_id)")

fig4, ax4 = plt.subplots(nrows=3, ncols=1, figsize=(30, 20))

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(y="recency", x="customer_id", data=rfm_data.sort_values(by="recency", ascending=True).head(5), palette=colors, ax=ax4[0])
ax4[0].set_ylabel("Besaran Value")
ax4[0].set_xlabel("Id Pelanggan")
ax4[0].set_title("By Recency (days)", loc="center", fontsize=18)
ax4[0].tick_params(axis ='x', labelsize=15)

sns.barplot(y="frequency", x="customer_id", data=rfm_data.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax4[1])
ax4[1].set_ylabel("Besaran Value")
ax4[1].set_xlabel("Id Pelanggan")
ax4[1].set_title("By Frequency", loc="center", fontsize=18)
ax4[1].tick_params(axis='x', labelsize=15)

sns.barplot(y="monetary", x="customer_id", data=rfm_data.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax4[2])
ax4[2].set_ylabel("Besaran Value")
ax4[2].set_xlabel("Id Pelanggan")
ax4[2].set_title("By Monetary", loc="center", fontsize=18)
ax4[2].tick_params(axis='x', labelsize=15)

st.pyplot(fig4)

with st.expander("See Explanation"):
    st.write(
        """Pelanggan terbaik berdasarkan:
        \n1) Recency adalah pelanggan dengan unique id "fb7e29c65321441231990afc201c1b14" yang transaksinya terjadi 50 hari yang lalu (menunjukkan transaksi terakhir dari pembeli).
        \n2) Monetary adalah pelanggan dengan unique id "da122df9eeddfedc1dc1f5349a1a690c" dengan besar nilai 7388 (menunjukkan total pembelian terbesar dari semua transaksi).
        \n3) Frequency adalah pelanggan dengan unique id "8d50f5eadf50201ccdcedfb9e2ac8455" dengan besar nilai 14 (menunjukkan transaksi terbanyak yang dilakukan oleh customer).
        """
    )
# # -*- coding: utf-8 -*-


# # Menyimpan Data Customer pada Variabel customers_df
# customers_df = pd.read_csv("C:/Users/chint/Documents/LearnCoding/PythonCode/e-commerce-analysis/E-commerce-public-dataset/E-Commerce Public Dataset/customers_dataset.csv")
# customers_df.head(2)

# # Pengecekan Data Customer
# print("Pengecekan Jumlah & Jenis Data:")
# customers_df.info()
# print("\nPengecekan Nilai NaN pada Data:")
# customers_df.isna().sum()

# # Pengecekan Duplikasi Data
# print("Jumlah duplikasi data: ", customers_df.duplicated().sum())

# # Pendeskripsian Data
# customers_df.describe(include="all")

# # Mengubah Tipe Data Menjadi String / Object
# customers_df.customer_zip_code_prefix = customers_df.customer_zip_code_prefix.astype(str)

# # Menyimpan Data Geolocation pada Variabel geolocations_df
# geolocations_df = pd.read_csv("C:/Users/chint/Documents/LearnCoding/PythonCode/e-commerce-analysis/E-commerce-public-dataset/E-Commerce Public Dataset/geolocation_dataset.csv")
# geolocations_df.head(2)

# # Pengecekan Data Geolocation
# print("Pengecekan Jumlah & Jenis Data:")
# geolocations_df.info()
# print("\nPengecekan Nilai NaN pada Data:")
# geolocations_df.isna().sum()

# # Pengecekan Duplikasi Data
# print("Jumlah duplikasi data: ", geolocations_df.duplicated().sum())

# # Pendeskripsian Data
# geolocations_df.describe(include="all")

# # Mengubah Tipe Data menjadi String / Object
# geolocations_df.geolocation_zip_code_prefix = geolocations_df.geolocation_zip_code_prefix.astype(str)

# # Menghapus Baris yang Mengandung Nilai Duplikat
# geolocations_df.drop_duplicates(inplace=True)

# # Menyimpan Data Order Item pada Variabel items_df
# items_df = pd.read_csv("C:/Users/chint/Documents/LearnCoding/PythonCode/e-commerce-analysis/E-commerce-public-dataset/E-Commerce Public Dataset/order_items_dataset.csv")
# items_df.head(2)

# # Pengecekan Data Order Item
# print("Pengecekan Jumlah & Jenis Data:")
# items_df.info()
# print("\nPengecekan Nilai NaN pada Data:")
# items_df.isna().sum()

# # Pengecekan Duplikasi Data
# print("Jumlah duplikasi data: ", items_df.duplicated().sum())

# # Pendeskripsian Data
# items_df.describe(include="all")

# # Mengubah Tipe Data menjadi Datetime
# items_df.shipping_limit_date = pd.to_datetime(items_df.shipping_limit_date)

# # Menyimpan Data Order Payment pada Variabel payments_df
# payments_df = pd.read_csv("C:/Users/chint/Documents/LearnCoding/PythonCode/e-commerce-analysis/E-commerce-public-dataset/E-Commerce Public Dataset/order_payments_dataset.csv")
# payments_df.head(2)

# # Pengecekan Data Order Payment
# print("Pengecekan Jumlah & Jenis Data:")
# payments_df.info()
# print("\nPengecekan Nilai NaN pada Data:")
# payments_df.isna().sum()

# # Pengecekan Duplikasi Data
# print("Jumlah duplikasi data: ", payments_df.duplicated().sum())

# # Pendeskripsian Data
# payments_df.describe(include="all")

# # Mengubah Tipe Data menjadi String / Object
# payments_df.payment_sequential = payments_df.payment_sequential.astype(str)

# # Menyimpan Data Order Review pada Variabel reviews_df
# reviews_df = pd.read_csv("C:/Users/chint/Documents/LearnCoding/PythonCode/e-commerce-analysis/E-commerce-public-dataset/E-Commerce Public Dataset/order_reviews_dataset.csv")
# reviews_df.head(2)

# # Pengecekan Data Order Review
# print("Pengecekan Jumlah & Jenis Data:")
# reviews_df.info()
# print("\nPengecekan Nilai NaN pada Data:")
# reviews_df.isna().sum()

# # Pengecekan Duplikasi Data
# print("Jumlah duplikasi data: ", reviews_df.duplicated().sum())

# # Pendeskripsian Data
# reviews_df.describe(include="all")

# # Mengubah Tipe Data menjadi Date Time
# datetime_columns = ["review_creation_date", "review_answer_timestamp"]

# for column in datetime_columns:
#   reviews_df[column] = pd.to_datetime(reviews_df[column])

# # Mengisi Sel yang Kosong dengan "Null"
# reviews_df.update(reviews_df[['review_comment_title','review_comment_message']].fillna("Null"))

# # Menyimpan Data Order pada Variabel orders_df
# orders_df = pd.read_csv("C:/Users/chint/Documents/LearnCoding/PythonCode/e-commerce-analysis/E-commerce-public-dataset/E-Commerce Public Dataset/orders_dataset.csv")
# orders_df.head(2)

# # Pengecekan Data Order
# print("Pengecekan Jumlah & Jenis Data:")
# orders_df.info()
# print("\nPengecekan Nilai NaN pada Data:")
# orders_df.isna().sum()

# # Pengecekan Duplikasi Data
# print("Jumlah duplikasi data: ", orders_df.duplicated().sum())

# # Pendeskripsian Data
# orders_df.describe(include="all")

# # Mengubah Tipe Data menjadi Date Time
# datetime_columns = ["order_purchase_timestamp", "order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date"]

# for column in datetime_columns:
#   orders_df[column] = pd.to_datetime(orders_df[column])

# # Menyimpan Data Product Category pada Variabel categories_df
# categories_df = pd.read_csv("C:/Users/chint/Documents/LearnCoding/PythonCode/e-commerce-analysis/E-commerce-public-dataset/E-Commerce Public Dataset/product_category_name_translation.csv")
# categories_df.head(2)

# # Pengecekan Data Product Category
# print("Pengecekan Jumlah & Jenis Data:")
# categories_df.info()
# print("\nPengecekan Nilai NaN pada Data:")
# categories_df.isna().sum()

# # Pengecekan Duplikasi Data
# print("Jumlah duplikasi data: ", categories_df.duplicated().sum())

# # Pendeskripsian Data
# categories_df.describe(include="all")

# # Menyimpan Data Product pada Variabel products_df
# products_df = pd.read_csv("C:/Users/chint/Documents/LearnCoding/PythonCode/e-commerce-analysis/E-commerce-public-dataset/E-Commerce Public Dataset/products_dataset.csv")
# products_df.head(2)

# # Pengecekan Data Product
# print("Pengecekan Jumlah & Jenis Data:")
# products_df.info()
# print("\nPengecekan Nilai NaN pada Data:")
# products_df.isna().sum()

# # Pengecekan Duplikasi Data
# print("Jumlah duplikasi data: ", products_df.duplicated().sum())

# # Pendeskripsian Data
# products_df.describe(include="all")

# # Melihat Kondisi Data
# products_df[products_df.isna()].info()

# # Karena semua data kosong, hapus semua baris data bernilai null
# products_df.dropna(inplace=True)

# # Menyimpan Data Seller pada Variabel sellers_df
# sellers_df = pd.read_csv("C:/Users/chint/Documents/LearnCoding/PythonCode/e-commerce-analysis/E-commerce-public-dataset/E-Commerce Public Dataset/sellers_dataset.csv")
# sellers_df.head(2)

# # Pengecekan Data Seller
# print("Pengecekan Jumlah & Jenis Data:")
# sellers_df.info()
# print("\nPengecekan Nilai NaN pada Data:")
# sellers_df.isna().sum()

# # Pengecekan Duplikasi Data
# print("Jumlah duplikasi data: ", sellers_df.duplicated().sum())

# # Pendeskripsian Data
# sellers_df.describe(include="all")

# # Mengubah Tipe Data menjadi String / Object
# sellers_df.seller_zip_code_prefix = sellers_df.seller_zip_code_prefix.astype(str)

# # Menunjukkan Semua Data
# customers_df.head(10)

# # Memfilter Data untuk Muncul Hanya Unique Customer
# filtered_customer = customers_df.drop_duplicates(subset=['customer_unique_id'], keep='first')
# filtered_customer.head(5)

# # Memahami City yang Memiliki Jumlah Customer Terbesar
# filtered_customer["customer_city"].value_counts().nlargest(5)

# top_5_city_key = filtered_customer["customer_city"].value_counts().nlargest(5).index.tolist()
# top_5_city_value = filtered_customer["customer_city"].value_counts().nlargest(5).tolist()
# bottom_5_city_key = filtered_customer["customer_city"].value_counts().tail(5).index.tolist()
# bottom_5_city_value = filtered_customer["customer_city"].value_counts().tail(5).tolist()

# # Menemukan Jumlah Customer yang Repeat Order
# counts = customers_df["customer_unique_id"].value_counts().tolist()
# filtered = filter(lambda count: count > 1, counts)
# print(f"Jumlah Customer yang Repeat Order Sebanyak: {len(list(filtered))}")

# repeater = customers_df["customer_unique_id"].value_counts()[customers_df["customer_unique_id"].value_counts() > 1]
# id_repeater = repeater.index.tolist()

# customers_df["status"] =""
# for index, row in customers_df.iterrows():
#   if customers_df["customer_unique_id"][index] in id_repeater:
#     row["status"] = "Repeater"
#   else:
#     row["status"] = "Non Repeater"

# # Mengetahui Distribusi Customer Repeater dan Tidak
# filtered_customer = customers_df.drop_duplicates(subset=['customer_unique_id'], keep='first')
# filtered_customer['status'].value_counts()

# repeater_key = filtered_customer['status'].value_counts().index.tolist()
# repeater_value = filtered_customer['status'].value_counts().tolist()

# items_df.head(5)

# orders_df.head(5)

# order_item = pd.merge(orders_df, items_df, on='order_id')
# order_item.head(5)

# # Memahami Macam Macam Status Order
# order_item["order_status"].unique()

# # Menyeleksi hanya yang berstatus delivered saja, karena statusnya selesai, sedangkan yang lainnya masih memungkinkan ada proses refund dlsb.
# filtered_order = order_item[order_item["order_status"] == "delivered"]

# # Mengelompokkan penjualan berdasarkan order_id
# group_filtered_order = filtered_order.groupby(by="order_id").agg({
#                           "order_item_id": "count",
#                           "price": "sum",
#                           "freight_value": "sum"
#                       })

# # Berapa Jumlah Barang yang Biasanya dibeli oleh Customer dalam sekali Transaksi?
# average_item = stats.mode(group_filtered_order["order_item_id"])
# average_item

# # Berapa Rerata Biaya yang dikeluarkan oleh Customer dalam sekali Transaksi?
# average_spent = np.average(group_filtered_order["price"])
# average_spent

# # Berapa Rerata Biaya Kirim yang dikeluarkan oleh Customer dalam sekali Transaksi?
# average_ongkir = np.average(group_filtered_order["freight_value"])
# average_ongkir

# # Menganalisis Hubungan antar Variabel
# group_filtered_order.corr()

# # Menggabungkan beberapa data
# merge_product = pd.merge(filtered_order, products_df, on='product_id')
# merge_categories = pd.merge(merge_product, categories_df, on='product_category_name')
# merge_customer = pd.merge(merge_categories, customers_df, on='customer_id')
# merge_categories.head(5)

# merge_customer = merge_customer[merge_customer["status"] == "Repeater"]

# # Produk yang paling banyak dibeli secara keseluruhan
# merge_categories["product_category_name_english"].value_counts().nlargest(5)

# # Produk yang paling sedikit dibeli secara keseluruhan
# merge_categories["product_category_name_english"].value_counts().tail(5)

# # Produk yang paling banyak dibeli oleh repeater
# merge_customer["product_category_name_english"].value_counts().nlargest(5)

# top_5_general_key = merge_categories["product_category_name_english"].value_counts().nlargest(5).index.tolist()
# top_5_general_value = merge_categories["product_category_name_english"].value_counts().nlargest(5).tolist()
# bottom_5_general_key = merge_categories["product_category_name_english"].value_counts().tail(5).index.tolist()
# bottom_5_general_value = merge_categories["product_category_name_english"].value_counts().tail(5).tolist()
# top_5_repeater_key = merge_customer["product_category_name_english"].value_counts().nlargest(5).index.tolist()
# top_5_repeater_value = merge_customer["product_category_name_english"].value_counts().nlargest(5).tolist()

# rfm_data = merge_customer.groupby(by="customer_unique_id", as_index=False).agg({
#     "order_purchase_timestamp": "max", # tanggal maksimal pembelian
#     "order_id": "nunique", # menghitung jumlah order
#     "price": "sum" # menghitung jumlah revenue yang dihasilkan
# })
# rfm_data.columns = ["customer_id", "max_order_timestamp", "frequency", "monetary"]

# # menghitung kapan terakhir pelanggan melakukan transaksi (hari)
# rfm_data["max_order_timestamp"] = rfm_data["max_order_timestamp"].dt.date
# recent_date = orders_df["order_purchase_timestamp"].dt.date.max()
# rfm_data["recency"] = rfm_data["max_order_timestamp"].apply(lambda x: (recent_date - x).days)

# rfm_data.drop("max_order_timestamp", axis=1, inplace=True)
# rfm_data.head()

# # Menampilkan dua figur sejajar
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,6))

# # Menampilkan 5 Kota dengan Jumlah Pembeli Terbesar di Bagian Kiri Subplot
# ax1.bar(top_5_city_key, top_5_city_value, color='green')
# ax1.set_xticklabels(top_5_city_key, rotation=45)
# ax1.set_xlabel('Nama Kota')
# ax1.set_ylabel('Jumlah Pembeli')
# ax1.set_title('Top 5 - Kota dengan Jumlah Pembeli Terbesar')

# # Menampilkan 5 Kota dengan Jumlah Pembeli Terkecil di Bagian Kanan Subplot
# ax2.bar(bottom_5_city_key, bottom_5_city_value, color='red')
# ax2.set_xticklabels(bottom_5_city_key, rotation=45)
# ax2.set_xlabel('Nama Kota')
# ax2.set_ylabel('Jumlah Pembeli')
# ax2.set_title('Bottom 5 - Kota dengan Jumlah Pembeli Terkecil')

# # Membuat Judul
# plt.suptitle("Kota dengan Jumlah Pembeli Terbesar & Terkecil", fontsize=20)

# # Menampilkan Visualisasi
# plt.show()

# plt.title('Distribusi Jumlah Pembeli')
# plt.pie(repeater_value, labels=repeater_key, colors=sns.color_palette('Set3'),
#         autopct='%1.1f%%', shadow=True, startangle=180)

# plt.axis('equal')
# plt.show()

# cmap = sns.diverging_palette(10, 220, as_cmap=True)
# # plt.matshow(group_filtered_order.corr(), color=cmap)
# # plt.show()

# sns.heatmap(
#     group_filtered_order.corr(),
#     cmap=cmap,
#     vmax=1,
#     vmin=-1,
#     center=0,
#     square=True,
#     linewidths=.5,
#     cbar_kws={"shrink": .5}
# )

# # Menampilkan dua figur sejajar
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,6))

# # Menampilkan 5 Produk Terlaris Secara Umum di Bagian Kiri Subplot
# ax1.bar(top_5_general_key, top_5_general_value, color='green')
# ax1.set_xticklabels(top_5_general_key, rotation=45)
# ax1.set_xlabel('Nama Produk')
# ax1.set_ylabel('Jumlah Terjual')
# ax1.set_title('Top 5 - Produk yang Diminati secara Umum')

# # Menampilkan 5 Produk Terlaris Bagi Repeater di Bagian Kanan Subplot
# ax2.bar(top_5_repeater_key, top_5_repeater_value, color='blue')
# ax2.set_xticklabels(top_5_repeater_key, rotation=45)
# ax2.set_xlabel('Nama Produk')
# ax2.set_ylabel('Jumlah Terjual')
# ax2.set_title('Bottom 5 - Produk yang Diminati oleh Repeater')

# # Membuat Judul
# plt.suptitle("Produk yang Paling Diminati", fontsize=20)

# # Menampilkan Visualisasi
# plt.show()

# plt.figure(figsize=(20, 5))

# sns.barplot(
#     y= bottom_5_general_value,
#     x= bottom_5_general_key
# )
# plt.title("Produk yang Kurang Diminati", loc="center", fontsize=15)
# plt.ylabel("Jumlah Terjual")
# plt.xlabel("Nama Produk")
# plt.tick_params(axis='x', labelsize=12)
# plt.show()

# fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(30, 20))

# colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]

# sns.barplot(y="recency", x="customer_id", data=rfm_data.sort_values(by="recency", ascending=True).head(5), palette=colors, ax=ax[0])
# ax[0].set_ylabel("Besaran Value")
# ax[0].set_xlabel("Id Pelanggan")
# ax[0].set_title("By Recency (days)", loc="center", fontsize=18)
# ax[0].tick_params(axis ='x', labelsize=15)

# sns.barplot(y="frequency", x="customer_id", data=rfm_data.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
# ax[1].set_ylabel("Besaran Value")
# ax[1].set_xlabel("Id Pelanggan")
# ax[1].set_title("By Frequency", loc="center", fontsize=18)
# ax[1].tick_params(axis='x', labelsize=15)

# sns.barplot(y="monetary", x="customer_id", data=rfm_data.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax[2])
# ax[2].set_ylabel("Besaran Value")
# ax[2].set_xlabel("Id Pelanggan")
# ax[2].set_title("By Monetary", loc="center", fontsize=18)
# ax[2].tick_params(axis='x', labelsize=15)

# plt.suptitle("Pelanggan Terbaik berdasarkan RFM Parameters (customer_unique_id)", fontsize=20)
# plt.show()

# #----------------------------------------------------------