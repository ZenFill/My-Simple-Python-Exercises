import random
import secrets
from typing import List

# Data nama-nama populer
NAMA_COWOK = [
    "Adi", "Ahmad", "Bambang", "Budi", "Citra", "Dani", "Daru", "Dedi",
    "Dwi", "Eka", "Erwin", "Fahmi", "Farhan", "Fauzi", "Fery", "Firdaus",
    "Ganda", "Ganteng", "Gede", "Gilang", "Gora", "Gugum", "Gun",
    "Hadi", "Haji", "Halim", "Hamid", "Hardi", "Harjono", "Harmoni", "Hasan",
    "Hendra", "Hendry", "Hendy", "Herianto", "Herman", "Hermawan",
    "Ikhsan", "Ilham", "Imam", "Imran", "Irfan", "Irwan", "Ismail",
    "Jaka", "Jamal", "Jamari", "Jamil", "Jarwo", "Jasmad", "Jazman",
    "Jendra", "Jendral", "Jenggi", "Jepang", "Jerzy", "Jese", "Jiwo",
    "Joby", "Joko", "Jondi", "Jopy", "Jordi", "Joshi", "Juan",
    "Judhi", "Judy", "Juha", "Julang", "Julianto", "Juliana", "Julien",
    "Kadir", "Kadri", "Kahlil", "Kaji", "Kaldi", "Kalis", "Kamal",
    "Kamil", "Kampar", "Kanadi", "Kananto", "Kandar", "Kangga", "Kangin",
    "Laksmi", "Lalu", "Lampe", "Lanang", "Landi", "Lando", "Lange",
    "Langit", "Lani", "Latif", "Laubern", "Laut", "Lawi", "Lawrence",
    "Mahdi", "Mahmud", "Mahmur", "Mahpud", "Mahsun", "Mahtom", "Maidu",
    "Mainto", "Maison", "Majid", "Makbul", "Makdar", "Makiman", "Makin",
    "Nabil", "Nadir", "Nafis", "Nafri", "Nagib", "Nahari", "Naidah",
    "Naidu", "Naiku", "Nail", "Naim", "Naina", "Nair", "Naito",
    "Noar", "Nobri", "Nofan", "Nogal", "Nohan", "Nohel", "Nohim",
    "Pardi", "Parjo", "Partono", "Pasrah", "Patmo", "Patro", "Paulus",
    "Payong", "Pazifik", "Pedri", "Peduk", "Peksi", "Pelangi", "Pelawi",
    "Raffi", "Rafi", "Rafim", "Rafiq", "Rafri", "Raga", "Ragad",
    "Ragga", "Raggi", "Rahardjo", "Rahasia", "Rahayu", "Rahmat", "Rahmin",
    "Sadi", "Sadik", "Sadio", "Sadli", "Sadmin", "Sadner", "Sadri",
    "Saiful", "Saifur", "Saigon", "Saihan", "Sailin", "Saillor", "Saim",
    "Tajib", "Tajir", "Takdir", "Takesi", "Takkan", "Takki", "Taksi",
    "Talani", "Talim", "Tamarai", "Tamarin", "Tambah", "Tambiyanto",
    "Ubu", "Ubur", "Ucap", "Uceng", "Uci", "Udal", "Udang",
    "Udaya", "Udi", "Udik", "Udim", "Udiman", "Udji", "Udjo",
    "Vadi", "Vadim", "Vali", "Valim", "Valon", "Vanda", "Vanderbilt",
    "Wadi", "Wadim", "Wado", "Wadiyo", "Wadjon", "Wadlyono", "Wafa",
    "Yadi", "Yahya", "Yahiro", "Yajnadi", "Yajyan", "Yaki", "Yakil",
    "Yamin", "Yamin", "Yaminda", "Yan", "Yana", "Yanadi", "Yanandra",
    "Zadi", "Zadik", "Zadim", "Zadzim", "Zaer", "Zafar", "Zafi"
]

