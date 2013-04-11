
class TicketOffice(object):
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

class Seat(object):
    def __init__(self, coach, seat_number):
        self.coach = coach
        self.seat_number = seat_number