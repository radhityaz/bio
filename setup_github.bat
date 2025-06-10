@echo off
echo ========================================
echo    SETUP GITHUB REPOSITORY
echo    Aplikasi Cek Kebugaran Harian
echo ========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git tidak terinstall!
    echo Silakan install Git terlebih dahulu: https://git-scm.com/
    pause
    exit /b 1
)

echo [1/6] Inisialisasi Git repository...
git init
if errorlevel 1 (
    echo ERROR: Gagal inisialisasi git repository
    pause
    exit /b 1
)

echo [2/6] Menambahkan semua file...
git add .
if errorlevel 1 (
    echo ERROR: Gagal menambahkan file
    pause
    exit /b 1
)

echo [3/6] Membuat commit pertama...
git commit -m "Initial commit: Aplikasi Cek Kebugaran Harian dengan GitHub Actions"
if errorlevel 1 (
    echo ERROR: Gagal membuat commit
    pause
    exit /b 1
)

echo [4/6] Setup branch main...
git branch -M main

echo.
echo ========================================
echo    SETUP REMOTE REPOSITORY
echo ========================================
echo.
echo Silakan buat repository baru di GitHub terlebih dahulu:
echo 1. Buka https://github.com/new
echo 2. Beri nama repository (contoh: cek-kebugaran-harian)
echo 3. Jangan centang "Initialize with README"
echo 4. Klik "Create repository"
echo.
set /p repo_url="Masukkan URL repository GitHub (https://github.com/username/repo.git): "

if "%repo_url%"=="" (
    echo ERROR: URL repository tidak boleh kosong!
    pause
    exit /b 1
)

echo [5/6] Menambahkan remote origin...
git remote add origin %repo_url%
if errorlevel 1 (
    echo ERROR: Gagal menambahkan remote origin
    pause
    exit /b 1
)

echo [6/6] Push ke GitHub...
git push -u origin main
if errorlevel 1 (
    echo ERROR: Gagal push ke GitHub
    echo Pastikan:
    echo - URL repository benar
    echo - Anda sudah login ke Git (git config user.name dan user.email)
    echo - Repository sudah dibuat di GitHub
    pause
    exit /b 1
)

echo.
echo ========================================
echo           SETUP BERHASIL!
echo ========================================
echo.
echo ✅ Repository berhasil di-upload ke GitHub
echo ✅ GitHub Actions sudah dikonfigurasi
echo ✅ Workflow akan berjalan otomatis pada push berikutnya
echo.
echo LANGKAH SELANJUTNYA:
echo 1. Buka repository di GitHub
echo 2. Klik tab "Actions" untuk melihat workflow
echo 3. Build APK akan berjalan otomatis
echo 4. Download APK dari "Artifacts" setelah build selesai
echo.
echo DOKUMENTASI:
echo - README.md: Dokumentasi aplikasi
echo - GITHUB_ACTIONS_TUTORIAL.md: Tutorial lengkap GitHub Actions
echo - build_apk.md: Panduan build APK alternatif
echo.
echo Repository URL: %repo_url%
echo.
pause