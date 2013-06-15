require './ticket_office'
require './reservations'
require 'test/unit'

# integration
class TestTicketReservation < Test::Unit::TestCase

  def test_reserve_seats
    office = TicketOffice.new("http://localhost:8081", "http://localhost:8082")
    request = ReservationRequest.new("express_2000", 4)

    reservation = office.make_reservation(request)

    assert_equal 4, reservation.seats.size
    assert_equal "A", reservation.seats[0].coach
    assert_equal "75bcd15", reservation.booking_reference
  end

end