NAMA_CEWEK = [
    "Aisyah", "Ani", "Anisa", "Anita", "Anja", "Anjar", "Anjuli",
    "Aniela", "Anis", "Anik", "Anike", "Anila", "Anile", "Anim",
    "Berliana", "Bernadine", "Bessa", "Betania", "Betina", "Betrice", "Betty",
    "Biah", "Bianca", "Bianet", "Bianni", "Biantas", "Biany", "Biara",
    "Caca", "Cacia", "Cadista", "Cadora", "Cadya", "Caecilia", "Caeli",
    "Caena", "Caera", "Caesia", "Caesti", "Caety", "Cafa", "Cafara",
    "Dacia", "Daciely", "Dacya", "Dadang", "Dadari", "Dadarilah", "Dadarna",
    "Dafina", "Dafinah", "Dagma", "Dagmar", "Dagmara", "Dagny", "Dagrina",
    "Eka", "Ekabuana", "Ekala", "Ekambara", "Ekamaya", "Ekamini", "Ekami",
    "Ekamna", "Ekananda", "Ekandra", "Ekane", "Ekani", "Ekanindya", "Ekanira",
    "Fadila", "Fadilah", "Fadile", "Fadilian", "Fadiliana", "Fadilin", "Fadilina",
    "Faditta", "Fadia", "Fadianta", "Fadianti", "Fadiara", "Fadiasari", "Fadiasih",
    "Gaia", "Gaiana", "Gaiant", "Gaianti", "Gaiba", "Gaibi", "Gaiby",
    "Gaidah", "Gaide", "Gaiden", "Gaider", "Gaidi", "Gaidia", "Gaidian",
    "Hani", "Hanidah", "Hanifa", "Hanifah", "Hanifah", "Hanifera", "Haniffa",
    "Hanif", "Haniha", "Hanihah", "Hanija", "Hanijara", "Hanilah", "Hanill",
    "Ida", "Idah", "Idabelle", "Idabellina", "Idabellis", "Idabellius", "Idabu",
    "Idabura", "Idacella", "Idacella", "Idacy", "Idada", "Idadah", "Idaddah",
    "Jasmine", "Jasmina", "Jasminah", "Jasminca", "Jasminde", "Jasmined", "Jasminen",
    "Jasmines", "Jasmineta", "Jasminfah", "Jasminia", "Jasminiah", "Jasminie", "Jasminja",
    "Karina", "Karinah", "Karinala", "Karinara", "Karinasari", "Karinata", "Karinaya",
    "Karinca", "Karinea", "Karineta", "Kariniah", "Karinilla", "Karinina", "Karinisa",
    "Lany", "Lanya", "Lanyah", "Lanyam", "Lanyami", "Lanyamik", "Lanyamila",
    "Lanyamira", "Lanyamit", "Lanyamita", "Lanyamitha", "Lanyamity", "Lanyamiya", "Lanyamizah",
    "Mania", "Maniah", "Maniara", "Maniassa", "Manibat", "Manica", "Manicha",
    "Manidah", "Manide", "Maniela", "Maniera", "Manif", "Manifah", "Manifasia",
    "Nadia", "Nadiah", "Nadiaja", "Nadiara", "Nadiare", "Nadiarine", "Nadiarini",
    "Nadiasari", "Nadiati", "Nadiatta", "Nadiaty", "Nadiatus", "Nadiaya", "Nadiayah",
    "Pasha", "Pashade", "Pashal", "Pashalina", "Pashalis", "Pasham", "Pashambe",
    "Pashami", "Pashamia", "Pashamie", "Pashamina", "Pashamit", "Pashamita", "Pashamity",
    "Rania", "Raniah", "Raniara", "Raniash", "Raniba", "Ranibah", "Ranibala",
    "Ranibare", "Ranibi", "Ranibiah", "Ranibila", "Ranibillah", "Ranibita", "Ranibya",
    "Sania", "Saniah", "Saniara", "Saniasih", "Saniba", "Sanibah", "Sanibala",
    "Sanibare", "Sanibi", "Sanibiah", "Sanibila", "Sanibillah", "Sanibita", "Sanibya",
    "Tania", "Taniah", "Taniara", "Taniasih", "Taniba", "Tanibah", "Tanibala",
    "Tanibare", "Tanibi", "Tanibiah", "Tanibila", "Tanibillah", "Tanibita", "Tanibya",
    "Vania", "Vaniah", "Vaniara", "Vaniasih", "Vaniba", "Vanibah", "Vanibala",
    "Vanibare", "Vanibi", "Vanibiah", "Vanibila", "Vanibillah", "Vanibita", "Vanibya",
    "Wania", "Waniah", "Waniara", "Waniasih", "Waniba", "Wanibah", "Wanibala",
    "Yania", "Yaniah", "Yaniara", "Yaniasih", "Yaniba", "Yanibah", "Yanibala",
    "Zania", "Zaniah", "Zaniara", "Zaniasih", "Zaniba", "Zanibah", "Zanibala"
]

