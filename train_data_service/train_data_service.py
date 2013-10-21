"""
You can get information about which each train has by using this service. For test purposes, you can start a local service using this code. You can assume the real service will behave the same way, but be available on a different url.

You need [Python 3.3](http://python.org) and [CherryPy](http://www.cherrypy.org/), then start the server by running:

    python start_service.py

You can use this service to get data for example about the train with id "express_2000" like this:

    http://localhost:8081/data_for_train/express_2000

this will return a json document with information about the seats that this train has. The document you get back will look for example like this:

    {"seats": {"1A": {"booking_reference": "", "seat_number": "1", "coach": "A"}, "2A": {"booking_reference": "", "seat_number": "2", "coach": "A"}}}

Note I've left out all the extraneous details about where the train is going to and from, at what time, whether there's a buffet car etc. All that's there is which seats the train has, and if they are already booked. A seat is available if the "booking_reference" field contains an empty string. To reserve seats on a train, you'll need to make a POST request to this url:

    http://localhost:8081/reserve

and attach form data for which seats to reserve. There should be three fields: 

    "train_id", "seats", "booking_reference"

The "seats" field should be a json encoded list of seat ids, for example:

    '["1A", "2A"]'

The other two fields are ordinary strings. Note the server will prevent you from booking a seat that is already reserved with another booking reference.

The service has one additional method, that will remove all reservations on a particular train. Use it with care:

    http://localhost:8081/reset/express_2000
"""
import json

class TrainDataService(object):
    
    def __init__(self, json_data):
        self.trains = json.loads(json_data)
    
    def data_for_train(self, train_id):
        return json.dumps(self.trains.get(train_id))
    
    def reserve(self, train_id, seats, booking_reference):
        train = self.trains.get(train_id)
        seats = json.loads(seats)
        for seat in seats:
            if not seat in train["seats"]:
                return "seat not found {0}".format(seat)
            existing_reservation =  train["seats"][seat]["booking_reference"]
            if existing_reservation and existing_reservation != booking_reference:
                return "already booked with reference: {0}".format(existing_reservation)
        for seat in seats:
            train["seats"][seat]["booking_reference"] = booking_reference
        return self.data_for_train(train_id)

    def reset(self, train_id):
        train = self.trains.get(train_id)
        for seat_id, seat in train["seats"].items():
            seat["booking_reference"] = ""
        return self.data_for_train(train_id)
    
