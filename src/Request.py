class Request:
    class_counter = 0

    def __init__(self, quantity, product):
        self._quantity = quantity
        self._product = product
        self._id = Request.class_counter
        Request.class_counter += 1

    def get_id(self):
        """Retrieve idx

        Returns:
            Int: idx
        """
        return self._id

    def get_product(self):
        """Retrieve product

        Returns:
            Product: product
        """
        return self._product

    def get_quantity(self):
        """Retrieve quantity

        Returns:
            Int: quantity
        """
        return self._quantity

    def set_product(self, product):
        """Update product

        Args:
            product (Product): product
        """
        self._product = product