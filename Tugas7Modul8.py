daftar_buku = [
    "978-602-03-1234-5, Pemrograman Python untuk Pemula, Andi Setiawan    , 10 , 50000 , 65000\n" ,
    "978-979-29-5678-9, Kalkulus Lanjut                , Dr. Rina Hartati , 7  , 70000 , 90000\n" ,
    "978-623-45-9876-2, Dasar-Dasar Statistik          , Budi Santoso     , 15 , 55000 , 75000\n" ,
    "978-602-45-1357-8, Sistem Basis Data              , Siti Nurhaliza   , 2  , 80000 , 100000\n",
    "978-979-40-2468-0, Algoritma dan Pemrograman      , Muhammad Fadli   , 12 , 60000 , 85000\n" ,
    "978-602-52-1111-3, Struktur Data                  , Rizky Pratama    , 8  , 65000 , 88000\n" ,
    "978-623-88-2222-4, Jaringan Komputer              , Dedi Firmansyah  , 3  , 75000 , 95000\n" ,
    "978-602-99-3333-1, Kecerdasan Buatan              , Lestari Dewi     , 9  , 90000 , 115000\n",
    "978-623-76-4444-7, Metode Penelitian Kuantitatif  , Tri Andayani     , 11 , 50000 , 70000\n" ,
    "978-602-88-5555-0, Pengantar Teknologi Informasi  , Agus Supriyanto  , 14 , 45000 , 60000\n"
]

with open ("Inventaris_Buku.txt","w") as file:
    for baris in daftar_buku:
        file.write(baris)

inventaris = { }
with open("Inventaris_Buku.txt","r") as file :
    for baris in file :
        karakter = ""
        kolom = [ ]
        for huruf in baris:
            if huruf == "," or huruf == "\n":
                kolom.append(karakter)
                karakter = ""
            else:
                karakter += huruf
        isbn = kolom[0]
        judul = kolom[1]
        penulis = kolom[2]
        stok = int(kolom[3])
        harga_beli = int(kolom[4])
        harga_jual = int(kolom[5])

        inventaris[isbn] = {
            "Judul": judul,
            "Penulis": penulis,
            "Stok":stok,
            "Harga Beli":harga_beli,
            "Harga Jual":harga_jual
        }

with open("laporan_inventaris.txt","w") as file:
    file.write("ISBN,Judul,Penulis,Stok,Harga Beli,Harga Jual,Potensi Keuntungan\n")
    for isbn in inventaris:
        data = inventaris[isbn]
        keuntungan=(data["Harga Jual"]-data["Harga Beli"])*data["Stok"]
        data["Potensi"] = keuntungan
        file.write(
            isbn + "," +
            data["Judul"] + "," +
            data["Penulis"] + "," +
            str(data["Stok"]) + "," +
            str(data["Harga Beli"]) + "," +
            str(data["Harga Jual"]) + "," +
            str(keuntungan) + "\n")
        
max_potensi = None
min_potensi = None
judul_max = ""
judul_min = ""

for isbn in inventaris:
    data = inventaris[isbn]
    potensi = data["Potensi"]
    if max_potensi is None or potensi > max_potensi:
        max_potensi = potensi
        judul_max = data["Judul"]
    if min_potensi is None or potensi < min_potensi:
        min_potensi = potensi
        judul_min = data["Judul"]

print("Buku dengan Potensi Keuntungan Tertinggi :")
print(judul_max,"(Rp",max_potensi,")")
print()
print("Buku dengan Potensi Keuntungan Terendah :")
print(judul_min,"(Rp",min_potensi,")")

total_nilai = 0
for isbn in inventaris:
    data = inventaris[isbn]
    total_nilai += data["Stok"] * data["Harga Beli"]

print("\n Total Nilai Inventaris: Rp",total_nilai)

print("\n Buku yang Perlu Restock(Stok < 5):")
for isbn in inventaris:
    data = inventaris[isbn]
    if data["Stok"] <5:
        print("-",data["Judul"],"(Stok:",data["Stok"],")")
