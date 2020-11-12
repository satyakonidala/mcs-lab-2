import socket

HOST = "192.168.0.108" # pi
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while 1:
        text = input() # Note change to the old (Python 2) raw_input
        if text == "quit":
            break
        s.send(text.encode())

        data = s.recv(1024)
        print("from server: ", data)

# print('Received', repr(data))
