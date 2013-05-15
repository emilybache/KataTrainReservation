using NUnit.Framework;

namespace KataTrainReservation
{
    [TestFixture]
    public class TicketOfficeTest {
    
        [Test]
        public void reserveSeats() {
            TicketOffice office = new TicketOffice("http://localhost:8081", "http://localhost:8082");
            ReservationRequest request = new ReservationRequest("express_2000", 4);
    
            Reservation reservation = office.makeReservation(request);
    
            Assert.AreEqual(4, reservation.seats.length);
            Assert.AreEqual("A", reservation.seats[0].coach);
            Assert.AreEqual("75bcd15", reservation.booking_reference);

        }
    }
}
