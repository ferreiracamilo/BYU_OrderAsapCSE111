from datetime import datetime
from Request import *
from Product import *
from Customer import *


class Order:
    CATEGORIES = ["Waiting", "In Process", "Delivered"]


    #INDEXES start at ZERO but this will work as order id as well, therefore enforcing start at 1
    class_counter = 1


    def __init__(self, customer, discount=0, tax_rate=12):
        #Not every order will be eligible or receive a discount, therefore is enforced ZERO
        #Tax Rate will assign a default tax rate in case there's nothing defined
        self._id = Order.class_counter
        self._date = datetime.now()
        self._requests = []
        self._status = "Waiting"
        self._customer = customer
        self._discount = discount
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


    def get_discount(self):
        """Retrieve discount

        Returns:
            Int: discount
        """
        return self._discount


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


    def set_discount(self, discount):
        """Update discount

        Args:
            discount (Float): discount
        """
        self._status = discount


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
            float: subtotal before taxes and discounts
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
            float: total after taxes and discounts
        """
        total = self.calculate_subtotal()
        if total > 0:
            total = total * (1+self._discount/100)
            total = total * (1+self._tax_rate/100)
        return total