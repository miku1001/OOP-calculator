#import MathematicOperator class
from calculator import MathematicalOperator


class CalculatorTed(MathematicalOperator):
    
    # Exponent
    def exponent(self, num1, num2):
        print()
        print("=" * 90)
        print("You choose, \033[35mEXPONENT\033[0m!".center(90))
        exp = num1 ** num2
        return exp

    # Roots
    def roots(self, num1, num2):
        print()
        print("=" * 90)
        print("You choose, \033[36mEXPONENT\033[0m!".center(90))
        root = num1 ** (1/num2)
        return root
    
    # Remainder
    def remainder(self,num1, num2):
        print()
        print("=" * 90)
        print("You choose, \033[36mREMAINDER\033[0m!".center(90))
        rem = num1 %  num2
        return rem
