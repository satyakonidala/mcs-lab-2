import bluetooth

hostMACAddress = 'A4:83:E7:34:53:7A' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 30
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