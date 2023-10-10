def get_letters_and_numbers():  # Returns tuple of allowed symbols
    symbols = []
    for i in range(65, 91):
        symbols.append(chr(i))
    for i in range(97, 123):
        symbols.append(chr(i))
    for i in range(0, 10):
        symbols.append(str(i))
    return tuple(symbols)


def count_letters_and_numbers(string):
    allowed_symbols = get_letters_and_numbers()
    count = 0
    for char in string:
        count += 1 if (char in allowed_symbols) else 0

    return count


print(count_letters_and_numbers("hel2!lo"))  # Expected output: 6
print(count_letters_and_numbers("wicked .. !"))  # Expected output: 6
print(count_letters_and_numbers("!?..A"))  # Expected output: 1
