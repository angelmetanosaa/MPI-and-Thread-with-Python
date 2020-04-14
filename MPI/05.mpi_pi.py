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
