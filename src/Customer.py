class Customer:
    def __init__(self, id, name, lastname, birthdate, billing_address, shipping_address):
        self.id = id,
        self.name = name,
        self.lastname = lastname,
        self.birthdate = birthdate,
        self.billing_address = billing_address,
        self.shipping_address = shipping_address

    def get_id(self):
        """Retrieve a id from a specific customer

        Returns:
            String: Customer id
        """
        return self.id

    def get_name(self):
        """Retrieve name

        Returns:
            String: name
        """
        return self.name

    def get_lastname(self):
        """Retrieve lastname

        Returns:
            String: lastname
        """
        return self.lastname

    def get_birthdate(self):
        """Retrieve birthdate

        Returns:
            String: birthdate
        """
        return self.birthdate

    def get_shipping_address(self):
        """Retrieve shipping address

        Returns:
            String: shipping address
        """
        return self.shipping_address

    def get_billing_address(self):
        """Retrieve billing address

        Returns:
            String: billing address
        """
        return self.billing_address

    def set_name(self, name):
        """Update name

        Args:
            name (String): name
        """
        self.name = name

    def set_lastname(self, lastname):
        """Update lastname

        Args:
            name (String): lastname
        """
        self.lastname = lastname

    def set_birthdate(self, birthdate):
        """Update birthdate

        Args:
            name (Date): birthdate
        """
        self.birthdate = birthdate

    def set_billing_address(self, billing_address):
        """Update billing_address

        Args:
            name (String): billing_address
        """
        self.billing_address = billing_address

    def set_shipping_address(self, shipping_address):
        """Update shipping_address

        Args:
            name (String): shipping_address
        """
        self.shipping_address = shipping_address