from socket import *
s = socket (AF_INET, SOCK_STREAM)

host = "127.0.0.1"
port = 7002

s.connect((host,port))

while True:
    y = input("client: ")
    s.send(y.encode('utf-8'))
    if y == "q":
        break

    x= s.recv(2048)
    if x.decode('utf=8') == "q":
        break
    print("server: ", x.decode('utf-8'))
s.close()    