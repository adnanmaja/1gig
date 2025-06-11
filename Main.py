import json
import csv
import sys
from mahasiswa import Mahasiswa

file_path = "D:/Python/gig1/mhs.json"
backup_path = "D:/Python/gig1/backup.json"
csv_path = "D:/Python/gig1/mhs.csv"

    

#json dump
def main():
    try:
        jumlahmhs = int(input("Jumlah mahasiswa yang ingin dimasukkan: "))
    except ValueError:
        print("Invalid")
        main()
    mahasiswas_new = []   
 
    #input interface
    for i in range(jumlahmhs):   
        jumlahke = i + 1
        print("\nData mahasiswa ke-" + str(jumlahke))
        nama = str(input("Nama: "))
        try:
            umur = int(input("Umur: "))
        except ValueError:
            print("Masukkan angka saja")
        fakultas = str(input("Fakultas: "))
        ipk = float(input("IPK: "))
        while True:
            di_skors = str(input("Apakah di skors? (y/n): ")).lower().strip()
            if di_skors in ['y', 'n']:
               break
            print("Masukkan y atau n saja")

        di_skors_bool = True if di_skors == 'y' else False

        #appending inputted data to mahasiswas_new[]
        mhs = Mahasiswa(nama, umur, fakultas, ipk, di_skors)
        mahasiswas_new.append(mhs.to_dict())
        print("Appended: "+ mhs.nama + "|" + "ID: " + str(id(mhs)))

    #inserting newly inputted data to the existing data at mhs.json
    with open(file_path, "r") as file:
        mahasiswas_existing = json.load(file)
        mahasiswas_ready = mahasiswas_existing + mahasiswas_new
        with open(file_path, "w") as file:
            json.dump(mahasiswas_ready, file, indent=4)

    jsonread()

        
#json read
def jsonread():
    with open(file_path, "r") as file:
        data = json.load(file)
        csvwrite()
        print("\nData tersimpan. Unutk melanjutkan, pilih salah satu di bawah: \n(1) List individual \n(2) List orang pintar\n")
        while True:
            try:
                inputlist = int(input("Pilih: "))
            except ValueError:
                print("Invalid")
            
            #Option (1), data individual mahasiswa
            if inputlist == 1:
                print("\nData individual mahaisiwa: \n")
                for m in data:
                    if m["ipk"] >= 3.5:
                        print(m["nama"], str(m["umur"]), m["fakultas"], str(m["ipk"]) + ", Pinter")
                    else:
                        print(m["nama"], str(m["umur"]), m["fakultas"], str(m["ipk"]) + ", Belum pinter")
                intermezzo()   
                return
            
            #Option (2), list data dgn ipk >= 3.5
            elif inputlist == 2:
                print("\nList orang pintar (IPK >= 3.5):\n")
                mhspintar = [m for m in data if m["ipk"] >= 3.5]
                for m in mhspintar:
                    print(m["nama"], str(m["umur"]), m["fakultas"], str(m["ipk"]) + ".")
                intermezzo()   
                return
            else: #input tdk sesuai dgn opsi yg ada, kembali ke input
                print("Masukkan angka sesuai opsi")  
               
       

#undo deletion of data
def jsonundo():
    with open(file_path, "r") as file:
        while True:
            try: 
                undoinp = str(input("Undo? (y/n) ")).lower().strip()
            except ValueError:
                print("Masukkan y/n saja")
            
            #rewriting mhs.json with backup.json
            if undoinp == 'y':
                with open(backup_path, "r") as backup:
                    prev_data = json.load(backup)
                    with open(file_path, "w") as undo:
                        json.dump(prev_data, undo, indent=4)
                print("Success")
                csvwrite()
                return
            elif undoinp == 'n':
                print("Terkonfirmasi")
                csvwrite()
                return
            else: #invalid input, kembali ke input
                print("Mohon masukkan data yang benar") 
            

#deleting a data on mhs.json
def jsondelete():
    with open(file_path, "r") as file:
        
        #backup
        old__data = file.read()
        data = json.loads(old__data)
        with open(backup_path, "w") as backup:
            backup.write(old__data)

        #interface
        print("\nHapus berdasarkan? \n(1) Nama\n(2) Umur\n(3) Fakultas")
        
        #while loop untuk memastikan data yang diinput sesuai dengan opsi yang tersedia
        while True:
            try:
                hapusinp = int(input("Pilih: "))
            except ValueError:
                print("Isi dengan angka saja")
            if hapusinp == 1: #berdasarkan nama
                hapusnama = input("Nama yang ingin dihapus:")
                with open(file_path, "w") as file:
                    data = [m for m in data if m["nama"] != hapusnama]
                    json.dump(data, file, indent=4)
                print(hapusnama + "sudah dihapus. Undo?(y/n)")
                jsonundo()
                return
            elif hapusinp == 2: #berdasarkan umur
                hapusumur = input("Hapus semua yang berumur:")
                with open(file_path, "w") as file:
                    data = [m for m in data if m["umur"] != hapusumur]
                    json.dump(data, file, indent=4)
                print(hapusumur + "sudah dihapus. Undo?(y/n)")
                jsonundo()
                return
            elif hapusinp == 3: #berdasarkan fakultas
                hapusfakul = input("Hapus berdasarkan fakultas:")
                with open(file_path, "w") as file:
                    data = [m for m in data if m["fakultas"] != hapusfakul]
                    json.dump(data, file, indent=4)
                print(hapusfakul + "sudah dihapus. Undo?(y/n)")
                jsonundo()
                return
            else: #input diluar opsi yang tersedia
                print("Invalid")
    
                
#setelah data tersimpan, gate menuju jsondelete()
def intermezzo():
    print("\n\nPilih aksi selanjutnya: \n(1) Input data\n(2) Hapus data\n(3) Keluar")
    while True:
        try:
            interinput = int(input("Pilih: "))
        except ValueError:
            print("Invalid")
        if interinput == 1:
            main()
            return
        elif interinput == 2:
            jsondelete()
            return
        elif interinput == 3: #keluar
            sys.exit()
        else:
            print("Invalid")


#writes in csv
def csvwrite():
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        

    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    
    print("CSV updated")


main()

