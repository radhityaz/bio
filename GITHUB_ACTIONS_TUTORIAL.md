# 🚀 Tutorial Build APK dengan GitHub Actions

Panduan lengkap untuk setup dan menggunakan GitHub Actions untuk build APK Android secara otomatis.

## 📋 Daftar Isi

1. [Persiapan Repository](#persiapan-repository)
2. [Setup GitHub Actions](#setup-github-actions)
3. [Konfigurasi Secrets](#konfigurasi-secrets)
4. [Menjalankan Build](#menjalankan-build)
5. [Download APK](#download-apk)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Setup](#advanced-setup)

## 🔧 Persiapan Repository

### 1. Upload Project ke GitHub

```bash
# Inisialisasi git repository
git init

# Tambahkan semua file
git add .

# Commit pertama
git commit -m "Initial commit: Aplikasi Cek Kebugaran Harian"

# Tambahkan remote repository (ganti dengan URL repo Anda)
git remote add origin https://github.com/username/cek-kebugaran-harian.git

# Push ke GitHub
git branch -M main
git push -u origin main
```

### 2. Verifikasi File yang Diperlukan

Pastikan file-file berikut ada di repository:

```
✅ .github/workflows/build-apk.yml
✅ .gitignore
✅ buildozer.spec
✅ requirements.txt
✅ main.py
✅ CekKebugaranHarian.py
```

## ⚙️ Setup GitHub Actions

### File Workflow Sudah Dibuat

File `.github/workflows/build-apk.yml` sudah otomatis dibuat dengan fitur:

- ✅ **Auto-trigger** pada push ke main/master
- ✅ **Manual trigger** dengan pilihan debug/release
- ✅ **Caching** untuk mempercepat build
- ✅ **Multi-architecture** support (arm64-v8a, armeabi-v7a)
- ✅ **Automatic versioning** dari buildozer.spec
- ✅ **APK signing** untuk release
- ✅ **Auto-upload** ke GitHub Releases

### Trigger Otomatis

Workflow akan berjalan otomatis ketika:
- Push ke branch `main` atau `master`
- Membuat Pull Request
- Manual trigger dari GitHub UI

## 🔐 Konfigurasi Secrets (Opsional)

### Untuk Release Build dengan Signing

1. **Buka Repository Settings**
   - Masuk ke repository GitHub
   - Klik **Settings** → **Secrets and variables** → **Actions**

2. **Tambahkan Secrets Berikut:**

   | Secret Name | Description | Required |
   |-------------|-------------|----------|
   | `KEYSTORE_BASE64` | Base64 encoded keystore file | Release only |
   | `KEYSTORE_PASSWORD` | Password untuk keystore | Release only |
   | `KEY_ALIAS` | Alias key dalam keystore | Release only |
   | `KEY_PASSWORD` | Password untuk key | Release only |
   | `GOOGLE_PLAY_SERVICE_ACCOUNT` | JSON service account | Play Store upload |

### Cara Membuat Keystore

```bash
# Generate keystore baru
keytool -genkey -v -keystore my-release-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-key-alias

# Convert ke base64 untuk GitHub Secrets
base64 -i my-release-key.jks | pbcopy  # macOS
base64 -w 0 my-release-key.jks          # Linux
certutil -encode my-release-key.jks tmp.b64 && findstr /v /c:- tmp.b64  # Windows
```

## 🏃‍♂️ Menjalankan Build

### Method 1: Auto Build (Push ke Repository)

```bash
# Buat perubahan
echo "# Update" >> README.md

# Commit dan push
git add .
git commit -m "Trigger build"
git push origin main
```

### Method 2: Manual Build

1. **Buka GitHub Repository**
2. **Klik tab "Actions"**
3. **Pilih "Build Android APK"**
4. **Klik "Run workflow"**
5. **Pilih build type:**
   - `debug` - untuk testing
   - `release` - untuk production
6. **Klik "Run workflow"**

### Method 3: Release Build dengan Tag

```bash
# Buat tag untuk release
git tag v1.0.0
git push origin v1.0.0
```

## 📱 Download APK

### Dari GitHub Actions Artifacts

1. **Buka tab "Actions"**
2. **Klik pada workflow run yang sudah selesai**
3. **Scroll ke bawah ke bagian "Artifacts"**
4. **Download file APK** (format: `android-apk-vX.X.X`)

### Dari GitHub Releases (jika menggunakan tag)

1. **Buka tab "Releases"**
2. **Download APK** dari release terbaru

## 🔍 Monitoring Build

### Melihat Progress Build

1. **Buka tab "Actions"**
2. **Klik pada workflow yang sedang berjalan**
3. **Klik pada job "build"**
4. **Expand step untuk melihat detail log**

### Status Build

- 🟡 **Yellow dot** - Build sedang berjalan
- ✅ **Green checkmark** - Build berhasil
- ❌ **Red X** - Build gagal

## 🐛 Troubleshooting

### Build Gagal - Common Issues

#### 1. **Java Version Error**
```
Error: Could not find or load main class
```
**Solusi:** Workflow sudah menggunakan Java 8, seharusnya tidak ada masalah.

#### 2. **NDK Error**
```
NDK not found
```
**Solusi:** Edit `buildozer.spec`, ubah:
```
android.ndk = 25b
# menjadi:
android.ndk = 23c
```

#### 3. **Memory Error**
```
Out of memory
```
**Solusi:** Workflow sudah menggunakan caching, retry build.

#### 4. **Permission Error**
```
Permission denied
```
**Solusi:** Pastikan tidak ada file yang di-commit dengan permission salah.

### Debug Build Issues

1. **Enable debug logging** di buildozer.spec:
```
[buildozer]
log_level = 2
```

2. **Cek log detail** di GitHub Actions

3. **Test build lokal** dengan Docker:
```bash
docker run --rm -v "$(pwd)":/home/user/hostcwd kivy/buildozer android debug
```

## 🚀 Advanced Setup

### Auto-increment Version

Tambahkan step untuk auto-increment version:

```yaml
- name: Auto-increment version
  run: |
    VERSION=$(grep "^version" buildozer.spec | cut -d'=' -f2 | tr -d ' ')
    NEW_VERSION=$(echo $VERSION | awk -F. '{$NF = $NF + 1;} 1' | sed 's/ /./g')
    sed -i "s/version = $VERSION/version = $NEW_VERSION/" buildozer.spec
    git config --local user.email "action@github.com"
    git config --local user.name "GitHub Action"
    git add buildozer.spec
    git commit -m "Auto-increment version to $NEW_VERSION" || exit 0
    git push
```

### Parallel Builds

Build multiple architectures secara parallel:

```yaml
strategy:
  matrix:
    arch: [armeabi-v7a, arm64-v8a]
steps:
  - name: Build APK
    run: buildozer android debug --arch ${{ matrix.arch }}
```

### Notification Setup

Tambahkan notifikasi Discord/Slack:

```yaml
- name: Notify Discord
  if: always()
  uses: sarisia/actions-status-discord@v1
  with:
    webhook: ${{ secrets.DISCORD_WEBHOOK }}
    status: ${{ job.status }}
    title: "APK Build"
    description: "Build completed for commit ${{ github.sha }}"
```

### Testing Integration

Tambahkan automated testing:

```yaml
- name: Run tests
  run: |
    pip install pytest
    pytest tests/ -v
```

## 📊 Build Statistics

### Typical Build Times

- **First build:** 15-25 menit (download dependencies)
- **Cached build:** 5-10 menit
- **Release build:** 10-15 menit (dengan signing)

### APK Size

- **Debug APK:** ~25-30 MB
- **Release APK:** ~20-25 MB (dengan ProGuard)

## 🎯 Best Practices

### 1. **Version Management**
- Gunakan semantic versioning (1.0.0)
- Update version di buildozer.spec sebelum release
- Gunakan tags untuk release builds

### 2. **Branch Strategy**
- `main/master` - production ready code
- `develop` - development branch
- `feature/*` - feature branches

### 3. **Security**
- Jangan commit keystore files
- Gunakan GitHub Secrets untuk sensitive data
- Review permissions pada Actions

### 4. **Performance**
- Gunakan caching untuk dependencies
- Build hanya ketika diperlukan
- Cleanup artifacts lama

## 📞 Support

Jika mengalami masalah:

1. **Cek GitHub Actions logs** untuk error detail
2. **Review buildozer.spec** configuration
3. **Test build lokal** dengan buildozer
4. **Buka issue** di repository untuk bantuan

---

🎉 **Selamat!** Anda sekarang memiliki CI/CD pipeline untuk build APK Android secara otomatis!