# Pavlo Yatluk
# dz_11
#3.  Сервер, який отримує у користувача фразу, а потім надсилає підраховану кількість слів у відповідь.

# КЛІЄНТ
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 60000))
message = input("Enter message:")
sock.send(bytes(message, encoding='UTF-8'))
data = sock.recv(1024)
sock.close()
print(data)

# СЕРВЕР
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 60000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    print(str(data))
    # data = list(data)
    data = len(data.split())
    conn.send(bytes(str(data), encoding='UTF-8'))
conn.close()