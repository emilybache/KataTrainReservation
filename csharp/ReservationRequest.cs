using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace KataTrainReservation
{
    public class ReservationRequest
    {
        public int TrainId { get; private set; }
        public int SeatCount { get; private set; }

        public ReservationRequest(int trainId, int seatCount)
        {
            this.TrainId = trainId;
            this.SeatCount = seatCount;
        }
    }
}