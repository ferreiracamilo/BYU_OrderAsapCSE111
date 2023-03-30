class Product:
    CATEGORIES = ["Beverages", "Bread/Bakery", "Canned/Jarred Goods", "Dairy", "Dry/Baking Goods", "Frozen Foods",
                  "Meat", "Produce", "Cleaners", "Paper Goods", "Personal Care", "Other"]

    def __init__(self, code, name, price, category):
        self.code = code
        self.name = name
        self.price = price
        self.category = category

    def get_code(self):
        """Retrieve code

        Returns:
            String: code
        """
        return self.code

    def get_name(self):
        """Retrieve name

        Returns:
            String: name
        """
        return self.name

    def get_price(self):
        """Retrieve price

        Returns:
            Float: price
        """
        return self.price

    def get_category(self):
        """Retrieve category

        Returns:
            String: category
        """
        return self.category

    def set_name(self, name):
        """Update name

        Args:
            name (String): name
        """
        self.name = name

    def set_price(self, price):
        """Update price

        Args:
            price (String): price
        """
        self.price = price

    def set_category(self, category):
        """Update category

        Args:
            category (String): category
        """
        self.category = category

    def __str__(self) -> str:
        # return f"{self.name}({self.age})"
        return f"Product code: {self.code}, Name: {self.name}, Price: {self.price}, Category: {self.category}"