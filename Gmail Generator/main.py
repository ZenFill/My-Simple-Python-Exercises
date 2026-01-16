"""
Gmail Generator - Aplikasi CLI untuk membuat nama Gmail yang keren
"""

from gmail_generator import (
    pembuat_nama_kombinasi,
    pembuat_nama_minimalis,
    pembuat_nama_profesional,
    pembuat_nama_aksi,
    pembuat_nama_glamor,
    simpan_ke_file
)

def main():
    """Jalankan Gmail Generator"""
    try:
        from gmail_generator import main as run_generator
        run_generator()
    except ImportError:
        print("❌ Error: Tidak dapat mengimport gmail_generator!")

if __name__ == "__main__":
    main()
