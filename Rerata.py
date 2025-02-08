# Program : Menghitung Rata-rata
# Programmer : Adedayesa Nurvitian
# Tanggal (v1.0) : 29 Januari 2025

nilai_list = []

for i in range(10):
    nilai = float(input(f"Masukkan nilai ke-{i+1} : "))
    nilai_list.append(nilai)

# Menghitung rata-rata
rata_rata = sum(nilai_list) / len(nilai_list)

# Menampilkan hasil rata-rata
print("Rata-rata nilai yang dimasukkan adalah : ", rata_rata)
