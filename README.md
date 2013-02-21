
Your task is to implement a feature for reserving seats on a train. A Train has some Carriages and each Carriage has some Seats. (This project contains starting code for these classes).

There is a business rule that says that for the train overall, no more than 70% of seats may be reserved in advance, and ideally no individual carriage should have more reservations than this either.

Your task is to write the code that takes a reservation request, and finds a suitable carriage for it to reserve seats in. (All the seats for one reservation should preferably be in the same carriage). You should return a Reservation object that lists the seats you have booked. If there are no suitable seats available to reserve, return an empty Reservation. 

For part II of this kata, introduce different sorts of seat reservation, for first and second class, aisle or window, table or no table. Any one carriage will have a mixture of aisle, window and table seats, but will be either all first- or all second-class.