from Request import *
import pytest

def test_auto_id():
    class_counter = Request.class_counter

    first_request = Request(1, "water bottle")
    second_request = Request(2, "water bottle")
    first_id = first_request.get_id()
    second_id = second_request.get_id()
    assert first_id is class_counter
    assert second_id is class_counter + 1


def test_get_id():
    check_id_req = Request(1, "water bottle")
    number = check_id_req.get_id()
    assert number >= 0 and isinstance(number, int)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
