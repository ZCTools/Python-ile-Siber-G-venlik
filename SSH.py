# Python WEB sunucusunun, SSH protokolüne erişip erişilmediğini bulma
import socket

def check_ssh(hostname, port): # SHH erişebilirliğini tespit etme
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Bir soket nesnesi oluşturur
        # AF_INET adres ailesini (IPv4) ve SOCK_STREAM soket türünü (TCP) belirtir.
        sock.settimeout(2) # 'Socket' nesnesinin zaman aşımı süresi
        result = sock.connect_ex((hostname, port)) # Bağlantı denemesi yapar
        if result == 0: # (Başarılıysa 0 dönmeli)
            print(f"[+] {hostname}:{port} SSH erişilebilir!") 
        else:
            print(f"[-] {hostname}:{port} SSH erişilemez")
        sock.close() # 'Socket' nesnesini kapatır
    except Exception as e:
        print(f"Hata: {e}") # Bağlantı yapılmadı, hata yazılır

def main():
    target_host = "https://www.örnek.site.com" # Kontrol yapılacak sunucu
    target_port = 22  # SSH portu
    check_ssh(target_host, target_port)

if __name__ == "__main__":
    main()

# UYARI: Bu kodu bir sunucuda denemek güvenlik sorunu yaratmaz
# Ama bazı durumlarda denemek yasal olmayabilir. 