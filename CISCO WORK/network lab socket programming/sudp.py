import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",9090))
addr1=("127.0.0.1",9090)
data=s.recv(1024).decode()
print("the data is received from the client")
print("the data is ",data)
s.sendto("data is received".encode(),addr1)
