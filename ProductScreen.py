# Margarito Galicia
# Final Project
# Stock Management

import tkinter as tk
from Product import *

def ProductScreenLauncher():
    # Initial Product Screen components
    ProductScreen = tk.Tk()
    ProductScreen.title("Product")
    ProductScreen.geometry("350x400")
    ProductScreen.resizable(width=False, height=False)

    # ProductID Label&Entries
    ProductIDLabel = tk.Label(ProductScreen, text="Product_ID: ")
    ProductIDLabel.place(x=42, y=50)
    ProductIDEntry = tk.Entry(ProductScreen)
    ProductIDEntry.place(x=120, y=50)

    # Product Code Label&Entries
    productNameLabel = tk.Label(ProductScreen, text="Product Name: ")
    productNameLabel.place(x=23, y=80)
    productNameEntry = tk.Entry(ProductScreen)
    productNameEntry.place(x=120, y=80)

    # Date Purchased Label&Entries
    productCostLabel = tk.Label(ProductScreen, text="Product Cost: ")
    productCostLabel.place(x=32, y=110)
    productCostEntry = tk.Entry(ProductScreen)
    productCostEntry.place(x=120, y=110)

    # Price Paid Label&Entries
    backroomAmountLabel = tk.Label(ProductScreen, text="Backroom Amount: ")
    backroomAmountLabel.place(x=0, y=140)
    backroomAmountEntry = tk.Entry(ProductScreen)
    backroomAmountEntry.place(x=120, y=140)

    # Price Paid Label&Entries
    salesFloorAmountLabel = tk.Label(ProductScreen, text="Sales Floor Amount: ")
    salesFloorAmountLabel.place(x=0, y=170)
    salesFloorAmountEntry = tk.Entry(ProductScreen)
    salesFloorAmountEntry.place(x=120, y=170)

    def Submit():
        newProduct = Product(ProductIDEntry.get(), productNameEntry.get(),
                             productCostEntry.get(), backroomAmountEntry.get(), salesFloorAmountEntry.get())
        newProduct.submit()

    SubmitButton = tk.Button(ProductScreen, text="Submit", command=Submit)
    SubmitButton.place(x=150, y=200)