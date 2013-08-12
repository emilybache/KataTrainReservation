
import urllib.request

url = "http://127.0.0.1:8082"

data = urllib.request.urlopen(url + "/booking_reference")
print("got booking reference: ", data.read().decode("utf-8"))
