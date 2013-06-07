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
        List<Seat> trainInformation = trainDataService.getTrainInformation(request.trainId);
		return new Reservation(request.trainId, trainInformation, "");
    }

}