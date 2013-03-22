
import cherrypy
import itertools

class BookingReferenceService(object):
    def __init__(self, starting_point):
        self.counter = itertools.count(starting_point)
    
    def booking_reference(self):
        next_number = self.counter.next()
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
    help_text = """
Use this program to start a booking reference service:

    python booking_reference_service.py

The service will start on this url:

    http://localhost:8082/booking_reference

If you have to restart the service, you can continue counting from the
previous reference by passing it on the command line:

    python booking_reference_service.py 75bcd15
    """
    import sys
    if "-help" in sys.argv or "--help" in sys.argv or "-h" in sys.argv:
        print help_text
    else:
        main(sys.argv[1:])