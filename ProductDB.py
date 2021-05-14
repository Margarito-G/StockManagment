# Margarito Galicia
# Final Project
# 5/4/21

import sqlite3
import re
from tkinter import messagebox
import csv

conn = sqlite3.connect("ProductDatabase.db")
c = conn.cursor()


def CreateProductDB():
    try:
        conn = sqlite3.connect("ProductDatabase.db")
        c = conn.cursor()

        c. execute(""" CREATE TABLE product(Product_ID integer, product_name string, product_cost integer,
                       backroom_amount integer, sales_floor_amount integer)""")
    except:
        print("Database has already been created")


# Function that adds Product information into database
def AddProduct(product_id, product_name, product_cost, backroom_amount, sales_floor_amount):
    c.execute(f"INSERT INTO product VALUES({product_id}, '{product_name}', {product_cost},"
              f" {backroom_amount}, {sales_floor_amount})")
    conn.commit()



