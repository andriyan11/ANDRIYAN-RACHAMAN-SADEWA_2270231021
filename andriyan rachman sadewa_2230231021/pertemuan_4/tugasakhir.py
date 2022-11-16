# TUGAS PRA UTS ANDRIYAN RACHMAN SADEWA 2270231021

menu = "y" or "Y"
while menu == "y" or "Y":
    print(" ========================================")
    print(" Selamat Datang Bella Bakery")
    print(" Jl. Cempaka Putih No. 15 Kota Bekasi")
    print(" No telp: 082111689768")
    print(" ========================================")
    pembeli = input(" Masukkan nama Pembeli: ")
    tanggal= input(" Masukkan tanggal: ")
    print(" ========================================")
    print(" List Menu Roti")
    print(" ========================================")
    print(" 1. Roti Coklat : Rp 5.000")
    print(" 2. Roti Tawar : Rp 10.000")
    print(" 3. Roti Nanas : Rp 6.000")
    print(" 4. Roti Srikaya : Rp 7.000")
    print(" 5. Roti Keju : Rp. 8.000")
    print(" ========================================")
    listMenu=str(input(" Masukkan angka sesuai dengan menu yang tersedia = "))
    jumlahPesanan=int(input(" Jumlah dibeli = "))
    if listMenu == "1":
        namaMenu= " Roti Coklat"
        harga=(5000*jumlahPesanan)
        pajak= int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga=int(harga+pajak)
        else:
            totalHarga=int(harga+pajak)
    elif listMenu == "2":
        namaMenu= " Roti Tawar "
        harga = (10000*jumlahPesanan)
        pajak = int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga =int(harga+pajak)
        else:
            totalHarga =int(harga+pajak)
    elif listMenu == "3":
        namaMenu= " Roti Nanas "
        harga=int(6000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga=int(harga+pajak)
    elif listMenu == "4":
        namaMenu= " Roti Srikaya "
        harga=int(7000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    elif listMenu == "5":
        namaMenu= " Roti Keju "
        harga=int(8000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    else:
        menu=input(" Maaf,Menu yang dipilih tidak tersedia di roti")
 
    print(" ------------------------------")
    print(" Menu :",namaMenu)
    print(" Jumlah Pesanan :", jumlahPesanan)
    print(" Harga :", harga)
    print(" Pajak :", pajak)
    print(" ------------------------------")
    print(" Total Pembayaran :", totalHarga)
    print(" ------------------------------")
    menu=input(" Mau pesan lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N) = ")