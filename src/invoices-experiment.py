import os
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
import Utils
import datetime

mydirx = f"{os.getcwd()}\\Resources\logo-color.png"
os.environ["INVOICE_LANG"] = "en"
one_address = "1235 Eduardo Acevedo, Miami, Florida, 35034"
parts = one_address.replace(", ", ",").split(",")
client = Client(summary='Finxter', email= 'camiloferreira2009@hotmail.com', address='ed acevedo 1565')
provider = Provider(summary='Door2Groceries Inc.', logo_filename=mydirx, address='234 Jimlik St', city='Opa Locka, Florida', bank_account='123-4555-12345', bank_code='221', phone='202-555-0120', email='info@door2groceries.com', vat_id='94253611771')
creator = Creator('Accountant Area')
invoice = Invoice(client, provider, creator)
number_of_items = int(input("Enter the number of Items: "))
for i in range(number_of_items):
    units = int(input(f"Enter the number of units for item no.{i+1}: "))
    price_per_unit = float(input(f"Enter the price per unit of item no.{i+1}: "))
    description = input("Enter the name of item/product: ")
    invoice.add_item(Item(count=units, price=price_per_unit, description=description))
invoice.currency = "$"
invoice.number = "10393069"
invoice.title = "Thanks for your purchase"
invoice.date = datetime.datetime(2020, 5, 17)
document = SimpleInvoice(invoice)
fileNamex = 'invoic3212e.pdf'
document.gen(fileNamex, generate_qr_code=True)