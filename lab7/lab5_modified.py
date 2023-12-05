"""
Smartphone and Store module
"""

import logging
from typing import Literal

logging.basicConfig(filename="exceptions.log", level=logging.ERROR)
console_handler = logging.StreamHandler()
fileHandler = logging.FileHandler("exceptions.log")
logger = logging.getLogger(__name__)

class Smartphone:
    """
    Object that describe a smartphone
    """

    def __init__(self, model, **kwargs):
        self.price = kwargs.get("price")
        self.model = model
        self.phone_numbers = kwargs.get("phone_numbers")
        self.memory = kwargs.get("memory")
        self.battery_capacity = kwargs.get("battery_capacity")

    def __del__(self):
        print("Smartphone object destroyed")

    def __repr__(self):
        return "Smartphone object"

    def get_info(self):
        """
        Method that return all values of Smartphone object
        """
        return {
            "price": f"{str(self.price)}$",
            "model": self.model,
            "phone numbers": ", ".join(self.phone_numbers),
            "memory": str(self.memory) + "Gb",
            "battery capacity": str(self.battery_capacity) + "mAh",
        }


class PhoneErrorException(Exception):
    """
    Custom exception for handling phone error
    """
    def __init__(self, message):
        super().__init__(message)


def logged(exception: Exception, mode: Literal["file", "console"]):
    """
    Decorator that logging passed exception by given mode
    mode: str["file", "console"] 
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                function(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logger.removeHandler(fileHandler)
                    logger.addHandler(console_handler)
                elif mode == "file":
                    logger.removeHandler(console_handler)
                    logger.addHandler(fileHandler)
                logger.exception("Exception caught: %s", e)
        return wrapper
    return decorator



class PhoneStore:
    """
    Object that defines Phone store instances
    """

    @logged(PhoneErrorException, "file")
    def __init__(self, phones):
        self.phones = []
        for phone in phones:
            if isinstance(phone, Smartphone):
                self.phones.append(phone)
            else:
                raise PhoneErrorException("One of given parameters in phones is not type of Smartphone")

    @logged(PhoneErrorException, "console")
    def add_phone(self, phone):
        """
        Method that add new Smartphone to PhoneStore
        """
        if isinstance(phone, Smartphone):
            self.phones.append(phone)
        else:
            raise PhoneErrorException("Given parameter is not type of Smartphone")

    def choose_best_phone(self):
        """
        Method that return phone that cost the most
        """
        best_phone = self.phones[0]
        for phone in self.phones:
            if phone.price > best_phone.price:
                best_phone = phone
        return best_phone

    def sort_by_price(self):
        """
        Method that return list of phones sorted by price (from 0 to +Infinity)
        """
        n = len(self.phones)
        sorted_phones = self.phones

        for i in range(n):
            for j in range(0, n - 1 - i):
                if sorted_phones[j].price > sorted_phones[j + 1].price:
                    sorted_phones[j], sorted_phones[j + 1] = sorted_phones[j + 1], sorted_phones[j]
        return sorted_phones


if __name__ == "__main__":
    store = PhoneStore([
        Smartphone(
            "Iphone 12 pro",
            price=1000,
            phone_numbers=["+380123456789", "+380555555652"],
            memory=64,
            battery_capacity=2500
        ),
        "",
        Smartphone(
            "Poco",
            price=500,
            phone_numbers=["+380985647569", "+380686513279"],
            memory=32,
            battery_capacity=2000
        ),
    ])

    for el in store.sort_by_price():
        print(el.price)

    print(store.choose_best_phone().model)
    
    store.add_phone("STR TO TEST AN EXCEPTION LOGGER")
