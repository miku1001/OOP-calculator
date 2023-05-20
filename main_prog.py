# import pyfiglet
import pyfiglet
# import class UserInteract
from ui import UserInteract
# import class LogicalOperator
from calculator import LogicalOperator

# Display operation Menu
print(pyfiglet.figlet_format("Simple Mini Calculator".center(50), font = "digital"))
print("To choose your desire operation: ")
print("\033[31mPress 1 \033[0m: Addition", " " * 35, "\033[32mPress 2 \033[0m: Subtraction \n"
      "\033[33mPress 3 \033[0m: Multiplication ", " " * 28, "\033[34mPress 4 \033[0m: Division")
print ("=" * 90)

# Assign variable for class
ui = UserInteract()
calc = LogicalOperator()

# Start Program
while True:
    # Get the first and second numbers
    num1 = ui.input_number()
    num2 = ui.input_number()

    # Choose Operation
    mode = ui.mode()
    if mode == 1:
        sum = calc.add(num1, num2)
        ui.print_ans(sum)
    if mode == 2:
        diff = calc.minus(num1, num2)
        ui.print_ans(diff)        
    if mode == 3:
        product = calc.multiply(num1, num2)
        ui.print_ans(product)
    if mode == 4:
        quotient = calc.divide(num1, num2)
        ui.print_ans(quotient)