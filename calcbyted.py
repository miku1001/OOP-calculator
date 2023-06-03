
from calculator import MathematicalOperator

class CalculatorTed(MathematicalOperator):
    #Exponent
    def exponent(self, num1, num2):
        exp = num1 ** num2
        return exp

