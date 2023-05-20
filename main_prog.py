# import class UserInterface
from ui import UserInterface
# import class LogicalOperator
from calculator import LogicalOperator

# Assign variable for class
ui = UserInterface()
calc = LogicalOperator()

# Display operation Menu
ui.operation()

# Start Program
while True:
    # Get the first and second numbers
    num1 = ui.input_number("first")
    num2 = ui.input_number("second")

    # Choose Operation
    mode = ui.mode()
    if mode == "1":
        sum = calc.add(num1, num2)
        print()
        ui.print_ans(sum)
    elif mode == "2":
        diff = calc.minus(num1, num2)
        print()
        ui.print_ans(diff)        
    elif mode == "3":
        product = calc.multiply(num1, num2)
        print()
        ui.print_ans(product)
    elif mode == "4":
        quotient = calc.divide(num1, num2)
        print()
        ui.print_ans(quotient)
    else:
        print()
        print("\033[31mInvalid choice!\033[0m \n")
        continue
    
    if not ui.again():
        break