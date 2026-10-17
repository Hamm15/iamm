#Latihan Pertama
for i in range(7, 0, -1):
    print(str(i) * i)

#Latihan Kedua
while True:
    bulan = int(input("Masukkan bulan (1-12): "))
    tahun = int(input("Masukkan tahun: "))

    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        jumlah_hari = 31
    elif bulan in [4, 6, 9, 11]:
        jumlah_hari = 30
    elif bulan == 2:
        if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
            jumlah_hari = 29
        else:
            jumlah_hari = 28
    else:
        print("Bulan tidak valid! Masukkan angka 1 sampai 12.\n")
        continue

    print(f"Jumlah hari pada bulan {bulan} tahun {tahun} adalah {jumlah_hari} hari.\n")

    ulang = input("Apakah ingin mengecek bulan lain? (y/t): ").lower()
    if ulang != 'y':
        print("Program selesai.")
        break
