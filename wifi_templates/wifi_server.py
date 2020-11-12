import socket

HOST = "192.168.1.108" # pi
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    try:
        client, clientInfo = s.accept()
        print("server recv from: ", clientInfo)
        while 1:
            data = client.recv(1024)
            if data != b"":
                print(data)
                client.sendall(data) # Echo back to client
    except:
        print("Closing socket")
        client.close()
        s.close()
