"""
This is a Python script for a simple mathematics quiz game. The code generates random mathematics problems.
Asks the user to solve them, and then provides feedback on whether the answers are correct.
"""
import random
from .math_quiz import math_quiz


"""
We import 'random' module to introduce randomness in which it provides functions that generate random numbers, used in instance where unpredictability is desired.
"""
def generate_random_integer(min, max):
    """
    This function generates a random integer number using the function random.randint
    input: min: int,max: int            return-> int   (Return random integer in range [a, b], including both end points.)
    """
    return random.randint(min, max)

def generate_random_math_operation():
    """
    This function generates a random mathematical operation using random.randchoice.
    Returns:  _type_: _Choose a random element from a non-empty sequence._
    """
    return random.choice(['+', '-', '*'])

def generate_math_problem_and_solution(number1, number2, operation):
    """
    This function generates a random math problem and its solution. 
    input: number1, number2, operation
    return-> math_problem: A function which defines the random problem           
    solution: The correct answer to the defined math_problem.
    """
    math_problem = f"{number1} {operation} {number2}"
    if operation == '+':
        solution = number1 + number2
    elif operation == '-':
        solution = number1 - number2
    else: solution = number1 * number2
    return math_problem, solution 

def math_quiz():
    """
    This function is to run the Maths quiz game. It sets the score as 0 and the total number of questions as 3.
    The loop iterates through a (total questions) times. In each iteration, a new math problem is generated using 
    generate_random_integer, generate_random_math_operation and generate_math_problem_and_solution.
    The problem is presented to the user, and the user provides an answer via the input function.
    The user's answer is converted to an integer using int(useranswer)and then compared to the correct answer (ANSWER).
    If the user's answer is correct (useranswer == ANSWER), the program prints "Correct! You earned a point." and increments the score (s) by 1.
    If the user's answer is wrong, the correct answer is displayed, and the score remains unchanged.
    After the loop completes, the final score is displayed.
    """
    score = 0
    total_questions = 3
    #score and total_questions variable is initialized.

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    for _ in range(total_questions):
        #for _ in range(total_questions): indicates that the loop will run total_questions times. 
        #The loop generates a new math problem in each iteration, asks the user for input, checks the correctness of the answer, and updates the score.

        number1 = generate_random_integer(1, 10); number2 = generate_random_integer(1, 5); operation = generate_random_math_operation()

        PROBLEM, ANSWER = generate_math_problem_and_solution(number1, number2, operation)
        print(f"\nQuestion: {PROBLEM}")

        # Get user input with error handling to show error if the input is something like a string which cannot be converted to integer value. 
        while True:
            user_answer = input("Your answer: ")
            try:
                user_answer = int(user_answer)
                break  # Break the loop if conversion to int is successful
            except ValueError:
                print("Invalid input. Please enter an integer and try again.")

        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
