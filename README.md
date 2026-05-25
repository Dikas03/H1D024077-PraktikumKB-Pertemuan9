# Praktikum Kecerdasan Buatan - Pertemuan 9
## Implementasi Dasar Algoritma Genetika (Knapsack Problem)

Repositori ini berisi implementasi dasar dari **Algoritma Genetika (Genetic Algorithm)** untuk menyelesaikan permasalahan optimasi kombinasi barang (*Knapsack Problem*) menggunakan bahasa pemrograman Python. Tugas ini diselesaikan secara modular sesuai dengan instruksi Modul 9 Praktikum Kecerdasan Buatan.

### 👤 Identitas Mahasiswa
* **Nama:** Dikas Setio Pramudo
* **NIM:** H1D024077
* **Prodi:** Informatika
* **Fakultas:** Teknik, Universitas Jenderal Soedirman

---

### ⚙️ Spesifikasi Metode Algoritma Genetika
Metode yang dikunci dan digunakan pada modul percobaan Pertemuan 9 ini meliputi:
* **Seleksi:** Roulette Wheel Selection (RWS)
* **Crossover:** One-Point Crossover
* **Mutasi:** Swap Mutation

---

### 📁 Struktur File Modular
* `inisiasipopulasi.py`: Modul untuk membangkitkan kromosom biner populasi awal secara acak.
* `EvaluasiFitness.py`: Modul untuk menghitung total profit dan total bobot dengan sistem penalti (*fitness = 0*) jika melebihi kapasitas beban.
* `selection.py`: Modul yang menyediakan fungsi seleksi orang tua berbasis proporsi fitness.
* `crossover.py`: Modul rekombinasi genetik untuk menghasilkan keturunan baru.
* `mutation.py`: Modul mutasi gen biner untuk menjaga keragaman genetik populasi agar menghindari konvergensi prematur.
* `main_pert9.py`: File eksekusi utama program yang berisi datasheet barang bawaan modul dan menampilkan visualisasi grafik konvergensi menggunakan `matplotlib`.

---

### 🚀 Cara Menjalankan Program
1. Pastikan library `matplotlib` dan `numpy` sudah terinstal di environment Python Anda:
   ```bash
   pip install matplotlib numpy
