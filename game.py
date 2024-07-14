import random

# Definisi tangga dan ular
tangga = {
    6: 11,
    14: 20,
    25: 32,
    38: 43,
    56: 62
}

ular = {
    9: 4,
    22: 18,
    28: 24,
    45: 35,
    59: 49
}

# Permainan
posisi_pemain = 0

while posisi_pemain < 100:
    # Lempar dadu
    dadu1 = random.randint(1, 6)
    dadu2 = random.randint(1, 6)
    total_langkah = dadu1 + dadu2

    # Pindah posisi pemain
    posisi_pemain += total_langkah

    # Periksa tangga dan ular
    if posisi_pemain in tangga:
        posisi_pemain = tangga[posisi_pemain]
        print(f"Naik tangga ke {posisi_pemain}")
    elif posisi_pemain in ular:
        posisi_pemain = ular[posisi_pemain]
        print(f"Terkena ular ke {posisi_pemain}")

    # Cek kemenangan
    if posisi_pemain >= 100:
        print(f"Selamat! Anda menang!")
        break

    # Tampilkan posisi saat ini
    print(f"Posisi Anda: {posisi_pemain}")

# Pesan akhir
if posisi_pemain < 100:
    print(f"Game berakhir. Anda mencapai posisi {posisi_pemain}")
