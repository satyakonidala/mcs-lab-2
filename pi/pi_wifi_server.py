import socket
import pi_car

def navigate_car(data):
    if(data =='forward'):
        print("driving forward")
        pi_car.mforward()
    if(data =='left'):
        print("driving left")
        pi_car.mleft()
    if(data =='right'):
        print("driving right")
        pi_car.mright()
    if(data =='back'):
        print("driving back")
        pi_car.mbackward()

ServerSocket = socket.socket()
host = "192.168.1.108"
port = 65222

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))
    ServerSocket.close()

ServerSocket.listen(5)
times_client_connected = 0

while True:
    print('Waiting for a Connection..')
    Client, address = ServerSocket.accept()
    times_client_connected += 1
    print(times_client_connected,' Connected to: ' + address[0] + ':' + str(address[1]))
    while True:
        data = Client.recv(2048)
        if data:
            print(data)
            navigate_car(data.decode())
            print("car info")
            print(pi_car.car_state().encode())
            Client.sendall(pi_car.car_state().encode())
        else:
            break
    Client.close()
ServerSocket.close()
