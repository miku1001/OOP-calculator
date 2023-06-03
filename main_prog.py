# import class UserInterface
from inherit_ui import InheritUserInt
# import class MathematiclOperator
from calculator import MathematicalOperator
from calcbyted import CalculatorTed

# Assign variable for class
ui = InheritUserInt()
calc = MathematicalOperator()
cted = CalculatorTed()

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
        ui.print_ans(sum)
    elif mode == "2":
        diff = calc.minus(num1, num2)
        ui.print_ans(diff)        
    elif mode == "3":
        product = calc.multiply(num1, num2)
        ui.print_ans(product)
    elif mode == "4":
        quotient = calc.divide(num1, num2)
        ui.print_ans(quotient)
    elif mode == "5":
        exp = cted.exponent(num1, num2)
        ui.print_ans(exp)
    elif mode == "6":
        root = cted.roots(num1, num2)
        ui.print_ans(root)
    elif mode == "7":
        rem = cted.remainder(num1, num2)
        ui.print_ans(rem)
    else:
        print("\033[31mInvalid choice!\033[0m \n")
        continue
    
    if not ui.again():
        break