from random import randint


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def play():
    number_up_range = 1000000
    question = randint(1, number_up_range)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_even(question):
    if question % 2:
        return False
    else:
        return True
