def hitung_rata_rata():
    # Pemetaan nilai huruf ke angka
    peta_nilai = {
        'A': 4.00,
        'A-': 3.75,
        'B+': 3.50,
        'B': 3.00,
        'B-': 2.75,
        'C+': 2.50,
        'C': 2.00,
        'C-': 1.75,
        'D': 1.50,
        'E': 1.25
    }
    
    total_nilai = 0.0
    jumlah_data = 0
    
    print("Masukkan nilai huruf satu per satu (tekan Enter tanpa isi nilai untuk selesai):")
    
    while True:
        input_huruf = input(f"Masukkan nilai ke-{jumlah_data + 1}: ").strip().upper()
        
        # Berhenti jika pengguna menekan Enter kosong
        if input_huruf == "":
            break
            
        if input_huruf in peta_nilai:
            total_nilai += peta_nilai[input_huruf]
            jumlah_data += 1
        else:
            print("Kategori huruf tidak valid, silakan coba lagi.")
            
    if jumlah_data > 0:
        rata_rata = total_nilai / jumlah_data
        print(f"\nTotal nilai angka: {total_nilai:.2f}")
        print(f"Jumlah mata kuliah: {jumlah_data}")
        print(f"Rata-rata nilai (IPK): {rata_rata:.2f}")
    else:
        print("\nTidak ada data nilai yang dimasukkan.")

# Memanggil fungsi
hitung_rata_rata()
