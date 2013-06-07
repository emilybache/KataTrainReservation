import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.util.Arrays;

import org.junit.Before;
import org.junit.Test;
import org.mockito.Matchers;

public class TicketOfficeTest {

    private TrainDataService trainDataService;
    private TicketOffice office;

    @Before
    public void createOffice() {
        trainDataService = mock(TrainDataService.class);
        office = new TicketOffice(trainDataService, null);
    }
    
    @Test
    public void shouldCallTrainDataServiceForTrainInformation() {
        ReservationRequest request = new ReservationRequest("express_2000", 4);
        office.makeReservation(request);

        verify(trainDataService).getTrainInformation(Matchers.eq("express_2000"));
    }

    @Test
    public void shouldReturnValuesProvidedByTrainDataService() {
        Seat aSeat = new Seat("A", 1);
        when(trainDataService.getTrainInformation(Matchers.anyString())).thenReturn(Arrays.asList(aSeat));

        ReservationRequest request = new ReservationRequest("express_2000", 4);
        Reservation reservation = office.makeReservation(request);

        assertEquals(aSeat, reservation.seats.get(0));
        assertEquals("express_2000", reservation.trainId);
    }
    
    @Test
    public void shouldCallTrainDataServiceForTrainInformationAsGivenInRequest() {
        ReservationRequest request = new ReservationRequest("cool_train", 4);
        office.makeReservation(request);

        verify(trainDataService).getTrainInformation(Matchers.eq("cool_train"));
    }

}
