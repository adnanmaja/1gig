def main():
    import sys
    from mahasiswa import Mahasiswa
    try:
        jumlahmhs = int(input("Jumlah mahasiswa yang ingin dimasukkan: "))
    except ValueError:
        print("Invalid")
        main()
    mahasiswas = []   
    try:  
        for i in range(jumlahmhs):   
            jumlahke = i + 1
            print("\nData mahasiswa ke-" + str(jumlahke))
            nama = str(input("Nama: "))
            umur = int(input("Umur: "))
            fakultas = str(input("Fakultas: "))
            ipk = float(input("IPK: "))

            while True:
                di_skors = str(input("Apakah di skors? (y/n): ")).lower()
                if di_skors in ['y', 'n']:
                    break
                print("Masukkan y atau n saja")

            mhs = Mahasiswa(nama, umur, fakultas, ipk, di_skors)
            mahasiswas.append(mhs) 
            print("Appended: "+ mhs.nama + "|" + "ID: " + str(id(mhs)))

            if mhs.di_skors == "y":
                mhs.di_skors = True
            else:
                mhs.di_skors = False 
    
    except ValueError:
        print("Masukkan data yang benar!!!!!!!!!!")
        main()

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
            print("\nList orang pintar (IPK >= 3.5):")
            for mhs in mhspintar:
                print(mhs.nama + ", " + str(mhs.umur) + ", " + mhs.fakultas + ", " + mhs.fakultas)
    except:
        print("Error")

def second():
    import csv
    with open('test.csv', 'r') as csv_file:
        csvread = csv.reader(csv_file)

        with open('new_names', 'w') as newname:
            csvwrite = csv.writer(newname)

            for lines in csvread:
                csvwrite.writerow(lines)

#json dump
def third():
    import json
    from mahasiswa import Mahasiswa
    try:
        jumlahmhs = int(input("Jumlah mahasiswa yang ingin dimasukkan: "))
    except ValueError:
        print("Invalid")
        main()
    mahasiswas = []   
 
    for i in range(jumlahmhs):   
        jumlahke = i + 1
        print("\nData mahasiswa ke-" + str(jumlahke))
        nama = str(input("Nama: "))
        umur = int(input("Umur: "))
        fakultas = str(input("Fakultas: "))
        ipk = float(input("IPK: "))
        di_skors = bool(input("Skors? (bool): "))
        mhs = Mahasiswa(nama, umur, fakultas, ipk, di_skors)
        mahasiswas.append(mhs)
        for mhs in mahasiswas:
            print(mhs.nama + ", "+ mhs.fakultas + ", "+ str(mhs.ipk) + ", " + str(mhs.di_skors))

    file_path = "D:/Python/gig1/mhs.json"
    with open(file_path, "a") as file:
        json.dump([m.to_dict() for m in mahasiswas], file, indent=4)
        print("Success brother")

        
#json read
def jsonread():
    import json
    from mahasiswa import Mahasiswa
    file_path = "D:/Python/gig1/mhs.json"

    with open(file_path, "r") as file:
        data = json.load(file)
        print("\nData tersimpan. Unutk melanjutkan, pilih salah satu di bawah: \n(1) List individual \n(2) List orang pintar\n")
        inputlist = int(input("Pilih: "))
        if inputlist == 1:
            print("\nData individual mahaisiwa: \n")
            for m in data:
                if m["ipk"] >= 3.5:
                    print(m["nama"], str(m["umur"]), m["fakultas"], str(m["ipk"]) + ", Pinter")
                else:
                    print(m["nama"], str(m["umur"]), m["fakultas"], str(m["ipk"]) + ", Pinter")
        elif inputlist == 2:
            print("\nList orang pintar (IPK >= 3.5):\n")
            mhspintar = [m for m in data if m["ipk"] >= 3.5]
            for m in mhspintar:
                print(m["nama"], str(m["umur"]), m["fakultas"], str(m["ipk"]) + ".")


def jsondelete():
    import json
    from mahasiswa import Mahasiswa
    file_path = "D:/Python/gig1/mhs.json"
    with open(file_path, "r") as file:
        data = json.load(file)

        print("Hapus berdasarkan? \n(1) Nama\n(2) Umur\n(3) Fakultas")
        hapusinp = int(input("Pilih: "))
        if hapusinp == 1:
            hapusnama = input("Nama yang ingin dihapus:")
            with open(file_path, "w") as file:
                data = [m for m in data if m["nama"] != hapusnama]
                json.dump(data, file, indent=4)


jsonread()
jsondelete()