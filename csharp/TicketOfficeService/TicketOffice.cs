namespace TicketOfficeService;

public record ReservationRequest(string TrainId, int SeatCount);
public record Reservation(string TrainId, string BookingId, List<Seat> Seats);
public record Seat(string Coach, int SeatNumber);

public class TicketOffice
{
    public Reservation MakeReservation(ReservationRequest request)
    {
        //TODO: implement this code!
        throw new NotImplementedException();
    }
}