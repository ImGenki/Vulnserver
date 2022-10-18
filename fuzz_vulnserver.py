import socket

print("Fuzzing for Ability server by Genki, Open source \n")
buffer=["A"]
counter=5
while len(buffer) <= 1000:
    buffer.append("A" * counter)
    counter+=20
commands=["TRUN ."]

for command in commands:
    for string in buffer:
        print("Fuzzing" + command + str(len(string)))
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect=s.connect(("IP adress",9999))
        s.recv(1024)
        s.send(bytes(command+""+string+'\r\n'))
        s.recv(1024)
        s.send(bytes('QUIT\r\n'))
        s.close()


