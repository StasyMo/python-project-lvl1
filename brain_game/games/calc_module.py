from random import choice, randint


rules_of_the_game = 'What is the result of the expression?'


def task_of_the_game(user_name: str):
    """Do the game and returns on screen the result of game of user."""
    UP_RANGE = 100
    calc_number1 = randint(1, UP_RANGE)
    calc_number2 = randint(1, UP_RANGE)
    math_operator = choice(['+', '-', '*'])
    print('Question: {0} {1} {2}'.format(calc_number1,
                                         math_operator, calc_number2),
          '\nYour answer: ', end='')
    user_answer = input()
    try:
        user_answer = int(user_answer)
    except ValueError:
        return print("The answer might be a number, but '{0}' "
                     "is not a number ;(. \n Let's try again, "
                     "{1}!".format(user_answer, user_name))
    if math_operator == '+':
        correct_answer = calc_number1 + calc_number2
    elif math_operator == '-':
        correct_answer = calc_number1 - calc_number2
    else:
        correct_answer = calc_number1 * calc_number2
    return user_answer, correct_answer
