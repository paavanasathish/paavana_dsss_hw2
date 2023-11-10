import unittest
from math_quiz import generate_random_integer, generate_random_math_operation, generate_math_problem_and_solution

"""This code has the test cases for all the functions functions. 
It checks whether the generated random integers fall between min val and max val, and 
the operation generated math operations are one of the expected operations and 
whether the generated math problems and solutions match the expected values..."""

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # generating 1000 random numbers and checking if each falls within the specified range.
        min = 1
        max = 10
        for _ in range(1000):  
            rand_num = generate_random_integer(min, max)
            self.assertTrue(min <= rand_num <= max)

    def test_generate_random_math_operation(self):
       # generating 1000 random operations and checking if each is one of the expected operations.
       for _ in range(100):  
        operation = generate_random_math_operation()
        self.assertIn(operation, ['+', '-', '*'])

    def test_generate_math_problem_and_solution(self):
        #  It defines a list of test cases, where each case includes input values (num1, num2, operator, expected_problem, expected_answer) 
        #  The loop then iterates through these test cases, calls the function with the input values, and checks if the output matches the expected values.
            test_cases = [
                            (5, 2, '+', '5 + 2', 7),
                            (5, 2, '+', '5 + 2', 7),
                            (8, 3, '-', '8 - 3', 5),
                            (4, 6, '*', '4 * 6', 24),
                            (10, 2, '+', '10 + 2', 12),
                            (7, 4, '-', '7 - 4', 3),
                            (3, 5, '*', '3 * 5', 15),
                            (1, 1, '+', '1 + 1', 2),
                            (0, 9, '-', '0 - 9', -9),
                            (6, 3, '*', '6 * 3', 18)
                          ]

            for number1, number2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_math_problem_and_solution(number1, number2, operator)
                #Calls the function to get the generated problem and answer.
                self.assertEqual(problem, expected_problem)
                #Checks if the generated problem matches the expected problem.
                self.assertEqual(answer, expected_answer)
                #Checks if the generated answer matches the expected answer.

if __name__ == "__main__":
    unittest.main()
