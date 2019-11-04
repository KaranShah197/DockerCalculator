import math


def addition(a, b):
    return int(a) + int(b)


def subtraction(a, b):
    return int(b) - int(a)


def multiplication(a, b):
    return int(a) * int(b)


def division(a, b):
    a = float(a)
    b = float(b)
    if a == 0 or b == 0:
        print("Either a or b is zero.")
        return 0
    else:
        return round(b / a, 9)


def power(a):
    return int(a) * int(a)


def root(a):
    return math.sqrt(a)


class DockerCalculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = power(a)
        return self.result

    def squareRoot(self, a):
        self.result = root(a)
        return self.result
