class TicketOffice

  def init(train_data_service, booking_reference_service)
  end

  def make_reservation(request)
    Reservation.new('', [Seat.new('','')])
  end
end
