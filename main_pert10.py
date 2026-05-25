import random
import matplotlib.pyplot as plt
import numpy as np

# Mengimpor fungsi-fungsi dari file praktikum sebelumnya
from inisiasipopulasi import inisialisasi_populasi
from EvaluasiFitness import hitung_fitness
from selection import tournament_selection
from crossover import two_point_crossover
from mutation import inversion_mutation

# =========================================================================
# DATASHEET FIX TUGAS PERTEMUAN 10 (Sesuai Gambar Shift Anda)
# =========================================================================
barang = [
    ("Barang1", 10, 5),   # Format: (Nama, Keuntungan, Ukuran)
    ("Barang2", 40, 4),
    ("Barang3", 30, 6),
    ("Barang4", 50, 3),
    ("Barang5", 35, 7),
]
ukuran_maksimal_gudang = 15 

# =========================================================================
# CORE ALGORITMA GENETIKA (NIM: H1D024077)
# =========================================================================
def run_ga_pertemuan_10(jumlah_generasi=50, jumlah_populasi=20, prob_crossover=0.5, prob_mutasi=0.1):
    nim_user = "H1D024077"
    metode_seleksi = "Tournament Selection (TS)"
    metode_crossover = "Two-Point Crossover"
    metode_mutasi = "Inversion Mutation"
    
    print("="*60)
    print(f"SISTEM KONFIGURASI NIM: {nim_user}")
    print(f"-> Metode Seleksi   : {metode_seleksi}")
    print(f"-> Metode Crossover : {metode_crossover}")
    print(f"-> Metode Mutasi    : {metode_mutasi}")
    print("="*60)

    jumlah_gen = len(barang)
    populasi = inisialisasi_populasi(jumlah_populasi, jumlah_gen)
    
    best_fitness_list = []
    worst_fitness_list = []
    avg_fitness_list = []
    all_fitness = []
    
    best_individu = None
    best_fitness_overall = -1

    for generasi in range(jumlah_generasi):
        # Evaluasi fitness
        fitness_populasi = [hitung_fitness(individu, barang, ukuran_maksimal_gudang) for individu in populasi]
        
        best_fitness = max(fitness_populasi)
        worst_fitness = min(fitness_populasi)
        avg_fitness = sum(fitness_populasi) / len(fitness_populasi)
        
        best_fitness_list.append(best_fitness)
        worst_fitness_list.append(worst_fitness)
        avg_fitness_list.append(avg_fitness)
        all_fitness.append(fitness_populasi.copy())
        
        if best_fitness > best_fitness_overall:
            best_fitness_overall = best_fitness
            index_best = fitness_populasi.index(best_fitness)
            best_individu = populasi[index_best].copy()
            
        new_populasi = []
        
        while len(new_populasi) < jumlah_populasi:
            # 1. SELEKSI PARENTS (Tournament Selection)
            available_pop = populasi.copy()
            available_fit = fitness_populasi.copy()
            
            parent1, idx1 = tournament_selection(available_pop, available_fit, k=3)
            del available_pop[idx1]
            del available_fit[idx1]
            
            parent2, _ = tournament_selection(available_pop, available_fit, k=3)
                
            # 2. CROSSOVER (Two-Point Crossover)
            if random.random() < prob_crossover:
                anak1, anak2 = two_point_crossover(parent1, parent2)
            else:
                anak1, anak2 = parent1.copy(), parent2.copy()
                
            # 3. MUTASI (Inversion Mutation)
            if random.random() < prob_mutasi:
                anak1 = inversion_mutation(anak1)
            if random.random() < prob_mutasi:
                anak2 = inversion_mutation(anak2)
            
            new_populasi.extend([anak1, anak2])
            
        populasi = new_populasi[:jumlah_populasi]

    # =========================================================================
    # PLOTTING GRAFIK EVALUASI
    # =========================================================================
    plt.figure(figsize=(12, 6))
    for i in range(jumlah_generasi):
        x = [i + 1] * len(all_fitness[i])
        y = all_fitness[i]
        plt.scatter(x, y, color='gray', alpha=0.15)
        
    plt.plot(range(1, jumlah_generasi + 1), best_fitness_list, color='blue', label='Fitness Tertinggi (Keuntungan Maks)')
    plt.plot(range(1, jumlah_generasi + 1), worst_fitness_list, color='orange', label='Fitness Terendah')
    plt.plot(range(1, jumlah_generasi + 1), avg_fitness_list, color='red', label='Fitness Rata-rata')
    
    plt.title(f'Grafik Konvergensi AG - NIM: {nim_user}\n({metode_seleksi} | {metode_crossover} | {metode_mutasi})')
    plt.xlabel('Generasi')
    plt.ylabel('Nilai Fitness (Total Keuntungan)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # =========================================================================
    # PRINT LOG SOLUSI TERBAIK
    # =========================================================================
    selected_items = [barang[i][0] for i in range(len(best_individu)) if best_individu[i] == 1]
    selected_weight = sum([barang[i][2] for i in range(len(best_individu)) if best_individu[i] == 1])
    
    print("\n" + "="*40)
    print("HASIL REKOMENDASI OPTIMASI GUDANG TOKO")
    print("="*40)
    print(f"Kromosom Terbaik     : {best_individu}")
    print(f"Total Keuntungan Maks: {best_fitness_overall}")
    print(f"Total Beban Ukuran   : {selected_weight} / {ukuran_maksimal_gudang}")
    print("Daftar Barang yang Harus Dibeli:")
    for item in selected_items:
        print(f"  - {item}")
    print("="*40)

# Jalankan program
run_ga_pertemuan_10()