
class TicketOffice(object):
    def make_reservation(self, reservation_request):
        # TODO: write this code!
        pass

class ReservationRequest(object):
    def __init__(self, train, seat_count):
        self.train = train
        self.seat_count = seat_count

class Reservation(object):
    def __init__(self, train, seats=None, booking_reference=None):
        self.train = train
        self.seats = seats or []
        self.booking_reference = booking_reference

class Train(object):
    def __init__(self, seats=None):
        self.seats = seats or []

class Seat(object):
    def __init__(self, carriage, seat_number):
        self.carriage = carriage
        self.seat_number = seat_number