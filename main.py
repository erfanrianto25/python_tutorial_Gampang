#kita akan mencoba membuat program aplikasi kasir dengan fitur diskon, tambah barang, dan hitung sisa uang belanja
#membuat variable
total_beli = 0
diskon = 0.1 #0.1 ini setara dengan 10% diskon jika jumlah pembelian lebih dari 100rb
sisa_uang = 0

#membuat input
jml_barang = int(input('Masukkan jumlah barang : '))

#membuat perulangan untuk tambah barang 
for i in range(jml_barang):
    nama_barang = input(f'Masukkan nama barang ke - {i+1}: ')
    harga_barang = float(input(f'Masukkan harga barang {nama_barang}: '))

    #membuat operator hitung
    total_beli += harga_barang

#membuat diskon barang
if total_beli >= 100000 :
    diskon_beli = total_beli * diskon
    total_beli -= diskon_beli
    print(f'\nKamu mendapatkan diskon sebesar {diskon*100}%')

#menghitung sisa uang 
sisa_uang = float(input('\nBayar: '))
sisa_uang = sisa_uang - total_beli

#membuat strok
print('\n----- STRUK BELANJA -----')
print(f'Total belanja = Rp.{total_beli}')
print(f'Jumlah uang = Rp.{sisa_uang}')
print('----- TERIMA KASIH -----')