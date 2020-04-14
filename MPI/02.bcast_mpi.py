# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.rank

# dapatkan total proses berjalan
size = comm.size
