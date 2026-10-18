# create a TCP server that listens for incoming connection requests on a specified port

import socket 

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) 
 # creating a socket object to allow communication between different applications
 # family is IPv4, AF_INET6 is for IPv6 
 # type is TCP, SOCK_DGRAM is for UDP. We are using TCP 

# TCP vs UDP is basically: TCP is a connection-based protocol, while UDP is a connectionless protocol.
# We have essentially craeated a server that is listening for incoming connection requests on a specified port over TCP.

# server bind takes a tuple of two args: IP address and port number
server.bind(("localhost", 5150))


server.listen(2) # listen for incoming requests. 2 means only 2 clients can connect at once.


while True:

    client_socket, client_address = server.accept()
    print(f"Connection from {client_address} has been established!")

    data = client_socket.recv(1024) # receive data from the client. 1024 is the buffer size

    message = data.decode("utf-8") # decode the bytes to string

    print(f"Message from client: {message}")

    client_socket.send(b"Hello from the server!")

    client_socket.close()


server.close()

