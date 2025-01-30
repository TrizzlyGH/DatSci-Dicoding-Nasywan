import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# Load dataset
day_data = pd.read_csv("data/data_1.csv")
hour_data = pd.read_csv("data/data_2.csv")

# Convert date column to datetime format
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Map categorical data to more informative labels
season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
weather_map = {1: 'Clear', 2: 'Mist', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow'}

day_data['season'] = day_data['season'].map(season_map)
day_data['weathersit'] = day_data['weathersit'].map(weather_map)

# Judul dashboard
st.title("📊 Bike Sharing Dashboard")
st.write("Analisis pola penggunaan sepeda berdasarkan waktu dan faktor cuaca.")

# Sidebar untuk filter
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim:", ["Semua"] + list(season_map.values()))
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

# Visualisasi distribusi jumlah peminjaman
st.subheader("Distribusi Jumlah Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(day_data['cnt'], bins=30, kde=True, ax=ax)
st.pyplot(fig)

# Visualisasi penggunaan sepeda berdasarkan musim
st.subheader("Jumlah Penyewa Berdasarkan Musim")
fig, ax = plt.subplots()
sns.barplot(data=day_data, x="season", y="cnt", ax=ax, ci=None)
st.pyplot(fig)

# Visualisasi pengaruh cuaca terhadap peminjaman
st.subheader("Jumlah Penyewa Berdasarkan Cuaca")
fig, ax = plt.subplots()
sns.boxplot(data=day_data, x="weathersit", y="cnt", ax=ax)
st.pyplot(fig)

# Visualisasi penggunaan sepeda berdasarkan waktu
st.subheader("Pola Penggunaan Sepeda per Jam")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x=hour_data['hr'].astype(str), y='cnt', data=hour_data, ax=ax)
st.pyplot(fig)

# Visualisasi tren penyewaan sepeda per hari
st.subheader("Tren Penyewaan Sepeda per Hari")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=day_data, x="dteday", y="cnt", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Visualisasi pengaruh suhu terhadap jumlah peminjaman
st.subheader("Pengaruh Suhu terhadap Penggunaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=day_data, palette="coolwarm", ax=ax)
st.pyplot(fig)

# Visualisasi pengaruh kelembaban terhadap peminjaman
st.subheader("Pengaruh Kelembaban terhadap Penggunaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='hum', y='cnt', data=day_data, palette="coolwarm", ax=ax)
st.pyplot(fig)

# Visualisasi pengaruh kecepatan angin terhadap peminjaman
st.subheader("Pengaruh Kecepatan Angin terhadap Penggunaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='windspeed', y='cnt', data=day_data, palette="coolwarm", ax=ax)
st.pyplot(fig)

# Visualisasi korelasi antar variabel
st.subheader("Heatmap Korelasi Antar Variabel")
fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(day_data.select_dtypes(include=['number']).corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

# Statistik ringkas (data akhir setelah filter)
st.write("**Statistik Data Setelah Filter:**")
st.write(day_data.describe())

st.write("---")
st.write("Dibuat oleh Muhammad Nasywan Sulthan Muyassar Arhata")