#halo guys kali ini kita akan mencoba membuat program sederhana permintaan dari subcriber

#import library menggunakan sys
import sys

#membuat fungsi hitung
def hitung_total(item,harga):
    total = 0
    for i in range(len(harga)):
        total += harga[i]
    return total

#membuat fungsi cetak struk
def cetak_struk(item,harga,total):
    print("\n========= Struk Belanja =========")
    for i in range(len(item)):
        print(f'{item[i]} \t Rp.{harga[i]}')
    print("===========================")
    print(f'Total=\t\tRp.{total}')
    print("===========================")

#membuat inisiasi item yang akan di tambah, ada nama barang dan harga barang
item = []
harga = []

#membuat input item/barang dan harga
while True:
    nama = input('Masukkan nama barang/(Ketik "selesai" untuk berhenti): ')
    if nama.lower() == "selesai":
        break
    else:
        try:
            harga_item = int(input("Masukkan harga barang : "))
            item.append(nama)
            harga.append(harga_item)
        except ValueError:
            print('Input yang kamu masukkan salah. Harap masukkan angka saja')
#membuat hitungan untuk total harga
total_harga = hitung_total(item, harga)

#mencetak struk belanja
cetak_struk(item, harga, total_harga)

#membuat program berhenti
sys.exit()