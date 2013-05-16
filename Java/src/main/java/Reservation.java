
public class Reservation {
	public final String trainId;
    public final String bookingId;
    public final Seat[] seats;

    public Reservation(String trainId, Seat[] seats, String bookingId) {
		this.trainId = trainId;
        this.bookingId = bookingId;
        this.seats = seats;
    }

}