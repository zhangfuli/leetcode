def sqr(x):
    y = x
    while abs(y * y - x) > 1e-6:
        y = (y + x / y) / 2
    return y


print(sqr(999))
