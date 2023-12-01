import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
 
filtered_customer = pd.read_csv("../dashboard/processed_data/filtered_customer.csv")
merge_customer = pd.read_csv("../dashboard/processed_data/merge_customer.csv")
rfm_data = pd.read_csv("../dashboard/processed_data/rfm_data.csv")

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