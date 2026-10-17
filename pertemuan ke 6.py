total_belanja = 0
jumlah_barang = 0
while True:
    harga = int(input("Masukan harga barang (ketik 0 untuk selesai): "))

    if harga == 0:
        break  #Selesai
    elif harga < 0:
        print("Peringatan: Harga tidak boleh negatif!")
    else:
        total_belanja += harga
        jumlah_barang += 1

print("|n--- RINGKASAN BELANJA ---")
print(f"Total Belanjaan : Rp{total_belanja}")
print(f"Jumlah Barang : {jumlah_barang} item")
