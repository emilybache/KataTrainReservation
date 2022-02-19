public class Trains : Dictionary<string, Train>
{
}

public record Train(Dictionary<string, Seat> seats);

public class Seat
{
    public string coach { get; init; }
    public string seat_number { get; init; }
    public string booking_reference { get; set; }
}

public record ReserveRequest(string train_id, string[] seats, string booking_reference);
