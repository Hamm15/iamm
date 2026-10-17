n = 10
print (n > 5)
d = ("Universitas Trisakti")
x = int( input("Masukan Angka: "))

# Program ini mengubah suhu dari celsius ke fahrenheit atau sebaliknya
print("Ketik F untuk mengubah dari fahrenheit ke celsius")
print("Ketik C untuk mengubah dari celsius ke fahrenheit")

pilihan = input("Masukkan pilihan: ")
suhu = int(input("Masukkan suhu: "))

if pilihan == "F":
    c = (suhu - 32) * 5/9
    print(f"{suhu} derajat fahrenheit adalah {c} derajat celsius")
else:
    f = (suhu * 9/5) + 32
    print(f"{suhu} derajat celsius adalah {f} derajat fahrenheit")

if pilihan == "F":
    c = (suhu - 32) * 5/9
    print(f"{suhu} derajat fahrenheit adalah {c} derajat celsius")
else:
    if pilihan == "C":
        f = (suhu * 9/5) + 32
        print(f"{suhu} derajat celsius adalah {f} derajat fahrenheit")

if pilihan == "F":
    c = (suhu - 32) * 5/9
    print(f"{suhu} derajat fahrenheit adalah {c} derajat celsius")
else:
    if pilihan == "C":
        f = (suhu * 9/5) + 32
        print(f"{suhu} derajat celsius adalah {f} derajat fahrenheit")
    else:
        print("Pilihan tidak valid")


