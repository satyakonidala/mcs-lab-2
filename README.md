
# For python backend
to create a venv folder (pre install venv: sudo apt-get install python3-venv):
python3 -m venv venv

activate the corresponding environment:
. venv/bin/activate


install from requirements.txt
pip install -r requirements.txt


export FLASK_APP=server.py && flask run


# For frontend

## for switching on the stream on pi
on the PI,type the following instructions would open mpeg streamer to ythe electron app:
(https://github.com/jacksonliam/mjpg-streamer)

to change the ip address to the PI's ip. (./frontend/index.html:38)

## for starting frontend electron:
npm install -g electron

for starting electron:
cd ./frontend/ && npm install && npm start
 



# References
https://stackoverflow.com/questions/22615475/flask-application-with-background-threads


