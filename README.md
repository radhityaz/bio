# Aplikasi Cek Kebugaran Harian

Aplikasi mobile untuk mengecek kebugaran harian berdasarkan BMI, detak jantung, langkah harian, dan tingkat nyeri otot.

## Fitur

- ✅ Kalkulasi BMI dengan kategori
- ❤️ Analisis detak jantung istirahat
- 🚶 Tracking langkah harian
- 💪 Evaluasi nyeri otot
- 📱 UI yang user-friendly untuk mobile
- 🎯 Rekomendasi kesehatan personal

## Perbaikan dari Kode Asli

1. **UI Modern**: Menggunakan Kivy framework dengan desain yang responsif
2. **Validasi Input**: Pengecekan input yang lebih robust
3. **Error Handling**: Penanganan error yang lebih baik
4. **Mobile-Ready**: Optimized untuk layar sentuh
5. **Visual Feedback**: Popup hasil dengan emoji dan formatting yang menarik

## Cara Menjalankan (Development)

### Prerequisites
```bash
pip install -r requirements.txt
```

### Jalankan Aplikasi
```bash
python main.py
```

## Build APK untuk Android

### Method 1: Menggunakan Buildozer (Linux/WSL)

1. **Install Buildozer**:
```bash
pip install buildozer
```

2. **Install Dependencies** (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

3. **Build APK**:
```bash
buildozer android debug
```

4. **APK akan tersedia di**: `bin/kebugaranharian-1.0-arm64-v8a-debug.apk`

### Method 2: Menggunakan GitHub Actions (Recommended)

Untuk build otomatis, gunakan GitHub Actions dengan workflow berikut:

```yaml
name: Build APK

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        sudo apt update
        sudo apt install -y git zip unzip openjdk-8-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
        pip install buildozer cython
    
    - name: Build APK
      run: buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: apk
        path: bin/*.apk
```

### Method 3: Menggunakan Google Colab

1. Buka Google Colab
2. Upload semua file project
3. Jalankan:

```python
!apt update
!apt install -y git zip unzip openjdk-8-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
!pip install buildozer cython
!buildozer android debug
```

## Struktur Project

```
bio/
├── main.py              # Aplikasi utama dengan UI Kivy
├── CekKebugaranHarian.py # Kode asli (untuk referensi)
├── buildozer.spec       # Konfigurasi build APK
├── requirements.txt     # Dependencies Python
└── README.md           # Dokumentasi ini
```

## Konfigurasi APK

- **Package Name**: org.example.kebugaranharian
- **Version**: 1.0
- **Target API**: 31
- **Min API**: 21
- **Architecture**: arm64-v8a, armeabi-v7a
- **Orientation**: Portrait

## Troubleshooting

### Error: "Command failed: gradlew assembleDebug"
- Pastikan Java 8 terinstall
- Cek koneksi internet untuk download dependencies

### Error: "No module named 'kivy'"
```bash
pip install kivy
```

### Build terlalu lama
- Gunakan GitHub Actions atau Google Colab
- Pastikan RAM minimal 4GB

## Kontribusi

Silakan buat pull request untuk perbaikan atau fitur baru!

## Lisensi

MIT License - bebas digunakan untuk keperluan apapun.