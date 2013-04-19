using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KataTrainReservation
{
    public class Reservation
    {
        public string TrainId { get; private set; }
        public string BookingId { get; private set; }
        public List<Seat> Seats { get; private set; }

        public Reservation(string trainId, string bookingId, List<Seat> seats)
        {
            this.TrainId = trainId;
            this.BookingId = bookingId;
            this.Seats = seats;
        }
    }
}
