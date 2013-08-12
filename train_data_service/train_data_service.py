
import json

class TrainDataService(object):
    
    def __init__(self, json_data):
        self.trains = json.loads(json_data)
    
    def data_for_train_as_dict(self, train_id):
        return self.trains.get(train_id)
        
    def data_for_train(self, train_id):
        return json.dumps(self.data_for_train_as_dict(train_id))
    
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
    
