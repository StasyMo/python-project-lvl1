from random import randint

rules = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    up_range = 100
    number1 = randint(1, up_range)
    number2 = randint(1, up_range)
    question = str(number1) + ' ' + str(number2)
    gcd = calculate_gcd(number1, number2)
    return question, str(gcd)


def calculate_gcd(number1: int, number2: int):
    if number1 < number2:
        minimal_number_gcd = number1
    else:
        minimal_number_gcd = number2
    gcd = 1
    for number in range(1, minimal_number_gcd + 1):
        if number1 % number == 0 and number2 % number == 0:
            gcd = number
    return gcd
