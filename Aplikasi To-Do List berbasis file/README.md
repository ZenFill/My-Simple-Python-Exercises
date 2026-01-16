# Aplikasi To-Do List Berbasis File

Ini adalah aplikasi To-Do List sederhana berbasis command-line (CLI) yang ditulis dengan Python. Aplikasi ini memungkinkan pengguna untuk mengelola daftar tugas mereka dengan fitur penyimpanan otomatis ke file teks.

## Fitur Utama

- **Lihat Tugas**: Menampilkan daftar semua tugas yang tersimpan.
- **Tambah Tugas**: Menambahkan tugas baru ke dalam daftar.
- **Hapus Tugas**: Menghapus tugas berdasarkan nomor urut.
- **Penyimpanan Persisten**: Data disimpan dalam file `todo.txt`, sehingga tugas tidak hilang saat aplikasi ditutup.

## Prasyarat

- Python 3.x terinstal di komputer Anda.

## Cara Menjalankan

1.  Pastikan Anda memiliki file `todo_app.py`.
2.  Buka terminal atau command prompt.
3.  Arahkan ke direktori tempat file disimpan.
4.  Jalankan aplikasi dengan perintah:

    ```bash
    python todo_app.py
    ```

## Cara Menggunakan

Setelah menjalankan aplikasi, Anda akan melihat menu utama dengan opsi berikut:

1.  **Lihat Tugas**: Pilih menu `1` untuk melihat daftar tugas Anda.
2.  **Tambah Tugas**: Pilih menu `2`, lalu ketikkan tugas yang ingin ditambahkan. Aplikasi akan menyimpannya secara otomatis.
3.  **Hapus Tugas**: Pilih menu `3`, lalu masukkan nomor tugas yang ingin dihapus.
4.  **Keluar**: Pilih menu `4` untuk menutup aplikasi.

## Struktur File

- `todo_app.py`: Kode sumber utama aplikasi.
- `todo.txt`: File teks tempat menyimpan daftar tugas (dibuat otomatis jika belum ada).

## Pengembangan

Kode ini menggunakan fungsi dasar Python seperti penanganan file (`open`, `read`, `write`) dan struktur data list.

```python
# Contoh cara data dimuat
def muat_tugas():
    with open("todo.txt", "r") as file:
        ...
```
