📘 Aplikasi Parkir – Sistem Input & Output dengan GUI Tkinter
Aplikasi ini merupakan sistem sederhana untuk mencatat parkir masuk dan parkir keluar menggunakan Python + Tkinter serta penyimpanan data berbasis file teks.
Aplikasi telah dipisah menjadi 7 file utama, sehingga mudah dipahami, dimodifikasi, dan dikembangkan.
📂 Struktur File
project-parkir/
│
├── main.py
├── file1_input_output.py
├── file2_gui.py
├── file3_interaksi_gui.py
├── file4_integrasi.py
├── file5_storage.py
├── file6_utils.py
└── file7_config.py


📑 Penjelasan Setiap File
1️⃣ file1_input_output.py — Input File & Output Data
Berisi fungsi-fungsi dasar untuk:
Membaca data dari file data_parkir.txt
Menulis data baru ke file
Mengecek apakah file ada, membuat jika belum ada
File ini menjadi fondasi pengelolaan data non-GUI.


2️⃣ file2_gui.py — Membuat Antarmuka GUI (Tkinter)
Membangun elemen GUI dasar:
Window utama
Frame input
Tombol-tombol
Entry untuk input plat nomor
Label output
Tidak berisi logika, hanya tampilan.

3️⃣ file3_interaksi_gui.py — Interaksi Elemen GUI
Mengatur bagaimana GUI merespon:
Event tombol
Event keyboard (ENTER, panah, simbol tertentu)
Auto uppercase pada input Entry
Menghubungkan GUI dengan fungsi event handler.

4️⃣ file4_integrasi.py — Integrasi Logika & Tampilan
Menggabungkan:
Logika penyimpanan data
Logika validasi input
Feedback ke user (messagebox)
Update tampilan GUI
Bagian ini menghubungkan backend & frontend.

5️⃣ file5_storage.py — Penyimpanan & Pembacaan Data GUI
Lapisan abstraksi untuk data:
Menyimpan data parkir masuk
Menyimpan data parkir keluar
Membaca log data
Berfungsi seperti "database mini" berbasis txt.

6️⃣ file6_utils.py — Fungsi Pendukung
Berisi utilitas:
Format tanggal & jam
Validasi plat nomor
Konversi uppercase otomatis
Helper kecil lainnya
Membantu file lain agar lebih bersih.

7️⃣ file7_config.py — Konfigurasi Aplikasi
Menyimpan konstanta:
Warna tombol
Ukuran font
Nama file penyimpanan
Keybinding khusus
Supaya konfigurasi mudah diubah tanpa mengedit file lain.

▶️ Cara Menjalankan Aplikasi
1. Pastikan Python Terinstal
Minimal Python 3.8+
Cek dengan:
python --version
2. Tidak perlu instal library tambahan
Tkinter sudah bawaan Python.
3. Jalankan aplikasi
Masuk ke folder project:
cd project-parkir
Lalu jalankan:
python main.py
🧭 Alur Penggunaan Program
📌 1. Input Plat
Ketik plat kendaraan → otomatis uppercase
📌 2. Parkir Masuk
Tekan tombol Parkir Masuk
atau
Tekan tombol ENTER (↵)
Data akan disimpan ke file.
📌 3. Parkir Keluar
Tekan tombol Parkir Keluar
atau
Tekan tombol “\” (backslash)
Data akan dicatat ke file.
📄 File Penyimpanan Data
Aplikasi membuat file:
data_parkir.txt
Format data:
[2025-12-02 10:24] MASUK : B 1234 ABC
[2025-12-02 11:10] KELUAR: B 1234 ABC
🛠️ Pengembangan Selanjutnya
Aplikasi masih sangat mudah dikembangkan, misalnya:
Export ke Excel
Tambah tarif parkir
Koneksi database SQLite
Sistem login petugas
Menambah fitur laporan harian