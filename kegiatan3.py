import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam cm
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
ukuran_interval = 10  # Misalnya, interval ukuran per 10 cm

#TODO 1: Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def kelompok_tinggi(tinggi, ukuran_interval):
    return ukuran_interval * (tinggi // ukuran_interval)

# TODO 2: Menghitung frekuensi tinggi badan dalam interval
tinggi_interval = [kelompok_tinggi(tinggi, ukuran_interval) for tinggi in tinggi_badan]
frekuensi = {interval: tinggi_interval.count(interval) for interval in set(tinggi_interval)}

# TODO 3: Visualisasi data dalam bentuk histogram
plt.hist(tinggi_badan, bins=range(150, 191, ukuran_interval), edgecolor='none', color='blue', alpha=0.7, label='Data Tinggi Badan')

# TODO 4: Menambahkan kurva PDF pada hasil visualisasi data
mu, std = np.mean(tinggi_badan), np.std(tinggi_badan)

xmin, xmax = plt.xlim()
x = np.linspace(155, 185, 100)
pdf = norm.pdf(x, mu, std)

plt.plot(x, pdf * len(tinggi_badan) * ukuran_interval, 'r', linewidth=2, label='PDF Distribusi Normal')
# Menambahkan label pada sumbu x dan y
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Frekuensi')
plt.title('Histogram Tinggi Badan dan PDF Distribusi Normal')
plt.legend()
plt.show()