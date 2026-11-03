def is_kabisat(tahun):
    """
    Fungsi untuk mengecek apakah tahun merupakan tahun kabisat.
    Mengembalikan True jika kabisat, False jika bukan.
    """
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    return False

def hitung_hari(bulan, tahun=None):
    """
    Fungsi untuk menentukan jumlah hari dalam suatu bulan.
    """
    # Bulan dengan 31 hari: Jan, Mar, Mei, Jul, Ags, Okt, Des
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # Bulan dengan 30 hari: Apr, Jun, Sep, Nov
    elif bulan in [4, 6, 9, 11]:
        return 30
    # Bulan Februari (bulan 2)
    elif bulan == 2:
        if is_kabisat(tahun):
            return 29
        else:
            return 28
    return 0

def main():
    print("Program ini akan menentukan jumlah hari dalam bulan tertentu")
    
    while True:
        print("Masukkan 0 untuk menghentikan program")
        bulan = int(input("masukkan bulan (1-12): "))
        
        if bulan == 0:
            print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
            break
            
        if 1 <= bulan <= 12:
            if bulan == 2:
                tahun = int(input("masukkan tahun (e.g., 2021): "))
                hari = hitung_hari(bulan, tahun)
            else:
                hari = hitung_hari(bulan)
                
            print(f"{hari} hari dalam sebulan")
        else:
            print("Bulan tidak valid! Masukkan angka antara 1 sampai 12.")

# Jalankan program utama
main()
