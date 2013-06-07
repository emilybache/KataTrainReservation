import static org.junit.Assert.*;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.mock;

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
}
