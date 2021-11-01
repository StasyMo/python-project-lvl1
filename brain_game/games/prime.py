from random import randint


rules = 'Answer "yes" if given number is prime. ' \
        'Otherwise answer "no".'
UP_RANGE = 1000


def get_question_and_answer():
    question = randint(1, UP_RANGE)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer


def is_prime(number: int):
    step_prime = 2
    while step_prime <= number / 2:
        if number % step_prime == 0:
            return False
        step_prime += 1
    return True
