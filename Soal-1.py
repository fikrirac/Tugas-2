#Menu Utama
def menu():
    awal = int(input(
        "--- Menu ---\n"
        "1. Daftar Kontak\n"
        "2. Tambah Kontak\n"
        "3. Keluar\n"
        "Pilih menu: "))
    return awal

#Menu
def daftar():
    print("Selamat Datang!")
    kontak = {}

    while True:
        awal = menu()

        if awal == 1:
            if bool(kontak) == True:
                for n, t in kontak.items():
                    print("---***---***---")
                    print("Nama: ", n)
                    print("No. Telpon: ", t)
            else:
                print(
                    "Daftar anda kosong"
                )

        elif awal == 2:
            nama = input("Nama: ")
            telp = input("No. Telpon: ")
            kontak.update({nama:telp})
            print(
                "Kontak berhasil ditambahkan"
            )
        elif awal == 3:
            print("Program selesai, sampai jumpa!")
            break
        else:
            print("Menu tidak tersedia. Silahkan masukkan menu lagi")

daftar()