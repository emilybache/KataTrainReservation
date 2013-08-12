""" Use py.test to run this test """

import json

from train_data_service import TrainDataService

def test_fetch_train_data():
    service = TrainDataService("""{ "foo_train": {"seats": {"1A": {"coach": "A", "seat_number": "1", "booking_reference": ""} }}}""")
    train_data = service.data_for_train("foo_train")
    assert "1A" in train_data

def test_reserve_seat():
     service = TrainDataService("""{ "foo_train": {"seats": {"1A": {"coach": "A", "seat_number": "1", "booking_reference": ""} }}}""")
     service.reserve("foo_train", json.dumps(["1A"]), "01234567")
     train_data = service.data_for_train("foo_train")
     assert '"booking_reference": "01234567"' in train_data

def test_reserve_seat_when_already_reserved():
    service = TrainDataService("""{ "foo_train": {"seats": {"1A": {"coach": "A", "seat_number": "1", "booking_reference": "existing"} }}}""")
    response = service.reserve("foo_train", json.dumps(["1A"]), "01234567")
    assert "already booked with reference: existing" in response
    train_data = service.data_for_train("foo_train")
    assert '"booking_reference": "existing"' in train_data

def test_reserve_with_typo_in_seatid():
    service = TrainDataService("""{ "foo_train": {"seats": {"1A": {"coach": "A", "seat_number": "1", "booking_reference": "existing"} }}}""")
    response = service.reserve("foo_train", json.dumps(["typo"]), "01234567")
    assert "seat not found typo" in response

def test_reset():
    service = TrainDataService("""{ "foo_train": {"seats": {"1A": {"coach": "A", "seat_number": "1", "booking_reference": "existing"} }}}""")
    train_data = service.reset("foo_train")
    assert 'existing' not in train_data
