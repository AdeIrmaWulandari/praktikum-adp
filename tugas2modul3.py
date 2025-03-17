n = int(input("Pemain 1 silahkan memasukkan angka positif yang diinginkan : "))
k = int(input("Pemain 1 silahkan memilih angka BOM : "))
for i in range (1,n+1) : 
    if i % k == 0 :
        print("BOM",end= " ")
    else :
        print(i, end= " ")
print("\n")
while True :
    tebakan_angka = int(input(f"Pemain 2 diminta menebak angka (1 -  {n}) : "))
    if tebakan_angka < 1 or tebakan_angka > n :
        print(f"Angka yang ditebak harus antara 1 - {n} ,silahkan coba lagi!")
        continue

    if tebakan_angka % k == 0 :
        print("Angka tebakan adalah BOM,Anda kalah")
        break
    else :
        print("Angka tebakan bukan BOM,Anda menang")
        break
