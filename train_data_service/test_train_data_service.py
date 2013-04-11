# Use py.test to run this test

from train_data_store import TrainDataService

def test_fetch_train_data():
    service = TrainDataService("""{ "foo_train": {"seats": [ {"coach": "A", "seat_number": "1"} ]}}""")
    train_data = service.data_for_train("foo_train")
    assert train_data == """{"seats": [{"coach": "A", "seat_number": "1"}]}"""
        
