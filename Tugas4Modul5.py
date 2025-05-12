jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa praktikum Adp :"))
mahasiswa = [ ]
for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa ke-{i+1}")
    nama=input("Nama : ")
    pretest = float(input("Nilai pretest : "))
    posttest = float(input("Nilai posttest : "))
    makalah = float(input("Nilai makalah : "))
    nilai_akhir = 0.4 * pretest + 0.4 * posttest + 0.2 * makalah
    mahasiswa.append([nama,nilai_akhir])

print("\n TABEL NILAI AKHIR MAHASISWA")
print("-------------------------------")
print("Nama Mahasiswa \t Nilai Akhir")
print("-------------------------------")

for m in mahasiswa:
    print(f"{m[0]}\t\t{m[1] : .1f}")
total=0
for m in mahasiswa:
    total += m[1]
rata_rata = total / jumlah_mahasiswa
print(f"\nRata-rata nilai akhir kelas adalah :{rata_rata: .1f} ")

Nilai_tertinggi = mahasiswa [0][1]
Nilai_terendah = mahasiswa [0][1]
for m in mahasiswa :
    if m[1] > Nilai_tertinggi:
        Nilai_tertinggi = m[1]
    if m[1] < Nilai_terendah:
        Nilai_terendah = m[1]

print("\nMahasisswa dengan nilai tertinggi adalah :")
for m in mahasiswa : 
    if m[1] == Nilai_tertinggi :
        print(f"({m[0]}) dengan nilai ({m[1]:.1f})")
print("\nMahasiswa dengan nilai terendah adalah : ")
for m in mahasiswa :
    if m[1] == Nilai_terendah :
        print(f"({m[0]}) dengan nilai ({m[1]:.1f})")
print("\nMahasiswa dengan nilai di atas rata-rata adalah :")
for m in mahasiswa :
    if m[1] > rata_rata:
        print(f"({m[0]}) dengan nilai ({m[1]:.1f})")
