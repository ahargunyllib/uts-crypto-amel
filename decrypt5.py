ciphertext = "paapareltenXrndraMioitlVnmgiaGtousm2arnoaLhlaatcyiklftamanoCnanorrgiummxsnnoyoaitraamdueiuaekmtksnspu7ego"

# Mencoba membaca setiap n-th character untuk menemukan pola:
for n in range(2, 7):
    for start in range(n):
        seq = ''.join([ciphertext[i] for i in range(start, len(ciphertext), n)])
        print(f"Interval {n}, Start {start}: {seq}")

# Interval 6, Start 0: perintahyangsamase
# Interval 6, Start 1: alnomorlimainideng
# Interval 6, Start 2: atdigunakanuntukso
# Interval 6, Start 3: pertisoalnomoremp
# Interval 6, Start 4: analamatformyaitu
# Interval 6, Start 5: rXMVG2LctCrxoauk7

plaintext = []

for start_idx in range(6):
    seq = ''.join([ciphertext[i] for i in range(start_idx, len(ciphertext), 6)])
    plaintext.append(seq)

print(plaintext[0] + plaintext[3] + plaintext[2] + plaintext[1] + plaintext[4] + plaintext[5])

# perintahyangsamasepertisoalnomorempatdigunakanuntuksoalnomorlimainidenganalamatformyaiturXMVG2LctCrxoauk7
# readable:
# perintah yang sama seperti soal nomor empat digunakan untuk soal nomor lima ini dengan alamat form yaitu rXMVG2LctCrxoauk7
# hasil:
# Jawaban dari nomor lima ini digunakan sebagai kunci untuk nomor sembilan dan nomor enam dengan hints square dengan i dan j dalam satu sel
