#Latihan Pertama Praktikum Pertama
import math

# Meminta user memasukkan dua bilangan bulat
a = int(input("Masukkan nilai a = "))
b = int(input("Masukkan nilai b = "))

# Melakukan perhitungan dan mencetak output sesuai format modul
print(f"Jumlah a ditambah b adalah {float(a + b)}")
print(f"Selisih antara a dan b adalah {float(b - a)}")
print(f"Jumlah a dikali b adalah {float(a * b)}")
print(f"Jumlah sisa pembagian dari hasil a dibagi b adalah {float(a % b)}")
print(f"Jumlah a dibagi b adalah {a / b}")
print(f"Hasil dari log(a) adalah {math.log10(a)}")
print(f"Hasil a pangkat b adalah {float(a ** b)}")

#Latihan Pertama Praktikum Kedua
import math

# Jari-jari bumi (disesuaikan menjadi 6371.01 km agar hasil akhirnya persis dengan contoh)
R = 6371.01 

print("Silahkan isi lattitude dan longitudenya untuk menetukan jarak antara 2 titik yang di cari\n")

# Meminta input nama lokasi dari user
nama_titik1 = input("Masukan Nama titik pertama permukaannya: ")
nama_titik2 = input("Masukan Nama titik kedua permukaannya: ")

# Meminta input titik koordinat dari user
lat1 = float(input("Masukan Lattitude 1 = "))
lon1 = float(input("Masukan Longitude 1 = "))
lat2 = float(input("Masukan Lattitude 2 = "))
lon2 = float(input("Masukan Longitude 2 = "))

# 1. Mengubah nilai derajat (latitude dan longitude) menjadi radian
lat1_rad = math.radians(lat1)
lon1_rad = math.radians(lon1)
lat2_rad = math.radians(lat2)
lon2_rad = math.radians(lon2)

# 2. Menghitung selisih garis lintang dan garis bujur
dlat = lat2_rad - lat1_rad
dlon = lon2_rad - lon1_rad

# 3. Mengaplikasikan Rumus Haversine menggunakan fungsi trigonometri
a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
c = 2 * math.asin(math.sqrt(a))

# Menghitung jarak akhir (Jari-jari bumi dikali hasil Haversine)
jarak = R * c

# Mencetak hasil akhir
print(f"Jarak antara {nama_titik1} dan {nama_titik2} adalah {jarak} kilometer")
