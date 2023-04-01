from datetime import datetime
from Request import *
from Product import *
from Customer import *
import os
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice

class Order:
    CATEGORIES = ["Waiting", "In Process", "Delivered"]


    #INDEXES start at ZERO but this will work as order id as well, therefore enforcing start at 1
    class_counter = 1


    def __init__(self, customer, tax_rate=12):
        #Tax Rate will assign a default tax rate in case there's nothing defined
        self._id = Order.class_counter
        self._date = datetime.now()
        self._requests = []
        self._status = "Waiting"
        self._customer = customer
        self._tax_rate = tax_rate
        Order.class_counter += 1


    def get_id(self):
        """Retrieve id

        Returns:
            Int: id
        """
        return self._id


    def get_customer(self):
        """Retrieve customer

        Returns:
            Customer: customer
        """
        return self._customer


    def get_date(self):
        """Retrieve date

        Returns:
            Date: date
        """
        return self._date

    def get_requests(self):
        """Retrieve requests

        Returns:
            List{Request}: requests
        """
        return self._requests


    def get_tax_rate(self):
        """Retrieve tax_rate

        Returns:
            Float: tax_rate
        """
        return self._tax_rate


    def get_status(self):
        """Retrieve status

        Returns:
            String: status
        """
        return self._status


    def set_status(self, status):
        """Update status

        Args:
            status (String): status
        """
        self._status = status


    def set_tax_rate(self, tax_rate):
        """Update tax_rate

        Args:
            tax_rate (Float): tax_rate
        """
        self._status = tax_rate


    def set_requests(self, requests_list):
        """Update _requests

        Args:
            requests_list (List[requests]): requests
        """
        self._requests = requests_list
    
    def add_request(self, request):
        """Update tax_rate

        Args:
            request (Request): request
        """
        self._requests.append(request)


    def calculate_subtotal(self):
        """Iterate the request list to calculate the summatory of product prices

        Returns:
            float: subtotal before taxes
        """
        subtotal = 0
        if len(self._requests) > 0:
            for request in self._requests:
                req_prod = request.get_product()
                req_qty = request.get_quantity()
                subtotal += req_prod.get_price() * req_qty
        return subtotal


    def calculate_total(self):
        """Iterate the request list to calculate the summatory of product prices

        Returns:
            float: total after taxes
        """
        total = self.calculate_subtotal()
        if total > 0:
            total = total * (1+self._tax_rate/100)
        return total


    def print_invoice(self):
        # customer_one = Customer(random.randint(1,100), sample.first_name(), sample.last_name(), sample.date(), sample.address(), sample.address(), sample.phone_number(), sample.email())

        # my_order = Order(customer_one)

        # product_one = Product("SKU344", "Sprinkle Water 1lt", 1, Product.Categories.BEVERAGES) 

        # product_two = Product("SKU122", "Paper Towels 200U", 4, Product.Categories.PAPER_GOOD)

        # request_one = Request(1, product_one)

        # request_two = Request(1, product_two)
        # my_order.add_request(request_one)
        # my_order.add_request(request_two)

        os.environ["INVOICE_LANG"] = "en"
        client = Client('Finxter')
        # one_address.replace(", ", ",").split(",")
        provider = Provider(summary='Door2Groceries Inc.', address='234 Jimlik St', city='Opa Locka, Florida', bank_account='123-4555-12345', bank_code='221', phone='202-555-0120', email='info@door2groceries.com')
        creator = Creator('Shubham Sayon')
        invoice = Invoice(client, provider, creator)
        invoice.use_tax = True
        

        for i in self._requests:

            product = i.get_product()
            quantity = i.get_quantity()
            invoice.add_item(Item(unit=quantity, price=product.get_price(), description=product.get_name(), tax=self._tax_rate))

        invoice.currency = "$"
        invoice.number = self._id
        document = SimpleInvoice(invoice)
        document.gen(f"invoice-order-{self.get_id}.pdf", generate_qr_code=True)
        Utils.walk(os.path.realpath(os.curdir))