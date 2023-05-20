# Create class
class UserInteract:
    # Create method to input number
    def input_number(self):
        num = float(input("Input a number: "))
        return num
    
    # Create method to print number
    def print_ans(self, answer):
        print("The answer is: ", answer)

    # Create method for operation choice
    def mode(self):
        mode = int(input("Enter Operation: "))
        return mode


    # Create method to ask user to continue or stop the program