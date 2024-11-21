from math import *
class BasicMath:
    def __init__(self, *nums):
        self.numbers = nums

    def addition(self):
        total = sum(self.numbers)
        print(f"Sum is {total}")
    def subtraction(self):
        total = self.numbers[0] - sum(self.numbers[1:])
        print(f"Difference is {total}")
    
    def multiplication(self):
        total = prod(self.numbers)
        print(f"Product is {total}")
    
    def division(self):
        try:
            if len(self.numbers) < 2:
                print("Please provide at least two numbers for division.")
                return

            # Start with the first number
            quotient = self.numbers[0]
            
            # Divide by each subsequent number
            for num in self.numbers[1:]:
                if num == 0:
                    print("Error: Division by zero is not allowed.")
                    return
                quotient, remainder = divmod(quotient, num)

            print(f"Quotient is {quotient}, Remainder is {remainder}")
        except ZeroDivisionError:
            print("Number cannot be divided by zero")

class Mid_Level_Math(BasicMath):
    def square(self):
        # For squaring a single number.
        if len(self.numbers) == 1:
            self.squaring = self.numbers[0] **2
            print(f"Square of {self.numbers} is {self.squaring}")
        else:
            print("Square operation requires exactly one number.")
    def cube(self):
        if len(self.numbers) == 1:
            self.cubing = self.numbers[0] **3
            print(f"Cubic value of {self.numbers} is {self.cubing}")
        else:
            print("Cubic operation requires exactly one number.")
