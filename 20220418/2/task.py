class SquareIO:

    def __init__(self):
        pass

    def inputCoeff(self, name):
        print(f"Input {name}:")
        return float(input())

    def printResult(self, result):
        print(f"Solution: {result}")

def solveSquare():
    sq = SquareIO()
    a = sq.inputCoeff("a")
    b = sq.inputCoeff("b")
    c = sq.inputCoeff("c")
    if a == 0:
        if b == 0:
            if c == 0:
                sq.printResult("Any number is solution.")
            else:
                sq.printResult("No solution!")
        else:
            sq.printResult(-c / b)
    else:
        D = b**2 - 4*a*c 
        if (D >= 0):
            sq.printResult(((-b - D**0.5)/2, (-b + D**0.5)/2))
        else:
            sq.printResult("No real solution!")

if __name__ == '__main__':
    solveSquare()