from datetime import datetime

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
        """Update tax_rate

        Args:
            tax_rate (List[requests]): requests
        """
        self._requests = requests_list