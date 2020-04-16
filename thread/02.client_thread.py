# import socket dan sys
import socket
import sys 

# fungsi utama
def main ():
    # buat socket bertipe TCP
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # tentukan IP server target
    ip = "127.0.0.1" 
    
    # tentukan port server
    port = 12345
    
    # lakukan koneksi ke server
    try :
        soc.connect((ip, port))
    except :
        # print error
        print("Koneksi Error!")
        # exit
        sys.exit()
    
    # tampilkan menu, enter quit to exit
    print("Silahkan ketik 'quit' untuk Keluar dan Berhenti")
    pesan = input(" ---> ")

    # selama pesan bukan "quit", lakukan loop forever
    while message != 'quit':
        # kirimkan pesan yang ditulis ke server
    
        
        # menu (user interface)
        message = input(" -> ")

    # send "quit" ke server
    soc.send(b'--quit--')

# panggil fungsi utama
if __name__ == "__main__":
    main()