# Data kata-kata yang bisa dikombinasikan
KATA_SIFAT = [
    "cool", "epic", "smart", "swift", "bold", "sharp", "wild", "brave",
    "true", "pure", "prime", "rare", "peak", "elite", "super", "ultra",
    "mega", "cyber", "delta", "sigma", "nova", "apex", "zenith"
]

KATA_BENDA = [
    "wolf", "tiger", "phoenix", "dragon", "falcon", "thunder", "storm",
    "fire", "frost", "shadow", "steel", "cyber", "nexus", "pulse",
    "knight", "sage", "mystic", "legend", "hero", "ninja", "titan"
]

KATA_AKSI = [
    "strike", "blaze", "rush", "surge", "spark", "crash", "dive", "soar",
    "hunt", "forge", "craft", "build", "code", "hack", "rock", "roll"
]

ANGKA_POPULER = [
    "007", "13", "27", "42", "88", "99", "2024", "360", "404"
]

SUFIKS = [
    "pro", "max", "x", "v2", "dev", "beta", "alpha", "delta",
    "prime", "core", "hub", "lab", "zone", "realm", "vault"
]

def pembuat_nama_kombinasi(jumlah: int = 5) -> List[str]:
    """Membuat nama Gmail dengan menggabungkan kata sifat + kata benda"""
    hasil = []
    for _ in range(jumlah):
        sifat = random.choice(KATA_SIFAT)
        benda = random.choice(KATA_BENDA)
        angka = random.randint(1, 999)
        nama = f"{sifat}{benda}{angka}"
        hasil.append(nama)
    return hasil

def pembuat_nama_minimalis(jumlah: int = 5) -> List[str]:
    """Membuat nama Gmail pendek dan simple"""
    hasil = []
    for _ in range(jumlah):
        benda = random.choice(KATA_BENDA)
        angka = random.randint(10, 99)
        nama = f"{benda}{angka}"
        hasil.append(nama)
    return hasil

def pembuat_nama_profesional(jumlah: int = 5) -> List[str]:
    """Membuat nama Gmail yang terlihat lebih profesional"""
    hasil = []
    for _ in range(jumlah):
        sifat = random.choice(KATA_SIFAT)
        benda = random.choice(KATA_BENDA)
        sufiks = random.choice(SUFIKS)
        nama = f"{sifat}.{benda}.{sufiks}"
        hasil.append(nama)
    return hasil

def pembuat_nama_aksi(jumlah: int = 5) -> List[str]:
    """Membuat nama Gmail dengan tema aksi dan pergerakan"""
    hasil = []
    for _ in range(jumlah):
        aksi = random.choice(KATA_AKSI)
        benda = random.choice(KATA_BENDA)
        angka = random.choice(ANGKA_POPULER)
        nama = f"{aksi}{benda}{angka}"
        hasil.append(nama)
    return hasil

