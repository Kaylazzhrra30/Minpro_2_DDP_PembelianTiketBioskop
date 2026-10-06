# library

import os
import pwinput
from prettytable import PrettyTable

# data akun

akun = {
    "admin": {
        "password": "bakekok",
        "role": "admin"
    },
    "user": {
        "password": "upinbotak",
        "role": "user"
    }
}

# login

def login():

    while True:

        print("\n===== LOGIN =====")

        Role = input("Role : ").strip()
        password = pwinput.pwinput("Password : ")

        if Role in akun and password == akun[Role]["password"]:

            print("\nLogin berhasil!")
            print(f"Selamat datang, {Role}.")

            return akun[Role]["role"]

        else:
            print("\nUsername atau password salah!")

role = login()

# data tiket dan film

data_tiket = []

daftar_film = [
    ("F01", "Hope", 50000),
    ("F02", "Insidious Out of the further", 45000),
    ("F03", "Operasi Pesta Copet", 40000),
    ("F04", "Runner", 45000)
]

# tambah film

def tambah_film():

    print("\nTAMBAH FILM")

    while True:
        id_film = input("Masukkan ID film: ").upper().strip()

        if id_film == "":
            print("ID film tidak boleh kosong!")
            continue

        sudah_ada = False

        for film in daftar_film:
            if film[0] == id_film:
                sudah_ada = True
                break

        if sudah_ada:
            print("ID film sudah digunakan!")
        else:
            break

    while True:
        nama_film = input("Masukkan nama film: ").strip()

        if nama_film == "":
            print("Nama film tidak boleh kosong!")
        else:
            break

    while True:
        try:
            harga = int(input("Masukkan harga film: "))

            if harga <= 0:
                print("Harga harus lebih dari 0!")
            else:
                break

        except ValueError:
            print("Harga harus berupa angka!")

    film_baru = (
        id_film,
        nama_film,
        harga
    )

    daftar_film.append(film_baru)

    print("\nFilm berhasil ditambahkan!")

# program utama

