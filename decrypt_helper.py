#!/usr/bin/env python3
"""
Helper script untuk dekripsi berbagai classical cipher
"""

import string
from collections import Counter
import re

def frequency_analysis(text):
    """Analisis frekuensi huruf dalam text"""
    text = ''.join(filter(str.isalpha, text.upper()))
    freq = Counter(text)
    total = len(text)
    print(f"\nFrequency Analysis (total: {total} letters):")
    for char, count in freq.most_common(10):
        print(f"{char}: {count} ({count/total*100:.2f}%)")
    return freq

def caesar_decrypt(ciphertext, shift):
    """Dekripsi Caesar cipher dengan shift tertentu"""
    result = []
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def caesar_bruteforce(ciphertext):
    """Coba semua kemungkinan shift Caesar"""
    print("\nCaesar Bruteforce:")
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift:2d}: {decrypted[:60]}...")

def vigenere_decrypt(ciphertext, key):
    """Dekripsi Vigenere cipher"""
    result = []
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)

def kasiski_examination(ciphertext):
    """Cari repeated sequences untuk menentukan panjang key Vigenere"""
    text = ''.join(filter(str.isalpha, ciphertext.upper()))
    sequences = {}

    # Cari trigrams yang berulang
    for length in range(3, 6):
        for i in range(len(text) - length):
            seq = text[i:i+length]
            if seq in sequences:
                sequences[seq].append(i)
            else:
                sequences[seq] = [i]

    print("\nRepeated sequences (Kasiski):")
    for seq, positions in sorted(sequences.items()):
        if len(positions) > 1:
            distances = [positions[i+1] - positions[i] for i in range(len(positions)-1)]
            print(f"{seq}: positions {positions}, distances {distances}")

def columnar_decrypt(ciphertext, key):
    """Dekripsi Columnar Transposition"""
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    n_cols = len(key)
    n_rows = len(ciphertext) // n_cols
    remainder = len(ciphertext) % n_cols

    # Buat grid
    grid = [''] * n_cols
    index = 0

    for col in key_order:
        col_length = n_rows + (1 if col < remainder else 0)
        grid[col] = ciphertext[index:index + col_length]
        index += col_length

    # Baca secara horizontal
    result = []
    for row in range(n_rows + 1):
        for col in range(n_cols):
            if row < len(grid[col]):
                result.append(grid[col][row])

    return ''.join(result)

def playfair_decrypt(ciphertext, key):
    """Dekripsi Playfair cipher"""
    # Buat matrix 5x5
    key = key.upper().replace('J', 'I')
    matrix = []
    used = set()

    for char in key:
        if char not in used and char.isalpha():
            matrix.append(char)
            used.add(char)

    for char in string.ascii_uppercase:
        if char not in used and char != 'J':
            matrix.append(char)
            used.add(char)

    # Buat dictionary posisi
    pos = {}
    for i, char in enumerate(matrix):
        pos[char] = (i // 5, i % 5)

    # Dekripsi
    ciphertext = ciphertext.upper().replace('J', 'I')
    ciphertext = ''.join(filter(str.isalpha, ciphertext))
    result = []

    for i in range(0, len(ciphertext), 2):
        if i + 1 >= len(ciphertext):
            break

        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = pos[a]
        row2, col2 = pos[b]

        if row1 == row2:  # Same row
            result.append(matrix[row1 * 5 + (col1 - 1) % 5])
            result.append(matrix[row2 * 5 + (col2 - 1) % 5])
        elif col1 == col2:  # Same column
            result.append(matrix[((row1 - 1) % 5) * 5 + col1])
            result.append(matrix[((row2 - 1) % 5) * 5 + col2])
        else:  # Rectangle
            result.append(matrix[row1 * 5 + col2])
            result.append(matrix[row2 * 5 + col1])

    return ''.join(result)

def adfgvx_decrypt(ciphertext, polybius_key, transposition_key):
    """Dekripsi ADFGVX cipher"""
    # Create reverse polybius square
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    adfgvx = "ADFGVX"

    polybius_square = {}
    key_string = polybius_key.upper() + alphabet
    used = set()
    chars = []

    for char in key_string:
        if char not in used and char in alphabet:
            chars.append(char)
            used.add(char)

    # Create polybius mapping
    for i, char in enumerate(chars):
        row, col = i // 6, i % 6
        polybius_square[adfgvx[row] + adfgvx[col]] = char

    # Reverse columnar transposition
    ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))
    decrypted_pairs = columnar_decrypt(ciphertext, transposition_key)

    # Decode pairs
    result = []
    for i in range(0, len(decrypted_pairs), 2):
        if i + 1 < len(decrypted_pairs):
            pair = decrypted_pairs[i:i+2]
            if pair in polybius_square:
                result.append(polybius_square[pair])

    return ''.join(result)

if __name__ == "__main__":
    print("Classical Cipher Decryption Helper")
    print("=" * 50)
