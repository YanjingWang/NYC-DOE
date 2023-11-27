from mimetypes import init


class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phonenumber):
        print(f"{self.brand} is calling {phonenumber}")

    # how to make OOP.py as main file, override this methods
    def __str__(self) -> str:   # means it returns string datatypes
        return f"Brand {self.brand} \nPrice = {self.price}"


# need to change script path to OOP.py
iphone = Phone("Iphone 13 pro", 3000)  # create the real object
samsung = Phone("Samsung S20", 1400)
print(iphone.brand)  # properties
print(samsung.price)
# iphone.call("3475743979") #behavior


# how to print objects
# Pycharm Ctrl + enter --override methods or command O
print(iphone)
print(samsung)


