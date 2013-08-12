"""This module uses Flask to expose a TrainDataService to http requests"""

from flask import Flask
from flask import request
app = Flask(__name__)

from train_data_service import TrainDataService

TRAIN_DATA = None

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/data_for_train/<train_id>')
def data_for_train(train_id):
    return TRAIN_DATA.data_for_train(train_id)

@app.route('/reserve', methods=["POST"])
def reserve():
    train_id = request.form["train_id"]
    seat_ids = request.form["seats"]
    booking_reference = request.form["booking_reference"]
    return TRAIN_DATA.reserve(train_id, seat_ids, booking_reference)

@app.route('/reset/<train_id>')
def reset(train_id):
    return TRAIN_DATA.reset(train_id)

def start(trains_data):
    global TRAIN_DATA
    TRAIN_DATA = TrainDataService(trains_data)

    app.config["SERVER_NAME"] = "127.0.0.1:8081"
    app.config["DEBUG"] = True
    app.run()
