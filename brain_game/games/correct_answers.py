"""Take numbers and returns the correct result."""


def calc_correct_answer(calc_number1: int, calc_number2: int,
                        math_operator: str):
    """Calculate the correct answer for brain-calc. Returns correct answer."""
    if math_operator == '+':
        return calc_number1 + calc_number2
    elif math_operator == '-':
        return calc_number1 - calc_number2
    return calc_number1 * calc_number2


def even_correct_answer(question_number: int):
    """Calculate the correct answer for brain-even. Returns correct answer."""
    if question_number % 2:
        return 'no'
    return 'yes'


def gcd_correct_answer(gcd_number1: int, gcd_number2: int):
    """Calculate the correct answer for brain-gcd. Returns correct answer."""
    if gcd_number1 < gcd_number2:
        minimal_number_gcd = gcd_number1
    else:
        minimal_number_gcd = gcd_number2
    for number in range(1, minimal_number_gcd + 1):
        if gcd_number1 % number == 0 and gcd_number2 % number == 0:
            gcd = number
    return gcd


def progression_correct_answer(progression: list,
                               progression_step: int, missed_elem: int, i: int,
                               PROGRESSION_LENGTH: int):
    while i < 10:
        progression[i] = progression[i - 1] + progression_step
        i += 1
    for i in range(PROGRESSION_LENGTH):
        if i == missed_elem:
            print('.. ', end='')
        else:
            print(progression[i], end=' ')
    return progression[missed_elem]


def prime_correct_answer(question_number: int):
    """Calculate the correct answer for brain-prime. Returns correct answer."""
    prime_answer = 1
    step_prime = 1
    while step_prime <= question_number / 2:
        if question_number % step_prime == 0:
            prime_answer = step_prime
        step_prime += 1
    if prime_answer == 1:
        return 'yes'
    return 'no'
