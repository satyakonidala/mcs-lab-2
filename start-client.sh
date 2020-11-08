#! bin/bash

cd ./frontend && npm start

export FLASK_APP=server.py && flask run