# Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis pola penggunaan sepeda berdasarkan data peminjaman sepeda yang tersedia di dataset bike sharing. Dataset ini mencakup data harian dan per jam, yang digunakan untuk mengeksplorasi bagaimana waktu (musim, hari, jam) dan cuaca (suhu, kelembaban, kecepatan angin) memengaruhi jumlah peminjaman sepeda.

## Menentukan Pertanyaan Bisnis
- **Pertanyaan 1**: Apa pola penggunaan sepeda berdasarkan waktu (jam, hari, atau musim)?
- **Pertanyaan 2**: Bagaimana cuaca memengaruhi jumlah peminjaman sepeda?

## Struktur Folder
```
submission/
├── dashboard/
│   ├── main_data.csv
│   └── dashboard.py
├── data/
│   ├── data_1.csv
│   └── data_2.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Cara Menjalankan Proyek

### 1. Install Dependencies
Jika menggunakan **virtual environment** (disarankan):
```bash
# Membuat dan mengaktifkan virtual environment
python -m venv env
source env/bin/activate   # di Linux/MacOS
env\Scripts\activate      # di Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Jalankan Streamlit Dashboard
```bash
streamlit run dashboard/dashboard.py
```

### 3. Menjalankan Jupyter Notebook
```bash
jupyter notebook notebook.ipynb
```

## Penjelasan File
- **`notebook.ipynb`**: Notebook ini berisi analisis eksplorasi data dan visualisasi terkait pola penggunaan sepeda berdasarkan cuaca dan waktu.
- **`dashboard.py`**: Aplikasi Streamlit yang menampilkan visualisasi interaktif berdasarkan analisis data yang dilakukan.
- **`requirements.txt`**: Daftar dependensi yang digunakan dalam proyek ini.
- **`data_1.csv` & `data_2.csv`**: Dataset yang digunakan untuk analisis.
- **`main_data.csv`**: Dataset utama yang digunakan untuk aplikasi Streamlit.
- **`url.txt`**: Berisi link ke aplikasi Streamlit yang sudah dideploy.

## Kesimpulan
- **Pertanyaan 1**: Pola penggunaan sepeda lebih tinggi selama musim panas dan gugur.
- **Pertanyaan 2**: Cuaca memiliki hubungan positif dengan jumlah penggunaan sepeda; semakin hangat, semakin banyak peminjaman sepeda.