import socket

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

client.connect(("localhost", 5150)) # connect to the server on localhost and port 5150

client.sendall(b"hello server, this is client")

data = client.recv(1024)

print(data.decode("utf-8"))

client.close()


