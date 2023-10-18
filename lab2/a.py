import math
x = 3

while 3 <= x <= 6:
    if 3 <= x < 4:
        result_of_operation = math.log((x + math.sin(x)), 3)
        print(f"Operation: log3 ({x} + sin({x})) \nResult of operation: {result_of_operation}\n")

    elif 4 <= x < 5:
        result_of_operation = math.log10((math.e ** x) + 4)
        print(f"Operation: lg (e ^ {x} + 4) \nResult of operation: {result_of_operation}\n")

    elif 5 <= x <= 6:
        result_of_operation = math.log(math.log10(x))
        print(f"Operation: ln (lg ({x})) \nResult of operation: {result_of_operation}\n")

    x = round(x + 0.2, 3)
