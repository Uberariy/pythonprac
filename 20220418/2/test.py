from unittest.mock import MagicMock
import unittest
import task

def run_test(params, result):
    task.SquareIO.inputCoeff = MagicMock(side_effect=params)
    task.SquareIO.printResult = MagicMock()
    task.solveSquare()
    res = task.SquareIO.printResult.call_args.args[0]
    print(result, res)
    if res in ["No real solution!", "No solution!"]:
        assert (result in ["No real solution!", "No solution!"])
    elif res in ["Any number is solution."]:
        pass
    elif type(result) is tuple and len(result) > 1:
        assert tuple(float(i) for i in result) == res
    else:
        assert float(result) == res

class TestSquare(unittest.TestCase):

    def test_01_square(self):
        run_test((1, 2, 1), (-1, -1))

    def test_02_square(self):
        run_test((1, 10, 1), (-9.898979485566356, -0.10102051443364424))

    def test_03_no_solution(self):
        run_test((10, 2, 1), "No real solution!")

    def test_04_a_eq_zero(self):
        run_test((0, 2, -10), 5)

    def test_05_ab_eq_zero(self):
        run_test((0, 0, -10), "No solution!")
    
    def test_06_abc_eq_zero(self):
        run_test((0, 0, 0), 22123214)