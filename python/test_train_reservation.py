
import unittest

from reservations import *
from ticket_office import *

class TestTicketOffice(unittest.TestCase):

    def test_reserve_seats(self):
        office = TicketOffice(train_data_service = "http://localhost:8081", 
                              booking_reference_service = "http://localhost:8082")
        request = ReservationRequest(train_id="express_2000", seat_count=4)
        
        reservation = office.make_reservation(request)
        
        self.assertEqual(4, len(reservation.seats))
        self.assertEqual("A", reservation.seats[0].coach)
        self.assertEqual("75bcd15", reservation.booking_reference)

if __name__ == '__main__':
    unittest.main()