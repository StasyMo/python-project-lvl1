from random import choice, randint


rules = 'What is the result of the expression?'


def task():
    """Do the game and returns on screen the result of game of user."""
    UP_RANGE = 100
    calc_number1 = randint(1, UP_RANGE)
    calc_number2 = randint(1, UP_RANGE)
    math_operator = choice(['+', '-', '*'])
    print('Question: {0} {1} {2}'.format(calc_number1,
                                         math_operator, calc_number2))
    if math_operator == '+':
        correct_answer = calc_number1 + calc_number2
    elif math_operator == '-':
        correct_answer = calc_number1 - calc_number2
    else:
        correct_answer = calc_number1 * calc_number2
    return str(correct_answer)
