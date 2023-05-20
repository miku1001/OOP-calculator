from ui import UserInteract
ui = UserInteract()
# Create class
class LogicalOperator:
    # Method for addition
    def add(self, num1, num2):
        # add num1, num2
        sum = num1 + num2
        return sum
    
    # Method for subtraction
    def minus(self, num1, num2):
        # subtract num1, num2
        diff = num1 - num2
        return diff
    
    # Method for multiplication
    def multiply(self, num1, num2):
        # multiply num1, num2
        product = num1 * num2
        return product
    
    # Method for division
    def divide(self, num1, num2):
        while True:
            try:
                # divide num1, num2
                quotient = num1 / num2
                return quotient
            except ZeroDivisionError:
                print()
                print("\033[31mERROR! Divided by zero\033[0m \n")
                num1 = ui.input_number()
                num2 = ui.input_number()
                
