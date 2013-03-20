
class TicketOffice(object):
    def reserve_seats(self, reservation_request):
        # TODO: write this code!
        pass

class ReservationRequest(object):
    def __init__(self, train, seat_count):
        this.train = train
        self.seat_count = seat_count

class Reservation(object):
    def __init__(self, train, seats=None, booking_reference=None):
        self.train = train
        self.seats = seats or []
        self.booking_reference = booking_reference

