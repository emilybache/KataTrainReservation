using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KataTrainReservation
{
    public class Seat
    {
        public string Coach { get; private set; }
        public int SeatNumber { get; private set; }

        public Seat(string coach, int seatNumber)
        {
            this.Coach = coach;
            this.SeatNumber = seatNumber;
        }

        public override int GetHashCode()
        {
            return base.GetHashCode();
        }

        /// <summary>
        /// N.B. this is not how you would override equals in a production environment. :)
        /// </summary>
        public override bool Equals(object obj)
        {
            Seat other = obj as Seat;

            return this.Coach == other.Coach && this.SeatNumber == other.SeatNumber;
        }
    }
}
