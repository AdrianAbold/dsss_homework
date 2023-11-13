import unittest
from math_quiz import random_number, random_operation, calculation


class TestMathGame(unittest.TestCase):

    def test_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation(self):
        x = 5
        y = 3
        rand_op = random_operation()
        if rand_op == '+': result = x + y
            self.assertEqual(result, 8)
        elif rand_op == '-': result = x - y
            self.assertEqual(result, 2)
        else: result = x * y
            self.assertEqual(result, 15)
        pass

    def test_calculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10)
            ]
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculation(num1, num2, operator)
                self.assertEqual(answer, expected_answer)
                pass
if __name__ == "__main__":
    unittest.main()
