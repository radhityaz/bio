# 📱 Aplikasi Cek Kebugaran Harian

[![Build APK](https://github.com/username/repo/actions/workflows/build-apk.yml/badge.svg)](https://github.com/username/repo/actions/workflows/build-apk.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Kivy](https://img.shields.io/badge/Kivy-2.3.0-green.svg)](https://kivy.org/)

Aplikasi mobile cross-platform untuk mengecek kebugaran harian berdasarkan BMI, detak jantung, jumlah langkah, dan tingkat nyeri otot. Dibangun dengan Python Kivy dan dilengkapi CI/CD pipeline untuk build APK otomatis.

## ✨ Fitur

- 📊 **Kalkulasi BMI** dengan kategori (Kurus, Normal, Gemuk, Obesitas)
- ❤️ **Analisis detak jantung** istirahat dengan status kesehatan
- 🚶 **Tracking langkah harian** dengan target 8.000 langkah
- 💪 **Evaluasi nyeri otot** dengan rekomendasi perawatan
- 📱 **Interface mobile-friendly** dengan desain modern
- 🎯 **Rekomendasi kesehatan** personal berdasarkan data input
- 🤖 **Auto-build APK** dengan GitHub Actions
- 🔄 **Cross-platform** (Android, iOS, Windows, macOS, Linux)

## 🚀 Quick Start

### Untuk Pengguna (Download APK)

1. **Download APK** dari [GitHub Releases](https://github.com/username/repo/releases)
2. **Install di Android** (Enable Unknown Sources)
3. **Buka aplikasi** dan mulai cek kebugaran!

### Untuk Developer (Build dari Source)

```bash
# Clone repository
git clone https://github.com/username/repo.git
cd repo

# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
python main.py
```

### Build APK dengan GitHub Actions

```bash
# Setup repository (otomatis)
./setup_github.bat

# Atau manual push untuk trigger build
git add .
git commit -m "Trigger build"
git push origin main
```

📖 **Panduan lengkap:** [QUICK_START.md](QUICK_START.md) | [GITHUB_ACTIONS_TUTORIAL.md](GITHUB_ACTIONS_TUTORIAL.md)

## 🛠️ Framework yang Digunakan

**Kivy** - Framework Python terbaik untuk pengembangan aplikasi mobile cross-platform:
- ✅ **Cross-platform** (Android, iOS, Windows, macOS, Linux)
- ⚡ **Native performance** dengan OpenGL rendering
- 🎨 **Rich UI components** dan animasi
- 👆 **Touch-friendly interface** dengan gesture support
- 📦 **Easy deployment** ke mobile devices
- 🔧 **Mature ecosystem** dengan dokumentasi lengkap

## 💻 Instalasi dan Menjalankan

### 1. Persiapan Environment

```bash
# Install Python 3.8+ jika belum ada
# Buat virtual environment (opsional tapi direkomendasikan)
python -m venv venv

# Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Menjalankan Aplikasi

```bash
python main.py
```

## Build APK untuk Android

### Persiapan Build Environment

1. **Install Buildozer** (untuk Linux/WSL):
```bash
pip install buildozer
```

2. **Install Dependencies** (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

### Build APK

```bash
# Inisialisasi buildozer (hanya sekali)
buildozer android debug

# Build APK
buildozer android debug
```

File APK akan tersedia di folder `bin/`

## Alternatif Build dengan GitHub Actions

Untuk build otomatis, Anda bisa menggunakan GitHub Actions. Buat file `.github/workflows/build.yml`:

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
        pip install buildozer
    
    - name: Build APK
      run: buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: apk
        path: bin/*.apk
```

## Struktur Aplikasi

```
bio/
├── main.py              # File utama aplikasi Kivy
├── CekKebugaranHarian.py # Script Python original
├── requirements.txt      # Dependencies Python
├── buildozer.spec       # Konfigurasi build Android
└── README.md           # Dokumentasi ini
```

## Cara Menggunakan Aplikasi

1. **Buka aplikasi**
2. **Isi data berikut:**
   - Usia (tahun)
   - Berat badan (kg)
   - Tinggi badan (cm)
   - Detak jantung istirahat (BPM)
   - Jumlah langkah hari ini
   - Skor nyeri otot (1-10)
3. **Tekan tombol "CEK KEBUGARAN"**
4. **Lihat hasil analisis** yang mencakup:
   - Status BMI
   - Kondisi detak jantung
   - Progress langkah harian
   - Rekomendasi untuk nyeri otot

## Troubleshooting

### Error saat install Kivy
```bash
# Jika ada error, coba install dependencies sistem:
# Ubuntu/Debian:
sudo apt install python3-dev

# Windows: Install Microsoft Visual C++ Build Tools
```

### Build APK gagal
- Pastikan menggunakan Linux atau WSL
- Pastikan semua dependencies sistem terinstall
- Cek log error di `.buildozer/`

## Pengembangan Lanjutan

### Fitur yang bisa ditambahkan:
- 📊 Grafik progress harian/mingguan
- 💾 Penyimpanan data lokal
- 🔔 Notifikasi reminder
- 🎨 Tema dan customization
- 📤 Export data ke CSV
- 🏆 Achievement system

### Optimasi:
- Tambahkan validasi input yang lebih robust
- Implementasi database SQLite
- Tambahkan unit tests
- Optimasi performa UI

## Lisensi

MIT License - Bebas digunakan untuk keperluan personal dan komersial.