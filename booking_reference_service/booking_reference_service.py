"""
You can get a unique booking reference using this service. For test purposes, you can start a local service using this code. You can assume the real service will behave the same way, but be available on a different url.

Install [Python 3.3](http://python.org) and [CherryPy](http://www.cherrypy.org/), then start the server by running:

    python booking_reference_service.py

You can use this service to get a unique booking reference. Make a GET request to:

    http://localhost:8082/booking_reference

This will return a string that looks a bit like this:

	75bcd15
"""

import cherrypy
import itertools

class BookingReferenceService(object):
    def __init__(self, starting_point):
        self.counter = itertools.count(starting_point)
    
    def booking_reference(self):
        next_number = next(self.counter)
        return str(hex(next_number))[2:]
        
    booking_reference.exposed = True
    
def main(args):
    if args:
        starting_point = int(args[0], 16) + 1
    else:
        starting_point = 123456789

    cherrypy.config.update({"server.socket_port" : 8082})
    cherrypy.quickstart(BookingReferenceService(starting_point))

if __name__ == "__main__":
    import sys
    help_text = """
Use this program to start a booking reference service:

    python {0}

The service will start on this url:

    http://localhost:8082/booking_reference

If you have to restart the service, you can continue counting from the
previous reference by passing it on the command line:

    python {0} 75bcd15
    """.format(sys.argv[0])
    if "-help" in sys.argv or "--help" in sys.argv or "-h" in sys.argv:
        print(help_text)
    else:
        main(sys.argv[1:])