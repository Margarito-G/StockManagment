# Margarito Galicia
# Final Project
# Stock Management System
# 5/02/21

from ProductScreen import *

MainScreen = tk.Tk()
MainScreen.title("Stock Management System")
MainScreen.geometry("400x400")
MainScreen.resizable(width=False, height=False)

# Open up ProductScreen
newProductButton = tk.Button(MainScreen, text="Add/Edit Product Info", width=20, command=ProductScreenLauncher)
newProductButton.place(x=120, y=350)

MainScreen.mainloop()