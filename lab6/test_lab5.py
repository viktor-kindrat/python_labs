from src.lab5 import Smartphone, PhoneStore


# Test cases for the Smartphone class
def test_smartphone_creation():
    phone = Smartphone(
        "Iphone 12 pro",
        price=1000,
        phone_numbers=["+380123456789", "+380555555652"],
        memory=64,
        battery_capacity=2500)
    assert phone.price == 1000
    assert phone.model == "Iphone 12 pro"
    assert phone.phone_numbers == ["+380123456789", "+380555555652"]
    assert phone.memory == 64
    assert phone.battery_capacity == 2500


def test_smartphone_repr():
    phone = Smartphone(
        "Iphone 12 pro",
        price=1000,
        phone_numbers=["+380123456789", "+380555555652"],
        memory=64,
        battery_capacity=2500)
    assert repr(phone) == "Smartphone object"


def test_smartphone_get_info():
    phone = Smartphone(
        "Iphone 12 pro",
        price=1000,
        phone_numbers=["+380123456789", "+380555555652"],
        memory=64,
        battery_capacity=2500)
    info = phone.get_info()
    assert info["price"] == "1000$"
    assert info["model"] == "Iphone 12 pro"
    assert info["phone numbers"] == ", ".join(["+380123456789", "+380555555652"])
    assert info["memory"] == "64Gb"
    assert info["battery capacity"] == "2500mAh"


# Test cases for the PhoneStore class
def test_phonestore_creation():
    phones = [
        Smartphone(
            "Iphone 12 pro",
            price=1000,
            phone_numbers=["+380123456789", "+380555555652"],
            memory=64,
            battery_capacity=2500),
        Smartphone(
            "Iphone 12 pro",
            price=500,
            phone_numbers=["+380123456789", "+380555555652"],
            memory=64,
            battery_capacity=2000),
    ]
    store = PhoneStore(phones)
    assert len(store.phones) == 2


def test_phonestore_add_phone():
    store = PhoneStore([])
    phone = Smartphone(
        "Iphone 12 pro",
        price=1000,
        phone_numbers=["+380123456789", "+380555555652"],
        memory=64,
        battery_capacity=2500)
    store.add_phone(phone)
    assert len(store.phones) == 1


def test_phonestore_choose_best_phone():
    phones = [
        Smartphone(
            "Iphone 12 pro",
            price=1000,
            phone_numbers=["+380123456789", "+380555555652"],
            memory=64,
            battery_capacity=2500),
        Smartphone(
            "Iphone 12 pro",
            price=500,
            phone_numbers=["+380123456789", "+380555555652"],
            memory=64,
            battery_capacity=2000),
    ]
    store = PhoneStore(phones)
    best_phone = store.choose_best_phone()
    assert best_phone.price == 1000


def test_phonestore_sort_by_price():
    phones = [
        Smartphone(
            "Iphone 12 pro",
            price=1000,
            phone_numbers=["+380123456789", "+380555555652"],
            memory=64,
            battery_capacity=2500),
        Smartphone(
            "Iphone 12 pro",
            price=500,
            phone_numbers=["+380123456789", "+380555555652"],
            memory=64,
            battery_capacity=2000),
    ]
    store = PhoneStore(phones)
    sorted_phones = store.sort_by_price()
    assert sorted_phones[0].price == 500
    assert sorted_phones[1].price == 1000
