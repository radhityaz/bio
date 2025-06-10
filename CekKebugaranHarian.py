def cek_kebugaran():
    print("\n=== CEK KEBUGARAN HARIAN ===")
    print("Isi data berikut (angka saja):\n")
    
    # Input
    usia = int(input("1. Usia (tahun): "))
    berat = int(input("2. Berat badan (kg): "))
    tinggi = int(input("3. Tinggi badan (cm): "))
    detak_jantung = int(input("4. Detak jantung istirahat (BPM): "))
    langkah = int(input("5. Jumlah langkah hari ini: "))
    nyeri = int(input("6. Skor nyeri otot (1-10): "))

    # Kalkulasi
    bmi = berat / ((tinggi/100) ** 2)
    
    # Output
    print("\n===  HASIL ANALISIS ===")
    
    # 1. BMI
    if bmi < 18.5:
        kategori_bmi = "Kurus"
    elif 18.5 <= bmi < 25:
        kategori_bmi = "Normal"
    elif 25 <= bmi < 30:
        kategori_bmi = "Gemuk"
    else:
        kategori_bmi = "Obesitas"
    print(f" BMI Anda: {bmi:.1f} ({kategori_bmi})")

    # 2. Kebugaran jantung
    if detak_jantung < 60:
        status_jantung = "Sangat baik (atletik)"
    elif 60 <= detak_jantung < 80:
        status_jantung = "Baik"
    else:
        status_jantung = "Perlu perhatian"
    print(f" Detak jantung istirahat: {detak_jantung} ({status_jantung})")

    # 3. Saran langkah
    target_langkah = 8000
    if langkah < target_langkah:
        print(f"Langkah hari ini: {langkah} (Kurang {target_langkah - langkah} dari target 8.000)")
    else:
        print(f" Langkah hari ini: {langkah} (Target tercapai!)")

    # 4. Rekomendasi peregangan
    if nyeri <= 3:
        print(" Nyeri otot rendah  Lanjutkan aktivitas normal!")
    elif 4 <= nyeri <= 6:
        print(" Nyeri otot sedang Lakukan peregangan 5 menit")
    else:
        print(" Nyeri otot tinggi Istirahatkan otot + kompres hangat!")

cek_kebugaran()