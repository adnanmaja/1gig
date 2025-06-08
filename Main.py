def main():
    from test_classnobj import Mahasiswa
    try:
        jumlahmhs = int(input("Jumlah mahasiswa yang ingin dimasukkan: "))
    except ValueError:
        print("Invalid")
        mahasiswas = []
    try:
        for i in range(jumlahmhs):
            jumlahke = i + 1
            print("\nData mahasiswa ke-" + str(jumlahke))
            nama = str(input("Nama: "))
            umur = int(input("Umur: "))
            fakultas = str(input("Fakultas: "))
            ipk = float(input("IPK: "))
            di_skors = str(input("Apakah di skors? (y/n): ")).lower()

            while True:
                if di_skors != 'y' or di_skors != 'n':
                    print("Masukkan y atau n saja")
                    break
            if mhs.di_skors == "y":
                mhs.di_skors = True
            else:
                mhs.di_skors = False

            try:
                mhs = Mahasiswa(nama, umur, fakultas, ipk, di_skors)
                mahasiswas.append(mhs)
            except ValueError:
                print("Masukkan data yang benar!!!!!!!!!!")
            print("Appended: "+ mhs.nama + "|" + "ID: " + str(id(mhs)))
    except UnboundLocalError:
        print("")
        sys.exit()    
    try:
        print("\nData tersimpan. Unutk melanjutkan, pilih salah satu di bawah: \n(1) List individual \n(2) List orang pintar\n")
        inputlist = int(input("Pilih: "))
        if inputlist == 1:
            for mhs in mahasiswas:
                if mhs.ipk >= 3.5:
                    print(mhs.nama + ", " + str(mhs.umur) + ", " + mhs.fakultas + ", Wong pinter")
                elif mhs.di_skors == True:
                    print(mhs.nama + ", " + str(mhs.umur) + ", " + mhs.fakultas + ", Wong pinter ra niat")
                else:
                    print(mhs.nama + ", " + str(mhs.umur) + ", " + mhs.fakultas + ", Wong goblok wkw")

        elif inputlist == 2:
            mhspintar = [mhs for mhs in mahasiswas if mhs.pinter]
            print("\nList orang pintar:")
            for mhs in mhspintar:
                print(mhs.nama + ", " + str(mhs.umur) + ", " + mhs.fakultas + ", " + mhs.fakultas)
    except:
        print("Error")

main()