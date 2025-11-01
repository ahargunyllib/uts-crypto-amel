#!/usr/bin/env python3
"""
Script untuk dekripsi cipher #6-10 setelah mendapat kunci dari form
Masukkan kunci yang didapat dari Google Forms
"""

from decrypt_helper import *
import re

# Read cipher.txt
with open('cipher.txt', 'r') as f:
    lines = f.readlines()

# Extract ciphers
cipher6 = lines[6].strip()

line9 = lines[8].strip()
cipher7_10 = ''.join([c for c in line9 if c.isupper()])

r_pos = cipher7_10.index('R')
b_pos = cipher7_10.index('B')
p_pos = cipher7_10.index('P')

cipher7 = cipher7_10[:r_pos]
cipher8 = cipher7_10[r_pos+1:b_pos]
cipher9 = cipher7_10[b_pos+1:p_pos]
cipher10 = cipher7_10[p_pos+1:]

print("=" * 80)
print("DEKRIPSI CIPHER #6-10 DENGAN KUNCI DARI FORM")
print("=" * 80)

# ============================================================================
# CIPHER #6 - PLAYFAIR
# ============================================================================
print("\n" + "=" * 80)
print("CIPHER #6 - PLAYFAIR")
print("=" * 80)
print(f"Ciphertext: {cipher6}")
print(f"Length: {len(cipher6)}")
print("\nHint dari Form #5: 'square dengan i dan j dalam satu sel' → Playfair")
print("\nMasukkan kunci Playfair yang didapat dari Form #5:")
print("(Jika tidak ada, tekan Enter untuk skip)")

playfair_key = input("Kunci Playfair: ").strip()

if playfair_key:
    try:
        result = playfair_decrypt(cipher6, playfair_key)
        print(f"\n✅ Hasil dekripsi Cipher #6:")
        print(f"   {result}")

        # Save result
        with open('results_cipher6.txt', 'w') as f:
            f.write(f"Cipher #6 (Playfair)\n")
            f.write(f"Key: {playfair_key}\n")
            f.write(f"Result: {result}\n")
        print(f"\n💾 Hasil disimpan ke results_cipher6.txt")
    except Exception as e:
        print(f"\n❌ Error: {e}")
else:
    print("\n⏭️  Skipped Cipher #6")

# ============================================================================
# CIPHER #7-10 - ADFGVX
# ============================================================================
print("\n" + "=" * 80)
print("CIPHER #7-10 - ADFGVX")
print("=" * 80)
print("\nHint dari Form #4: AA = 8")
print("Artinya: Polybius square dimulai dengan '8' di posisi [A,A]")
print("\nADFGVX cipher memerlukan 2 kunci:")
print("  1. Polybius key (untuk polybius square 6x6)")
print("  2. Transposition key (untuk columnar transposition)")

# Common settings for all ADFGVX ciphers
print("\n" + "-" * 80)
print("Masukkan kunci yang sama untuk semua ADFGVX cipher (7-10):")
print("Atau masukkan kunci berbeda untuk setiap cipher di bawah ini.")
print("-" * 80)

# Ask for common keys first
print("\nKunci umum untuk semua cipher (kosongkan jika ingin input per cipher):")
common_polybius = input("  Polybius key (harus dimulai dengan '8'): ").strip()
common_trans = input("  Transposition key: ").strip()

results = {}

# Decrypt each cipher
for idx, cipher in [(7, cipher7), (8, cipher8), (9, cipher9), (10, cipher10)]:
    print(f"\n{'=' * 80}")
    print(f"CIPHER #{idx}")
    print(f"{'=' * 80}")
    print(f"Length: {len(cipher)} chars")
    print(f"First 80 chars: {cipher[:80]}...")

    # Get keys
    if common_polybius and common_trans:
        polybius_key = common_polybius
        trans_key = common_trans
        print(f"\nMenggunakan kunci umum:")
    else:
        print(f"\nMasukkan kunci untuk Cipher #{idx}:")
        polybius_key = input(f"  Polybius key (harus dimulai dengan '8'): ").strip()
        trans_key = input(f"  Transposition key: ").strip()

    if polybius_key and trans_key:
        # Ensure polybius key starts with 8
        if not polybius_key.startswith('8'):
            print(f"\n⚠️  Warning: Polybius key tidak dimulai dengan '8', menambahkan '8' di awal...")
            polybius_key = '8' + polybius_key

        try:
            result = adfgvx_decrypt(cipher, polybius_key, trans_key)
            print(f"\n✅ Hasil dekripsi Cipher #{idx}:")
            print(f"   Polybius key: {polybius_key}")
            print(f"   Transposition key: {trans_key}")
            print(f"   Result: {result}")

            results[idx] = {
                'polybius_key': polybius_key,
                'trans_key': trans_key,
                'result': result
            }
        except Exception as e:
            print(f"\n❌ Error: {e}")
    else:
        print(f"\n⏭️  Skipped Cipher #{idx}")

# Save all ADFGVX results
if results:
    print(f"\n{'=' * 80}")
    print("MENYIMPAN HASIL")
    print(f"{'=' * 80}")

    with open('results_cipher7_10.txt', 'w') as f:
        f.write("HASIL DEKRIPSI CIPHER #7-10 (ADFGVX)\n")
        f.write("=" * 80 + "\n\n")

        for idx in sorted(results.keys()):
            f.write(f"Cipher #{idx}:\n")
            f.write(f"  Polybius key: {results[idx]['polybius_key']}\n")
            f.write(f"  Transposition key: {results[idx]['trans_key']}\n")
            f.write(f"  Result: {results[idx]['result']}\n")
            f.write("\n")

    print(f"💾 Hasil disimpan ke results_cipher7_10.txt")

# Final summary
print(f"\n{'=' * 80}")
print("RINGKASAN")
print(f"{'=' * 80}")
print("\nCipher yang berhasil didekripsi:")
if playfair_key:
    print("  ✅ Cipher #6 (Playfair)")
for idx in sorted(results.keys()):
    print(f"  ✅ Cipher #{idx} (ADFGVX)")

print("\nFile hasil:")
if playfair_key:
    print("  📄 results_cipher6.txt")
if results:
    print("  📄 results_cipher7_10.txt")

print("\nLangkah selanjutnya:")
print("  1. Verifikasi hasil dekripsi")
print("  2. Update laporan_cryptography.md dengan hasil lengkap")
print("  3. Selesai! 🎉")
