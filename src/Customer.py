import re
import Utils

class Customer:
    def __init__(self, id, name, lastname, birthdate, billing_address, shipping_address, phone_number, email):
        self._id = id
        self._name = name
        self._lastname = lastname
        self._birthdate = birthdate
        self._billing_address = billing_address
        self._shipping_address = shipping_address
        self._phone_number = phone_number
        self._email = email

    def get_id(self):
        """Retrieve a id from a specific customer

        Returns:
            String: Customer id
        """
        return self._id

    def get_name(self):
        """Retrieve name

        Returns:
            String: name
        """
        return self._name

    def get_lastname(self):
        """Retrieve lastname

        Returns:
            String: lastname
        """
        return self._lastname

    def get_birthdate(self):
        """Retrieve birthdate

        Returns:
            String: birthdate
        """
        return self._birthdate

    def get_shipping_address(self):
        """Retrieve shipping address

        Returns:
            String: shipping address
        """
        return self._shipping_address

    def get_billing_address(self):
        """Retrieve billing address

        Returns:
            String: billing address
        """
        return self._billing_address
    
    def get_phone_number(self):
        """Retrieve phone number

        Returns:
            String: phone number
        """
        return self._phone_number
    
    def get_email (self):
        """Retrieve email

        Returns:
            String: email
        """
        return self._email

    def set_name(self, name):
        """Update name

        Args:
            name (String): name
        """
        self._name = name

    def set_lastname(self, lastname):
        """Update lastname

        Args:
            name (String): lastname
        """
        self._lastname = lastname

    def set_birthdate(self, birthdate):
        """Update birthdate

        Args:
            name (Date): birthdate
        """
        self._birthdate = birthdate

    def set_billing_address(self, billing_address):
        """Update billing_address

        Args:
            name (String): billing_address
        """
        self._billing_address = billing_address

    def set_shipping_address(self, shipping_address):
        """Update shipping_address

        Args:
            name (String): shipping_address
        """
        self._shipping_address = shipping_address

    def set_phone_number(self, phone_number):
        """Update phone_number

        Args:
            name (String): phone_number
        """
        self._phone_number = phone_number

    def set_email(self, email):
        """Update email

        Args:
            name (String): email
        """
        if Utils.validate_email(email):
            self._email = email