class Smartphone:
    def __init__(self, price, model, phone_numbers, memory, battery_capacity):
        self.price = price
        self.model = model
        self.phone_numbers = phone_numbers
        self.memory = memory
        self.battery_capacity = battery_capacity

    def __del__(self):
        print("Smartphone object destroyed")

    def __repr__(self):
        return "Smartphone object"

    def get_info(self):
        print("Price", self.price, "$")
        print("Model", self.model)
        print("Phone numbers", ", ".join(self.phone_numbers))
        print("Memory", self.memory, "Gb")
        print("Battery capacity", self.battery_capacity, "mAh")


class PhoneStore:
    def __init__(self, phones):
        self.phones = []
        for phone in phones:
            if repr(phone) == "Smartphone object":
                self.phones.append(phone)
            else:
                print("WARNING! One of your phones is not of type Smartphone".center(100))

    def add_phone(self, phone):
        if repr(phone) == "Smartphone object":
            self.phones.push(phone)
        else:
            print("Error! Your object is not of type Smartphone")

    def choose_best_phone(self):
        best_phone = self.phones[0]
        for phone in self.phones:
            if phone.price > best_phone.price:
                best_phone = phone
        return best_phone

    def sort_by_price(self):
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
            1000,
            "Iphone 12 pro",
            ["+380123456789", "+380555555652"],
            64,
            2500
        ),
        "",
        Smartphone(
            500,
            "Poco",
            ["+380985647569", "+380686513279"],
            32,
            2000
        ),
    ])

    for el in store.sort_by_price():
        print(el.price)

    print(store.choose_best_phone().model)
