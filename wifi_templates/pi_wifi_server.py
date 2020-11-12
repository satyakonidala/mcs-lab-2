import socket

PI_IP = "192.168.1.108" # pi
PI_PORT = 65222     # Port to listen on

class style():
  YELLOW = '\033[33m'
  BLUE = '\033[34m'
  ENDC = '\033[0m'

print(style.YELLOW, "[server]" , "starting server at ", PI_IP, ":", PI_PORT, style.ENDC)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((PI_IP, PI_PORT))
    s.listen()

    try:
        client, clientInfo = s.accept()
        print(style.YELLOW, "[server]" ,"server recv from: ", clientInfo, style.ENDC)
        while 1:
            data = client.recv(1024)
            if data != b"":
                print(style.YELLOW, "data from client:", data, style.ENDC)
                client.sendall(data) # Echo back to client
    except:
        print(style.YELLOW,"Closing socket", style.ENDC)
        client.close()
        s.close()
