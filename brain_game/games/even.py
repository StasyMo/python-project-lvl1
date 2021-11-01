from random import randint


rules = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_UP_RANGE = 1000


def get_question_and_answer():
    question = randint(1, NUMBER_UP_RANGE)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer


def is_even(number):
    if number % 2:
        return False
    else:
        return True
