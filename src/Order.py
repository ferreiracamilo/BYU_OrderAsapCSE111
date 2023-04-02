from enum import Enum
from datetime import datetime
from Request import *
from Product import *
from Customer import *
import os
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice

class Order:

    class Status(str, Enum):
        WAITING = "Waiting"
        IN_PROCESS = "In Process"
        DELIVERED = "Delivered"

        def __str__(self):
            return str(self.value)


    #INDEXES start at ZERO but this will work as order id as well, therefore enforcing start at 1
    class_counter = 1


    def __init__(self, customer, tax_rate=12):
        #Tax Rate will assign a default tax rate in case there"s nothing defined
        self._id = Order.class_counter
        self._date = datetime.now()
        self._requests = []
        self._status = Order.Status.WAITING
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
        """Update _requests

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
        isCreated = False
        os.environ["INVOICE_LANG"] = "en"
        
        #### Collect customer information and set as client for invoice ####
        cx_fullname = self._customer.get_fullname()
        cx_address = self._customer.get_address_formatted()[0]
        cx_city = f"{self._customer.get_address_formatted()[1]}, {self._customer.get_address_formatted()[2]}" #Combine city and state
        cx_email = self._customer.get_email()
        cx_phone = self._customer.get_phone_number()
        client = Client(summary=cx_fullname, address=cx_address, city=cx_city, email=cx_email, phone=cx_phone)

        #### Collect provider information and set as provider for invoice ####
        prov_name = "Door2Groceries Inc."
        prov_address = "234 Jimlik St"
        prov_city = "Opa Locka, Florida"
        prov_bank_acc = "123-4555-12345"
        prov_bank_cod = "221"
        prov_phone = "202-555-0120"
        prov_email = "info@door2groceries.com"
        prov_logo = f"{os.getcwd()}\\Resources\logo-color.png" #Combine current working directoy and subdir along file name
        provider = Provider(summary=prov_name, address=prov_address, city=prov_city, bank_account=prov_bank_acc, bank_code=prov_bank_cod, phone=prov_phone, email=prov_email, logo_filename=prov_logo)
        
        creator = Creator("Accountant Area")
        
        invoice = Invoice(client, provider, creator)
        invoice.use_tax = True #Before proceeding to list items enable taxes

        for i in self._requests:
            product_name = i.get_product().get_name()
            product_price = i.get_product().get_price()
            quantity = i.get_quantity()
            one_item = Item(count=quantity, price=product_price, description=product_name, tax=self._tax_rate)
            invoice.add_item(one_item)

        invoice.currency = "$"
        invoice.number = self._id #load order id to invoice id
        invoice.title = "Thanks for your purchase"
        

        #invoice.date = self.get_date() #load creation date to invoice date

        document = SimpleInvoice(invoice)
        dateTimeStr = self._date.strftime("%m_%d_%Y-%H_%M_%S")
        invoice_name = f"invoice-{dateTimeStr}-{self._id}.pdf"
        document.gen(invoice_name, generate_qr_code=True)
        #PDF will be generated by default into parent directory, then it is needed to move it over Invoices subfolder
        isCreated = True
        return isCreated