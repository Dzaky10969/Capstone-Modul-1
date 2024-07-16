from prettytable import PrettyTable

# Data karyawan awal
karyawan = [
    {'No ID': 'CT1', 'Nama': 'Dzaky', 'Tanggal Lahir': '2000-02-05', 'Jabatan': 'CTO', 'Gaji': 18000000},
    {'No ID': 'IT2', 'Nama': 'Salim', 'Tanggal Lahir': '2002-04-10', 'Jabatan': ' Senior Staff IT', 'Gaji': 7200000},
    {'No ID': 'IT3', 'Nama': 'Siska', 'Tanggal Lahir': '2003-07-21', 'Jabatan': 'Staff IT', 'Gaji': 5200000},
]
#tampilkan_menu:
def tampilkan_menu():
    print("\n==============================")
    print("    Sistem Pendataan Karyawan")
    print("==============================")
    print("1. Tampilkan daftar karyawan")
    print("2. Tambah karyawan")
    print("3. Hapus karyawan")
    print("4. Ubah data karyawan")
    print("5. Keluar program")
    print("==============================")

def tampilkan_sub_menu(submenu):
    print(f"\n1. {submenu} data")
    print("2. Kembali ke menu utama")

def tampilkan_karyawan():
    while True:
        print("\n1. Tampilkan seluruh karyawan")
        print("2. Cari karyawan berdasarkan No ID")
        print("3. Sorting data karyawan")
        print("4. Kembali ke menu utama")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tampilkan_seluruh_karyawan()
        elif pilihan == '2':
            cari_karyawan()
        elif pilihan == '3':
            sorting_karyawan()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def tampilkan_seluruh_karyawan():
    table = PrettyTable()
    table.field_names = ["No ID", "Nama", "Tanggal Lahir", "Jabatan", "Gaji"]
    for k in karyawan:
        table.add_row([k['No ID'], k['Nama'], k['Tanggal Lahir'], k['Jabatan'], k['Gaji']])
    print(table)

def cari_karyawan():
    no_id = input("Masukkan No ID karyawan: ")
    table = PrettyTable()
    table.field_names = ["No ID", "Nama", "Tanggal Lahir", "Jabatan", "Gaji"]
    found = False
    for k in karyawan:
        if k['No ID'] == no_id:
            table.add_row([k['No ID'], k['Nama'], k['Tanggal Lahir'], k['Jabatan'], k['Gaji']])
            found = True
    if found:
        print(table)
    else:
        print(f"\nKaryawan dengan No ID {no_id} tidak ditemukan.")

def sorting_karyawan():
    print("\n1. Sort Tanggal Lahir")
    print("2. Sort Gaji")
    print("3. Kembali")
    sort_choice = input("Pilih menu: ")
    if sort_choice in ['1', '2']:
        order = input("Masukkan urutan (asc/desc): ")
        reverse_order = (order == 'desc')
        if sort_choice == '1':
            karyawan.sort(key=get_tanggal_lahir, reverse=reverse_order)
        elif sort_choice == '2':
            karyawan.sort(key=get_gaji, reverse=reverse_order)
        print("Data karyawan berhasil diurutkan.")
    elif sort_choice == '3':
        return

def get_tanggal_lahir(karyawan):
    return karyawan['Tanggal Lahir']

def get_gaji(karyawan):
    return karyawan['Gaji']

def tambah_karyawan():
    while True:
        tampilkan_sub_menu("Tambah")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            no_id = input("Masukkan No ID: ")
            if any(k['No ID'] == no_id for k in karyawan):
                print(f"Karyawan dengan No ID {no_id} sudah ada.")
                continue
            nama = input("Masukkan Nama: ")
            tanggal_lahir = input_tanggal_lahir()
            jabatan = input("Masukkan Jabatan: ")
            gaji = int(input("Masukkan Gaji: "))
            karyawan.append({'No ID': no_id, 'Nama': nama, 'Tanggal Lahir': tanggal_lahir, 'Jabatan': jabatan, 'Gaji': gaji})
            print(f"\nKaryawan {nama} telah ditambahkan.")
            if input("Apakah data yang ditambah sudah benar (y/n)? ").lower() == 'y':
                break
        elif pilihan == '2':
            break

def input_tanggal_lahir():
    print("Mohon isi Tanggal Lahir Sesuai Instruksi (YYYY-MM-DD)")
    while True:
        try:
            tahun = int(input("Masukkan Tahun Lahir (YYYY): "))
            bulan = int(input("Masukkan Bulan Lahir (MM): "))
            if bulan not in range(1, 13):
                print("Bulan tidak valid. Silakan coba lagi.")
                continue
            if bulan == 2:
                if tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0):
                    max_hari = 29
                else:
                    max_hari = 28
            elif bulan in [4, 6, 9, 11]:
                max_hari = 30
            else:
                max_hari = 31
            hari = int(input("Masukkan Hari Lahir (DD): "))
            if hari not in range(1, max_hari + 1):
                print("Hari tidak valid. Silakan coba lagi.")
                continue
            return f"{tahun:04d}-{bulan:02d}-{hari:02d}"
        except ValueError:
            print("Input tidak valid. Silakan coba lagi.")

def hapus_karyawan():
    while True:
        print("\n1. Hapus karyawan berdasarkan No ID")
        print("2. Hapus semua karyawan")
        print("3. Kembali ke menu utama")
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            no_id = input("Masukkan No ID karyawan yang ingin dihapus: ")
            for k in karyawan:
                if k['No ID'] == no_id:
                    karyawan.remove(k)
                    print(f"\nKaryawan dengan No ID {no_id} telah dihapus.")
                    if input("Apakah data yang dihapus sudah benar (y/n)? ").lower() == 'y':
                        return
            print(f"\nKaryawan dengan No ID {no_id} tidak ditemukan.")
        elif pilihan == '2':
            karyawan.clear()
            print("\nSemua karyawan telah dihapus.")
            if input("Apakah data yang dihapus sudah benar (y/n)? ").lower() == 'y':
                return
        elif pilihan == '3':
            breakF

def ubah_karyawan():
    while True:
        tampilkan_sub_menu("Ubah")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            no_id = input("Masukkan No ID karyawan yang ingin diubah: ")
            for k in karyawan:
                if k['No ID'] == no_id:
                    k['Nama'] = input("Masukkan Nama baru: ")
                    k['Tanggal Lahir'] = input_tanggal_lahir()
                    k['Jabatan'] = input("Masukkan Jabatan baru: ")
                    k['Gaji'] = int(input("Masukkan Gaji baru: "))
                    print(f"\nKaryawan dengan No ID {no_id} telah diubah.")
                    if input("Apakah data yang diubah sudah benar (y/n)? ").lower() == 'y':
                        return
            print(f"\nKaryawan dengan No ID {no_id} tidak ditemukan.")
        elif pilihan == '2':
            break

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        try:
            if pilihan == '1':
                tampilkan_karyawan()
            elif pilihan == '2':
                tambah_karyawan()
            elif pilihan == '3':
                hapus_karyawan()
            elif pilihan == '4':
                ubah_karyawan()
            elif pilihan == '5':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError as e:
            print(f"Error: {e}. Input tidak valid. Silakan coba lagi.")

main()
