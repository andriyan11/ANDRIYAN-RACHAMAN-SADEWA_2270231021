#halaman 56 modul praktikum algoritma pemograman
#create by ANDRIYAN RACHMAN SADEWA_2270231021

#Contoh penggunaan Nested Loop
#Catatan: Penggunaan modulo pada kondisional mengasumsikan nilaiselain nol sebagai True(benar) dan nol sebagai False(salah)

i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print(i, " is prime")
    i = i + 1
print("Good bye!")