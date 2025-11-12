import math


def square(s):
    return math.ceil(s*s)


side = float(input("Сторона квадрата: "))
print(f"Площадь квадрата: {square(side)}")
