# Todo List Application

## 1. Tujuan Aplikasi
Aplikasi Todo List ini dibuat untuk membantu pengguna mengelola tugas sehari-hari dengan mudah melalui web interface. Data tugas disimpan secara lokal menggunakan database SQLite sehingga dapat diakses dan dikelola kapan saja.

## 2. Tech Stack yang Digunakan
- Bahasa Pemrograman: Python 3
- Framework Web: Flask
- Database: SQLite
- Template Engine: Jinja2 (default Flask)
- Editor Teks: Nano/Vim (opsional)

## 3. Fitur-fitur Aplikasi

### Functional Requirements
- Menambah tugas baru dengan kategori (Pribadi/Umum).
- Menampilkan daftar tugas yang tersimpan dalam database.
- Menyimpan data tugas secara persist di database SQLite.
- Menyediakan kolom tanggal pembuatan tugas dan tanggal penyelesaian.
- Fitur hapus tugas yang sudah selesai.

### Non-Functional Requirements
- Aplikasi berjalan secara lokal pada sistem operasi yang mendukung Python.
- Web server menggunakan Flask dengan performa ringan.
- User interface sederhana, responsif, dan mudah digunakan.
- Data disimpan secara lokal tanpa perlu koneksi internet.

## 4. Cara Instalasi dan Menjalankan Aplikasi

### Prasyarat
- Python 3 terinstall di sistem.
- Pip terinstall.
- Virtual environment (disarankan).

### Langkah Instalasi

1. Clone atau download project ke komputer.

2. Masuk ke folder project:

```bash
cd todo-project
