"""
This is a guiding test for this kata. You can run it using python 3.3 like this:

    python3 -m unittest guiding_test.py

You need only implement one of the interfaces, and should edit this file to remove one of the test cases as appropriate. 
You should also change the value of the "reservation_script" variable to match the name of your command line program, if
that is the interface you have chosen.
"""

import urllib.request
import json
import subprocess
import unittest
import os

url = "http://127.0.0.1:8083"
interpreter = "python3"
reservation_script = os.path.join("python", "reserve.py")

class TrainReservationTest(unittest.TestCase):

    def hidden_test_reserve_seats_via_POST(self):
        form_data = {"train_id": "express_2000", "seats": 4}
        data = urllib.parse.urlencode(form_data)
        
        req = urllib.request.Request(url + "/reserve", bytes(data, encoding="ISO-8859-1"))
        response = urllib.request.urlopen(req).read().decode("ISO-8859-1")
        reservation = json.loads(response)
        
        assert 4 == len(reservation["seats"])
        assert "1A" == reservation["seats"][0]
        assert "75bcd15" == reservation["booking_reference"]


    def test_reserve_seats_via_cmd(self):
        response = subprocess.check_output([interpreter, reservation_script, "express2000", "4"], stderr=subprocess.STDOUT, universal_newlines = True)
        reservation = json.loads(response)
        
        assert 4 == len(reservation["seats"])
        assert "1A" == reservation["seats"][0]
        assert "75bcd15" == reservation["booking_reference"]
