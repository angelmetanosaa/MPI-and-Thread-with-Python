#import os, request, threading, urllib.request, urllib.error, urllib.parse, dan time
import os
import requests
import threading
import urllib.request, urllib.error, urllib.parse
import time

#inisiasi url
url = "https://apod.nasa.gov/apod/image/1901/LOmbradellaTerraFinazzi.jpg"

#membuat fungsi buildRange untuk membangun sistem hitungan range
def buildRange(value, numsplits):
    #membuat array dengan nama lst
    lst = []
    #melakukan perulangan sebanyak numsplits
    for i in range(numsplits):
        #jika i == 0
        if i == 0:
            lst.append('%s-%s' % (i, int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0))))
        #jika selain 0, maka 
        else:
            lst.append('%s-%s' % (int(round(1 + i * value/(numsplits*1.0),0)), int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0))))
    #mengembalikan nilai lst
    return lst

#membuat class SplitBufferThreads
class SplitBufferThreads(threading.Thread):
    """ Splits the buffer to ny number of threads
        thereby, concurrently downloading through
        ny number of threads.
    """
    # fungsi __init__; init untuk assign url dan hasil respons = None
    def __init__(self, url, byteRange):
        super(SplitBufferThreads, self).__init__()
        self.__url = url
        self.__byteRange = byteRange
        self.req = None
        
    #fungsi utama yang diekseskusi ketika thread berjalan
    def run(self):
        #spesifikasi range dari file yang didownload dalam ukuran byte
        self.req = urllib.request.Request(self.__url,  headers={'Range': 'bytes=%s' % self.__byteRange})
    
    #fungsi getFileData untuk membuka dan membaca file yang didownload
    def getFileData(self):
        #menjalankan fungsi getFileData untuk membaca file
        return urllib.request.urlopen(self.req).read()

def main(url=None, splitBy=3):
    start_time = time.time()
    if not url:
        print("Please Enter some url to begin download.")
        return

    fileName = url.split('/')[-1]
    sizeInBytes = requests.head(url, headers={'Accept-Encoding': 'identity'}).headers.get('content-length', None)
    print("%s bytes to download." % sizeInBytes)
    if not sizeInBytes:
        print("Size cannot be determined.")
        return

    dataLst = []
    for idx in range(splitBy):
        byteRange = buildRange(int(sizeInBytes), splitBy)[idx]
        bufTh = SplitBufferThreads(url, byteRange)
        bufTh.start()
        bufTh.join()
        dataLst.append(bufTh.getFileData())

    content = b''.join(dataLst)

    if dataLst:
        if os.path.exists(fileName):
            os.remove(fileName)
        print("--- %s seconds ---" % str(time.time() - start_time))
        with open(fileName, 'wb') as fh:
            fh.write(content)
        print("Finished Writing file %s" % fileName)

if __name__ == '__main__':
    main(url)
