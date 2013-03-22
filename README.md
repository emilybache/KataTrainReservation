
# Kata: Train Reservation

You're working on some software for a railway operator, that will be part of their online booking system. You're working on the "TicketOffice" class, and your next task is to implement a feature for reserving seats on a train. The TicketOffice class needs a method "make_reservation" that will return a Reservation object. It will take as argument a ReservationRequest object, which contains all the needed information about what the customer wants, including which train they want to go on, and the number of seats they need.

Your task is to write the code that takes a ReservationRequest, and finds suitable seats to reserve. You should return a Reservation object that lists the seats you have booked, and a booking reference. If it is not possible to find suitable seats to reserve, return an empty Reservation with no booking reference.

You can get a unique booking reference using a REST-based service. For test purposes, you can start a local service using the provided code in the "booking_reference_service" folder. You can assume the real service will behave the same way, but be available on a different url.

Install [Python](http://python.org) and [CherryPy](http://www.cherrypy.org/), then start the server by running:

    python booking_reference_service.py

You can use this service to get a unique booking reference. Make a GET request to: 

    http://localhost:8082/booking_reference

You can get information about which each train has by using the train data service. For test purposes, you can start a local service using the provided code in the "train_data_service" folder. You can assume the real service will behave the same way, but be available on a different url.

Install [Python](http://python.org) and [CherryPy](http://www.cherrypy.org/), then start the server by running:

    python train_data_service.py

You can use this service to get data for example about the train with id "express_2000" like this:

    http://localhost:8081/data_for_train/express_2000

this will return a json document with information about the seats that this train has.

## Part 2: business rules around reservations

When you have basic seat reservation working, you should start paying attention to the business rules and policies around which seats may be reserved. For the train overall, no more than 70% of seats may be reserved in advance, and ideally no individual carriage should have no more than 70% reserved seats either. However, there is another business rule that says you _must_ put all the seats for one reservation in the same carriage. This could make you and go over 70% for some carriages, just make sure to keep to 70% for the whole train.
