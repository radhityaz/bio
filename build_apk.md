# Panduan Build APK untuk Android

## Metode 1: Menggunakan Buildozer (Linux/WSL)

### Persiapan Environment

1. **Install WSL** (jika menggunakan Windows):
```bash
wsl --install Ubuntu
```

2. **Install Dependencies** di WSL/Linux:
```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Install buildozer
pip3 install --user buildozer
```

3. **Build APK**:
```bash
# Masuk ke direktori project
cd /mnt/c/Users/"Radhitya Guntoro A"/Downloads/bio

# Build debug APK
buildozer android debug
```

## Metode 2: Menggunakan GitHub Actions (Otomatis)

1. **Upload project ke GitHub**
2. **Buat file** `.github/workflows/build-apk.yml`:

```yaml
name: Build Android APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install system dependencies
      run: |
        sudo apt update
        sudo apt install -y git zip unzip openjdk-8-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
    
    - name: Install buildozer
      run: pip install buildozer
    
    - name: Build APK
      run: buildozer android debug
    
    - name: Upload APK artifact
      uses: actions/upload-artifact@v3
      with:
        name: android-apk
        path: bin/*.apk
```

## Metode 3: Menggunakan Replit/Gitpod (Online)

### Replit:
1. Buka [replit.com](https://replit.com)
2. Import project dari GitHub
3. Install buildozer: `pip install buildozer`
4. Run: `buildozer android debug`

### Gitpod:
1. Buka [gitpod.io](https://gitpod.io)
2. Import project: `gitpod.io/#https://github.com/username/repo`
3. Install dependencies dan build

## Metode 4: Menggunakan Docker

1. **Buat Dockerfile**:
```dockerfile
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

RUN pip3 install buildozer

WORKDIR /app
COPY . .

RUN buildozer android debug
```

2. **Build dengan Docker**:
```bash
docker build -t kebugaran-app .
docker run -v $(pwd)/bin:/app/bin kebugaran-app
```

## Tips Troubleshooting

### Error umum dan solusi:

1. **Java version error**:
```bash
sudo update-alternatives --config java
# Pilih Java 8
```

2. **NDK error**:
```bash
# Edit buildozer.spec, ubah:
android.ndk = 25b
# menjadi:
android.ndk = 23c
```

3. **Memory error**:
```bash
# Tambahkan swap space
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

4. **Permission error**:
```bash
sudo chown -R $USER:$USER ~/.buildozer
```

## Hasil Build

Setelah build berhasil, file APK akan tersedia di:
- `bin/cekkebugaranharian-0.1-arm64-v8a-debug.apk`
- `bin/cekkebugaranharian-0.1-armeabi-v7a-debug.apk`

## Install APK ke Android

1. **Transfer APK** ke device Android
2. **Enable Unknown Sources** di Settings > Security
3. **Install APK** dengan file manager

## Catatan Penting

- Build APK memerlukan waktu 30-60 menit untuk pertama kali
- Ukuran APK sekitar 20-30 MB
- Untuk production, gunakan `buildozer android release`
- Untuk upload ke Play Store, perlu signing key