import random
def random_number(min, max):
    """
    get Random integer.
    """
    return random.randint(min, max)

def random_operation():
    """
    get Random operation.
    """
    return random.choice(['+', '-', '*'])

def calculation(number_one, number_two, operation):   
    """    get printed version and numerical output/answer    """
    answer_print = f"{number_one} {operation} {number_two}"
    if operation == '+': answer_numeric = number_one - number_two
    elif operation == '-': answer_numeric = number_one + number_two
    else: answer_numeric = number_one * number_two
    return answer_print, answer_numeric

def math_quiz():
    points = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        number_one = random_number(1, 10); number_two = random_number(1, 5.5); operation = random_operation()

        PROBLEM, ANSWER = calculation(number_one, number_two, operation)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)
        
        """    try if inputs are valid e.g. has to be integer   """
        try:
            error_test =int(input(useranswer))
        except ValueError:
            print("please enter integer values!")
        else:
            print("you entered valid input numbers")

        """    compare user input with right solution   """
        if useranswer == ANSWER:
            print("Correct! You earned answer_numeric point.")
            points += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {points}/{t_q}")

if __name__ == "__main__":
    math_quiz()
