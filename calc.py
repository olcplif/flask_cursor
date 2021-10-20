class Calc:
    def __init__(self, num_1, num_2, act):
        self.num_1 = int(num_1)
        self.num_2 = int(num_2)
        self.act = act

    def div(self):
        try:
            result = self.num_1 / self.num_2
        except ZeroDivisionError:
            return "Error: division by zero!"
        return result

    def sum(self):
        return self.num_1 + self.num_2

    def dif(self):
        return self.num_1 - self.num_2

    def mult(self):
        return self.num_1 * self.num_2

    def show_calc(self):
        if self.act == "sum":
            result = f"{self.num_1} + {self.num_2} = {self.sum()}"
        elif self.act == "div":
            result = f"{self.num_1} / {self.num_2} = {self.div()}"
        elif self.act == "dif":
            result = f"{self.num_1} - {self.num_2} = {self.dif()}"
        elif self.act == "mult":
            result = f"{self.num_1} * {self.num_2} = {self.mult()}"
        else:
            result = "Error: unknown example!"
        return result
