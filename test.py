import bisect

a = [0, 1, 2, 3, 4, 5, 5, 5, 7]
b = 6
print(bisect.bisect_left(a, b))
