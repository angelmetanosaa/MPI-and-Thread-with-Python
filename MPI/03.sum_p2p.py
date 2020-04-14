# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import random

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.rank

# dapatkan total proses berjalan
size = comm.size

# generate angka integer secara random untuk setiap proses
angka = random.randint(1, size)
print("Rank",rank,"punya angka", angka)

hasil = 0

# jika saya adalah proses dengan rank 0 maka:
# saya menerima nilai dari proses 1 s.d proses dengan rank terbesar
# menjumlah semua nilai yang didapat (termasuk nilai proses saya)
if rank == 0 :
    i=1
    hasil = hasil + angka
    while i < (size):
        dapet = comm.recv(source=i)
        i=i+1
        hasil = hasil + dapet
    print("Rank", rank, "Menjumlahkan jadi : ", hasil)
	
# jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
    kirim = comm.send(angka, dest=0)
