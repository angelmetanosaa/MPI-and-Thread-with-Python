# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.rank

# dapatkan total proses berjalan
size = comm.size

# jika saya rank terbesar maka saya akan mengirimkan pesan ke proses yang mempunyai rank 0 s.d rank terbesar-1
pesan = 999
if rank == size-1 :
    print("rank",rank, "Mengirim")
    i=0
    while i < (size-1):
        comm.send(pesan, dest=i)
        i=i+1

# jika saya bukan rank terbesar maka saya akan menerima pesan yang berasal dari proses dengan rank terbesar
elif (rank<size-1):
    terima = comm.recv(source=size-1) 
    print("rank",rank,"dapat pesan", terima)
