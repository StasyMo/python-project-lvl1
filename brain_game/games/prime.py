from random import randint


rules = 'Answer "yes" if given number is prime. ' \
        'Otherwise answer "no".'


def task():
    UP_RANGE = 1000
    question_number = randint(1, UP_RANGE)
    print('Question: {}'.format(question_number))
    correct_answer = if_prime(question_number)
    return correct_answer


def if_prime(question_number: int):
    step_prime = 1
    prime_answer = 1
    while step_prime <= question_number / 2:
        if question_number % step_prime == 0:
            prime_answer = step_prime
        step_prime += 1
    if prime_answer == 1:
        return 'yes'
    return 'no'
