# Kata: Train Reservation

Railway operators aren't always known for their use of cutting edge technology, and in this case they're a little behind the times. The railway people want you to help them to improve their online booking service. They'd like to be able to not only sell tickets online, but to decide exactly which seats should be reserved, at the time of booking.

You're working on the "TicketOffice" service, and your next task is to implement the feature for reserving seats on a particular train. The railway operator has a service-oriented architecture, and both the interface you'll need to fulfill, and some services you'll need to use are already implemented.

All the starting code for this kata is available in [my github repo](https://github.com/emilybache/KataTrainReservation). The latest version of these instructions is also there.

## Business Rules around Reservations

There are various business rules and policies around which seats may be reserved. For a train overall, no more than 70% of seats may be reserved in advance, and ideally no individual coach should have no more than 70% reserved seats either. However, there is another business rule that says you _must_ put all the seats for one reservation in the same coach. This could make you and go over 70% for some coaches, just make sure to keep to 70% for the whole train.

## The Guiding Test

The Ticket Office service needs to respond to a HTTP POST request that comes with form data telling you which train the customer wants to reserve seats on, and how many they want. It should return a json document detailing the reservation that has been made. 

A reservation comprises a json document with three fields, the train id, booking reference, and the ids of the seats that have been reserved. Example json:

	{"train_id": "express_2000", "booking_reference": "75bcd15", "seats": ["1A", "1B"]}

If it is not possible to find suitable seats to reserve, the service should instead return an empty list of seats and an empty string for the booking reference. The test cases in guiding_test.py outline the expected interface. (For Python 2.x users, there is also a version called 'python2\_guiding\_test.py')

### Command line option

If you think it's too hard to come up with a fully deployed HTTP service, you could instead write a command line program which takes the train id and number of seats as command line arguments, and returns the same json as above.

### Booking Reference Service

You can get a unique booking reference using a REST-based service. For test purposes, you can start a local service using the provided code in the "booking_reference_service" folder. You can assume the real service will behave the same way, but be available on a different url.

Install [Python 3.3](http://python.org) and [CherryPy](http://www.cherrypy.org/), then start the server by running:

    python booking_reference_service.py

You can use this service to get a unique booking reference. Make a GET request to:

    http://localhost:8082/booking_reference

This will return a string that looks a bit like this:

	75bcd15
	
### Train Data Service 

You can get information about which each train has by using the train data service. For test purposes, you can start a local service using the provided code in the "train_data_service" folder. You can assume the real service will behave the same way, but be available on a different url.

Again, you need [Python 3.3](http://python.org) and [CherryPy](http://www.cherrypy.org/), then start the server by running:

    python start_service.py

You can use this service to get data for example about the train with id "express_2000" like this:

    http://localhost:8081/data_for_train/express_2000

this will return a json document with information about the seats that this train has. The document you get back will look for example like this:

    {"seats": {"1A": {"booking_reference": "", "seat_number": "1", "coach": "A"}, "2A": {"booking_reference": "", "seat_number": "2", "coach": "A"}}}

Note I've left out all the extraneous details about where the train is going to and from, at what time, whether there's a buffet car etc. All that's there is which seats the train has, and if they are already booked. A seat is available if the "booking_reference" field contains an empty string. To reserve seats on a train, you'll need to make a POST request to this url:

    http://localhost:8081/reserve

and attach form data for which seats to reserve. There should be three fields: 

    "train_id", "seats", "booking_reference"

The "seats" field should be a json encoded list of seat ids, for example:

    '["1A", "2A"]'

The other two fields are ordinary strings. Note the server will prevent you from booking a seat that is already reserved with another booking reference.

The service has one additional method, that will remove all reservations on a particular train. Use it with care:

    http://localhost:8081/reset/express_2000

