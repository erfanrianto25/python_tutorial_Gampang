print("===== KASIR PUTRA JAYA =====")
print("=== SELAMAT BERBELANJA ===")

harga = []
barang = []
total_harga = 0
while True:
    print(""""========== NAMA BARANG ==========
	----------------------------------
	|KODE| NAMA BARANG | HARGA |
	----------------------------------
	| 1 | KEYBOARD    | Rp. 100.000,00 |
	| 2 | MOUSE       | Rp. 95.000,00  |
	| 3 | FLASHDISK   | Rp. 63.000,00  |
	| 4 | SPEAKER     | Rp. 90.000,00  |
	| 5 | JOYSTICK    | Rp. 85.000,00  |
	| 6 | MOUSEPAD    | Rp. 10.000,00  |
	----------------------------------
	""")

    KODE = int(input("Masukkan Kode Barang : "))
    if KODE == 1:
        barang.append("KEYBOARD")
        harga.append(100000)
        total_harga += 100000
    elif KODE == 2:
        barang.append("MOUSE")
        harga.append(95000)
        total_harga += 95000
    elif KODE == 3:
        barang.append("FLASHDISK")
        harga.append(63000)
        total_harga += 63000
    elif KODE == 4:
        barang.append("SPEAKER")
        harga.append(90000)
        total_harga += 90000
    elif KODE == 5:
        barang.append("JOYSTICK")
        harga.append(85000)
        total_harga += 85000
    elif KODE == 6:
        barang.append("MOUSEPAD")
        harga.append(10000)
        total_harga += 10000
    else:
        print("Barang Tidak Tersedia !!!")
    
    beli_barang_lain = input("Beli barang lain ?\tTekan YES/NO : ")
    if beli_barang_lain == "NO" or beli_barang_lain == 'no' :
        print("")
        break
print(f"""
barang : {barang}
harga : {harga}
jumlah : Rp.{total_harga}
""")

bayar = int(input("Bayar Rp. "))
if bayar > total_harga:
    print("Sisa uang kembalian :Rp.",bayar - total_harga)
elif bayar == total_harga:
    print("Anda membayar dengan uang Pas !")
else :
    print("Uang yang anda bayarkan kurang :Rp.",bayar - total_harga)