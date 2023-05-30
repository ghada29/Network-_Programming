from socket import *
s = socket (AF_INET, SOCK_STREAM)
print("socket successfully created")

host = "127.0.0.1"
port = 7002

s.bind((host,port))
print("socket binded to ", port)

s.listen(5)
print("socket is listening...")

c, addr = s.accept()
print("Get Connection from", addr[0])

while True:
    x= c.recv(2048)
    if x.decode('utf=8') == "q":
        break
    print("client: ", x.decode('utf-8'))

    y = input("server: ")
    c.send(y.encode('utf-8'))
    if y == "q":
        break
s.close()