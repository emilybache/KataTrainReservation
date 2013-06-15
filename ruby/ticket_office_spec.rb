require './ticket_office'
require './reservations'

describe TicketOffice do

  it 'should return reservation' do
    office  = TicketOffice.new
    request = ReservationRequest.new("express_2000", 4)

    reservation = office.make_reservation(request)
    expect(reservation).to be_a Reservation
  end

  it 'should ask for train data' do
    #fake_data = double() - not needed yet
    #fake_data.stub(:seats) { [] }
    office  = TicketOffice.new
    request = ReservationRequest.new("express_2000", 1)

    reservation = office.make_reservation(request)
    expect(reservation.seats.size).to eq 1
  end

  # TODO add another test to should return emptz reservation when not found
end
