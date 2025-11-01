ciphertext = "lrwndrnqciifqrlaqdoevzgnkeinfrlnjrltqiigorynpxdvilnnmrnhpkuxufaypfmbtvmccksnogavgeazarigwueairncgkuallkfcdurndoenrnq"

def vigenere_decrypt(ciphertext, key):
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

# TODO: key is already found. find a way to discover the key programmatically
keys_to_try = ["cran"]

for key in keys_to_try:
    decrypted = vigenere_decrypt(ciphertext, key)
    print(f"Trying key: {key}")
    print("Decrypted message:", decrypted + "\n")

# plaintext:
# jawabandarisoalnomortigainiadalahalgoritmayangdigunakanuntuksoalnomorempatsampaienamyaitudenganpetunjuksamuelmorland
# readable:
# jawaban dari soal nomor tiga ini adalah algoritma yang digunakan untuk soal nomor empat sampai enam yaitu dengan petunjuk samuel morland
