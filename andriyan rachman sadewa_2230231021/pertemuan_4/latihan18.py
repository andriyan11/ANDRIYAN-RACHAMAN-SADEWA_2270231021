#halaman 47 modul praktikum algoritma pemograman
#create by ANDRIYAN RACHMAN SADEWA_2270231021

# data and time (latihan)

import datetime as dt

print("silahkan masukan tanggal,\nbulan dan tahum lahir anda \n")
tanggal = int(input("tanggal\t:"))
bulan = int(input("bulan\t:"))
tahun = int(input("tahun\t:"))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda salah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"hari nya adalah : {tanggal_lahir:%A}")
print(f"umur anda adalah: {umur_tahun}) tahun, {umur_bulan_sisa}bulan")