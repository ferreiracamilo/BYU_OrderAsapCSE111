import pytest
from Order import *
from Customer import *
from faker import Faker
import random

sample = Faker()

print(f'name: {sample.idnumber()}')
print(f'address: {sample.address()}')

def test_auto_id():
    class_counter = Order.class_counter
    customer_one = Customer(random.randint(0,100), sample.first_name(), sample.last_name(), sample.date(), sample.address(), sample.address())
    # customer, discount, tax_rate):
     

    first_product = Order(1, "water bottle")
    second_product = Order(2, "water bottle")
    first_id = first_product.get_id()
    second_id = second_product.get_id()
    assert first_id is class_counter
    assert second_id is class_counter + 1


def test_get_id():
    check_id_req = Order(1, "water bottle")
    number = check_id_req.get_id()
    assert number >= 0 and isinstance(number, int)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])