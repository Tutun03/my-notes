import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",9090))
s.listen()
while True:
    (c,cip)=s.accept()
    data1=c.recv(1024).decode()
    print("a value is recieved:",data1)
    data2=c.recv(1024).decode()
    print("b value is received:",data2)
    data3=data1+data2
    c.send(data3.encode())
