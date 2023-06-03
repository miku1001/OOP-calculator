# Import UserInteract for ZeroDivision error
from inherit_ui import InheritUserInt
ui = InheritUserInt()

# Create class
class MathematicalOperator:
    # Method for addition
    def add(self, num1, num2):
        print()
        print("=" * 90)
        print("You choose, \033[31mADDITION\033[0m!".center(90))
        # add num1, num2
        sum = num1 + num2
        return sum
    
    # Method for subtraction
    def minus(self, num1, num2):
        print()
        print("=" * 90)
        print("You choose, \033[32mSUBTRACTION\033[0m!".center(90))
        # subtract num1, num2
        diff = num1 - num2
        return diff
    
    # Method for multiplication
    def multiply(self, num1, num2):
        print()
        print("=" * 90)
        print("You choose, \033[33mMULTIPLICATION\033[0m!".center(90))
        # multiply num1, num2
        product = num1 * num2
        return product
    
    # Method for division
    def divide(self, num1, num2):
        print()
        print("=" * 90)
        print("You choose, \033[34mDIVISION\033[0m!".center(90))
        while True:
            try:
                # divide num1, num2
                quotient = num1 / num2
                return quotient
            except ZeroDivisionError:
                print()
                print("\033[31mERROR! Divided by zero.\033[0m \n")
                num1 = ui.input_number("first")
                num2 = ui.input_number("second")