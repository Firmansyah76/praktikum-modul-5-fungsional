import matplotlib.pyplot as plt
from functools import reduce

# Data nilai-nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# Menghitung rata-rata menggunakan fungsi reduce
rata_rata = reduce(lambda x, y: x + y, nilai_mahasiswa) / len(nilai_mahasiswa)
print("Rata-rata nilai mahasiswa:", rata_rata)

# Membuat label mahasiswa (sumbu x) dalam bentuk fungsional dinamis (list-map-lambda)
label_mahasiswa = list(map(lambda i: f"{i+1}", range(len(nilai_mahasiswa))))

# Membuat DataFrame dengan nilai-nilai mahasiswa dan rata-rata
print("Rata-rata nilai mahasiswa:", rata_rata)


# Visualisasi data dalam bentuk diagram batang
plt.figure(figsize=(8, 6))
plt.bar(label_mahasiswa, nilai_mahasiswa, color='blue', label='Nilai Mahasiswa')
plt.axhline(y=rata_rata, color='red', linestyle='--', label=f'Rata-rata: {rata_rata:.2f}')
plt.xlabel('Mahasiswa')
plt.ylabel('Nilai')
plt.title('Diagram Batang Nilai Mahasiswa')
plt.legend()
plt.tight_layout()

# Menampilkan plot
plt.show()