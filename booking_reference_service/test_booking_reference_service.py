# Use py.test to run this test

from booking_reference_service import BookingReferenceService

def test_booking_number_looks_like_a_suitable_string():
    service = BookingReferenceService(123456789)
    booking_number = service.booking_reference()
    assert len(booking_number) > 5
    assert not booking_number.startswith("0x")
    
def test_booking_reference_is_unique():
    service = BookingReferenceService(123456789)
    booking_number1 = service.booking_reference()
    booking_number2 = service.booking_reference()
    assert not booking_number1 == booking_number2