# Gmail Generator 🎯

Aplikasi CLI interaktif untuk menghasilkan nama Gmail yang keren dan unik!

## Fitur Utama ✨

### 1. **Kombinasi** 🔥
Menggabungkan kata sifat + kata benda + angka
```
Contoh: coolwolf007, epicdragon99, sharpfalcon42
```

### 2. **Minimalis** ⚡
Nama pendek dan simple, cocok untuk yang suka kesederhanaan
```
Contoh: wolf27, dragon88, falcon13
```

### 3. **Profesional** 💼
Nama dengan titik pemisah yang terlihat lebih resmi
```
Contoh: cool.wolf.pro, epic.dragon.max, sharp.falcon.x
```

### 4. **Aksi** 🚀
Tema gerakan dan kecepatan - dinamis dan energik!
```
Contoh: strikedragon007, blazetiger360, rushphoenix99
```

### 5. **Glamor** ✨
Nama mewah dan eksklusif dengan kombinasi vokal-konsonan
```
Contoh: velina.luxe, sirona.royal, delina.elite
```

### 6. **Nama Cowok** 👨
Menggunakan daftar nama cowok populer dengan berbagai format
```
Contoh: ahmad23, bambang_45, dani.67, erwin1995
```

### 7. **Nama Cewek** 👩
Menggunakan daftar nama cewek populer dengan berbagai format
```
Contoh: aisyah28, berliana_52, eka.19, jasmine2001
```

### 8. **Nama Cowok+** 👨✨
Menggabungkan nama cowok dengan kata sifat atau benda
```
Contoh: ahmadcool, bambangwolf, danidragon, erwinfury
```

### 9. **Nama Cewek+** 👩✨
Menggabungkan nama cewek dengan kata sifat atau benda
```
Contoh: aisyahcool, berlianawolf, ekadragon, jasminefury
```

### 10. **Random Mix** 🎲
Menggabungkan semua strategi untuk variasi maksimal

## Cara Penggunaan 🚀

### Menjalankan Aplikasi

```bash
python "Gmail Generator/gmail_generator.py"
```

### Workflow

1. Aplikasi menampilkan menu dengan 10 strategi pembuat nama
2. Pilih strategi yang diinginkan (1-10)
3. Masukkan jumlah nama yang ingin dibuat (1-50)
4. Lihat hasil nama Gmail yang dikurasi
5. Pilih apakah ingin menyimpan ke file atau tidak

## Fitur Bonus 💡

- ✅ **Nama Asli**: Database 100+ nama cowok dan cewek populer
- ✅ **Simpan ke File**: Eksport daftar nama Gmail ke file `.txt`
- ✅ **Preview Instant**: Lihat hasil sebelum menyimpan
- ✅ **Flexible**: Buat 1-50 nama sekaligus
- ✅ **Mix & Match**: Coba berbagai strategi
- ✅ **Variasi Format**: Nama + angka, underscore, dot, tahun

## Contoh Output

```
✨ Hasil - Strategi Nama Cewek:
--------------------------------------------------
 1. aisyah456@gmail.com
 2. berliana_789@gmail.com
 3. eka.123@gmail.com
 4. jasmine2005@gmail.com
 5. karina45@gmail.com
--------------------------------------------------
```

## Dependensi 📦

Hanya menggunakan Python standard library - **tidak ada dependensi eksternal** yang diperlukan!

## Tips & Trik 💭

1. **Untuk email pribadi**: Gunakan "Nama Cowok" atau "Nama Cewek"
2. **Untuk profil sosial**: Coba "Nama Cowok+" atau "Nama Cewek+"
3. **Untuk gaming/hobby**: Gunakan "Aksi" atau "Kombinasi"
4. **Untuk mencari sesuatu yang unik**: Gunakan "Glamor" atau "Random Mix"
5. **Mix variasi**: Pilih "Random Mix" untuk kombinasi terbaik

## Struktur Kode

### Generator Dasar
- `pembuat_nama_kombinasi()` - Generator kombinasi kata
- `pembuat_nama_minimalis()` - Generator nama pendek
- `pembuat_nama_profesional()` - Generator dengan dot separator
- `pembuat_nama_aksi()` - Generator tema aksi
- `pembuat_nama_glamor()` - Generator nama mewah

### Generator Nama Orang
- `pembuat_nama_cowok()` - Generator nama cowok dengan variasi format
- `pembuat_nama_cewek()` - Generator nama cewek dengan variasi format
- `pembuat_nama_cowok_plus()` - Generator nama cowok + kata tambahan
- `pembuat_nama_cewek_plus()` - Generator nama cewek + kata tambahan

### Utility
- `simpan_ke_file()` - Fungsi penyimpanan file
- `main()` - Loop utama aplikasi

## Data Yang Tersedia 📊

- **NAMA_COWOK**: 140+ nama cowok populer Indonesia
- **NAMA_CEWEK**: 140+ nama cewek populer Indonesia
- **KATA_SIFAT**: 23 kata sifat untuk deskripsi
- **KATA_BENDA**: 20 kata benda untuk kombinasi
- **KATA_AKSI**: 16 kata aksi untuk tema gerakan
- **ANGKA_POPULER**: 9 angka populer (007, 13, 27, 42, 88, 99, 2024, 360, 404)
- **SUFIKS**: 15 sufiks untuk tambahan profesional

## Educational Value 🎓

Aplikasi ini mendemonstrasikan:
- Penggunaan list dan dictionary dalam Python
- String manipulation dan formatting
- File I/O operations
- Interactive CLI dengan while loop
- Function decomposition dan code organization
- Random module untuk randomisasi
- Data structures untuk menyimpan informasi

