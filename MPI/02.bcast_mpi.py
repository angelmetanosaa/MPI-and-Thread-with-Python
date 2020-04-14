# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.rank

# dapatkan total proses berjalan
size = comm.size

# jika saya rank 0 maka saya akan melakukan broadscast
if rank == 0 :
    pesan = 777
else :
    pesan = None

# Lakukan Broadcasr pesan
pesan = comm.bcast(pesan, root=0)
    
	
# jika saya bukan rank 0 maka saya menerima pesan
if rank == 0:
    print('Proses {} broadcast data:'.format(rank), pesan)
else :
    print('Proses {} terima data:'.format(rank), pesan)
