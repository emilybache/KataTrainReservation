import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
        // books all seats - maybe need to revisit later
        Seat aSeat = new Seat("A", 1);
        when(trainDataService.getTrainInformation(Matchers.anyString())).thenReturn(Arrays.asList(aSeat));

        ReservationRequest request = new ReservationRequest("express_2000", 1);
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

    @Test
    public void shouldBookOneSeat() {
        List<Seat> moreThanOneSeat = createSeatsUpTo(2);
        when(trainDataService.getTrainInformation(Matchers.anyString())).thenReturn(moreThanOneSeat);

        ReservationRequest request = new ReservationRequest("express_2000", 1);
        Reservation reservation = office.makeReservation(request);

        assertEquals(1, reservation.seats.size());
    }

    private List<Seat> createSeatsUpTo(int numberOfSeats) {
        List<Seat> seats = new ArrayList<Seat>();
        for (int i = 0; i < numberOfSeats; i++) {
            seats.add(new Seat("A", i));
        }
        return seats;
    }

    @Test
    // just here for regression
    public void shouldBookManySeats() {
        int requestedNumberOfSeats = 2;
        
        when(trainDataService.getTrainInformation(Matchers.anyString())).thenReturn(createSeatsUpTo(requestedNumberOfSeats + 3));

        ReservationRequest request = new ReservationRequest("express_2000", requestedNumberOfSeats);
        Reservation reservation = office.makeReservation(request);

        assertEquals(requestedNumberOfSeats, reservation.seats.size());
    }

    // more cases
    // not enough seats
    // train not available
    // reuse guidance test
    // continue with booking id
    // variate on booking id
}
