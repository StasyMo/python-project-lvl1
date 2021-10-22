from random import randint

rules = 'Find the greatest common divisor of given numbers.'


def task():
    UP_RANGE = 100
    gcd_number1 = randint(1, UP_RANGE)
    gcd_number2 = randint(1, UP_RANGE)
    print('Question: {0} {1} '.format(gcd_number1, gcd_number2))
    gcd = if_prime(gcd_number1, gcd_number2)
    return str(gcd)


def if_prime(gcd_number1: int, gcd_number2: int):
    if gcd_number1 < gcd_number2:
        minimal_number_gcd = gcd_number1
    else:
        minimal_number_gcd = gcd_number2
    gcd = 1
    for number in range(1, minimal_number_gcd + 1):
        if gcd_number1 % number == 0 and gcd_number2 % number == 0:
            gcd = number
    return gcd
