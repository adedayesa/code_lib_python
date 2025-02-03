harga_barang = float(input("Masukkan harga barang : "))

pajak = 0.11

# pajak yang harus di bayar
pajak_bayar = harga_barang * pajak

# hitungan setelah ppn 11%
total_harga = harga_barang + pajak_bayar

# hasilnya
print("PPN 11% : Rp", pajak_bayar)
print("Total harga setelah pajak : Rp", total_harga)