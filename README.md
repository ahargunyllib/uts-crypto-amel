# UTS Kriptografi - Dekripsi 10 Cipher

## 📊 Status Saat Ini

**✅ Selesai: 5/10 cipher**
- Cipher #1: Caesar (shift 4)
- Cipher #2: Caesar (shift 14)
- Cipher #3: Vigenere (key: BERIKUT)
- Cipher #4: Route Cipher (interval 4)
- Cipher #5: Transposition (Samuel Morland)

**⚠️ Partial: 5/10 cipher** (menunggu kunci dari Google Forms)
- Cipher #6: Playfair (butuh kunci dari Form #5)
- Cipher #7-10: ADFGVX (butuh kunci dari Form #4 dan #5)

## 📁 File Penting

### Dokumentasi
- **`laporan_cryptography.md`** - Laporan lengkap (5 bagian, 10 cipher) ⭐
- **`DECRYPTION_STATUS.md`** - Status detail semua cipher
- **`README.md`** - File ini

### Scripts Python
- **`decrypt_helper.py`** - Fungsi dekripsi untuk semua jenis cipher
- **`decrypt_with_form_keys.py`** - Script interaktif untuk dekripsi #6-10 ⭐
- **`decrypt_remaining_ciphers.py`** - Script otomatis untuk coba berbagai kunci
- **`analyze_updated_cipher.py`** - Analisis struktur cipher.txt
- **`extract_keys_from_plaintext.py`** - Extract kunci potensial dari plaintext

### Data
- **`cipher.txt`** - File ciphertext asli

## 🚀 Cara Melanjutkan Dekripsi

### Langkah 1: Akses Google Forms

Anda perlu mengakses 2 Google Forms yang URL-nya sudah didekripsi:

**Form #4** (dari Cipher #4):
- URL: [Hasil dekripsi Cipher #4]
- Isi form dengan jawaban dari Cipher #1-3
- Catat hint yang diberikan untuk Cipher #7-10
- Hint yang sudah diketahui: **AA = 8**

**Form #5**:
- URL: `rXMVG2LctCrxoauk7`
- Isi form dengan jawaban dari Cipher #1-4
- Catat kunci Playfair untuk Cipher #6
- Hint yang sudah diketahui: "square dengan i dan j dalam satu sel"

### Langkah 2: Dekripsi dengan Kunci dari Form

Setelah mendapat kunci dari form, jalankan script interaktif:

```bash
python3 decrypt_with_form_keys.py
```

Script ini akan:
1. Meminta kunci Playfair untuk Cipher #6
2. Meminta kunci ADFGVX untuk Cipher #7-10
3. Melakukan dekripsi otomatis
4. Menyimpan hasil ke file `results_cipher6.txt` dan `results_cipher7_10.txt`

### Langkah 3: Update Laporan

Setelah semua cipher berhasil didekripsi, update `laporan_cryptography.md`:
- Tambahkan hasil dekripsi Cipher #6 di Bagian 4
- Tambahkan hasil dekripsi Cipher #7-10 di Bagian 5
- Update status dari "Partial" menjadi "Selesai"

## 🔑 Informasi Kunci yang Sudah Diketahui

### Cascade Dependency
```
Cipher #1 (shift 4)
    ↓ memberikan konteks
Cipher #2 (shift 14)
    ↓ memberikan key "PACKAGER"
Cipher #3 (key: BERIKUT)
    ↓ memberikan algoritma "Samuel Morland"
Cipher #4 (interval 4)
    ↓ memberikan Form URL + hint AA=8
Cipher #5 (Samuel Morland)
    ↓ memberikan Form URL: rXMVG2LctCrxoauk7
Cipher #6 (Playfair)
    ↓ key dari Form #5
Cipher #7-10 (ADFGVX)
    ↓ key dari Form #4 dan #5
    ↓ hint: AA = 8
```

### Kunci yang Sudah Berhasil
- **Cipher #1**: Caesar shift = 4
- **Cipher #2**: Caesar shift = 14
- **Cipher #3**: Vigenere key = BERIKUT (dari hasil #1)
- **Cipher #4**: Route interval = 4 (dari hint Samuel Morland)
- **Cipher #5**: Transposition (algoritma Samuel Morland)

### Kunci yang Masih Dibutuhkan
- **Cipher #6**: Playfair key = ??? (dari Form #5)
- **Cipher #7**: ADFGVX polybius key = 8??? + transposition key = ???
- **Cipher #8**: ADFGVX polybius key = 8??? + transposition key = ???
- **Cipher #9**: ADFGVX polybius key = 8??? + transposition key = ???
- **Cipher #10**: ADFGVX polybius key = 8??? + transposition key = ???

### Hint yang Ada
- **AA = 8**: Polybius square untuk ADFGVX dimulai dengan '8' di posisi [A,A]
- **Samuel Morland**: Algoritma transposisi untuk Cipher #4-6
- **Playfair square**: I dan J dalam satu sel (standard Playfair)

## 📖 Referensi Teknis

### Caesar Cipher
- Shift: 0-25
- Formula: `plaintext = (ciphertext - shift) mod 26`

### Vigenere Cipher
- Polyalphabetic substitution
- Formula: `plaintext[i] = (ciphertext[i] - key[i mod len(key)]) mod 26`

### Route/Rail Fence Cipher
- Transposition cipher
- Read every nth character (interval)

### Playfair Cipher
- 5×5 grid with I/J combined
- Digraph encryption (2 chars at a time)
- Rules: same row, same column, rectangle

### ADFGVX Cipher
- Two-layer cipher:
  1. Polybius square (6×6) → ADFGVX pairs
  2. Columnar transposition
- Uses only letters: A, D, F, G, V, X

## 🛠️ Troubleshooting

### Jika dekripsi gagal:
1. Pastikan kunci sudah benar dari form
2. Untuk ADFGVX, pastikan polybius key dimulai dengan '8'
3. Cek apakah ciphertext sudah diekstrak dengan benar
4. Jalankan `python3 analyze_updated_cipher.py` untuk verifikasi

### Jika ada error:
1. Pastikan semua dependencies terinstall: `pip3 install -r requirements.txt` (jika ada)
2. Pastikan Python 3.6+ terinstall
3. Cek encoding file (harus UTF-8)

## 📝 Catatan

- Semua cipher menggunakan metode klasik (pre-computer era)
- Sistem cascade: hasil cipher sebelumnya mempengaruhi cipher berikutnya
- Google Forms digunakan sebagai "key distribution system"
- Total ada 10 cipher dalam 5 bagian (sesuai struktur laporan)

## 🎯 Next Steps

1. ✅ Cipher #1-5 sudah selesai
2. ⏳ Akses Form #4 untuk mendapat kunci ADFGVX
3. ⏳ Akses Form #5 untuk mendapat kunci Playfair
4. ⏳ Jalankan `decrypt_with_form_keys.py`
5. ⏳ Update `laporan_cryptography.md`
6. ⏳ Verifikasi semua hasil
7. ⏳ Selesai! 🎉

## 📧 Support

Jika ada pertanyaan atau issues, cek file-file berikut:
- `DECRYPTION_STATUS.md` - Status detail
- `laporan_cryptography.md` - Dokumentasi lengkap
- Script comments - Penjelasan teknis

---

**Last Updated**: 2025-11-01
**Status**: 5/10 cipher complete, waiting for form keys
