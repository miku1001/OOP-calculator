# import pyfiglet
import pyfiglet

# Create class
class UserInterface:
    # Display Operations
    def operation(self):
        print(pyfiglet.figlet_format("Simple Mini Calculator".center(50), font = "digital"))
        print("To choose your desire operation: ")
        print("\033[31mPress 1 \033[0m: Addition", " " * 35, "\033[32mPress 2 \033[0m: Subtraction \n"
        "\033[33mPress 3 \033[0m: Multiplication ", " " * 28, "\033[34mPress 4 \033[0m: Division \n"
        "\033[35mPress 5 \033[0m: Exponent", " " * 35, "\033[36mPress 6 \033[0m: Roots \n"
        "\033[30mPress 7 \033[0m: Remainder")
        print ("=" * 90)
        print("\033[31mNOTE \033[0m: When choosing exponent: First Number = Base, Second Number = Exponent \n"
              "\033[31mNOTE \033[0m: When choosing exponent: First Number = Base, Second Number = Root")
        print ("-" * 90)

    # Create method to input number
    def input_number(self, number_type):
        while True:
            try:
                num = float(input("Input {} number: ".format(number_type)))
                return num
            except ValueError:
                print()
                print("\033[31mERROR!, you entered invalid character!\033[0m \n")
                continue
    
    # Create method to print number
    def print_ans(self, answer):
        print()
        print("The answer is \033[42m" + str(answer) + "\033[0m")
        print()

    # Create method for operation choice
    def mode(self):
        mode = input("Enter Operation: ")
        return mode

    # Create method to ask user to continue or stop the program
    def again(self):
        while True:
            retry = input("Do you want to continue? "
                          "Type \033[32mY\033[0m if yes or \033[31mN\033[0m if no: ")
            print()
            if retry.lower() == 'n':
                # Stop the program
                print("Closing Program... Thank you for using! \U0001F64B")
                return False
            # If y
            elif retry.lower() == 'y':
                # Back to the first part
                return True
                print()
            # If invalid character
            else:
                print()
                print("\033[31mInvalid character!\033[0m")
                print()
                continue