while True:

    os.system("cls" if os.name == "nt" else "clear")

    # menu admin

    if role == "admin":

        print("\n===== MENU ADMIN =====")
        print("1. Tambah Tiket")
        print("2. Lihat Data Pembelian")
        print("3. Ubah Data Tiket")
        print("4. Hapus Data Tiket")
        print("5. Lihat Daftar Film")
        print("6. Tambah Film")
        print("7. Keluar")

    # menu user

    else:

        print("\n===== MENU USER =====")
        print("1. Tambah Tiket")
        print("2. Lihat Daftar Film")
        print("3. Lihat Data Pembelian")
        print("4. Keluar")

    pilihan = input("Pilih menu: ").strip()

    # tambah tiket

    if pilihan == "1":

        print("\nPEMBELIAN TIKET")

        while True:
            nama = input("Masukkan nama pembeli: ").strip()

            if nama == "":
                print("Nama tidak boleh kosong!")
            else:
                break

        print("\nDAFTAR FILM")

        for film in daftar_film:
            print(f"ID     : {film[0]}")
            print(f"Film   : {film[1]}")
            print(f"Harga  : Rp{film[2]:,.0f}")
            print("------------------------")

        while True:
            id_film = input("Masukkan ID film: ").upper().strip()

            film = None

            for data in daftar_film:
                if data[0] == id_film:
                    film = data
                    break

            if film is None:
                print("ID film tidak ditemukan!")
            else:
                break

        while True:
            kategori = input(
                "Kategori tiket (REGULER/VIP): "
            ).upper().strip()

            if kategori == "REGULER":
                harga_tiket = film[2]
                break

            elif kategori == "VIP":
                harga_tiket = film[2] + 20000
                break

            else:
                print("Kategori hanya REGULER atau VIP!")

        while True:
            try:
                jumlah = int(input("Jumlah tiket: "))

                if jumlah <= 0:
                    print("Jumlah tiket harus lebih dari 0!")
                else:
                    break

            except ValueError:
                print("Input harus berupa angka!")

        total_harga = harga_tiket * jumlah

        id_transaksi = len(data_tiket) + 1

        tiket = (
            id_transaksi,
            nama,
            film[1],
            kategori,
            jumlah,
            total_harga
        )

        data_tiket.append(tiket)

        print("\nTiket berhasil ditambahkan!")
        print(f"ID Transaksi : {id_transaksi}")
        print(f"Nama         : {nama}")
        print(f"Film         : {film[1]}")
        print(f"Kategori     : {kategori}")
        print(f"Jumlah       : {jumlah}")
        print(f"Total Harga  : Rp{total_harga:,.0f}")

    # admin - lihat data pembelian

    elif role == "admin" and pilihan == "2":

        print("\nDATA PEMBELIAN")

        if len(data_tiket) == 0:

            print("Belum ada data pembelian tiket.")

        else:

            tabel = PrettyTable()

            tabel.field_names = [
                "ID",
                "Nama",
                "Film",
                "Kategori",
                "Jumlah",
                "Total"
            ]

            for tiket in data_tiket:

                tabel.add_row([
                    tiket[0],
                    tiket[1],
                    tiket[2],
                    tiket[3],
                    tiket[4],
                    f"Rp{tiket[5]:,.0f}"
                ])

            print(tabel)

    # user - lihat daftar film

    elif role == "user" and pilihan == "2":

        print("\nDAFTAR FILM")

        for film in daftar_film:
            print(f"ID     : {film[0]}")
            print(f"Film   : {film[1]}")
            print(f"Harga  : Rp{film[2]:,.0f}")
            print("------------------------")

    # user - lihat data pembelian

    elif role == "user" and pilihan == "3":

        print("\nDATA PEMBELIAN")

        if len(data_tiket) == 0:

            print("Belum ada data pembelian tiket.")

        else:

            tabel = PrettyTable()

            tabel.field_names = [
                "ID",
                "Nama",
                "Film",
                "Kategori",
                "Jumlah",
                "Total"
            ]

            for tiket in data_tiket:

                tabel.add_row([
                    tiket[0],
                    tiket[1],
                    tiket[2],
                    tiket[3],
                    tiket[4],
                    f"Rp{tiket[5]:,.0f}"
                ])

            print(tabel)

    # admin - ubah data tiket

    elif role == "admin" and pilihan == "3":

        print("\nUBAH DATA TIKET")

        if len(data_tiket) == 0:

            print("Belum ada data pembelian.")

        else:

            for tiket in data_tiket:
                print(f"ID Transaksi : {tiket[0]}")
                print(f"Nama         : {tiket[1]}")
                print(f"Film         : {tiket[2]}")
                print(f"Kategori     : {tiket[3]}")
                print(f"Jumlah       : {tiket[4]}")

            while True:

                try:
                    id_transaksi = int(
                        input("Masukkan ID transaksi yang ingin diubah: ")
                    )

                    if id_transaksi <= 0:
                        print("ID harus lebih dari 0!")
                    else:
                        break

                except ValueError:
                    print("ID harus berupa angka!")

            index = -1

            for i in range(len(data_tiket)):

                if data_tiket[i][0] == id_transaksi:
                    index = i
                    break

            if index == -1:

                print("Data transaksi tidak ditemukan!")

            else:

                tiket_lama = data_tiket[index]

                print("\nData yang akan diubah:")
                print(f"Nama     : {tiket_lama[1]}")
                print(f"Film     : {tiket_lama[2]}")
                print(f"Kategori : {tiket_lama[3]}")
                print(f"Jumlah   : {tiket_lama[4]}")

                while True:

                    nama = input("Nama pembeli baru: ").strip()

                    if nama == "":
                        print("Nama tidak boleh kosong!")
                    else:
                        break

                print("\nDAFTAR FILM")

                for film in daftar_film:
                    print(f"ID     : {film[0]}")
                    print(f"Film   : {film[1]}")
                    print(f"Harga  : Rp{film[2]:,.0f}")
                    print("------------------------")

                while True:

                    id_film = input(
                        "Masukkan ID film baru: "
                    ).upper().strip()

                    film = None

                    for data in daftar_film:

                        if data[0] == id_film:
                            film = data
                            break

                    if film is None:
                        print("ID film tidak ditemukan!")
                    else:
                        break

                while True:

                    kategori = input(
                        "Kategori baru (REGULER/VIP): "
                    ).upper().strip()

                    if kategori == "REGULER":
                        harga_tiket = film[2]
                        break

                    elif kategori == "VIP":
                        harga_tiket = film[2] + 20000
                        break

                    else:
                        print("Kategori hanya REGULER atau VIP!")

                while True:

                    try:
                        jumlah = int(
                            input("Jumlah tiket baru: ")
                        )

                        if jumlah <= 0:
                            print("Jumlah tiket harus lebih dari 0!")
                        else:
                            break

                    except ValueError:
                        print("Input harus berupa angka!")

                total_harga = harga_tiket * jumlah

                tiket_baru = (
                    id_transaksi,
                    nama,
                    film[1],
                    kategori,
                    jumlah,
                    total_harga
                )

                data_tiket[index] = tiket_baru

                print("\nData tiket berhasil diubah!")
                print(f"Total harga baru: Rp{total_harga:,.0f}")

    # admin - hapus data tiket

    elif role == "admin" and pilihan == "4":

        print("\nHAPUS DATA TIKET")

        if len(data_tiket) == 0:

            print("Belum ada data pembelian.")

        else:

            for tiket in data_tiket:
                print(f"ID Transaksi : {tiket[0]}")
                print(f"Nama         : {tiket[1]}")
                print(f"Film         : {tiket[2]}")
                print(f"Kategori     : {tiket[3]}")
                print(f"Jumlah       : {tiket[4]}")

            while True:

                try:
                    id_transaksi = int(
                        input("Masukkan ID transaksi yang ingin dihapus: ")
                    )

                    if id_transaksi <= 0:
                        print("ID harus lebih dari 0!")
                    else:
                        break

                except ValueError:
                    print("ID harus berupa angka!")

            index = -1

            for i in range(len(data_tiket)):

                if data_tiket[i][0] == id_transaksi:
                    index = i
                    break

            if index == -1:

                print("Data transaksi tidak ditemukan!")

            else:

                tiket = data_tiket[index]

                print("\nData yang akan dihapus:")
                print(f"Nama : {tiket[1]}")
                print(f"Film : {tiket[2]}")

                while True:

                    konfirmasi = input(
                        "Yakin ingin menghapus? (Y/T): "
                    ).upper().strip()

                    if konfirmasi == "Y":

                        data_tiket.pop(index)

                        print("Data tiket berhasil dihapus!")
                        break

                    elif konfirmasi == "T":

                        print("Penghapusan dibatalkan.")
                        break

                    else:

                        print("Masukkan hanya Y atau T!")

    # admin - lihat daftar film

    elif role == "admin" and pilihan == "5":

        print("\nDAFTAR FILM")

        for film in daftar_film:
            print(f"ID     : {film[0]}")
            print(f"Film   : {film[1]}")
            print(f"Harga  : Rp{film[2]:,.0f}")
            print("------------------------")

    # admin - tambah film

    elif role == "admin" and pilihan == "6":

        tambah_film()

    # keluar admin

    elif role == "admin" and pilihan == "7":

        print("\nTerima kasih, selamat menonton!.")
        break

    # keluar user

    elif role == "user" and pilihan == "4":

        print("\nTerima kasih, selamat menonton!.")
        break

    # menu tidak valid

    else:

        print("Pilihan menu tidak valid!")