

<p align="center">
  <b>Selamat datang di repositori Python Komunitas Bellshade!</b><br>
  Proyek open-source ini didedikasikan untuk menyediakan kurikulum dan koleksi implementasi kode Python terlengkap — mulai dari konsep dasar pemula, pemrograman berorientasi objek, struktur data, algoritma klasik, komputasi matematika, hingga penerapan praktis di dunia nyata seperti Kecerdasan Buatan (AI/ML), Pemrosesan Citra, Kriptografi, dan Web Scraping.
</p>

[📚 Alur Belajar](#-peta-jalur-belajar-learning-roadmap) •
[📂 Struktur Modul](#-struktur-dan-katalog-modul) •
[🚀 Memulai & Instalasi](#-panduan-instalasi--memulai-getting-started) •
[🧪 Standar Pengujian](#-standar-pengujian--kualitas-kode-testing--qa) •
[🤝 Cara Berkontribusi](#-panduan-kontribusi-contributing-guide) •
[📑 Indeks Direktori](DIRECTORY.md)

</div>

---

## 📑 Daftar Isi

- [🎯 Tentang Repositori](#-tentang-repositori)
- [🗺️ Peta Jalur Belajar (Learning Roadmap)](#-peta-jalur-belajar-learning-roadmap)
- [📂 Struktur dan Katalog Modul](#-struktur-dan-katalog-modul)
  - [1. Dasar Pemrograman (`Basic/`)](#1-dasar-pemrograman-basic)
  - [2. Pemrograman Berorientasi Objek (`object_oriented/`)](#2-pemrograman-berorientasi-objek-object_oriented)
  - [3. Struktur Data (`struktur_data/`)](#3-struktur-data-struktur_data)
  - [4. Algoritma Komputasi (`algorithm/`)](#4-algoritma-komputasi-algorithm)
  - [5. Matematika & Analisis Numerik (`math/`)](#5-matematika--analisis-numerik-math)
  - [6. Implementasi Domain Khusus (`implementation/`)](#6-implementasi-domain-khusus-implementation)
  - [7. Pemrograman Web & Otomasi (`web_programming/`)](#7-pemrograman-web--otomasi-web_programming)
  - [8. Lainnya & Mini Projects (`other/`)](#8-lainnya--mini-projects-other)
- [🚀 Panduan Instalasi & Memulai (Getting Started)](#-panduan-instalasi--memulai-getting-started)
  - [Prasyarat Sistem](#prasyarat-sistem)
  - [Metode 1: Menggunakan `uv` (Direkomendasikan & Super Cepat)](#metode-1-menggunakan-uv-direkomendasikan--super-cepat)
  - [Metode 2: Menggunakan `venv` + `pip` Standar](#metode-2-menggunakan-venv--pip-standar)
  - [Cara Menjalankan Skrip](#cara-menjalankan-skrip)
- [🧪 Standar Pengujian & Kualitas Kode (Testing & QA)](#-standar-pengujian--kualitas-kode-testing--qa)
  - [Menjalankan Pengujian Otomatis (`pytest` & `doctest`)](#menjalankan-pengujian-otomatis-pytest--doctest)
  - [Format & Linting Kode (`flake8`, `black`, `isort`)](#format--linting-kode-flake8-black-isort)
  - [Git Hook Otomatis (`pre-commit`)](#git-hook-otomatis-pre-commit)
- [🤝 Panduan Kontribusi (Contributing Guide)](#-panduan-kontribusi-contributing-guide)
  - [Aturan Penulisan Fungsi & Docstrings](#aturan-penulisan-fungsi--docstrings)
  - [Langkah-Langkah Membuat Pull Request](#langkah-langkah-membuat-pull-request)
- [📜 Lisensi](#-lisensi)

---

## 🎯 Tentang Repositori

Tujuan utama repositori ini adalah:
1. **Menghilangkan Kendala Bahasa:** Menyajikan seluruh penjelasan, komentar, dan materi dalam Bahasa Indonesia yang mudah dipahami.
2. **Koleksi Komprehensif:** Menghubungkan konsep teoritis (struktur data & algoritma) dengan implementasi nyata (aplikasi industri, machine learning, automasi).
3. **Standar Kode Industri:** Setiap modul dirancang menggunakan konvensi kode Python modern (PEP 8, Type Hinting, Clean Architecture, Docstrings, dan Doctests otomatis).
4. **Terbuka & Kolaboratif:** Menyediakan ruang ramah bagi siapa pun untuk belajar, berbagi, mereview kode, dan berkontribusi ke dunia open-source.

---

## 🗺️ Peta Jalur Belajar (Learning Roadmap)

Bagi Anda yang baru memulai atau ingin memperdalam pemahaman, berikut alur belajar yang direkomendasikan:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        TAHAP 1: DASAR (BASIC)                         │
│  Sintaks dasar, tipe data, variabel, operator, percabangan, loop,     │
│  fungsi, exception handling, scope, lambda, hingga dekorator.          │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│            TAHAP 2: PEMROGRAMAN BERORIENTASI OBJEK (OOP)               │
│  Class & Object, Enkapsulasi, Inheritance, Polimorfisme, Abstraksi,   │
│  Magic Methods, Metaclass (Singleton, Factory, Proxy, Composite).      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                     TAHAP 3: STRUKTUR DATA                             │
│  Linked List (Singly & Doubly), Stack, Queue, Binary Search Tree,     │
│  AVL Tree (Self-balancing), Fenwick Tree (Binary Indexed Tree).        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                    TAHAP 4: ALGORITMA & MATEMATIKA                     │
│  Sorting, Searching, Backtracking, Divide & Conquer, Bitwise, Flow,   │
│  Analisis Numerik, Teori Bilangan, Kalkulus, Aljabar Linear Matriks.   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│               TAHAP 5: DOMAIN TERAPAN & PROYEK RIIL                   │
│  Artificial Intelligence, Machine Learning, Computer Vision, Kripto,   │
│  Kompresi Data, Simulasi Fisika, Web Scraping & Otomasi.               │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📂 Struktur dan Katalog Modul

Repositori ini tersusun secara modular. Di bawah ini adalah rincian materi dari setiap folder utama:

### 1. Dasar Pemrograman ([`Basic/`](Basic/))
Berisi 26 sub-modul materi fundamental Python dari nol hingga menengah:
- **01 - 05:** Pengenalan sintaksis, tipe data primitif, manajemen variabel, operasi aritmatika/bitwise/logika, dan manipulasi string.
- **06 - 09:** Input/Output interaktif, logika percabangan (`if-elif-else`), struktur perulangan (`for`, `while`), dan pembuatan fungsi rekursif.
- **10 - 15:** Koleksi data (`list`, `tuple`, `dict`, `set`), penanganan galat (*exception handling*), modularisasi skrip, modul `datetime`, dan modul `math`.
- **16 - 20:** Dasar kelas, pewarisan, akses kontrol (`public`, `private`, `protected`), iterator generator, dan ekspresi lambda.
- **21 - 26:** Regular Expression (Regex), variabel scope, latihan kalkulator modular, casting tipe data, list/dict comprehension, serta fungsi dekorator tingkat lanjut.

### 2. Pemrograman Berorientasi Objek ([`object_oriented/`](object_oriented/))
Eksplorasi paradigma OOP dari fondasi hingga arsitektur *Design Patterns*:
- **Basic OOP:** Definisi kelas, inisialisasi objek, konstruktor & destruktor, atribut instance vs atribut kelas.
- **Intermediate OOP:** 4 pilar utama — *Enkapsulasi* (data hiding & property), *Pewarisan* (single/multiple inheritance), *Polimorfisme* (method overriding), dan *Abstraksi* (Abstract Base Class).
- **Advance OOP:**
  - `arguments`: Penggunaan `*args` dan `**kwargs` dinamis.
  - `decorators`: Dekorator berantai (*decorator chaining*), dekorator dengan argumen.
  - `generators`: Pembuatan generator berbasis `yield` untuk efisiensi memori.
  - `magic_methods`: Dunder methods (`__str__`, `__repr__`, `__add__`, `__eq__`, dll.).
  - `metaclass & patterns`: Implementasi pola desain klasik seperti **Singleton**, **Factory Pattern**, **Proxy Pattern**, dan **Composite Pattern**.
  - `type_hint`: Penerapan static typing menggunakan modul `typing`.

### 3. Struktur Data ([`struktur_data/`](struktur_data/))
Implementasi struktur data murni tanpa pustaka eksternal:
- **Linked Lists:** *Singly Linked List* dan *Doubly Linked List* lengkap dengan operasi insert, delete, traversal, dan search.
- **Stack & Queue:** Implementasi struktur LIFO dan FIFO.
- **Tree Structures:**
  - *Binary Tree* & *Binary Search Tree (BST)*: Operasi traversal (*Pre-order*, *In-order*, *Post-order*), pencarian nilai minimum/maksimum, penjumlahan node (*Node Sum*), dan *Path Sum*.
  - *AVL Tree:* Pohon biner yang menyeimbangkan dirinya sendiri secara otomatis (*self-balancing*) melalui rotasi (*LL, RR, LR, RL*).
  - *Fenwick Tree:* Binary Indexed Tree untuk query penjumlahan rentang (*Range Sum Query*) berkinerja tinggi $O(\log n)$.
  - *Mirror Tree:* Transformasi cermin dari pohon biner.

### 4. Algoritma Komputasi ([`algorithm/`](algorithm/))
Koleksi algoritma penting dalam ilmu komputer:
- **Sorting:** Quick Sort, Merge Sort, Bubble Sort, Bead Sort, Bitonic Sort, Bucket Sort, Circle Sort, Gnome Sort, Bogo Sort, dan Pop Sort.
- **Searching:** Linear Search, Binary Search, dan pencarian pada matriks terurut.
- **Backtracking:** Penyelesaian masalah klasik seperti *N-Queens Problem*, *Sudoku Solver*, *Knight's Tour*, *Rat in a Maze*, *Pencarian Kata*, Pewarnaan Graf (*Graph Coloring*), dan Siklus Hamilton.
- **Divide and Conquer:** Convex Hull, Closest Pair of Points, Inversion Count, Max Subarray Sum, K-th Order Statistic.
- **Manipulasi Bit (Bitwise):** Penghitungan bit aktif, Two's Complement, pencarian bit ganjil, pembalik bit (*Reverse Bit*), dan manipulasi register biner.
- **Network Flow & Graf:** Ford-Fulkerson Algorithm dan Minimum Cut untuk optimalisasi aliran jaringan pipa/kapasitas.
- **Operasi Matriks:** Perkalian matriks, eliminasi Gauss, pencarian determinan, matriks spiral, Sherman-Morrison, dan invers matriks.
- **Analisis Numerik:** Bisection Method, Newton-Raphson, Secant Method, Jacobi Iteration, LU Decomposition.

### 5. Matematika & Analisis Numerik ([`math/`](math/))
Implementasi formula analitis, kalkulus, dan teori bilangan:
- **Kalkulus & Analisis Numerik:** Integral Riemann, Integrasi Aturan Simpson, Metode Trapesium, Runge-Kutta, Deret Taylor.
- **Teori Bilangan:** Sieve of Eratosthenes, Segmented Sieve, Deteksi Bilangan Prima, Faktorisasi Prima, Angka Proth, Aliquot Sum, Bilangan Armstrong/Krisnamurthy/Happy Number.
- **Aljabar & Geometri:** Teorema Pythagoras, Sudut & Radian, Trigonometri kustom, Transformasi Koordinat, Segitiga Pascal.
- **Fungsi Aktivasi & Statistik:** Sigmoid, ReLU, Softmax, R2 Score, Varians, Standar Deviasi, Konvolusi.

### 6. Implementasi Domain Khusus ([`implementation/`](implementation/))
Penerapan algoritma pada domain industri dan sains terapan:
- **Artificial Intelligence & Machine Learning:**
  - Regresi: Linear Regression, Logistic Regression, Ridge Regression, Lasso Regression, Polynomial Regression.
  - Klasifikasi & Clustering: K-Means Clustering, K-Nearest Neighbors (KNN), Gaussian Naive Bayes, Decision Tree, Random Forest.
  - Deep Learning: Long Short-Term Memory (LSTM) dan Neural Network dasar.
- **Computer Vision & Image Processing:**
  - Klasifikasi Citra menggunakan Convolutional Neural Networks (CNN).
  - Filter pengolahan citra (efek sepia, manipulasi saluran warna).
- **Kriptografi & Sandi (Cipher):**
  - Sandi Klasik: Caesar Cipher, Affine Cipher, Atbash Cipher, Playfair Cipher, Hill Cipher, ROT13.
  - Encoding: Base16, Base32, Base64, Base85.
  - Modul Matematika Kripto (*Cryptomath*).
- **Kompresi Data:**
  - Huffman Coding (kompresi berbasis frekuensi karakter).
  - Lempel-Ziv (LZ77 / LZ78).
  - Transformasi Burrows-Wheeler (BWT).
- **Blockchain & Kriptografi Modern:**
  - Persamaan Diophantine, Chinese Remainder Theorem, Modular Division.
- **Fisika & Sains:**
  - Simulasi Gravitasi *N-Body Simulation*.
  - Perhitungan kinematika dan dinamika gerak percepatan.
  - Pemodelan *Cellular Automata* (Conway's Game of Life, Nagel-Schreckenberg Traffic Model).
- **Geodesi & Navigasi:**
  - Rumus Haversine (perhitungan jarak kelengkungan permukaan bumi).
  - Jarak Ellipsoidal.

### 7. Pemrograman Web & Otomasi ([`web_programming/`](web_programming/))
- **Web Scraping:** Ekstraksi data HTML/XML langsung menggunakan `lxml`, `BeautifulSoup4`, dan XPath (contoh: pemantau data COVID-19, statistik emisi karbon).
- **Pengambilan Data API:** Konsumsi REST API publik secara aman menggunakan modul `requests` dan random quote fetcher.
- **Helper Web:** Generator tautan Breadcrumb dinamis dan pembagi halaman (*Pagination Helper*).

### 8. Lainnya & Mini Projects ([`other/`](other/))
- Puzzle Klasik Menara Hanoi (*Tower of Hanoi*).
- Logika gerbang Boolean (*Logic Gates Simulator*).
- Penentu hari dari tanggal (*Doomsday Algorithm* & *Zeller's Congruence*).
- Verifikator kekuatan kata sandi (*Strong Password Checker*).
- Grafika menggunakan modul bawaan `turtle` (menggambar logo, geometri).

---

## 🚀 Panduan Instalasi & Memulai (Getting Started)

### Prasyarat Sistem
Pastikan perangkat Anda telah terpasang:
- **Python 3.13 atau versi yang lebih baru** ([Unduh Python](https://www.python.org/downloads/))
- **Git** ([Unduh Git](https://git-scm.com/))

Clone repositori ini ke komputer lokal Anda:
```bash
git clone https://github.com/bellshade/Python.git
cd Python
```

---

### Metode 1: Menggunakan `uv` (Direkomendasikan & Super Cepat)
Proyek ini mendukung [**uv**](https://github.com/astral-sh/uv), package manager Python modern berbasis Rust yang sangat cepat.

1. **Instal `uv`** (jika belum terpasang):
   ```bash
   # Windows (PowerShell)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Linux / macOS
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Sinkronisasi lingkungan & pasang dependensi pengembangan:**
   ```bash
   uv add -r dev-requirements.txt
   uv add -r requirements.txt
   ```

3. **Jalankan pengujian menggunakan `uv`:**
   ```bash
   uv run pytest
   ```

---

### Metode 2: Menggunakan `venv` + `pip` Standar

1. **Buat dan aktifkan Virtual Environment:**
   ```bash
   # Membuat virtual environment
   python -m venv .venv

   # Mengaktifkan di Windows (PowerShell)
   .venv\Scripts\Activate.ps1

   # Mengaktifkan di Windows (Command Prompt)
   .venv\Scripts\activate.bat

   # Mengaktifkan di Linux / macOS
   source .venv/bin/activate
   ```

2. **Pasang seluruh dependensi:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   pip install -r dev-requirements.txt
   ```

---

### Cara Menjalankan Skrip

Setiap file skrip Python dapat dijalankan secara mandiri. Contoh eksekusi:

```bash
# Menjalankan materi pengenalan dasar
python Basic/01_introduction/Introduction.py

# Menjalankan algoritma pengurutan Quick Sort
python algorithm/sorting/quick_sorting.py

# Menjalankan struktur data AVL Tree
python struktur_data/tree/avl_tree/avl_tree.py

# Menjalankan algoritma enkripsi Caesar Cipher
python implementation/chiper/caesar.py
```

---

## 🧪 Standar Pengujian & Kualitas Kode (Testing & QA)

Repositori ini menerapkan standar kualitas kode tinggi yang terintegrasi langsung dengan **CI/CD GitHub Actions**.

### Menjalankan Pengujian Otomatis (`pytest` & `doctest`)
Semua fungsi algoritma diwajibkan menyertakan *doctest* di dalam blok docstring-nya. Konfigurasi pengujian diatur pada `pytest.ini`.

Untuk menjalankan seluruh rangkaian pengujian:
```bash
pytest
```

Untuk menguji satu file atau folder tertentu:
```bash
# Menguji modul spesifik
pytest algorithm/sorting/merge_sort.py --doctest-modules

# Menguji seluruh folder struktur data
pytest struktur_data/ --doctest-modules
```

Untuk memeriksa cakupan kode (*code coverage*):
```bash
pytest --cov=.
```

---

### Format & Linting Kode (`flake8`, `black`, `isort`)
Kami menjaga konsistensi gaya penulisan kode di seluruh repositori:
- **Black:** Memformat kode secara otomatis sesuai standar PEP 8.
- **isort:** Mengurutkan import modul secara rapi.
- **Flake8:** Memastikan tidak ada variabel tak terpakai, syntax error, atau kompleksitas fungsi berlebih (`max-line-length=100`, `max-complexity=25`).

Jalankan perintah berikut sebelum mengirimkan kontribusi:
```bash
# Periksa gaya kode dengan Flake8
flake8 .

# Format otomatis dengan Black & isort
black .
isort .
```

---

### Git Hook Otomatis (`pre-commit`)
Gunakan tool `pre-commit` agar pemeriksaan format dan linting berjalan otomatis setiap kali Anda melakukan `git commit`:

```bash
# Memasang hook ke repository lokal
pre-commit install

# Menjalankan hook secara manual ke seluruh file
pre-commit run --all-files
```

---

## 🤝 Panduan Kontribusi (Contributing Guide)

Kami menyambut kontribusi dari siapa saja! Baik berupa perbaikan bug, penambahan materi penjelasan, implementasi algoritma baru, ataupun optimasi kode yang sudah ada.

### Aturan Penulisan Fungsi & Docstrings
Setiap kode algoritma baru yang ditambahkan harus memenuhi kriteria berikut:
1. Menggunakan penamaan fungsi dan variabel yang deskriptif (*snake_case*).
2. Menyertakan petunjuk tipe data (*Type Hints*).
3. Mengembalikan nilai hasil perhitungan (`return`), hindari mencetak langsung (`print()`) di dalam fungsi algoritma.
4. Memiliki **Docstring lengkap** yang berisi penjelasan fungsi, parameter, return value, dan contoh pengujian (*Doctest*).

**Contoh Template Kode yang Baik:**
```python
def binary_search(array: list[int], target: int) -> int:
    """
    Melakukan pencarian biner pada list yang sudah terurut.

    Parameter:
        array (list[int]): List integer yang telah terurut secara menaik.
        target (int): Nilai yang ingin dicari posisinya.

    Return:
        int: Indeks dari target jika ditemukan, atau -1 jika tidak ada.

    Contoh / Doctest:
    >>> binary_search([1, 3, 5, 7, 9, 11], 7)
    3
    >>> binary_search([2, 4, 6, 8, 10], 5)
    -1
    >>> binary_search([], 1)
    -1
    """
    kiri, kanan = 0, len(array) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if array[tengah] == target:
            return tengah
        elif array[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
```

---

### Langkah-Langkah Membuat Pull Request

1. **Fork** repositori ini ke akun GitHub Anda.
2. Buat branch fitur baru:
   ```bash
   git checkout -b fitur/nama-algoritma-baru
   ```
3. Tulis kode algoritma/materi Anda beserta pengujian *doctest*.
4. Pastikan semua pengujian lulus secara lokal:
   ```bash
   pytest
   flake8 .
   ```
5. Commit perubahan Anda:
   ```bash
   git commit -m "feat(algorithm): menambahkan implementasi binary search"
   ```
6. Push branch ke repository fork Anda:
   ```bash
   git push origin fitur/nama-algoritma-baru
   ```
7. Buat **Pull Request (PR)** melalui antarmuka GitHub dan isi template PR dengan jelas.

Untuk informasi selengkapnya mengenai tata tertib dan panduan komunitas, silakan baca [CONTRIBUTING.md](CONTRIBUTING.md) dan [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

## 📜 Lisensi

Proyek ini didistribusikan di bawah lisensi terbuka **MIT License**. Anda bebas menggunakan, memodifikasi, dan mendistribusikan kode ini untuk keperluan edukasi maupun komersial dengan tetap menyertakan atribusi hak cipta asli. Lihat file [LICENSE](LICENSE) untuk informasi selengkapnya.

---

<div align="center">
  <b>Dikelola dengan ❤️ oleh Komunitas <a href="https://github.com/bellshade">Bellshade</a></b><br>
  <i>Mari bersama memajukan ekosistem edukasi pemrograman di Indonesia!</i>
</div>
