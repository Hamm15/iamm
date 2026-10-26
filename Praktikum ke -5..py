def hitung_tiket_kebun_binatang():
    total_harga = 0.0
    jumlah_pengunjung = 0

    print("=== PROGRAM PENGHITUNG TIKET KEBUN BINATANG ===")
    print("Masukkan umur pengunjung satu per satu.")
    print("Tekan Enter tanpa mengisi umur untuk mengakhiri input.\n")

    # Perulangan untuk menginput umur pengunjung secara berulang
    while True:
        input_umur = input(
            f"Masukkan umur pengunjung ke-{jumlah_pengunjung + 1}: "
        ).strip()

        # Jika pengguna menekan Enter (string kosong), perulangan selesai
        if input_umur == "":
            break

        # Memastikan input berupa angka
        if not input_umur.isdigit():
            print("Input tidak valid! Harap masukkan angka umur yang benar.")
            continue

        umur = int(input_umur)

        # Pengondisian penentuan harga tiket berdasarkan umur
        if umur <= 2:
            harga = 0
        elif 3 <= umur <= 12:
            harga = 14
        elif umur >= 65:
            harga = 18
        else:
            harga = 23  # Kategori normal (13 - 64 tahun)

        total_harga += harga
        jumlah_pengunjung += 1
        print(f"Harga tiket untuk umur {umur} tahun: ${harga}")

    # Menampilkan ringkasan tagihan
    print("\n" + "=" * 40)
    print(f"Total pengunjung : {jumlah_pengunjung} orang")
    print(f"Total biaya tiket: ${total_harga:.2f}")
    print("=" * 40)

    # Memproses pembayaran jika ada tagihan
    if total_harga > 0:
        while True:
            try:
                uang_dibayar = float(
                    input("\nMasukkan jumlah uang pembayaran ($): ")
                )

                if uang_dibayar < total_harga:
                    kekurangan = total_harga - uang_dibayar
                    print(
                        f"Uang Anda kurang ${kekurangan:.2f}! Silakan masukkan nominal yang cukup."
                    )
                else:
                    kembalian = uang_dibayar - total_harga
                    print("\n=== PEMBAYARAN BERHASIL ===")
                    print(f"Uang Dibayar : ${uang_dibayar:.2f}")
                    print(f"Total Biaya  : ${total_harga:.2f}")
                    print(f"Kembalian    : ${kembalian:.2f}")
                    print("Terima kasih telah berkunjung!")
                    break
            except ValueError:
                print("Harap masukkan nominal uang berupa angka!")
    else:
        print("\nSemua pengunjung gratis! Tidak perlu melakukan pembayaran.")


# Jalankan fungsi utama
hitung_tiket_kebun_binatang()
