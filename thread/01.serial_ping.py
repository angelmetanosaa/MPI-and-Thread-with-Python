# import library os (untuk melakukan perintah ping)
# import library re (untuk melakukan filtering/regex)
import os, re

# import library time untuk mengukur waktu
import time

# ambil waktu awal menggunakan time.time()
start = time.time()

# gunakan regex filter t"Received = (\d)
# regex ini digunakan untuk mencari kata "Received = x" x adalah angka (\d)
received_packages = re.compile(r"Received = (\d)")

"""
windows:
ping x.x.x.x -n 2
received_packages = re.compile(r"Received = (\d)")
melihat Received = xxx (desimal)

Pinging 10.30.32.16 with 32 bytes of data:
Reply from 10.30.32.16: bytes=32 time<1ms TTL=128
Reply from 10.30.32.16: bytes=32 time<1ms TTL=128

Ping statistics for 10.30.32.16:
    Packets: Sent = 2, Received = 2, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
"""
# lihat 3 baris paling bawah dari hasil ping
# terdapat baris: Packets: Sent = 2, Received = 2, Lost = 0 (0% loss),
# yang dilihat adalah jumlah Received. Kebetulan hasilnya adalah 2
# pada ping x.x.x.x -n 2 artinya dilakukan ping sebanyak 2 kali
# jika received = 0 maka host mati
# jika received = 1 maka host hidup tetapi ada ping yang hilang
# jika received = 2 maka host hidup


# lakukan ping untuk 20 host

    # tentukan IP yang akan diping, hanya akan diubah bagian akhirnya
    
    
    # lakukan ping -n 2
    

    # loop forever
    while True:
        # baca hasil dari perintah ping per line
        
        
        # akan keluar dari loop jika tidak ada lagi line
        
        
        # lakukan filtering dengan regex. gunakan findall dan regex filter yang sudah ditentukan
        
        
        # tampilkan hasil regex untuk mengetahui banyaknya respon ping yang diperoleh 
        
            

# ambil waktu berakhir


# tampilkan selisih waktu akhir dengan awal untuk mengetahui lama waktu eksekusi
