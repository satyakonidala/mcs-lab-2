from flask import Flask
from flask import request

import socket

HOST_IP = "192.168.1.108" # pi
HOST_PORT = 65222        # The port used by the server

app = Flask(__name__)

@app.route('/health')
def health():
    return 'ok'

@app.route('/post-to-car',methods=['POST'])
def postToCar():
    data_to_post = request.form['data']
    print("sendind data",data_to_post)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST_IP, HOST_PORT))
        s.send(data_to_post.encode())
        data_from_server = s.recv(1024)
        print("data_from_server", data_from_server)
        print(data_from_server)
        s.close()
    return data_from_server.decode()


if __name__ == '__main__':
   app.run()