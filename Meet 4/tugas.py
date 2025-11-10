nilai = float(input("Masukkan nilai (0–100): "))

if nilai >= 80 and nilai <= 100:
    grade = "A"
elif nilai >= 70 and nilai < 80:
    grade = "B"
elif nilai >= 60 and nilai < 70:
    grade = "C"
elif nilai >= 40 and nilai < 60:
    grade = "D"
else:
    grade = "E"

print("Nilai Anda:", nilai, "=> Grade:", grade)