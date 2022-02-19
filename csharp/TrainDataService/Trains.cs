public class Trains : Dictionary<string, Train>
{
}

public record Train(Dictionary<string, Seat> seats);

public record Seat(string coach, string seat_number, string booking_reference);