#A
#HINT 1
print("Masukan data kamu dengan sesuai!")

#HINT 2
nama = input ("Masukan nama lengkap :")
alamat = input ("Masukan alamat/tempat tinggal :")
kampus = input ("Masukan Nama kampus :")
jurusan = input ("Masukan Jurusan kamu :")
gedung = input ("Dimana gedung kampus jurusan kamu :")

#HINT 3
print("\nBerikut data kamu!\n")
      
#HINT 4
print("\nHalo nama saya Ilha Wahyudin, Saya tinggal di Kabupaten Pandeglang, Saya berkuliah di Universitas Trisakti, Jurusan Sistem Informasi di gedung E, dan saya siap ikut praktikum algoritma dan pemrograman!\n")
       

#B
# HINT 1:
print("Hitung Luas Ruangan")

# HINT 2:
panjang = float(input("Masukkan Panjang Ruangan: "))
lebar = float(input("Masukkan Lebar Ruangan: "))
satuan = input("Masukkan Satuan (Meter/Inci): ")

# HINT 4:
luas = panjang * lebar

# HINT 5:
print(f"\nLuas ruangan dengan panjang  {panjang}  dan lebar  {lebar}  adalah  {luas}  {satuan}!\n")

#B
#HINT 1
nama = input("Masukkan nama kamu: ")
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))
bmi = berat / (tinggi ** 2)
print(f"{nama}, Skor BMI kamu adalah {bmi}")
