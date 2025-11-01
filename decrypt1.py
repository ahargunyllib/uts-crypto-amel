ciphertext = "fivmoyxehepelwsepyxwovmtxskvejmwiferceowitypylwsephirkerneaeferrsqsvwexyhmkyreoerwifekemtixyrnyowseprsqsvxmkecemxyehetxewmhevmpegmjvehipwmkkmszerfexxmwxefippews"

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

# shift 4:
# berikutadalahsoalutskriptografisebanyaksepuluhsoaldenganjawabannomorsatudigunakansebagaipetunjuksoalnomortigayaituadaptasidarilacifradelsiggiovanbattistabellaso
# readable
# berikut adalah soal uts kriptografi sebanyak sepuluh soal dengan jawaban nomor satu digunakan sebagai petunjuk soal nomor tiga yaitu adaptasi dari la cifra del sig giovan battista bellaso
