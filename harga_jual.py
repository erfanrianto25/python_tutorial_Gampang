#menghitun harga jual dari modal dan untung

def hitung_harga_jual(modal,untung):
    harga_jual = modal + (modal * (untung/100))
    return harga_jual

#input user
modal = float(input("Masukkan modal awal :Rp. "))
untung = float(input("Masukkan untung dalam persen :"))

harga_jual = hitung_harga_jual (modal,untung)
print('Harga jualnya adalah Rp. : ',harga_jual)