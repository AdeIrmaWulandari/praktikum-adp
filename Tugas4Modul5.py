jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa praktikum Adp :"))
nama_mahasiswa = [ ]
nilai_akhir_mahasiswa = [ ]

for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa ke-{i+1}")
    nama=input("Nama : ")
    pretest = float(input("Nilai pretest : "))
    posttest = float(input("Nilai posttest : "))
    makalah = float(input("Nilai makalah : "))
    nilai_akhir = 0.4 * pretest + 0.4 * posttest + 0.2 * makalah
    nama_mahasiswa.append(nama)
    nilai_akhir_mahasiswa.append(nilai_akhir)

print("\n TABEL NILAI AKHIR MAHASISWA")
print("-------------------------------")
print("Nama Mahasiswa \t\t Nilai Akhir")
print("-------------------------------")

for i in range (jumlah_mahasiswa):
    print(f"{nama_mahasiswa[i]}\t\t{nilai_akhir_mahasiswa[i] : .1f}")
total = 0
for nilai in nilai_akhir_mahasiswa:
    total += nilai
rata_rata = total / jumlah_mahasiswa
print(f"\nRata-rata nilai akhir kelas adalah: {rata_rata:.1f}")

Nilai_tertinggi = nilai_akhir_mahasiswa[0]
Nilai_terendah = nilai_akhir_mahasiswa[0]
for nilai in nilai_akhir_mahasiswa:
    if nilai > Nilai_tertinggi:
        Nilai_tertinggi = nilai
    if nilai < Nilai_terendah:
        Nilai_terendah = nilai


print("\nMahasisswa dengan nilai tertinggi adalah :")
for i in range (jumlah_mahasiswa) : 
    if nilai_akhir_mahasiswa[i] == Nilai_tertinggi :
        print(f"({nama_mahasiswa[i]}) dengan nilai ({nilai_akhir_mahasiswa[i]:.1f})")
print("\nMahasiswa dengan nilai terendah adalah : ")
for i in range (jumlah_mahasiswa) :
    if nilai_akhir_mahasiswa[i] == Nilai_terendah :
        print(f"({nama_mahasiswa[i]}) dengan nilai ({nilai_akhir_mahasiswa[i]:.1f})")
print("\nMahasiswa dengan nilai di atas rata-rata adalah :")
for i in range (jumlah_mahasiswa) :
    if nilai_akhir_mahasiswa[i] > rata_rata:
        print(f"({nama_mahasiswa[i]}) dengan nilai ({nilai_akhir_mahasiswa[i]:.1f})")
