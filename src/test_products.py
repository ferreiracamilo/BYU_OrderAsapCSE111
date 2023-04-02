import pytest
from Product import *

def test_toString():
    #first_request = Request(1, "water bottle")
    #(self, code, name, price, category):
    prod_code = "SKU-1234"
    prod_name = "Sprinkle Water"
    prod_price = 13.93
    newProduct = Product("SKU-1234","Sprinkle Water", 13.93, Product.Categories.BAKERY)
    productOutput = f"{newProduct}"
    expectedOutput = f"Product code: {prod_code}, Name: {prod_name}, Price: {prod_price}, Category: Bread/Bakery"
    assert productOutput == expectedOutput, "Product string output does not match with expected format"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])