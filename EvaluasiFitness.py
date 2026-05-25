def hitung_fitness(kromosom, barang, kapasitas_tas):
    total_harga = 0
    total_bobot = 0
    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_harga += barang[i][1] # Indeks 1 adalah Harga/Nilai
            total_bobot += barang[i][2] # Indeks 2 adalah Bobot
            
    if total_bobot > kapasitas_tas:
        return 0 # Penalti jika melebihi kapasitas
    else:
        return total_harga