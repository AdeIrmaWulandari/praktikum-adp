while True :
    jumlah_baris = int(input("Masukkan jumlah baris kursi (minimal 4): "))
    kolom_kursi = int(input("Masukkan kolom kursi (minimal 4): "))
    if jumlah_baris >= 4 and kolom_kursi >= 4 :
        print("ukuran bioskop adalah",jumlah_baris,'x',kolom_kursi)
        break
    else:
        print("Jumlah baris dan kolom minimal 4! silahkan coba lagi.")
        print("Harap masukkan angka yang valid")
        continue
    
kursi_dipesan = set()

print("LAYOUT KURSI BISKOP: ")
nomor = 1
for i in range (jumlah_baris) :
    for j in range (kolom_kursi) :
         print(f"{nomor:>5}",end= " ")
         if nomor % kolom_kursi == 0 :
             print( )
         nomor += 1

while True :
    print()
    nomor_kursi = int(input("Masukkan nomor kursi yang dipesan(atau 0 untuk selesai) : "))
    if nomor_kursi == 0 :
        print("Terima kasih telah memesan tiket")
        break
    if nomor_kursi < 1 or nomor_kursi > jumlah_baris * kolom_kursi:
        print("Nomor kursi tidak tersedia,silahkan masukkan nomor kursi yang lain.")
        continue
    if nomor_kursi in kursi_dipesan:
        print("Kursi sudah dipesan,silahkan pilih kursi lain")
        continue
    else :
        print(f"Kursi {nomor_kursi} berhasil dipesan.")
    print()

    kursi_dipesan.add(nomor_kursi)
    print("LAYOUT KURSI DIPESAN: ")
    nomor = 1
    for i in range (jumlah_baris):
        for j in range (kolom_kursi):
            if nomor in kursi_dipesan:
                print(f"{'X':>5}" , end=" ")
            else:
                print(f"{nomor:5}", end=" ") 
            if nomor % kolom_kursi == 0 :

                 print()
            nomor += 1

