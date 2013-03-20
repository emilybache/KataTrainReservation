
# Kata: Train Reservation

You're working on some software for a railway operator, that will be part of their online booking system. You're working on the "TicketOffice" class, and your next task is to implement a feature for reserving seats on a train. The TicketOffice class needs a method "reserveSeats" that will return a Reservation object. It will take as argument a ReservationRequest object, which contains all the needed information about what the customer wants, including which train they want to go on, and the number of seats they need.

There is a business rule that says that for the train overall, no more than 70% of seats may be reserved in advance, and ideally no individual carriage should have no more than 70% reserved seats either. However, there is another business rule that says you must put all the seats for one reservation in the same carriage. This could make you and go over 70% for some carriages, just make sure to keep to 70% for the whole train.

Your task is to write the code that takes a reservation request, and finds a suitable carriage for it to reserve seats in. You should return a Reservation object that lists the seats you have booked, and a booking reference. If it is not possible to find suitable seats to reserve, return an empty Reservation with no booking reference.

You can get a unique booking reference using a REST-based service. For this kata, use the provided code in the "booking_reference_service" folder. Install [Python](http://python.org) and [CherryPy](http://www.cherrypy.org/), then start the server by running:

    python booking_reference_service.py

You can use this service to get a unique booking reference. Make a GET request to: 

    http://localhost:8080/booking_reference
