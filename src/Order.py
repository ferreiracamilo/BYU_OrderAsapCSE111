from datetime import datetime

class Order:
    CATEGORIES = ["Waiting", "In Process", "Delivered"]

    class_counter = 0

    def __init__(self, customer, discount, tax_rate):
        self.id = Order.class_counter,
        self.date = datetime.now(),
        self.requests = [],
        self.status = "Waiting",
        self.customer = customer,
        self.discount = discount,
        self.tax_rate = tax_rate
        Order.class_counter += 1

    def get_id(self):
        """Retrieve id

        Returns:
            Int: id
        """
        return self.id

    def get_customer(self):
        """Retrieve customer

        Returns:
            Customer: customer
        """
        return self.customer

    def get_date(self):
        """Retrieve date

        Returns:
            Date: date
        """
        return self.date

    def get_discount(self):
        """Retrieve discount

        Returns:
            Int: discount
        """
        return self.discount

    def get_requests(self):
        """Retrieve requests

        Returns:
            List{Request}: requests
        """
        return self.requests

    def get_tax_rate(self):
        """Retrieve tax_rate

        Returns:
            Float: tax_rate
        """
        return self.tax_rate

    def get_status(self):
        """Retrieve status

        Returns:
            String: status
        """
        return self.status

    def set_status(self, status):
        """Update status

        Args:
            status (String): status
        """
        self.status = status

    def set_discount(self, discount):
        """Update discount

        Args:
            discount (Float): discount
        """
        self.status = discount

    def set_tax_rate(self, tax_rate):
        """Update tax_rate

        Args:
            tax_rate (Float): tax_rate
        """
        self.status = tax_rate

    def set_requests(self, requests_list):
        """Update tax_rate

        Args:
            tax_rate (List[requests]): requests
        """
        self.requests = requests_list