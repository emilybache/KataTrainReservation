import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.util.Arrays;

import org.junit.Test;
import org.mockito.Matchers;

public class TicketOfficeTest {

    @Test
    public void shouldCallTrainDataServiceForTrainInformation() {
        TrainDataService trainDataService = mock(TrainDataService.class);
        TicketOffice office = new TicketOffice(trainDataService, null);

        ReservationRequest request = new ReservationRequest("express_2000", 4);

        office.makeReservation(request);

        verify(trainDataService).getTrainInformation(Matchers.eq("express_2000"));
    }

    @Test
    public void shouldReturnValuesProvidedByTrainDataService() {
        Seat aSeat = new Seat("A", 1);

        TrainDataService trainDataService = mock(TrainDataService.class);
        when(trainDataService.getTrainInformation(Matchers.anyString())).thenReturn(Arrays.asList(aSeat));

        TicketOffice office = new TicketOffice(trainDataService, null);
        ReservationRequest request = new ReservationRequest("express_2000", 4);

        Reservation reservation = office.makeReservation(request);
        assertEquals(aSeat, reservation.seats.get(0));
    }
}
