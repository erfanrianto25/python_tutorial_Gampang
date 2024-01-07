data_list = []

def pemesanan():
    nama_pemesan = input("Masukkan nama pemesan: ")
    total_pembayaran = 0  # Inisialisasi total pembayaran untuk setiap pemesanan

    while True:
        menu = int(input("Masukkan nomor menu (1-5): "))
        jumlah = int(input("Masukkan jumlah pesanan: "))

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

        total_pembayaran += total_harga(jumlah, harga)

        lanjutkan = input("Apakah Anda ingin menambah pesanan? (y/n): ") 
         
        if lanjutkan.lower() == 'n':
            break               

    service_charge = total_pembayaran * 0.1
    total_pembayaran += service_charge

    data_list.append((nama_pemesan, total_pembayaran))
    print("\nAnda telah memesan dengan total harga: Rp {}\nService Charge: Rp {}".format(total_pembayaran, service_charge))

def pembayaran(total_pembayaran):
    while True:
        uang_dibayarkan = float(input("Masukkan jumlah uang yang dibayarkan: Rp. "))

        if uang_dibayarkan < total_pembayaran:
            print("Uang yang dibayarkan kurang. Silahkan masukkan uang yang cukup")
        else:
            break

    sisa = uang_dibayarkan - total_pembayaran
    print("Pembayaran berhasil !!!")
    print("Sisa uang anda : Rp. {}".format(sisa))

def total_harga(jumlah, harga):
    return jumlah * harga

def cetak_menu():
    print("Selamat datang di Caffe GACOR!")
    print('anda rungat?? Pesan Dulu Mazzeh')
    print()
    print("Berikut adalah menu kami:")
    print("1. KOPI HITAM\tRp. 6.000")
    print("2. JOSHUA \tRp. 7.000")
    print("3. WEDANG JAHE\tRp. 7.000")
    print("4. SUSU SODA\tRp. 12.000")
    print("5. MEGA MENDUNG\tRp. 12.000")
    print("Silahkan Di Pilih Mazzeh !!!!")

def cetak_ringkasan_pemesanan():
    print("\nRingkasan Pemesanan:")
    for item in data_list:
        print("\nNama Pemesan: {}\nTotal Harga : Rp. {}".format(item[0], item[1]))

    total_pembayaran = sum(item[1] for item in data_list)
    print("\nTotal Pembayaran: Rp {}".format(total_pembayaran))
    print('SELAMAT ANDA DIKENAKAN PPN PAJAK 0.1%')
    pembayaran(total_pembayaran)
    print("\nTerima kasih BROO Semoga JACKPOT YA!!")
    print("WIFI GRATIS")
    print("Username : NOMPAK BECAK KASARKAJU")
    print("Password : lecaklaju12")

def main():
    cetak_menu()
    pemesanan()
    cetak_ringkasan_pemesanan()

if __name__ == "__main__":
    main()
