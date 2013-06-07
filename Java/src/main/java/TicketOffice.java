import java.util.List;

public class TicketOffice {

    private TrainDataService trainDataService;

    public TicketOffice(String trainDataService, String bookingReferenceService) {
        //TODO: implement this code!
    }

    public TicketOffice(TrainDataService trainDataService, Object bookingReferenceService) {
        this.trainDataService = trainDataService;
    }

    public Reservation makeReservation(ReservationRequest request) {
        List<Seat> availableSeats = trainDataService.getTrainInformation(request.trainId);
        
        boolean notEnoughSeats = availableSeats.size() < request.seatCount;
        if (notEnoughSeats) {
            return null;
        }
        
        List<Seat> requestedSeats = availableSeats.subList(0, request.seatCount);
        return new Reservation(request.trainId, requestedSeats, "");
    }

}