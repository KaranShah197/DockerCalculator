def addition(a, b):
    return a + b


def subtraction(a, b):
    if a < b:
        return b - a
    elif a > b:
        return a - b
    else:
        return 0


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
