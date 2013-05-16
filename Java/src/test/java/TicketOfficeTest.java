import org.junit.*;
import static org.junit.Assert.*;

public class TicketOfficeTest {
    
    @Test
    public void reserveSeats() {
        TicketOffice office = new TicketOffice("http://localhost:8081", "http://localhost:8082");
        ReservationRequest request = new ReservationRequest("express_2000", 4);
    
        Reservation reservation = office.makeReservation(request);
    
        assertEquals(4, reservation.seats.length);
        assertEquals("A", reservation.seats[0].coach);
        assertEquals("75bcd15", reservation.bookingId);

    }
}
