# import mpi4py
from mpi4py import MPI
import math

# buat fungsi dekomposisi bernama local_loop 
# local_loop akan menghitung setiap bagiannya
# gunakan 4/(1+x^2), perhatikan batas awal dan akhir untuk dekomposisi
# misalkan size = 4 maka proses 0 menghitung 0-25, proses 1 menghitung 26-50, dst
def local_loop(num_steps,begin,end):
    step = 1.0/num_steps
    sum = 0
    for i in range(begin, num_steps, end):
        x= (i+0.5)*step
        sum = sum + 4.0/(1.0+x*x)
    #print(sum)
    return sum*step 

# fungsi Pi
def Pi():
    
    # buat COMM
    comm = MPI.COMM_WORLD
    
    # dapatkan rank proses
    rank = comm.rank
    
    # dapatkan total proses berjalan
    size = comm.size
    
    # lakukan penjumlahan dari local_sum proses-proses yang ada ke proses 0
    # bisa digunakan reduce atau p2p sum
    if rank == 0:
        n = size
    else :
        n = None
    
    n = comm.bcast(n, root=0)

    # value dari local_loop
    z = local_loop(n, rank, size)

    phi = comm.reduce(z , op=MPI.SUM, root=0)

    # jika saya proses dengan rank 0  maka tampilkan hasilnya
    if rank == 0:
        selisih = phi-math.pi
        print ("Nilai phi terdekat : ", phi, "Dengan Selisih : ", selisih)
        print ("Nilai Phi Real     : ", math.pi)
    
# panggil fungsi utama    
if __name__ == '__main__':
    Pi()
