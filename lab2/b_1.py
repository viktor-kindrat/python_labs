import numpy as np

a = 0
b = 1
d = 0.0001

for x in np.arange(a, b, 0.1):
    sum = 0
    k = 0

    while sum < d:
        _temp = (((- 1) ** k) * (x ** (2 * k + 3))) / ((2 * k + 1) * (2 * k + 3))
        if _temp == 0:
            break
        sum += _temp
        k += 1

        print(x, sum, sep=", ")
