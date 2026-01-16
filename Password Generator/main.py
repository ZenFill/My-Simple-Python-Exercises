import os
import tkinter as tk
from tkinter import messagebox
import secrets  # Pengganti random agar lebih aman
import string
import pyperclip

# --- Logika Backend ---

def check_strength(password):
    score = 0
    # Kriteria penilaian
    if len(password) >= 12: score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    # Tentukan status berdasarkan skor
    if score <= 2:
        return "Lemah (Weak)", "red"
    elif score <= 4:
        return "Sedang (Medium)", "#FFC107" # Kuning gelap
    else:
        return "Kuat (Strong)", "green"

def generate_password():
    length_str = entry_length.get()
    
    # Validasi Input
    if not length_str.isdigit():
        messagebox.showerror("Error", "Panjang harus berupa angka!")
        return
    
    length = int(length_str)
    if length < 8:
        messagebox.showwarning("Warning", "Disarankan minimal 8 karakter agar aman.")

    # Kumpulkan opsi karakter
    chars = string.ascii_letters
    if var_digits.get():
        chars += string.digits
    if var_symbols.get():
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "Pilih minimal satu jenis karakter!")
        return

    # Generate Password
    password = ''.join(secrets.choice(chars) for _ in range(length))
    
    # Tampilkan Hasil
    entry_result.delete(0, tk.END)
    entry_result.insert(0, password)
    
    # Cek Kekuatan
    status_text, status_color = check_strength(password)
    label_strength.config(text=f"Kekuatan: {status_text}", fg=status_color)

def copy_to_clipboard():
    password = entry_result.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Sukses", "Password berhasil disalin!")
    else:
        messagebox.showwarning("Kosong", "Belum ada password yang dibuat.")

def save_to_file():
    password = entry_result.get()
    if not password:
        messagebox.showwarning("Kosong", "Tidak ada password untuk disimpan.")
        return

    # Cek/Buat folder data
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Simpan file
    filename = os.path.join("data", "password_history.txt")
    
    try:
        with open(filename, "a") as f:
            f.write(f"{password}\n")
        messagebox.showinfo("Tersimpan", f"Password disimpan di folder data!")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan: {e}")

# --- Setup GUI (Tampilan) ---
root = tk.Tk()
root.title("Secure Password Generator v2.0")
root.geometry("450x550") # Saya perbesar sedikit tingginya agar muat semua tombol
root.config(bg="#f4f4f9")

# Judul
label_title = tk.Label(root, text="🛡️ Secure Pass Generator", font=("Segoe UI", 18, "bold"), bg="#f4f4f9", fg="#333")
label_title.pack(pady=20)

# Frame Input Panjang
frame_input = tk.Frame(root, bg="#f4f4f9")
frame_input.pack(pady=5)

tk.Label(frame_input, text="Panjang Karakter:", font=("Arial", 11), bg="#f4f4f9").pack(side=tk.LEFT, padx=10)
entry_length = tk.Entry(frame_input, width=5, font=("Arial", 11), justify="center")
entry_length.insert(0, "16")
entry_length.pack(side=tk.LEFT)

# Checkbox Options
frame_opts = tk.Frame(root, bg="#f4f4f9")
frame_opts.pack(pady=10)

var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

chk_digits = tk.Checkbutton(frame_opts, text="Gunakan Angka (0-9)", variable=var_digits, bg="#f4f4f9", font=("Arial", 10))
chk_digits.pack(anchor="w")
chk_symbols = tk.Checkbutton(frame_opts, text="Gunakan Simbol (!@#)", variable=var_symbols, bg="#f4f4f9", font=("Arial", 10))
chk_symbols.pack(anchor="w")

# Tombol Generate Utama
btn_generate = tk.Button(root, text="GENERATE PASSWORD", command=generate_password, 
                         bg="#007bff", fg="white", font=("Segoe UI", 11, "bold"), 
                         relief="flat", height=2, cursor="hand2")
btn_generate.pack(pady=10, fill=tk.X, padx=40)

# Kolom Hasil Password
entry_result = tk.Entry(root, font=("Consolas", 14), justify="center", bd=2, relief="solid")
entry_result.pack(pady=5, fill=tk.X, padx=40)

# Label Indikator Kekuatan
label_strength = tk.Label(root, text="Kekuatan: -", font=("Arial", 10, "bold"), bg="#f4f4f9", fg="#666")
label_strength.pack(pady=5)

# Tombol Copy
btn_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, 
                     bg="#28a745", fg="white", font=("Segoe UI", 10), cursor="hand2")
btn_copy.pack(pady=5, fill=tk.X, padx=100) # Saya buat lebih rapi

# --- TOMBOL SIMPAN (YANG TADI HILANG) ---
btn_save = tk.Button(root, text="Simpan ke File (History)", command=save_to_file, 
                     bg="#17a2b8", fg="white", font=("Segoe UI", 10), cursor="hand2")
btn_save.pack(pady=5, fill=tk.X, padx=100)

# Menjalankan loop aplikasi
root.mainloop()