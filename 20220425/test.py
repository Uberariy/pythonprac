import unittest
import task


class TestTask(unittest.TestCase):

    def test_01_a_eq_zero(self):
        self.assertEqual(task.solve(0, 10), None)

    def test_02_default(self):
        self.assertEqual(task.solve(2, 10), -5.0)