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
