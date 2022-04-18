import unittest
import task


class TestAdder(unittest.TestCase):

    def test_numbers(self):
        self.assertEqual(task.solveSquare(1, 2, 1), (-1, -1))

    def test_numbers2(self):
        self.assertEqual(task.solveSquare(10, 2, 1), None)

    def test_numbers3(self):
        self.assertEqual(task.solveSquare(1, 10, 1), (-9.898979485566356, -0.10102051443364424))

"""
    def test_exception(self):
        with assertRaises(TypeError):
            adder.adder(123)"""