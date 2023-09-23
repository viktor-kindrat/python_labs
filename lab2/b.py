# Range: [0, 1]
# Step: 0.1
# Divergence: 0.0001

k = 0
x = 0

operations_result = 0

while 0 <= x <= 1:
    operations_result += (((- 1) ** k) * (x ** (2 * k + 3))) / ((2 * k + 1) * (2 * k + 3))
    
    x += round(x + 0.1, 3)
    k += 1

print("Summa is:", operations_result)
print("Rounded summa is:", round(operations_result, 4))
print("Divergence:", operations_result - round(operations_result))
