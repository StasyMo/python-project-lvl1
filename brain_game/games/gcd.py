from random import randint

rules = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    up_range = 100
    gcd_number1 = randint(1, up_range)
    gcd_number2 = randint(1, up_range)
    question = str(gcd_number1) + ' ' + str(gcd_number2)
    gcd = calculate_gcd(gcd_number1, gcd_number2)
    return question, str(gcd)


def calculate_gcd(gcd_number1: int, gcd_number2: int):
    if gcd_number1 < gcd_number2:
        minimal_number_gcd = gcd_number1
    else:
        minimal_number_gcd = gcd_number2
    gcd = 1
    for number in range(1, minimal_number_gcd + 1):
        if gcd_number1 % number == 0 and gcd_number2 % number == 0:
            gcd = number
    return gcd
