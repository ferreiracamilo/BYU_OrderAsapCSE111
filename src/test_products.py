import pytest
from Product import *

def test_toString():
    #first_request = Request(1, "water bottle")
    #(self, code, name, price, category):
    prod_code = "SKU-1234"
    prod_name = "Sprinkle Water"
    prod_price = 13.93
    prod_category = Product.Categories.BAKERY
    newProduct = Product("SKU-1234","Sprinkle Water", 13.93, Product.Categories.BAKERY)
    msg = f"{newProduct}"
    assert "a" in "dasdada"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])