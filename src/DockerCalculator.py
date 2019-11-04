import math


def addition(a, b):
    return int(a) + int(b)


def subtraction(a, b):
    if a < b:
        return b - a
    elif a > b:
        return a - b
    else:
        return 0


def multiplication(a, b):
    return a * b


def division(a, b):
    if a == 0 or b == 0:
        print("Either a or b is zero.")
        return 0
    else:
        return b / a


def power(a):
    return a * a


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
