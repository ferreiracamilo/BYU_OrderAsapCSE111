from Request import *
import pytest

def test_auto_increment_id():
    class_counter = Request.class_counter
    first_request = Request(1, "water bottle")
    second_request = Request(2, "water bottle")
    first_id = first_request.get_id()
    second_id = second_request.get_id()
    assert first_id is class_counter, "ID does not match with class counter"
    assert second_id is class_counter + 1, "Next ID does not match value expected"


def test_id_valtype():
    check_id_req = Request(1, "water bottle")
    number = check_id_req.get_id()
    assert isinstance(number, int), "ID is not number type"
    assert number >= 1, "ID is smaller than 1"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
