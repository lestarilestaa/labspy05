daftar = {}
while True :
    print("")
    a = input(" L)lihat, T)tambah, U)ubah, H)hapus, C)cari, K)keluar :")
    if a.lower() == 'k' :
        print ("\n==================== T E R I M A  K A S I H ====================")
        break
    elif a.lower() == 't':
        print("\nMasukan Data")
        nama = input("Nama           : ")
        nim = int(input("NIM            : "))
        tugas = int(input("Nilai Tugas    : "))
        UTS = int(input("Nilai UTS      : "))
        UAS = int(input("Nilai UAS      : "))
        a = tugas * 30 / 100
        b = UTS * 35 / 100
        c = UAS * 35 / 100
        akhir = a + b + c
        daftar[nama] = [nama, nim, tugas, UTS, UAS, akhir]
    elif a.lower() == 'u':
        print ("\nUbah daftar")
        nama = input("Masukan nama                   : ")
        if nama in daftar.keys():
            tugas = int(input("Masukan Nilai Tugas baru       : "))
            UTS = int(input("Masukan Nilai UTS baru         : "))
            UAS = int(input("Masukan Nilai UAS baru         : "))
            a = tugas * 30 / 100
            b = UTS * 35 / 100
            c = UAS * 35 / 100
            akhir = a + b + c
            daftar[nama] = [nama, nim, tugas, UTS, UAS, akhir]
        else :
                print("\nNama Tidak Ada")
    elif a.lower() == 'c':
        print ("\nCari Nama")
        nama = input("Masukan Nama     : ")
        if nama in daftar.keys():
            print ("\nDaftarnya {0} adalah {1}".format(nama, daftar[nama]))
        else:
            print("\nDaftar {0} tidak ada".format(nama))
    elif a.lower() == 'h':
        print("\nHapus Data")
        nama=input("Masukan Nama        :")
        if nama in daftar.keys():
            del daftar[nama]
        else:
            print("\nNama Tidak Ada")
    elif a.lower() == 'l':
        print("\nDaftar Nilai:")
        print("________________________________________________________________________")
        print("| No |     Nama       |    NIM    | Tugas |  UTS  |  UAS  | Akhir      |")
        print("________________________________________________________________________")
        no = 1
        for i in daftar.values():
            print("| {0:2} | {1:14} | {2:9} | {3:5} | {4:5} | {5:5} | {6:10} |".format (no, i[0], i[1], i[2], i[3], i[4], i[5]))
            print("________________________________________________________________________".format (i[0][:6]))
            no += 1
        if daftar == {}:
             print ("|                            TIDAK ADA DATA                            |")
             print ("|______________________________________________________________________|")