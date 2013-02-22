
import urllib2, urllib

def example_client():
    request = urllib2.Request("http://localhost:8080/booking_number")
    booking_number = urllib2.urlopen(request).read()
    return booking_number

        
