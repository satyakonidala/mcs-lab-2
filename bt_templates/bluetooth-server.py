import bluetooth

hostMACAddress = 'DC:A6:32:96:1F:92' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 5
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
print("listening on port ", port)
client = None
try:
    client, clientInfo = s.accept()
    print("client connected", clientInfo)
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data) # Echo back to client
except:
    print("Closing socket")
    if client:
        client.close()
    s.close()