"""
Smartphone and Store module
"""


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


class PhoneStore:
    """
    Object that defines Phone store instances
    """

    def __init__(self, phones):
        self.phones = []
        for phone in phones:
            if isinstance(phone, Smartphone):
                self.phones.append(phone)
            else:
                print("WARNING! One of your phones is not of type Smartphone".center(100))

    def add_phone(self, phone):
        """
        Method that add new Smartphone to PhoneStore
        """
        if isinstance(phone, Smartphone):
            self.phones.append(phone)
        else:
            print("Error! Your object is not of type Smartphone")

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
