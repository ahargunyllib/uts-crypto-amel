ciphertext = "VOGWZROFWGCOZBCACFRIOWBWOROZOVYIBQWMOBURWUIBOYOBIBHIYGCOZBCACFHWUOBCACFSADOHBCACFGOHIOBUYOGSHSZOVSBOAMOWHIFSDCGWHCFWFSGAWDOQYOUSF"

def caesar_decrypt(ciphertext, shift):
    result = []
    for char in ciphertext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

for i in range(26):
    print("Shift:", i)
    decrypted = caesar_decrypt(ciphertext, i)
    print(decrypted + "\n")

# Shift 14:
# HASILDARISOALNOMORDUAINIADALAHKUNCIYANGDIGUNAKANUNTUKSOALNOMORTIGANOMOREMPATNOMORSATUANGKASETELAHENAMYAITUREPOSITORIRESMIPACKAGER
# readable:
# HASIL DARI SOAL NOMOR DUA INI ADALAH KUNCI YANG DIGUNAKAN UNTUK SOAL NOMOR TIGA NOMOR EMPAT NOMOR SATU ANGKA SETELAH ENAM YAITU REPOSITORI RESMI PACKAGER
