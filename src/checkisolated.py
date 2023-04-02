from Order import *
from Customer import *
from Product import *
from Request import *
from faker import Faker
import random

sample = Faker()

def main():
    address_sample = "234 Morrison St, Miami, Florida, 33054"
    customer_one = Customer(random.randint(1,100), sample.first_name(), sample.last_name(), sample.date(), address_sample, sample.address(), sample.phone_number(), sample.email())
    product_one = Product("SKU344", "Sprinkle Water 1lt", 1, Product.Categories.BEVERAGES) 
    product_two = Product("SKU122", "Paper Towels 200U", 4, Product.Categories.PAPER_GOOD)
    request_one = Request(1.0, product_one)
    request_two = Request(1.0, product_two)
    
    my_order1 = Order(customer_one)
    my_order1.add_request(request_one)
    my_order1.add_request(request_two)
    my_order1.print_invoice()

    my_order2 = Order(customer_one)
    my_order2.add_request(request_one)
    my_order2.add_request(request_two)
    my_order2.print_invoice()

    my_order3 = Order(customer_one)
    my_order3.add_request(request_one)
    my_order3.add_request(request_two)
    my_order3.print_invoice()

    my_order4 = Order(customer_one)
    my_order4.add_request(request_one)
    my_order4.add_request(request_two)
    my_order4.print_invoice()
    Utils.walk(os.path.realpath(os.curdir))

main()