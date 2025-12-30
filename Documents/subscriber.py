import socket

client = socket.socket()
client.connect(("localhost", 9999))

while True:
    data = client.recv(1024)
    if not data:
        break
    print("Received:", data.decode())

client.close()
