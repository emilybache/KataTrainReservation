class ReservationRequest
  attr_reader :train_id
  attr_reader :seat_count

  def initialize(train_id, seat_count)
    @train_id = train_id
    @seat_count = seat_count
  end
end

class Reservation
  attr_reader :train_id
  attr_reader :seats

  def initialize(train_id, seats)
    @train_id = train_id
    @seats = seats
  end
end

class Seat
  attr_reader :coach
  attr_reader :number

  def initialize(coach, number)
    @coach = coach
    @number = number
  end
end