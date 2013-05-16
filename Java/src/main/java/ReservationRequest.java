
public class ReservationRequest {
	public final String trainId;
    public final int seatCount;

    public ReservationRequest(String trainId, int seatCount) {
		this.trainId = trainId;
        this.seatCount = seatCount;
    }

}