
class TicketOffice(object):
	def __init__(self, trains=None):
		self.trains = trains or {}
	
	def add_train(self, train_id, train):
		self.trains[train_id] = train

    def make_reservation(self, reservation_request):
        # TODO: write this code!
        pass

class ReservationRequest(object):
    def __init__(self, train_id, seat_count):
        self.train_id = train_id
        self.seat_count = seat_count

class Reservation(object):
    def __init__(self, train_id, seats=None, booking_reference=None):
        self.train_id = train_id
        self.seats = seats or []
        self.booking_reference = booking_reference

class Train(object):
    def __init__(self, seats=None):
        self.seats = seats or []

class Seat(object):
    def __init__(self, carriage, seat_number):
        self.carriage = carriage
        self.seat_number = seat_number