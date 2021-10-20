from random import randint

rules_of_the_game = 'Find the greatest common divisor of given numbers.'


def task_of_the_game():
    UP_RANGE = 100
    gcd_number1 = randint(1, UP_RANGE)
    gcd_number2 = randint(1, UP_RANGE)
    print('Question: {0} {1} '.format(gcd_number1, gcd_number2),
          '\nYour answer: ', end='')
    user_answer = input()
    try:
        user_answer = int(user_answer)
    except ValueError:
        print("The answer might be a number")
    if gcd_number1 < gcd_number2:
        minimal_number_gcd = gcd_number1
    else:
        minimal_number_gcd = gcd_number2
    for number in range(1, minimal_number_gcd + 1):
        if gcd_number1 % number == 0 and gcd_number2 % number == 0:
            gcd = number
    return user_answer, gcd
