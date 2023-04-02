import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import re
import Utils

class App:
    def __init__(self, root):

        # call function when shipping entry is clicked
        def clickShippingEntry(*args):
            txt_cx_shipping_address.delete(0, 'end')


        # call function when billing entry is clicked
        def clickBillingEntry(*args):
            txt_cx_billing_address.delete(0, 'end')


        # call function when shipping entry is clicked
        def clickBirthdateEntry(*args):
            txt_cx_birthdate.delete(0, 'end')
        

        def show_message(error=""):
            messagebox.showerror(message=error, title="Error warning")


        def validate_non_empty():
            len_name = len(txt_cx_name.get())
            len_lname = len(txt_cx_lastname.get())
            len_billing = len(txt_cx_billing_address.get())
            len_email = len(txt_cx_email.get())
            len_bdate = len(txt_cx_birthdate.get())
            len_shipping = len(txt_cx_shipping_address.get())
            len_water = len(txt_prods_water.get())
            len_flour = len(txt_prods_flour.get())
            len_sugar = len(txt_prods_sugar.get())
            len_towel = len(txt_prods_towel.get())
            len_toilet = len(txt_prods_toilet.get())
            len_garbage = len(txt_prods_garbage.get())
            if len_name < 1 or len_lname < 1 or len_billing < 1 or len_email < 1 or len_bdate < 1 or len_shipping < 1 or len_water < 1 or len_flour < 1 or len_sugar < 1 or len_towel < 1 or len_toilet < 1 or len_garbage < 1:
                show_message("All fields are required, review them to assure there's no empty field")
        
        def validate_addresses():
            txt_cx_billing_address
            txt_cx_shipping_address
            billing_comma = len(re.findall(",", txt_cx_billing_address.get()))
            shipping_comma = len(re.findall(",", txt_cx_shipping_address.get()))
            if billing_comma < 3 or shipping_comma < 3:
                show_message("Adress must follow template > 'St Address,City,State,ZipCode'")

        def validate_birthdate():
            isBdate = Utils.is_date(txt_cx_birthdate.get(), fuzzy=False)
            if isBdate == False:
                show_message("Birthdate must follow template 'MM/DD/YYYY'")

        def validate_email():
            

        def btn_generate_invoice_command():
            validate_non_empty()
            validate_addresses()
            validate_birthdate()
            print(txt_prods_flour.get())

        #setting title
        root.title("Invoice Generator")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        lbl_cx_name=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_cx_name["font"] = ft
        lbl_cx_name["fg"] = "#333333"
        lbl_cx_name["justify"] = "center"
        lbl_cx_name["text"] = "Customer Name:"
        lbl_cx_name.place(x=28,y=40,width=100,height=25)

        txt_cx_name=tk.Entry(root)
        txt_cx_name["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_cx_name["font"] = ft
        txt_cx_name["fg"] = "#333333"
        txt_cx_name["justify"] = "center"
        txt_cx_name["text"] = "name input"
        txt_cx_name.place(x=129,y=40,width=186,height=30)
        txt_cx_name["show"] = "name input"

        lbl_cx_lastname=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_cx_lastname["font"] = ft
        lbl_cx_lastname["fg"] = "#333333"
        lbl_cx_lastname["justify"] = "center"
        lbl_cx_lastname["text"] = "Customer Last Name:"
        lbl_cx_lastname.place(x=3,y=80,width=125,height=25)

        txt_cx_lastname=tk.Entry(root)
        txt_cx_lastname["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_cx_lastname["font"] = ft
        txt_cx_lastname["fg"] = "#333333"
        txt_cx_lastname["justify"] = "center"
        txt_cx_lastname["text"] = "lastname input"
        txt_cx_lastname.place(x=129,y=80,width=186,height=30)

        lbl_cx_billing_address=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_cx_billing_address["font"] = ft
        lbl_cx_billing_address["fg"] = "#333333"
        lbl_cx_billing_address["justify"] = "center"
        lbl_cx_billing_address["text"] = "Billing Address:"
        lbl_cx_billing_address.place(x=38,y=120,width=90,height=25)

        txt_cx_billing_address=tk.Entry(root)
        txt_cx_billing_address["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_cx_billing_address["font"] = ft
        txt_cx_billing_address["fg"] = "#333333"
        txt_cx_billing_address["justify"] = "center"
        txt_cx_billing_address["text"] = "234 Ron St, Opa Locka, Billing"
        txt_cx_billing_address.insert(0,"St Address, City, State, Zip Code")
        txt_cx_billing_address.place(x=129,y=120,width=186,height=30)
        # Use bind method
        txt_cx_billing_address.bind("<Button-1>", clickBillingEntry)

        lbl_cx_phone=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_cx_phone["font"] = ft
        lbl_cx_phone["fg"] = "#333333"
        lbl_cx_phone["justify"] = "center"
        lbl_cx_phone["text"] = "Phone number:"
        lbl_cx_phone.place(x=318,y=80,width=92,height=25)

        txt_cx_phone=tk.Entry(root)
        txt_cx_phone["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_cx_phone["font"] = ft
        txt_cx_phone["fg"] = "#333333"
        txt_cx_phone["justify"] = "center"
        txt_cx_phone["text"] = "phone input"
        txt_cx_phone.place(x=410,y=80,width=186,height=30)

        lbl_cx_email=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_cx_email["font"] = ft
        lbl_cx_email["fg"] = "#333333"
        lbl_cx_email["justify"] = "center"
        lbl_cx_email["text"] = "Email"
        lbl_cx_email.place(x=368,y=120,width=40,height=25)

        txt_cx_email=tk.Entry(root)
        txt_cx_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_cx_email["font"] = ft
        txt_cx_email["fg"] = "#333333"
        txt_cx_email["justify"] = "center"
        txt_cx_email["text"] = "email input"
        txt_cx_email.place(x=410,y=120,width=186,height=30)

        lbl_cx_birthdate=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_cx_birthdate["font"] = ft
        lbl_cx_birthdate["fg"] = "#333333"
        lbl_cx_birthdate["justify"] = "center"
        lbl_cx_birthdate["text"] = "Birthdate:"
        lbl_cx_birthdate.place(x=348,y=40,width=60,height=25)

        txt_cx_birthdate=tk.Entry(root)
        txt_cx_birthdate["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_cx_birthdate["font"] = ft
        txt_cx_birthdate["fg"] = "#333333"
        txt_cx_birthdate["justify"] = "center"
        txt_cx_birthdate["text"] = "MM/DD/YYYY"
        txt_cx_birthdate.insert(0,"MM/DD/YYYY")
        txt_cx_birthdate.place(x=410,y=40,width=186,height=30)
        txt_cx_birthdate.bind("<Button-1>", clickBirthdateEntry)

        lbl_cx_shipping_address=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_cx_shipping_address["font"] = ft
        lbl_cx_shipping_address["fg"] = "#333333"
        lbl_cx_shipping_address["justify"] = "center"
        lbl_cx_shipping_address["text"] = "Shipping Address:"
        lbl_cx_shipping_address.place(x=20,y=160,width=105,height=25)

        txt_cx_shipping_address=tk.Entry(root)
        txt_cx_shipping_address["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_cx_shipping_address["font"] = ft
        txt_cx_shipping_address["fg"] = "#333333"
        txt_cx_shipping_address["justify"] = "center"
        txt_cx_shipping_address["text"] = "234 Ron St, Opa Locka, Shipping"
        txt_cx_shipping_address.insert(0,"St Address, City, State, Zip Code")
        txt_cx_shipping_address.place(x=129,y=160,width=186,height=30)
        # Use bind method
        txt_cx_shipping_address.bind("<Button-1>", clickShippingEntry)

        lbl_cx_section=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_cx_section["font"] = ft
        lbl_cx_section["fg"] = "#333333"
        lbl_cx_section["justify"] = "center"
        lbl_cx_section["text"] = "*** CUSTOMER INFORMATION ***"
        lbl_cx_section.place(x=200,y=5,width=200,height=25)

        lbl_prods_section=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_prods_section["font"] = ft
        lbl_prods_section["fg"] = "#333333"
        lbl_prods_section["justify"] = "center"
        lbl_prods_section["text"] = "*** PRODUCT LIST ***"
        lbl_prods_section.place(x=230,y=210,width=140,height=25)

        lbl_prods_water=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_prods_water["font"] = ft
        lbl_prods_water["fg"] = "#333333"
        lbl_prods_water["justify"] = "center"
        lbl_prods_water["text"] = "Sprinkle Water 1lt - 3.99 USD"
        lbl_prods_water.place(x=10,y=260,width=171,height=30)

        lbl_prods_flour=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_prods_flour["font"] = ft
        lbl_prods_flour["fg"] = "#333333"
        lbl_prods_flour["justify"] = "center"
        lbl_prods_flour["text"] = "Flour 1kg - 1.40 USD"
        lbl_prods_flour.place(x=60,y=290,width=127,height=30)

        lbl_prods_sugar=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_prods_sugar["font"] = ft
        lbl_prods_sugar["fg"] = "#333333"
        lbl_prods_sugar["justify"] = "center"
        lbl_prods_sugar["text"] = "Sugar 1kg - 0.40 USD"
        lbl_prods_sugar.place(x=60,y=320,width=121,height=30)

        lbl_prods_towel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_prods_towel["font"] = ft
        lbl_prods_towel["fg"] = "#333333"
        lbl_prods_towel["justify"] = "center"
        lbl_prods_towel["text"] = "Paper Towel 500pcs - 2.20 USD"
        lbl_prods_towel.place(x=335,y=260,width=173,height=36)

        lbl_prods_toilet=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_prods_toilet["font"] = ft
        lbl_prods_toilet["fg"] = "#333333"
        lbl_prods_toilet["justify"] = "center"
        lbl_prods_toilet["text"] = "Toilet Paper 300pcs - 5.80 USD"
        lbl_prods_toilet.place(x=334,y=290,width=174,height=30)

        lbl_prods_garbage=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_prods_garbage["font"] = ft
        lbl_prods_garbage["fg"] = "#333333"
        lbl_prods_garbage["justify"] = "center"
        lbl_prods_garbage["text"] = "Garbage Can 1lt - 3.20 USD"
        lbl_prods_garbage.place(x=330,y=320,width=163,height=30)

        txt_prods_water=tk.Entry(root)
        txt_prods_water["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_prods_water["font"] = ft
        txt_prods_water["fg"] = "#333333"
        txt_prods_water["justify"] = "center"
        txt_prods_water["text"] = "water1"
        txt_prods_water.insert(0,0)
        txt_prods_water.place(x=190,y=260,width=70,height=25)

        txt_prods_flour=tk.Entry(root)
        txt_prods_flour["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_prods_flour["font"] = ft
        txt_prods_flour["fg"] = "#333333"
        txt_prods_flour["justify"] = "center"
        txt_prods_flour["text"] = "flour1"
        txt_prods_flour.insert(0,0)
        txt_prods_flour.place(x=190,y=290,width=70,height=25)

        txt_prods_sugar=tk.Entry(root)
        txt_prods_sugar["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_prods_sugar["font"] = ft
        txt_prods_sugar["fg"] = "#333333"
        txt_prods_sugar["justify"] = "center"
        txt_prods_sugar["text"] = "sugar1"
        txt_prods_sugar.insert(0,0)
        txt_prods_sugar.place(x=190,y=320,width=70,height=25)

        txt_prods_towel=tk.Entry(root)
        txt_prods_towel["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_prods_towel["font"] = ft
        txt_prods_towel["fg"] = "#333333"
        txt_prods_towel["justify"] = "center"
        txt_prods_towel["text"] = "towel1"
        txt_prods_towel.insert(0,0)
        txt_prods_towel.place(x=520,y=260,width=70,height=25)

        txt_prods_toilet=tk.Entry(root)
        txt_prods_toilet["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_prods_toilet["font"] = ft
        txt_prods_toilet["fg"] = "#333333"
        txt_prods_toilet["justify"] = "center"
        txt_prods_toilet["text"] = "toiler1"
        txt_prods_toilet.insert(0,0)
        txt_prods_toilet.place(x=520,y=290,width=70,height=25)

        txt_prods_garbage=tk.Entry(root)
        txt_prods_garbage["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        txt_prods_garbage["font"] = ft
        txt_prods_garbage["fg"] = "#333333"
        txt_prods_garbage["justify"] = "center"
        txt_prods_garbage["text"] = "garb1"
        txt_prods_garbage.insert(0,0)
        txt_prods_garbage.place(x=520,y=320,width=70,height=25)

        lbl_accumulated_section=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_accumulated_section["font"] = ft
        lbl_accumulated_section["fg"] = "#333333"
        lbl_accumulated_section["justify"] = "center"
        lbl_accumulated_section["text"] = "*** ACCUMULATED ***"
        lbl_accumulated_section.place(x=220,y=360,width=152,height=30)

        lbl_accumulated_total=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_accumulated_total["font"] = ft
        lbl_accumulated_total["fg"] = "#333333"
        lbl_accumulated_total["justify"] = "center"
        lbl_accumulated_total["text"] = "Total: 308 USD"
        lbl_accumulated_total.place(x=310,y=390,width=166,height=31)

        lbl_accumulated_subtotal=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lbl_accumulated_subtotal["font"] = ft
        lbl_accumulated_subtotal["fg"] = "#333333"
        lbl_accumulated_subtotal["justify"] = "center"
        lbl_accumulated_subtotal["text"] = "Subtotal: 290 USD"
        lbl_accumulated_subtotal.place(x=110,y=390,width=166,height=31)

        btn_generate_invoice=tk.Button(root)
        btn_generate_invoice["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btn_generate_invoice["font"] = ft
        btn_generate_invoice["fg"] = "#000000"
        btn_generate_invoice["justify"] = "center"
        btn_generate_invoice["text"] = "Generate Invoice"
        btn_generate_invoice.place(x=250,y=450,width=100,height=25)
        btn_generate_invoice["command"] = btn_generate_invoice_command

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
