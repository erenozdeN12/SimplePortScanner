import pyfiglet
import sys
import socket
from datetime import datetime
import getopt


ascii_banner = pyfiglet.figlet_format("Basit Port Tarayıcı")
print(ascii_banner)
  
if len(sys.argv) == 2:
     
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Hatalı Kullanım (python simple_PortScanner.py xx.xx.xx.xx)")


 
print("-" * 50)
print("Taranacak Hedef: " + target)
print("Tarih:" + str(datetime.now()))
print("-" * 50)
  
try:
     
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
         
        result = s.connect_ex((target,port))
        if result ==0:
            print("{} Numaralı Port Açık".format(port), "Banner = {}".format(s.recv(1024).decode()))
        s.close()
         
except KeyboardInterrupt:
        print("\n Programdan Çıkılıyor")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Bulunamadı")
        sys.exit()
except socket.error:
        print("\ Server yanıt vermiyor")
        sys.exit()