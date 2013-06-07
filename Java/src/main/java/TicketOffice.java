public class TicketOffice {
    
    private TrainDataService trainDataService;

    public TicketOffice(String trainDataService, String bookingReferenceService) {
		//TODO: implement this code!
    }

    public TicketOffice(TrainDataService trainDataService, Object bookingReferenceService) {
        this.trainDataService = trainDataService;
    }

    public Reservation makeReservation(ReservationRequest request) {
        trainDataService.getTrainInformation("express_2000");
		return null;
    }

}