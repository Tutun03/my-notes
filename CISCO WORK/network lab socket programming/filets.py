import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",9090))
s.listen()
print("listening..")
(c,cip)=s.accept()
file=c.recv(1024).decode("utf-8")

print("filename received by server from client",file)
c.send("filename received".encode("utf-8"))
