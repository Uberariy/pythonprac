def solveSquare(a, b, c):
    D = b**2 - 4*a*c 
    if (D >= 0):
        return ((-b - D**0.5)/2, (-b + D**0.5)/2)
    else:
        return None

