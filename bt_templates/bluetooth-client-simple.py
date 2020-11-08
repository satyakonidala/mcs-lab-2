import bluetooth

host = "DC:A6:32:96:1F:92"
port = 11
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))
print("sending on port", port)
try:
    while 1:
        text = input() # Note change to the old (Python 2) raw_input
        if text == "quit":
            break
        sock.send(text)
        sock.close()
except:
    print("Closing connection to server")
    sock.close()