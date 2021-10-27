from random import randint


rules = 'Answer "yes" if given number is prime. ' \
        'Otherwise answer "no".'


def play():
    UP_RANGE = 1000
    question = randint(1, UP_RANGE)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_prime(question_number: int):
    step_prime = 1
    prime_answer = 1
    while step_prime <= question_number / 2:
        if question_number % step_prime == 0:
            prime_answer = step_prime
        step_prime += 1
    if prime_answer == 1:
        return True
    return False
