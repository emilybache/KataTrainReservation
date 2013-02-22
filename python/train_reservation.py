
def reserve_seats(train, reservation_request):
    # TODO: write this code!
    pass

class ReservationRequest(object):
    def __init__(self, seat_count):
        self.seat_count = seat_count

class Reservation(object):
    def __init__(self, train, seats=None, booking_reference=None):
        self.train = train
        self.seats = seats or []
        self.booking_reference = booking_reference

class Train(object):
    def __init__(self, carriages=None, maximum_reservation_percentage=70):
        self.carriages = carriages or []
        self.maximum_reservation_percentage = maximum_reservation_percentage

class Carriage(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat(self) for i in range(capacity)]
        
class Seat(object):
    def __init__(self, carriage):
        self.carriage = carriage
        
