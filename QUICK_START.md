# 🚀 Quick Start Guide - Build APK dengan GitHub Actions

## ⚡ Setup Cepat (5 Menit)

### 1. Persiapan GitHub Repository

```bash
# Jalankan script otomatis
setup_github.bat
```

**ATAU manual:**

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

### 2. Trigger Build APK

**Otomatis:** Push apapun ke repository akan trigger build

**Manual:**
1. Buka repository di GitHub
2. Klik tab **"Actions"**
3. Pilih **"Build Android APK"**
4. Klik **"Run workflow"** → **"Run workflow"**

### 3. Download APK

1. Tunggu build selesai (15-25 menit)
2. Klik pada workflow yang sudah selesai
3. Scroll ke **"Artifacts"**
4. Download **"android-apk-vX.X.X"**
5. Extract ZIP → Install APK ke Android

---

## 📱 Test Aplikasi Lokal

```bash
# Install dependencies
pip install kivy

# Jalankan aplikasi
python main.py

# ATAU
run_app.bat
```

---

## 🔧 File Penting

| File | Fungsi |
|------|--------|
| `.github/workflows/build-apk.yml` | 🤖 GitHub Actions workflow |
| `buildozer.spec` | ⚙️ Konfigurasi build APK |
| `main.py` | 📱 Aplikasi Kivy utama |
| `requirements.txt` | 📦 Dependencies Python |
| `.gitignore` | 🚫 File yang diabaikan Git |

---

## 🎯 Hasil Build

✅ **APK Debug:** `cek-kebugaran-harian-v1.0.0-debug.apk`  
✅ **Size:** ~25-30 MB  
✅ **Support:** Android 5.0+ (API 21+)  
✅ **Architecture:** ARM64 + ARMv7  

---

## 🆘 Troubleshooting Cepat

### Build Gagal?
1. **Cek log** di GitHub Actions
2. **Retry build** (sering berhasil di attempt kedua)
3. **Edit buildozer.spec** jika ada error NDK

### APK Tidak Bisa Install?
1. **Enable Unknown Sources** di Android
2. **Download ulang** APK (mungkin corrupt)
3. **Coba APK architecture lain**

### Aplikasi Crash?
1. **Cek Android version** (minimal 5.0)
2. **Restart device**
3. **Clear app data**

---

## 📚 Dokumentasi Lengkap

- 📖 **README.md** - Dokumentasi aplikasi
- 🔧 **GITHUB_ACTIONS_TUTORIAL.md** - Tutorial lengkap
- 🏗️ **build_apk.md** - Metode build alternatif

---

## 🎉 Selesai!

Anda sekarang memiliki:
- ✅ Aplikasi mobile yang berfungsi
- ✅ CI/CD pipeline otomatis
- ✅ APK yang siap distribusi
- ✅ Dokumentasi lengkap

**Happy coding! 🚀**