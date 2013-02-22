
import cherrypy
import itertools

class BookingReferenceService(object):
    def __init__(self, starting_point):
        self.counter = itertools.count(starting_point)
    
    def booking_reference(self):
        next_number = self.counter.next()
        return str(hex(next_number))[2:]
        
    booking_reference.exposed = True
    
if __name__ == "__main__":
    """ 
    Use this code to start a booking reference service on http://localhost:8080/booking_reference
    
    If you have to restart the service, you can continue counting from the previous reference
    by passing it on the command line
    """
    import sys
    if len(sys.argv) > 1:
        starting_point = int(sys.argv[1], 16) + 1
    else:
        starting_point = 123456789
    
    cherrypy.quickstart(BookingReferenceService(starting_point))