def pembuat_nama_glamor(jumlah: int = 5) -> List[str]:
    """Membuat nama Gmail yang terlihat mewah dan eksklusif"""
    hasil = []
    konsonan = "bcdfghjklmnprstvwxyz"
    vokal = "aeiou"
    
    for _ in range(jumlah):
        # Buat nama unik dengan kombinasi konsonal-vokal
        panjang = random.randint(5, 8)
        nama = ""
        for i in range(panjang):
            if i % 2 == 0:
                nama += random.choice(konsonan)
            else:
                nama += random.choice(vokal)
        
        # Tambahkan sufiks mewah
        sufiks = random.choice(["luxe", "royal", "prime", "elite", "vip"])
        nama = f"{nama}.{sufiks}"
        hasil.append(nama)
    
    return hasil

def pembuat_nama_cowok(jumlah: int = 5) -> List[str]:
    """Membuat nama Gmail menggunakan nama cowok populer"""
    hasil = []
    for _ in range(jumlah):
        nama = random.choice(NAMA_COWOK)
        angka = random.randint(1, 999)
        sufiks = random.choice(["", ".", "_"])
        
        # Variasi format
        variasi = random.choice([1, 2, 3, 4])
        if variasi == 1:
            hasil.append(f"{nama.lower()}{angka}")
        elif variasi == 2:
            hasil.append(f"{nama.lower()}_{angka}")
        elif variasi == 3:
            hasil.append(f"{nama.lower()}.{angka}")
        else:
            tahun = random.choice(["19", "20"])
            hasil.append(f"{nama.lower()}{tahun}{random.randint(90, 99)}")
    
    return hasil

def pembuat_nama_cewek(jumlah: int = 5) -> List[str]:
    """Membuat nama Gmail menggunakan nama cewek populer"""
    hasil = []
    for _ in range(jumlah):
        nama = random.choice(NAMA_CEWEK)
        angka = random.randint(1, 999)
        
        # Variasi format
        variasi = random.choice([1, 2, 3, 4])
        if variasi == 1:
            hasil.append(f"{nama.lower()}{angka}")
        elif variasi == 2:
            hasil.append(f"{nama.lower()}_{angka}")
        elif variasi == 3:
            hasil.append(f"{nama.lower()}.{angka}")
        else:
            tahun = random.choice(["19", "20"])
            hasil.append(f"{nama.lower()}{tahun}{random.randint(90, 99)}")
    
    return hasil

def pembuat_nama_cowok_plus(jumlah: int = 5) -> List[str]:
    """Membuat nama Gmail dengan nama cowok + kata sifat/benda"""
    hasil = []
    for _ in range(jumlah):
        nama = random.choice(NAMA_COWOK)
        tambahan = random.choice([
            random.choice(KATA_SIFAT),
            random.choice(KATA_BENDA),
            str(random.randint(10, 99))
        ])
        
        nama_lengkap = f"{nama.lower()}{tambahan}"
        hasil.append(nama_lengkap)
    
    return hasil

def pembuat_nama_cewek_plus(jumlah: int = 5) -> List[str]:
    """Membuat nama Gmail dengan nama cewek + kata sifat/benda"""
    hasil = []
    for _ in range(jumlah):
        nama = random.choice(NAMA_CEWEK)
        tambahan = random.choice([
            random.choice(KATA_SIFAT),
            random.choice(KATA_BENDA),
            str(random.randint(10, 99))
        ])
        
        nama_lengkap = f"{nama.lower()}{tambahan}"
        hasil.append(nama_lengkap)
    
    return hasil

def tampilkan_menu():
    """Menampilkan menu utama aplikasi"""
    print("\n" + "="*50)
    print("   🎯 GMAIL NAME GENERATOR - PEMBUAT NAMA GMAIL 🎯")
    print("="*50)
    print("\nPilih strategi pembuat nama:")
    print("1. 🔥 Kombinasi (kata sifat + benda + angka)")
    print("2. ⚡ Minimalis (pendek dan simple)")
    print("3. 💼 Profesional (dengan titik pemisah)")
    print("4. 🚀 Aksi (tema gerakan dan kecepatan)")
    print("5. ✨ Glamor (nama mewah dan eksklusif)")
    print("6. 👨 Nama Cowok (nama asli dengan variasi)")
    print("7. 👩 Nama Cewek (nama asli dengan variasi)")
    print("8. 👨✨ Nama Cowok+ (nama + kata sifat/benda)")
    print("9. 👩✨ Nama Cewek+ (nama + kata sifat/benda)")
    print("10. 🎲 Random Mix (semua strategi campur)")
    print("0. ❌ Keluar")
    print("="*50)

