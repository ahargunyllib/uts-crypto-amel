ciphertext = "jriaumslrsinu.longamtlhouefrk/oemxrmeYmpnLbadjetaaripginaEkitbuhk4tta8dtnuephmnsibg:nxa/tKn/sjjfo7uo"

# Mencoba membaca setiap n-th character untuk menemukan pola:
for n in range(2, 7):
    for start in range(n):
        seq = ''.join([ciphertext[i] for i in range(start, len(ciphertext), n)])
        print(f"Interval {n}, Start {start}: {seq}")

# Interval 4, Start 0: juruntukmendapatkanhintso
# Interval 4, Start 1: rms.gle/xYLjagEb48umbxKj7
# Interval 4, Start 2: isilahformberikutdenganju
# Interval 4, Start 3: alnomorempatinihttps://fo

plaintext = []

for start_idx in range(4):
    seq = ''.join([ciphertext[i] for i in range(start_idx, len(ciphertext), 4)])
    plaintext.append(seq)

print(plaintext[2] + plaintext[0] + plaintext[3] + plaintext[1])

# isilahformberikutdenganjujuruntukmendapatkanhintsoalnomorempatinihttps://forms.gle/xYLjagEb48umbxKj7
# readable:
# isilah form berikut dengan jujur untuk mendapatkan hint soal nomor empat ini https://forms.gle/xYLjagEb48umbxKj7
# hasil:
# Hints untuk algoritma nomor 7 sampai 10 adalah AA=8 dan jawaban dari nomor empat ini digunakan sebagai kunci untuk nomor delapan dan nomor lima yaitu hasil dari proses hashing
