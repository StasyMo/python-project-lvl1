from random import randint


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def task():
    number_up_range = 1000000
    question_number = randint(1, number_up_range)
    print('Question: {}'.format(question_number))
    correct_answer = if_even(question_number)
    return correct_answer


def if_even(question_number):
    if question_number % 2:
        return 'no'
    else:
        return 'yes'
