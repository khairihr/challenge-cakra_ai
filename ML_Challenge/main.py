pertanyaan = (("Siapa Nama Saya?"), 
              ("Siapa Nama Ingame Saya?"), 
              ("Siapa Kucing Saya?"), 
              ("Siapa Pencipta Lagu POWER?"), 
              ("Siapa G-Dragon?"))
pilihan_jawaban = (("A. Khairi", "B. Ridho ", "C. Ahmad ", "D. Sahrudin "), 
                   ("A. Ritter", "B. KHRD", "C. KHRI", "D. RHK"), 
                   ("A. Jennie", "B. Karina", "C. Kawai", "D. Aespa"), 
                   ("A. Sutopo", "B. Mahmud", "C. G-Dragon", "D. Dadang"), 
                   ("A. Artis", "B. Selebriti", "C. Body Builder", "D. Rapper"))
jawaban_benar = ("A", "A", "C", "C", "D")
jawaban_user = []
skor_total = 0
indeks_pertanyaan = 0

for soal in pertanyaan:
    print("---------------")
    print(soal)
    for pilihan in pilihan_jawaban[indeks_pertanyaan]:
        print(pilihan)

    jawaban = input("Jawab (A, B, C, D): ").upper()
    jawaban_user.append(jawaban)
    if jawaban == jawaban_benar[indeks_pertanyaan]:
        skor_total += 1
        print("BENAR COY")
    else:
        print("SALAH EUYY")
        print(f"Jawaban yang benernya {jawaban_benar[indeks_pertanyaan]}")
    indeks_pertanyaan += 1

print("------------")
print("    HASIL   ")
print("------------")

print("Jawaban Benar: ", end="")
for jawaban in jawaban_benar:
    print(jawaban, end=" ")
print()

print("Jawaban Kamu: ", end="")
for jawaban in jawaban_user:
    print(jawaban, end=" ")
print()

skor_persen = (skor_total / len(pertanyaan) * 100)
print(f"Nilainya adalah: {skor_persen}%")