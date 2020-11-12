
import socket
import threading
import time

PI_IP = "192.168.1.108" # pi
PI_PORT = 65222

HOST_IP = "192.168.1.104" # host
HOST_PORT = 65211

class style():
  YELLOW = '\033[33m'
  BLUE = '\033[34m'
  ENDC = '\033[0m'

# pi => host
def start_server():
  print(style.YELLOW, "[server]" , "starting server at ", HOST_IP, ":", HOST_PORT, style.ENDC)
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST_IP, HOST_PORT))
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

# host => pi
def start_client():
  print(style.BLUE, "[client]" ,"starting client in 2 seconds....", style.ENDC)
  time.sleep(15)
  print(style.BLUE, "[client]" ,"starting client and connecting to server at ", PI_IP, ":", PI_PORT, style.ENDC)
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((PI_IP, PI_PORT))
    while 1:
        text = input() # Note change to the old (Python 2) raw_input
        if text == "quit":
            break
        s.send(text.encode())

        data = s.recv(1024)
        print(style.BLUE, "[client]" ,"from server: ", data, style.ENDC)

server_thead = threading.Thread(target=start_server)
client_thread = threading.Thread(target=start_client)

server_thead.start()
client_thread.start()

client_thread.join()
server_thead.join()

print("Success, terminating")
