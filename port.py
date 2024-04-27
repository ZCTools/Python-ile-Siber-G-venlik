# Bir web sunucusunun açık portlarını tarama
import socket

# UYARI: Bir WEB sitesine IZINSIZ bir şekilde\nport taraması yapmak suçtur ve etik değildir.

target = "örnek.site.com" # Tarama yapılacak site / IP Adresi
ports = [22, 80, 443] # Portlar
#       SSH HTTP HTTPS

def scan_port(port):
    try:
        scanPorts = socket.socket() # Socket kütüphanesini başlatma
        scanPorts.settimeout(1)     # Zamanaşımı ayarı
        scanPorts.connect((target, port)) # Bağlantı kurma
        print(f"{port} portu açık!") # Bağlantı kontrolü
        scanPorts.close() # Bağlantı kurulduktan sonra kapatma

    except: # Hata oluşursa
        pass

for port in ports:
    scan_port(port) # Portları tekrar kontrol eder

# UYARI: Bir WEB sitesine IZINSIZ bir şekilde\nport taraması yapmak suçtur ve etik değildir.