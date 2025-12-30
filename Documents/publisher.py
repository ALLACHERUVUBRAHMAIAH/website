import socket
import time

server = socket.socket()
server.bind(("localhost", 9999))
server.listen(1)

print("Publisher waiting for subscriber...")
conn, addr = server.accept()
print("Subscriber connected")

messages = ["News 1", "News 2", "News 3"]

for msg in messages:
    conn.send(msg.encode())
    time.sleep(2)

conn.close()
server.close()
