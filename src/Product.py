from enum import Enum

class Product:

    class Categories(str, Enum):
        BEVERAGES = "Beverages"
        BAKERY = "Bread/Bakery"
        CANNED = "Canned/Jarred Goods"
        DAIRY = "Dairy"
        DRY_GOOD = "Dry/Baking Goods"
        FROZEN_FOOD = "FrozenFoods"
        MEAT = "Meat"
        PRODUCE = "Produce"
        CLEANER = "Cleaners"
        PAPER_GOOD = "Paper Goods"
        PERSONAL_CARE = "Personal Care"
        OTHER = "Other"

        def __str__(self):
            return str(self.value)
    

    def __init__(self, code, name, price, category):
        self._code = code
        self._name = name
        self._price = price
        self._category = category


    def get_code(self):
        """Retrieve code

        Returns:
            String: code
        """
        return self._code


    def get_name(self):
        """Retrieve name

        Returns:
            String: name
        """
        return self._name


    def get_price(self):
        """Retrieve price

        Returns:
            Float: price
        """
        return self._price


    def get_category(self):
        """Retrieve category

        Returns:
            String: category
        """
        return self._category


    def set_name(self, name):
        """Update name

        Args:
            name (String): name
        """
        self._name = name


    def set_price(self, price):
        """Update price

        Args:
            price (String): price
        """
        self._price = price


    def set_category(self, category):
        """Update category

        Args:
            category (String): category
        """
        self._category = category


    def __str__(self) -> str:
        # return f"{self.name}({self.age})"
        return f"Product code: {self._code}, Name: {self._name}, Price: {self._price}, Category: {self._category}"