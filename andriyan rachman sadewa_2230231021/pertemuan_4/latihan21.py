#halaman 51 modul praktikum algoritma pemograman
#create by ANDRIYAN RACHMAN SADEWA_2270231021

# latihan

# kalkulator
print(20*"=")
print("kalkulator sederhana")
print(20*"=" + "\n")

angka_1 = float(input("masukan angka 1 ="))
operator = input("operator(+,-,x,/)")
angka_2 = float(input("masukan angka 2 ="))

# percabangannya
if operator =="+":
        hasil = angka_1 + angka_2
        print(f"hasilnya adalah {hasil}")
elif operator =="-":
        hasil = angka_1 - angka_2
        print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator =="*":
         hasil = angka_1 / angka_2
         print(f"hasilnya adalah {hasil}")
else : 
        print("masukan yang bener dong!, aku pusing")
        print("Akhir dari program, terima gajih!")

