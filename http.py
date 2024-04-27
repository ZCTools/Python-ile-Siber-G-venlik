# Bir web sitesinin çerez politikalarını kontrol etme
import requests

url = "https://www.örnek.site.com" # Hedef sitenin URL / IP Adresi
response = requests.get(url) # Siteye bir 'HTTPS GET' isteği atar

# Çerez politikalarını kontrol etme yeri
if 'Set-Cookie' in response.headers: # Set-Cookie başlığını kontrol eder
    cookie_policy = response.headers['Set-Cookie'] # Çerez politikalarının bulunması
    print("Çerez Politikası: ") # Çerez politikalarını yazdırma(9 ve 10.satır)
    print(cookie_policy)
else:
    print("Çerez Politikası bulunamadı.") # Çerez politikası yoksa yazar
