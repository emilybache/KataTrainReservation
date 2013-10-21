"""
Equivalent of 'guiding_test.py' except for Python2.x, which comes as standard on many systems.

Run it with:

    python python2_guiding_test.py

"""
import json
import subprocess
import unittest
import os
import urllib2, urllib

url = "http://127.0.0.1:8083"
interpreter = "python"
reservation_script = os.path.join("python", "reserve.py")

class TrainReservationTest(unittest.TestCase):

    def test_reserve_seats_via_POST(self):
        form_data = {"train_id": "express_2000", "seat_count": 4}
        data = urllib.urlencode(form_data)
        
        response = urllib2.urlopen(url + "/reserve", data=data).read()
        reservation = json.loads(response)
        
        assert "express_2000" == reservation["train_id"]
        assert 4 == len(reservation["seats"])
        assert "1A" == reservation["seats"][0]
        assert "75bcd15" == reservation["booking_reference"]


    def test_reserve_seats_via_cmd(self):
        response = subprocess.check_output([interpreter, reservation_script, "express2000", "4"], stderr=subprocess.STDOUT, universal_newlines = True)
        reservation = json.loads(response)
        
        assert "express_2000" == reservation["train_id"]
        assert 4 == len(reservation["seats"])
        assert "1A" == reservation["seats"][0]
        assert "75bcd15" == reservation["booking_reference"]



if __name__ == "__main__":
    unittest.main()