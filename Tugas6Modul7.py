def input_data(jumlah):
    nama = []
    nim = []
    uts = []
    uas = []
    tugas = []

    for i in range(jumlah):
        print("Mahasiswa ke- ",i+1)
        nama.append(input("Nama : "))
        nim.append(int(input("NIM : ")))
        uts.append(float(input("Nilai UTS : ")))
        uas.append(float(input("Nilai UAS : ")))
        tugas.append(float(input("Nilai Tugas : ")))
    return nama,nim,uts,uas,tugas
    
def hitung_rata(array):
    total = 0
    for nilai in array:
        total += nilai
    return total/len(array)

def hitung_nilai_akhir(uts,uas,tugas):
    akhir = []
    for i in range(len(uts)):
        nilai = 0.35 * uas[i] + 0.35 * uts [i] + 0.30* tugas [i]
        akhir.append(nilai)
    return akhir

def  tentukan_peringkat (nilai_akhir):
    peringkat = [1] * len(nilai_akhir)
    for i in range(len(nilai_akhir)):
        for j in range (len(nilai_akhir)):
            if nilai_akhir[j] > nilai_akhir [i]:
                peringkat[i] += 1
    return peringkat

def urutkan_data (nama,nim,uts,uas,tugas,akhir):
    for i in range (len(akhir)-1):
        for j in range(len(akhir)-1-i):
            if akhir [j] < akhir [j+1]:
                akhir[j],akhir[j+1] = akhir [j+1],akhir[j]
                nama[j],nama[j+1] = nama [j+1],nama[j]
                nim[j],nim[j+1] = nim [j+1],nim[j]
                uas[j],uas[j+1] = uts[j+1],uas[j]
                uts[j],uts[j+1] = uts [j+1],uts[j]
                tugas[j],tugas[j+1] = tugas [j+1],tugas[j]
    
def tampilkan_tabel(nama,nim,uts,uas,tugas,akhir,peringkat):
    print("\n|{:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<12} | {:<10} | "
          .format("Nama","NIM","UTS","UAS","Tugas","Nilai Akhir","Peringkat"))
    for i in range (len(nama)):
        print("---------------------------------------------------------------------------------------------")
        print("|{:<10} | {:<10} | {:<10.2f} | {:<10.2f} | {:<10.2f} | {:<12.2f} | {:<10} | "
              .format(nama[i] , nim[i] , uts[i] , uas[i] , tugas[i] , akhir[i] , peringkat[i]) )
        print("---------------------------------------------------------------------------------------------")
    print("\n|{:<10} | {:<10} | {:<10.2f} | {:<10.2f} | {:<10.2f} | {:<12.2f} | {:<10} | ".format(
                 "Rata-rata" , " ",hitung_rata(uts),hitung_rata(uas),hitung_rata(tugas),hitung_rata(akhir) ," "))
    print("-------------------------------------------------------------------------------------------------")

n = int(input("Masukkan jumlah mahasiswa : "))   
nama,nim,uts,uas,tugas = input_data(n)
akhir = hitung_nilai_akhir(uts,uas,tugas)
urutkan_data(nama,nim,uts,uas,tugas,akhir)
peringkat = tentukan_peringkat(akhir)
tampilkan_tabel(nama,nim,uts,uas,tugas,akhir,peringkat)
