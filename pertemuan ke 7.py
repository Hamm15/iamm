for baris in range(1, 11):
    for kolom in range(1, 11):
        print(baris * kolom, end="\t")
    print()

lama_parkir = int(input("Masukan lama parkir(dalam jam): "))

if lama_parkir <= 2:
    total_biaya = 5,000
else:
    total_biaya = 5,000 + (lama_parkir - 2) * 3,000

print("Total biaya parkir: Rp", total_biaya)
