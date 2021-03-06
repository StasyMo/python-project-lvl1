from random import choice, randint


rules = 'What is the result of the expression?'
UP_RANGE = 100


def get_question_and_answer():
    """Do the game and returns on screen the result of game of user."""
    calc_number1 = randint(1, UP_RANGE)
    calc_number2 = randint(1, UP_RANGE)
    math_operator = choice(['+', '-', '*'])
    question = f"{calc_number1} {math_operator} {calc_number2}"
    if math_operator == '+':
        correct_answer = calc_number1 + calc_number2
    elif math_operator == '-':
        correct_answer = calc_number1 - calc_number2
    else:
        correct_answer = calc_number1 * calc_number2
    return question, str(correct_answer)
