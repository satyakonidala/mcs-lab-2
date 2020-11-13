
On Host
=============

For starting python backend
----------------
to create a venv folder (pre install venv: sudo apt-get install python3-venv):
```
python3 -m venv venv
. venv/bin/activate #activate the corresponding environment:
pip install -r requirements.txt #install from requirements.txt
```

export FLASK_APP=server.py && flask run


for starting frontend electron:
----------------
install electron and dependencies:
```
npm install -g electron
cd ./frontend
npm install
```


for starting electron:
cd ./frontend/ && npm start



On PI
=============

For switching on the stream on pi
----------------
on the PI,type the following instructions would open mpeg streamer to ythe electron app:
(https://github.com/jacksonliam/mjpg-streamer)

```
sudo apt-get install cmake libjpeg8-dev
sudo apt-get install gcc g++
cd ./pi/mjpg-streamer-experimental
make
sudo make install
```

From the mjpeg streamer experimental folder:
```
export LD_LIBRARY_PATH=.
./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"
```

to change the ip address to the PI's ip. (./frontend/index.html:38)


For starting pi wifi server
----------------
```
python3 ./pi/pi_wifi_server.py
```




