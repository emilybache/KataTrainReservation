import urllib.request
import json

url = "http://127.0.0.1:8081"

# check for free seats on the train "express_2000"
train_data = urllib.request.urlopen(url + "/data_for_train/express_2000")
print("original reservation situation: ", train_data.read().decode("utf-8"))

# book a seat
train_id = "express_2000"
seats = ["1A"]
booking_reference = "01234567"

form_data = {"train_id": train_id, "seats": json.dumps(seats), "booking_reference": booking_reference}
data = urllib.parse.urlencode(form_data)
req = urllib.request.Request(url + "/reserve", bytes(data, encoding="ISO-8859-1"))
print("situation after reservation: ", urllib.request.urlopen(req).read().decode("utf-8"))

# reserve the seat again and it is not updated
train_id = "express_2000"
seats = ["1A"]
booking_reference = "new_reference"

form_data = {"train_id": train_id, "seats": json.dumps(seats), "booking_reference": booking_reference}
data = urllib.parse.urlencode(form_data)
req = urllib.request.Request(url + "/reserve", bytes(data, encoding="ISO-8859-1"))
print("reservation should have failed: ", urllib.request.urlopen(req).read().decode("utf-8"))

# remove all seat reservations for train express_2000
reset = urllib.request.urlopen(url + "/reset/express_2000")
print("reservations are all removed: ", reset.read().decode("utf-8"))
