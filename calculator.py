import math

class Calculator:
    def __init__(self):
        self.memory = 0.0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a % b

    def sin(self, a):
        return math.sin(math.radians(a))

    def cos(self, a):
        return math.cos(math.radians(a))

    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Нельзя взять корень из отрицательного числа")
        return math.sqrt(a)

    def floor(self, a):
        return math.floor(a)

    def ceil(self, a):
        return math.ceil(a)

    # Работа с памятью
    def memory_clear(self):
        self.memory = 0.0

    def memory_add(self, value):
        self.memory += value

    def memory_subtract(self, value):
        self.memory -= value

    def memory_recall(self):
        return self.memory
