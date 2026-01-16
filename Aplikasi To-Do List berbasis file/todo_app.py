import os

# Nama file tempat kita menyimpan data
NAMA_FILE = "todo.txt"

def muat_tugas():
    """Membaca tugas dari file teks dan mengembalikannya sebagai list."""
    tugas = []
    if os.path.exists(NAMA_FILE):
        with open(NAMA_FILE, "r") as file:
            for baris in file:
                # .strip() menghapus karakter baris baru (\n) di akhir
                tugas.append(baris.strip())
    return tugas

def simpan_tugas(tugas):
    """Menulis seluruh list tugas ke dalam file teks."""
    with open(NAMA_FILE, "w") as file:
        for t in tugas:
            file.write(t + "\n")

def tampilkan_daftar(tugas):
    """Menampilkan semua tugas dengan nomor urut."""
    print("\n--- Daftar Tugas ---")
    if not tugas:
        print("Belum ada tugas.")
    else:
        for index, t in enumerate(tugas):
            print(f"{index + 1}. {t}")
    print("--------------------")

def main():
    # 1. Muat data saat aplikasi dimulai
    daftar_tugas = muat_tugas()

    while True:
        print("\nMENU APLIKASI:")
        print("1. Lihat Tugas")
        print("2. Tambah Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            tampilkan_daftar(daftar_tugas)
        
        elif pilihan == '2':
            tugas_baru = input("Masukkan tugas baru: ")
            daftar_tugas.append(tugas_baru)
            simpan_tugas(daftar_tugas) # Simpan otomatis
            print("Tugas berhasil ditambahkan!")
            
        elif pilihan == '3':
            tampilkan_daftar(daftar_tugas)
            try:
                nomor = int(input("Hapus tugas nomor berapa? "))
                if 1 <= nomor <= len(daftar_tugas):
                    hapus = daftar_tugas.pop(nomor - 1)
                    simpan_tugas(daftar_tugas) # Simpan otomatis
                    print(f"Tugas '{hapus}' berhasil dihapus.")
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Masukkan angka yang benar.")
                
        elif pilihan == '4':
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()