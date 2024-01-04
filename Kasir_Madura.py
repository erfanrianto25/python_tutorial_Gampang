data_list = []

def pemesanan():
    nama_pemesan = input("Masukkan nama pemesan: ")

    menu = int(input("Masukkan nomor menu (1-5): "))
    jumlah = int(input("Masukkan jumlah pesanan: "))

    # Pemilihan menu dan harga sesuai dengan pilihan pengguna
    if menu == 1:
        nama_menu = "KOPI HITAM"
        harga = 6000
    elif menu == 2:
        nama_menu = "JOSHUA "
        harga = 7000
    elif menu == 3:
        nama_menu = "WEDANG JAHE "
        harga = 7000
    elif menu == 4:
        nama_menu = "SUSU SODA "
        harga = 12000
    elif menu == 5:
        nama_menu = "MEGA MENDUNG "
        harga = 12000
    else:
        print("Nomor menu tidak valid.")
        return

    total = total_harga(jumlah, harga)
    service_charge = total * 0.1
    total_pembayaran = total + service_charge

    data_list.append((nama_pemesan, nama_menu, jumlah, total_pembayaran))
    print("\nAnda telah memesan : {} {} x {} pcs. \nTotal harga: Rp {} \nHarga Produk: Rp {} \nService Charge: Rp {}".format(nama_menu, harga, jumlah, total_pembayaran, total, service_charge))

def pembayaran(total_pembayaran):
    while True:
        uang_dibayarkan = float(input("Masukkan jumlah uang yang dibayarkan: "))
        
        if uang_dibayarkan < total_pembayaran:
            print("Uang yang dibayarkan kurang. Silahkan masukkan uang yang cukup.")
        else:
            break

    sisa_uang = uang_dibayarkan - total_pembayaran
    print("Pembayaran berhasil.")
    print("Sisa uang Anda: Rp {}".format(sisa_uang))

def cetak_menu():
    print("Selamat datang di Caffe GACOR!")
    print('anda rungat?? Pesan Dulu Mazzeh')
    print()
    print("Berikut adalah menu kami:")
    print("1. KOPI HITAM\tRp. 6.000")
    print("2. JOSHUA \t\tRp. 7.000")
    print("3. WEDANG JAHE\tRp. 7.000")
    print("4. SUSU SODA\tRp. 12.000")
    print("5. MEGA MENDUNG\tRp. 12.000")
    print("Silahkan Di Pilih Mazzeh !!!!")
    # Kode cetak_menu (sama seperti yang sudah ada)

def total_harga(jumlah, harga):
    return jumlah * harga

def cetak_ringkasan_pemesanan():
    print("\nRingkasan Pemesanan:")
    for item in data_list:
        print("Nama Pemesan : {}\nMenu : {}\nHarga: {}\nJumlah Total Rp. {}".format(item[0], item[1], item[2], item[3]))

    total_pembayaran = sum(item[3] for item in data_list)
    print("\nTotal Pembayaran: Rp {}".format(total_pembayaran))
    print('SELAMAT ANDA DIKENAKAN  PPN PAJAK 0.1%')

    pembayaran(total_pembayaran)  # Panggil fungsi pembayaran untuk memproses pembayaran

    print("\nTerima kasih BROO Semoga JACKPOT YA!!")
    print("WIFI GRATIS")
    print("Username : NOMPAK BECAK KASARKAJU")
    print("Password : lecaklaju12")

def main():
    cetak_menu()

    # Perulangan untuk mengambil pemesanan sampai pengguna menentukan untuk selesai
    while True:
        print("\n")
        pemesanan()

        lanjutkan = input("Apakah Anda ingin melanjutkan pemesanan? (y/n): ")
        if lanjutkan.lower() == 'n':
            break

    cetak_ringkasan_pemesanan()

if __name__ == "__main__":
    main()

