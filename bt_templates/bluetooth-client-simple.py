import bluetooth

serverMACAddress = 'DC:A6:32:96:1F:92'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
# while 1:
#     text = raw_input() # Note change to the old (Python 2) raw_input
#     if text == "quit":
#         break
#     s.send(text)
s.send("text")
s.close()