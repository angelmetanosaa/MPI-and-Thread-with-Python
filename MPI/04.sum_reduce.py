# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import random
import numpy as np

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.rank

# dapatkan total proses berjalan
size = comm.size

# generate angka integer secara random untuk setiap proses
angka = np.array(random.randint(1, size))

if rank !=0 :
    print("Rank",rank,"punya angka", angka)

hasil = np.array(0)

# lakukam penjumlahan dengan teknik reduce, root reduce adalah proses dengan rank 0
comm.Reduce(angka, hasil, op=MPI.SUM, root=0)

# jika saya proses dengan rank 0 maka saya akan menampilkan hasilnya
if rank==0:
    print("Rank", rank, "Hasil Semua tanpa (rank 0) : ", hasil-angka)
