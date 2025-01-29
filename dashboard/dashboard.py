import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_data = pd.read_csv("data/data_1.csv")
hour_data = pd.read_csv("data/data_2.csv")

# Judul dashboard
st.title("📊 Bike Sharing Dashboard")
st.write("Analisis pola penggunaan sepeda berdasarkan waktu dan faktor cuaca.")

# Sidebar untuk filter
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim:", ["Semua", 1, 2, 3, 4])
selected_date_range = st.sidebar.date_input("Pilih Rentang Tanggal:", [])
selected_temp_range = st.sidebar.slider("Pilih Rentang Suhu:", float(day_data['temp'].min()), float(day_data['temp'].max()), (float(day_data['temp'].min()), float(day_data['temp'].max())))

# Filter berdasarkan musim jika dipilih
if selected_season != "Semua":
    day_data = day_data[day_data["season"] == selected_season]

# Filter berdasarkan suhu
day_data = day_data[(day_data['temp'] >= selected_temp_range[0]) & (day_data['temp'] <= selected_temp_range[1])]

# Menampilkan sekilas data jika dipilih
if st.checkbox("Tampilkan Dataframe"):
    st.write(day_data.head())

# Statistik ringkas
st.metric(label="Rata-rata Peminjaman", value=int(day_data['cnt'].mean()))
st.metric(label="Rata-rata Suhu", value=round(day_data['temp'].mean(), 2))

# Visualisasi penggunaan sepeda berdasarkan waktu
st.subheader("Pola Penggunaan Sepeda per Jam")
plt.figure(figsize=(10, 6))
sns.boxplot(x=hour_data['hr'].astype(str), y='cnt', data=hour_data)
plt.xlabel("Jam")
plt.ylabel("Jumlah Penggunaan Sepeda")
st.pyplot(plt)

# Visualisasi pengaruh suhu terhadap jumlah peminjaman
st.subheader("Pengaruh Suhu terhadap Penggunaan Sepeda")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=day_data, palette="coolwarm")
plt.xlabel("Suhu (Skala Normalisasi)")
plt.ylabel("Jumlah Penggunaan Sepeda")
st.pyplot(plt)

# Visualisasi pengaruh kelembaban terhadap peminjaman
st.subheader("Pengaruh Kelembaban terhadap Penggunaan Sepeda")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='hum', y='cnt', data=day_data, palette="coolwarm")
plt.xlabel("Kelembaban (%)")
plt.ylabel("Jumlah Penggunaan Sepeda")
st.pyplot(plt)

# Visualisasi pengaruh kecepatan angin
st.subheader("Pengaruh Kecepatan Angin terhadap Penggunaan Sepeda")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='windspeed', y='cnt', data=day_data, palette="coolwarm")
plt.xlabel("Kecepatan Angin (m/s)")
plt.ylabel("Jumlah Penggunaan Sepeda")
st.pyplot(plt)

st.write("---")
st.write("Dibuat oleh Muhammad Nasywan Sulthan Muyassar Arhata")
