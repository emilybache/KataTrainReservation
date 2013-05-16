using Microsoft.VisualStudio.TestTools.UnitTesting;
using TrainWreck.Core;

namespace KataTrainReservation
{
    [TestClass]
    public class TicketOfficeTest {
    
        [TestMethod]
        public void reserveSeats() {
            TicketOffice office = new TicketOffice("http://localhost:8081", "http://localhost:8082");
            ReservationRequest request = new ReservationRequest("express_2000", 4);
    
            Reservation reservation = office.MakeReservation(request);
    
            Assert.AreEqual(4, reservation.Seats.Count);
            Assert.AreEqual("A", reservation.Seats[0].Coach);
            Assert.AreEqual("75bcd15", reservation.BookingId);

        }
    }
}