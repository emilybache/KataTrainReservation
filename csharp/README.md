# Instructions to run the C# services

### Booking Reference Service

You can get a unique booking reference using a REST-based service. For test purposes, you can start a local service using the provided code in the "BookingReferenceService" project. You can assume the real service will behave the same way, but be available on a different url.

    cd BookingReferenceService
    dotnet run

You can use this service to get a unique booking reference. Make a GET request to:

    http://localhost:5041/booking_reference

This will return a string that looks a bit like this:

	75bcd15
	
### Train Data Service 

You can get information about which each train has by using the train data service. For test purposes, you can start a local service using the provided code in the "TrainDataService" project. You can assume the real service will behave the same way, but be available on a different url.

    cd TrainDataService
    dotnet run

You can use this service to get data for example about the train with id "express_2000" like this:

    http://localhost:5091/data_for_train/express_2000

this will return a json document with information about the seats that this train has. The document you get back will look for example like this:

    {"seats": {"1A": {"booking_reference": "", "seat_number": "1", "coach": "A"}, "2A": {"booking_reference": "", "seat_number": "2", "coach": "A"}}}

Note I've left out all the extraneous details about where the train is going to and from, at what time, whether there's a buffet car etc. All that's there is which seats the train has, and if they are already booked. A seat is available if the "booking_reference" field contains an empty string. To reserve seats on a train, you'll need to make a POST request to this url:

    http://localhost:5091/reserve

and attach form data for which seats to reserve. There should be three fields: 

    "train_id", "seats", "booking_reference"

The "seats" field should be a json encoded list of seat ids, for example:

    '["1A", "2A"]'

The other two fields are ordinary strings. Note the server will prevent you from booking a seat that is already reserved with another booking reference.

The service has one additional method, that will remove all reservations on a particular train. Use it with care:

    http://localhost:5091/reset/express_2000

