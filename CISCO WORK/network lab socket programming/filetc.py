import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("127.0.0.1",9090))
filename=open("hi.txt", "r")
data=filename.read()
c.send("hi.txt".encode("utf-8"))
name=c.recv(1024).decode("utf=8")
print("server says: filename recieved")
