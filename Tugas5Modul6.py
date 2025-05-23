print("===KALKULATOR MATRIKS===")

baris_A = int(input("Masukkan jumlah baris matriks A : "))
kolom_A = int(input("Masukkan jumlah kolom matriks A : "))
print("Masukkan elemen matriks A : ")
A = [ ]
for i in range(baris_A):
    baris = [ ]
    for j in range(kolom_A):
        elemen = int(input(f"A[{i}][{j}] : "))
        baris.append(elemen)
    A.append(baris)

baris_B = int(input("Masukkan jumlah baris matriks B : "))
kolom_B = int (input("Masukkan jumlah kolom matriks B : "))
print("Masukkan elemen matriks B : ")
B = [ ]
for i in range (baris_B):
    baris=[ ]
    for j in range(kolom_B):
        elemen = int(input(f"B[{i}][{j}] :"))
        baris.append(elemen)
    B.append(baris)

while True:
    print("\nMenu Operasi Matriks :")
    print("1.Penjumlahan")
    print("2.Pengurangan")
    print("3.Perkalian")
    print("4.Determinan(2x2)")
    print("5.Invers")
    print("6.Transpose")
    print("0.Keluar")
    pilihan=int(input("Pilih operasi yang akan dilakukan 0-6: "))

    if pilihan == 1 :
        if baris_A == baris_B and kolom_A == kolom_B:
            hasil = [ ]
            for i in range (baris_A):
                baris = [ ]
                for j in range (kolom_A):
                    baris.append(A[i][j] + B[i][j])
                hasil.append(baris)
            print("Hasil penjumlahan adalah :")
            for baris in hasil:
                print(baris)
        else:
            ("Ukuran matriks tidak sama.")

    elif pilihan == 2 :
        if baris_A == baris_B and kolom_A == kolom_B :
            hasil = [ ]
            for i in range (baris_A):
                baris = [ ]
                for j in range(kolom_A):
                    baris.append(A[i][j] - B[i][j])
                hasil.append(baris)
            print("Hasil pengurangan adalah : ")
            for baris in hasil:
                print(baris)
        else:
            print("Ukuran matriks tidak sama.")

    elif pilihan == 3 :
        if kolom_A == baris_B:
            hasil = []
            for i in range(baris_A):
                baris = [ ]
                for j in range (kolom_B):
                    total = 0
                    for k in range(kolom_A):
                        total += A[i][k] * B[k][j]
                    baris.append(total)
                hasil.append(baris)
            print("Hasil perkalian adalah :")
            for baris in hasil:
                print(baris)
        else:
            print("Jumlah kolom A harus sama dengan jumlah baris B.")

    elif pilihan == 4 :
        if baris_A == 2 and kolom_A == 2 and baris_B == 2 and kolom_B == 2 :
            detA = A[0][0] * A[1][1] - A[0][1] * A[1][0]
            detB = B[0][0] * B[1][1] - B[0][1] * B[1][0]
            print(f"Determinan A : {detA}")
            print(f"Determinan B : {detB}")
        else:
            print("Determinan hanya untuk matriks 2x2.")

    elif pilihan == 5 :
        if baris_A == 2 and kolom_A == 2 and baris_B == 2 and kolom_B == 2 :
            detA = A[0][0] * A[1][1] - A[0][1] * A[1][0]
            detB = B[0][0] * B[1][1] - B[0][1] * B[1][0]
            if detA != 0 :
                print("Invers A :")
                inversA = [[A[1][1]/detA, -A[0][1]/detA],[-A[1][0]/detA,A[0][0]/detA]]
                for baris in inversA:
                    print(baris)
            else:
                print("Matriks A tidak memiliki invers (determinan 0).")

            if detB != 0 :
                print("Invers B :")
                inversB = [[B[1][1]/detB, -B[0][1]/detB],[-B[1][0]/detB,B[0][0]/detB]]
                for baris in inversB:
                    print(baris)
            else:
                print("Matriks B tidak memiliki invers (determinan 0).")

        else:
            print("Invers hanya didukung untuk matriks 2x2.")

    elif pilihan == 6 :
        print("Transpose A :")
        for j in range(kolom_A):
            baris = [ ]
            for i in range (baris_A):
                baris.append(A[i][j])
            print(baris)
        print("Tranpose B :")
        for j in range(kolom_B):
            baris = [ ]
            for i in range (baris_B):
                baris.append(B[i][j])
            print(baris)
        
    elif pilihan == 0 :
        print("Terima kasih !")
        break
    else:
        print("Pilihan tidak valid.")

            

            

            



