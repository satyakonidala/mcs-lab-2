import socket

HOST = "192.168.1.108" # pi
PORT = 65222        # The port used by the server

print(style.BLUE, "[client]" ,"starting client and connecting to server at ", HOST_IP, ":", HOST_PORT, style.ENDC)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST_IP, HOST_PORT))
    while 1:
        text = input() # Note change to the old (Python 2) raw_input
        if text == "quit":
            break
        s.send(text.encode())

        data = s.recv(1024)
        print(style.BLUE, "[client]" ,"from server: ", data, style.ENDC)

