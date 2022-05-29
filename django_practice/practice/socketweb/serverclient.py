import socket
#127.0.0.1''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 1025))
sock.send("hello".encode())


data_transferred = 0
filename = 'hello'
with open("D:\python\django_practice\practice\media"+"\\"+filename+".txt", 'rb') as f:
    try:
        data = f.read(1024)
        while data:
            data_transferred += sock.send(data)
            data = f.read(1024)
    except Exception as ex:
        print(ex)
print("%s  %d" %(filename, data_transferred))

