import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5000))
server.listen(0)
client, add = server.accept()
data = client.recv(65535)
print("receive data:", data.decode())

filename = 'hello2'
data = client.recv(1024)
data_transferred = 0
with open("D:\python\django_practice\practice\media"+"\\"+filename+".txt", 'wb') as f: #현재dir에 filename으로 파일을 받는다
    try:
        while data: #데이터가 있을 때까지
            f.write(data) #1024바이트 쓴다
            data_transferred += len(data)
            data = client.recv(1024) #1024바이트를 받아 온다
    except Exception as ex:
        print(ex)
print('파일 %s 받기 완료. 전송량 %d' %(filename, data_transferred))

