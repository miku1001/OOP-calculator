# Create class
class UserInterface:
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
        print("The answer is: ", answer)

    # Create method for operation choice
    def mode(self):
        mode = int(input("Enter Operation: "))
        return mode

    # Create method to ask user to continue or stop the program
    def again(self):
        while True:
            retry = input("Do you want to continue? \n"
                          "Type \033[32mY\033[0m if yes or \033[31mN\033[0m if no: ")
            if retry.lower() == 'n':
                # Stop the program
                print("Closing Program... Thank you! \U0001F64B")
                return False
            # If y
            elif retry.lower() == 'y':
                # Back to the first part
                return True
            # If invalid character
            else:
                print()
                print("\033[31mInvalid character!\033[0m \n")
                continue