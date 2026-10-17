def cek_jenis_segitiga():
    print("=== PROGRAM MENCEK JENIS SEGITIGA ===")
    
    # Input tiga panjang sisi
    a = float(input("Masukkan panjang sisi 1 (a): "))
    b = float(input("Masukkan panjang sisi 2 (b): "))
    c = float(input("Masukkan panjang sisi 3 (c): "))

    # 1. Validasi apakah ketiga sisi dapat membentuk segitiga
    if (a + b > c) and (a + c > b) and (b + c > a):
        # 2. Cek jenis segitiga jika valid
        if a == b == c:
            print("Jenis Segitiga: Sama Sisi")
        elif a == b or a == c or b == c:
            print("Jenis Segitiga: Sama Kaki")
        else:
            print("Jenis Segitiga: Sembarang")
    else:
        print("Tidak mungkin membentuk segitiga")

# Jalankan fungsi
cek_jenis_segitiga()
