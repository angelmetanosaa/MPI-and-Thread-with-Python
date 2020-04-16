# import socket, sys, traceback dan threading
import socket
import sys
import traceback
import threading

# jalankan server
def main():
    start_server()

# fungsi saat server dijalankan
def start_server():
    # tentukan IP server
    ip = "127.0.0.1"
    
    # tentukan port server
    port = 12345

    # buat socket bertipe TCP
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # option socket
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket Telah dibuat")

    # lakukan bind
    try :
        soc.bind((ip,port))
    except :
        # exit pada saat error
        print("Bind Gagal! Error : " + str(sys.exc_info()))
        sys.exit()

    # listen hingga 5 antrian
    soc.listen(5)
    
    print("Socket sedang Mendengarkan")

    # infinite loop, jangan reset setiap ada request
    while True:
        # terima koneksi
        
        
        # dapatkan IP dan port
        
        print("Connected dengan " + ip + ":" + port)

        # jalankan thread untuk setiap koneksi yang terhubung
        try:
            
        except:
            # print kesalahan jika thread tidak berhasil dijalankan
            print("Thread tidak berjalan.")
            traceback.print_exc()

    # tutup socket
    


def client_thread(connection, ip, port, max_buffer_size = 4096):
    # flag koneksi
    

    # selama koneksi aktif
    while is_active:

        # terima pesan dari client
        
        
        # dapatkan ukuran pesan
        
        
        # print jika pesan terlalu besar
        if client_input_size > max_buffer_size:
            print("The input size is greater than expected {}")

        # dapatkan pesan setelah didecode
        
        
        # jika "quit" maka flag koneksi = false, matikan koneksi
        if "quit" in client_input:
            # ubah flag
        
            print("Client meminta keluar")
            
            # matikan koneksi
            
            print("Connection " + ip + ":" + port + " ditutup")
            
        else:
            # tampilkan pesan dari client
            
            
# panggil fungsi utama
if __name__ == "__main__":
    main()