def simpan_ke_file(nama_file: str, daftar_gmail: List[str]):
    """Menyimpan daftar Gmail ke file"""
    try:
        with open(nama_file, "w", encoding="utf-8") as f:
            for gmail in daftar_gmail:
                f.write(f"{gmail}@gmail.com\n")
        print(f"\n✅ Tersimpan ke file: {nama_file}")
        print(f"   Total: {len(daftar_gmail)} nama Gmail")
    except Exception as e:
        print(f"\n❌ Error menyimpan file: {e}")

def main():
    """Fungsi utama aplikasi"""
    print("\n🎉 Selamat datang di Gmail Generator!")
    
    while True:
        tampilkan_menu()
        pilihan = input("\nMasukkan pilihan (0-10): ").strip()
        
        if pilihan == "0":
            print("\n👋 Terima kasih telah menggunakan Gmail Generator!")
            break
        
        if pilihan in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            try:
                jumlah = int(input("Berapa banyak nama yang ingin dibuat? (1-50): "))
                if jumlah < 1 or jumlah > 50:
                    print("❌ Masukkan angka antara 1-50!")
                    continue
                
                print("\n⏳ Sedang membuat nama Gmail...")
                
                if pilihan == "1":
                    daftar = pembuat_nama_kombinasi(jumlah)
                    tipe = "Kombinasi"
                elif pilihan == "2":
                    daftar = pembuat_nama_minimalis(jumlah)
                    tipe = "Minimalis"
                elif pilihan == "3":
                    daftar = pembuat_nama_profesional(jumlah)
                    tipe = "Profesional"
                elif pilihan == "4":
                    daftar = pembuat_nama_aksi(jumlah)
                    tipe = "Aksi"
                elif pilihan == "5":
                    daftar = pembuat_nama_glamor(jumlah)
                    tipe = "Glamor"
                elif pilihan == "6":
                    daftar = pembuat_nama_cowok(jumlah)
                    tipe = "Nama Cowok"
                elif pilihan == "7":
                    daftar = pembuat_nama_cewek(jumlah)
                    tipe = "Nama Cewek"
                elif pilihan == "8":
                    daftar = pembuat_nama_cowok_plus(jumlah)
                    tipe = "Nama Cowok+"
                elif pilihan == "9":
                    daftar = pembuat_nama_cewek_plus(jumlah)
                    tipe = "Nama Cewek+"
                else:  # pilihan == "10"
                    semua_pembuat = [
                        pembuat_nama_kombinasi,
                        pembuat_nama_minimalis,
                        pembuat_nama_profesional,
                        pembuat_nama_aksi,
                        pembuat_nama_glamor,
                        pembuat_nama_cowok,
                        pembuat_nama_cewek,
                        pembuat_nama_cowok_plus,
                        pembuat_nama_cewek_plus
                    ]
                    daftar = []
                    per_tipe = jumlah // 9
                    sisa = jumlah % 9
                    for i, pembuat in enumerate(semua_pembuat):
                        tambah = per_tipe + (1 if i < sisa else 0)
                        daftar.extend(pembuat(tambah))
                    random.shuffle(daftar)
                    tipe = "Random Mix"
                
                # Tampilkan hasil
                print(f"\n✨ Hasil - Strategi {tipe}:")
                print("-" * 50)
                for i, nama in enumerate(daftar, 1):
                    print(f"{i:2d}. {nama}@gmail.com")
                print("-" * 50)
                
                # Tanyakan apakah ingin menyimpan
                simpan = input("\nSimpan ke file? (y/n): ").strip().lower()
                if simpan == "y":
                    nama_file = f"gmail_{tipe.lower().replace(' ', '_').replace('+', 'plus')}.txt"
                    simpan_ke_file(nama_file, daftar)
                
            except ValueError:
                print("❌ Masukkan angka yang valid!")
        else:
            print("❌ Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()
