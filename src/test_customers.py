import pytest
import random
from Customer import *
from faker import Faker

sample = Faker()

def test_constructor_email_validation():
    with pytest.raises(Exception) as e:
        customer_two = Customer(random.randint(1,100), sample.first_name(), sample.last_name(), sample.date(), sample.address(), sample.address(), sample.phone_number(), "dasda")
    assert "Email provided is not valid" in str(e.value), "Exception does not match with the expected one"
    assert e.type == Exception, "Exception raised does not match Exception type expected"

def test_setter_email_validation():
    customer_one = Customer(random.randint(1,100), sample.first_name(), sample.last_name(), sample.date(), sample.address(), sample.address(), sample.phone_number(), sample.email())
    email1 = customer_one.get_email()
    
    unauthorized1 = "@mail"
    customer_one.set_email(unauthorized1)
    email2 = customer_one.get_email()

    unauthorized2 = "mail@"
    customer_one.set_email(unauthorized2)
    email3 = customer_one.get_email()

    unauthorized3 = "mail@mail"
    customer_one.set_email(unauthorized3)
    email4 = customer_one.get_email()

    unauthorized4 = "@mail.com"
    customer_one.set_email(unauthorized4)
    email5 = customer_one.get_email()

    unauthorized5 = "mail#mail.com"
    customer_one.set_email(unauthorized5)
    email6 = customer_one.get_email()

    authorized1 = "mail@mail.com"
    customer_one.set_email(authorized1)
    email7 = customer_one.get_email()
    
    assert email1 == email2, f"Email was updated to an unauthorized value > {unauthorized1}"
    assert email1 == email3, f"Email was updated to an unauthorized value > {unauthorized2}"
    assert email1 == email4, f"Email was updated to an unauthorized value > {unauthorized3}"
    assert email1 == email5, f"Email was updated to an unauthorized value > {unauthorized4}"
    assert email1 == email6, f"Email was updated to an unauthorized value > {unauthorized5}"
    assert email1 != email7, f"Email was not updated to authorized value > {authorized1}"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])