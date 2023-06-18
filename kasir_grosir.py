# membuat daftar belanja
daftar_belanja = []

#membuat fungsi untuk tambah barang ke daftar belanja
def add_barang ():
    nama_barang = input('Masukkan nama barang: ')
    jumlah_barang = int(input('Masukkan jumlah barang: '))
    harga_barang = int(input('Harga barang: '))
    daftar_belanja.append({"nama":nama_barang,"jumlah":jumlah_barang,"harga":harga_barang})

#membuat fungsi menghitung total harga
def hitung_total_harga():
    total_harga = 0
    for barang in daftar_belanja:
        total_harga += barang["jumlah"]* barang["harga"]
    return total_harga

#membuat cetak struk dengan format nilai rupiah
def cetak_struk():
    print("========Struk Belanja==========")
    for barang in daftar_belanja:
        subtotal = barang["jumlah"]*barang["harga"]
        print(f"{barang['nama']}: {barang['jumlah']} x {format(barang['harga'], ',d')} = {format(subtotal, ',d')}")
    print(f"Total harga: {format(hitung_total_harga(), ',d')}")
    print("===================================")

#fungsi user
def main():
    while True:
        print("===Aplikasi Kasir Grosir===")
        print('1. Tambah Barang')
        print('2. Cetak Struk')
        print('3. Keluar')
        pilihan = input('1/2/3 : ')
        #membuat percabangan
        if pilihan == "1":
            add_barang()
        elif pilihan == "2":
            cetak_struk()
        elif pilihan == "3":
            print('Terima kasih telah menggunakan aplikasi kasir grosir')
            break
        else:
            print("Pilihan tidak tersedia")

#run program
main()