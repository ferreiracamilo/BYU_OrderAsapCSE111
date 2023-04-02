import pytest
from Order import *
from Customer import *
from Product import *
from Request import *
from faker import Faker
import random

sample = Faker()

def test_subtotal_calculation():
    customer_one = Customer(random.randint(1,100), sample.first_name(), sample.last_name(), sample.date(), sample.address(), sample.address(), sample.phone_number(), sample.email())
    my_order = Order(customer_one)
    product_one = Product("SKU344", "Sprinkle Water 1lt", 1, Product.Categories.BEVERAGES) 
    product_two = Product("SKU122", "Paper Towels 200U", 4, Product.Categories.PAPER_GOOD)
    request_one = Request(1, product_one)
    request_two = Request(1, product_two)
    my_order.add_request(request_one)
    my_order.add_request(request_two)
    subtotal = my_order.calculate_subtotal()
    assert subtotal == 5, "Subtotal calculated does not match the expected one"


def test_total_calculation():
    customer_one = Customer(random.randint(1,100), sample.first_name(), sample.last_name(), sample.date(), sample.address(), sample.address(), sample.phone_number(), sample.email())
    my_order = Order(customer_one)
    product_one = Product("SKU344", "Sprinkle Water 1lt", 1, Product.Categories.BEVERAGES) 
    product_two = Product("SKU122", "Paper Towels 200U", 4, Product.Categories.PAPER_GOOD)
    request_one = Request(1, product_one)
    request_two = Request(1, product_two)
    my_order.add_request(request_one)
    my_order.add_request(request_two)
    total = round(my_order.calculate_total(),1)
    assert total == 5.6, "Total calculated does not match the expected one"


def test_auto_increment_id():
    class_counter = Order.class_counter
    customer_one = Customer(random.randint(1,100), sample.first_name(), sample.last_name(), sample.date(), sample.address(), sample.address(), sample.phone_number(), sample.email())
    first_order = Order(customer_one)
    second_order = Order(customer_one)
    first_id = first_order.get_id()
    second_id = second_order.get_id()
    assert first_id is class_counter
    assert second_id is class_counter + 1


def test_id_valtype():
    customer_one = Customer(random.randint(1,100), sample.first_name(), sample.last_name(), sample.date(), sample.address(), sample.address(), sample.phone_number(), sample.email())
    check_id_req = Order(customer_one)
    number = check_id_req.get_id()
    assert number >= 1 and isinstance(number, int)


def test_invoice_creation():
    address_sample = "234 Morrison St, Miami, Florida, 33054"
    customer_one = Customer(random.randint(1,100), sample.first_name(), sample.last_name(), sample.date(), address_sample, sample.address(), sample.phone_number(), sample.email())
    my_order = Order(customer_one)
    product_one = Product("SKU344", "Sprinkle Water 1lt", 1, Product.Categories.BEVERAGES) 
    product_two = Product("SKU122", "Paper Towels 200U", 4, Product.Categories.PAPER_GOOD)
    request_one = Request(1.0, product_one)
    request_two = Request(1.0, product_two)
    my_order.add_request(request_one)
    my_order.add_request(request_two)
    isInvoiceCreated = my_order.print_invoice()
    Utils.remove(os.path.realpath(os.curdir))
    assert isInvoiceCreated == True, "Invoice has not been generated"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])