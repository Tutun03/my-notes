import socket
addr=("127.0.0.1",9090)
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
c.connect(("127.0.0.1",9090))
data=input("enter data")
c.sendto(data.encode(),addr)
l=c.recvfrom(1024).decode()
print("server says",l)
