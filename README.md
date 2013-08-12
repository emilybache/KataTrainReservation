# Kata: Train Reservation

Railway operators aren't always known for their use of cutting edge technology, and in this case they're a little behind the times. The railway people want you to help them to improve their online booking service. They'd like to be able to not only sell tickets online, but to decide exactly which seats should be reserved, at the time of booking.

You're working on the "TicketOffice" class, and your next task is to implement the feature for reserving seats on a particular train. The TicketOffice class needs a method "make_reservation" that will return a Reservation object. It will take as argument a ReservationRequest object, which contains all the needed information about what the customer wants, including which train they want to go on, and the number of seats they need.

Your task is to write the code that takes a ReservationRequest, and finds suitable seats to reserve. You should return a Reservation object that lists the seats you have booked, and a booking reference. If it is not possible to find suitable seats to reserve, return an empty Reservation with no booking reference. You'll also need to design a way to store the information about which seats are reserved on which train.

All the starting code for this kata is available in [my github repo](https://github.com/emilybache/KataTrainReservation). The latest version of these instructions is also there.

### The Services for Booking Reference and Train Data

You can get a unique booking reference using a REST-based service. For test purposes, you can start a local service using the provided code in the "booking_reference_service" folder. You can assume the real service will behave the same way, but be available on a different url.

Install [Python 3.3](http://python.org) and [CherryPy](http://www.cherrypy.org/), then start the server by running:

    python booking_reference_service.py

You can use this service to get a unique booking reference. Make a GET request to:

    http://localhost:8082/booking_reference

This will return a string that looks a bit like this:

	75bcd15

You can get information about which each train has by using the train data service. For test purposes, you can start a local service using the provided code in the "train_data_service" folder. You can assume the real service will behave the same way, but be available on a different url.

Again, you need [Python 3.3](http://python.org) and [CherryPy](http://www.cherrypy.org/), then start the server by running:

    python start_service.py

You can use this service to get data for example about the train with id "express_2000" like this:

    http://localhost:8081/data_for_train/express_2000

this will return a json document with information about the seats that this train has. The document you get back will look for example like this:

    {"seats": {"7B": {"booking_reference": "", "seat_number": "7", "coach": "B"}, "3A": {"booking_reference": "", "seat_number": "3", "coach": "A"}}

Note I've left out all the extraneous details about where the train is going to and from, at what time, whether there's a buffet car etc. All that's there is which seats the train has, and if they are already booked, the "booking_reference" field will not be empty. To reserve seats on a train, you'll need to make a POST request to this url:

    http://localhost:8081/reserve

and attach form data for which seats to reserve. There should be three fields: 

    "train_id", "seats", "booking_reference"

The "seats" field should be a json encoded list of seat ids, for example:

    '["1A", "1B"]'

The other two fields are ordinary strings. Note the server will prevent you from booking a seat that is already reserved with another booking reference.

The service has one additional method, that will remove all reservations on a particular train:

    http://localhost:8081/reset/express_2000

## Part 2: Business Rules around Reservations

When you have basic seat reservation working, you should start paying attention to the business rules and policies around which seats may be reserved. For the train overall, no more than 70% of seats may be reserved in advance, and ideally no individual coach should have no more than 70% reserved seats either. However, there is another business rule that says you _must_ put all the seats for one reservation in the same coach. This could make you and go over 70% for some coaches, just make sure to keep to 70% for the whole train.
