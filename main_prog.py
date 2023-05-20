# import pyfiglet
import pyfiglet

# Display operation Menu
print(pyfiglet.figlet_format("Simple Mini Calculator".center(50), font = "digital"))
print("To choose your desire operation: ")
print("\033[31mPress 1 \033[0m: Addition", " " * 35, "\033[32mPress 2 \033[0m: Subtraction \n"
      "\033[33mPress 3 \033[0m: Multiplication ", " " * 28, "\033[34mPress 4 \033[0m: Division")
print ("=" * 90)