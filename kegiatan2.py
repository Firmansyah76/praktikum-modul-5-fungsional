import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga_produk, jumlah_terjual = zip(*[(harga, jumlah) for _, harga, jumlah in data_transaksi])

# Membuat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Scatter plot
ax1.scatter(harga_produk, jumlah_terjual, color='blue')
ax1.set_xlabel('Harga Produk')
ax1.set_ylabel('Jumlah Produk Terjual')
ax1.set_title('Scatter Plot Hubungan Harga Produk dan Jumlah Terjual')

# Hitung total pendapatan untuk setiap produk
total_pendapatan = list(map(lambda x: x[1] * x[2], data_transaksi))

# Bar chart untuk menyajikan pendapatan produk
produk_names = [produk for produk, _, _ in data_transaksi]
ax2.bar(produk_names, total_pendapatan, color='blue')
ax2.set_xlabel('Produk')
ax2.set_ylabel('Total Pendapatan')
ax2.set_title('Bar Chart Total Pendapatan per Produk')

plt.tight_layout()
plt.show()