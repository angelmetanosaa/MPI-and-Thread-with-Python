# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.rank

# dapatkan total proses berjalan
size = comm.size

# jika saya rank ke 0 maka saya akan mengirimkan pesan ke proses yang mempunyai rank 1 s.d size
pesan = 999
if rank == 0:
    print("rank",rank, "Mengirim")
    i=1
    while i < (size):
        comm.send(pesan, dest=i)
        i=i+1
	

# jika saya bukan rank 0 maka saya menerima pesan yang berasal dari proses dengan rank 0
else:
    terima = comm.recv(source=0) 
    print("rank",rank,"dapat pesan", terima)
