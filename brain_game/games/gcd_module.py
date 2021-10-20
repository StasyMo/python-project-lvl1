from random import randint

rules_of_the_game = 'Find the greatest common divisor of given numbers.'


def task_of_the_game(user_name: str):
    UP_RANGE = 100
    gcd_number1 = randint(1, UP_RANGE)
    gcd_number2 = randint(1, UP_RANGE)
    print('Question: {0} {1} '.format(gcd_number1, gcd_number2),
          'Your answer: ', end='')
    user_answer = input()
    try:
        user_answer = int(user_answer)
    except ValueError:
        return print("The answer might be a number, but '{0}' "
                     "is not a number ;(. \n Let's try again, "
                     "{1}!".format(user_answer, user_name))
    if gcd_number1 < gcd_number2:
        minimal_number_gcd = gcd_number1
    else:
        minimal_number_gcd = gcd_number2
    for number in range(1, minimal_number_gcd + 1):
        if gcd_number1 % number == 0 and gcd_number2 % number == 0:
            gcd = number
    return user_answer, gcd
