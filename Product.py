import re
import ProductDB
from tkinter import messagebox


# Class for Product Verification
class Product:
    def __init__(self, product_id, product_name, product_cost, backroom_amount, sales_floor_amount):
        self.product_id = product_id
        self.product_name = product_name
        self.product_cost = product_cost
        self.backroom_amount = backroom_amount
        self.sales_floor_amount = sales_floor_amount

    def checkProductID(self):
        if re.match(r"^\d+$", self.product_id):
            return True
        else:
            return False

    def Check_product_name(self):
        if re.match(r"^[a-zA-Z]+$", self.product_name):
            return True
        else:
            return False

    def checkProductID(self):
        if re.match(r"^\d+.\d\d$", self.product_id):
            return True
        else:
            return False

    def Check_Backroom_Amount(self):
        if re.match(r"^\d+$", self.backroom_amount):
            return True
        else:
            return False

    def Check_SalesFloor_Amount(self):
        if re.match(r"^\d+$", self.sales_floor_amount):
            return True
        else:
            return False

    def submit(self):
        ProductDB.CreateProductDB()
        ProductDB.AddProduct(self.product_id, self.product_name, self.product_cost,
                             self.backroom_amount, self.sales_floor_amount)
        messagebox.showinfo("Information", "Information has been added")