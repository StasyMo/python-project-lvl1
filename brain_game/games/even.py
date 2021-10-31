from random import randint


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    number_up_range = 1000000
    question = randint(1, number_up_range)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer


def is_even(number):
    if number % 2:
        return False
    else:
        return True
