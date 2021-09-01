# Exponent function program

def raise_power(x, y):
    res = 1
    for i in range(y):
        res = res * x
    return res


print(raise_power(4, 2))
