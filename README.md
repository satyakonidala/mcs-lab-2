
On Host
=============

Start python backend
----------------
to create a venv folder (pre install venv: sudo apt-get install python3-venv):

activate the venv environment and install from requirements.txt
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

start the server
```bash
export FLASK_APP=server.py && flask run
```

Install and frontend electron:
----------------
install electron and dependencies:
```bash
npm install -g electron
cd ./frontend
npm install
```


for starting electron:
```bash
cd ./frontend/ && npm start
```


On PI
=============

Switch on video stream on pi
----------------
on the PI,type the following instructions would open mpeg streamer to ythe electron app:
(https://github.com/jacksonliam/mjpg-streamer)

```bash
sudo apt-get install cmake libjpeg8-dev
sudo apt-get install gcc g++
cd ./pi/mjpg-streamer-experimental
make
sudo make install
```

From the mjpeg streamer experimental folder:
```bash
export LD_LIBRARY_PATH=.
./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"
```

to change the ip address to the PI's ip. (./frontend/index.html:38)


Start pi wifi server
----------------
```bash
python3 ./pi/pi_wifi_server.py
```




