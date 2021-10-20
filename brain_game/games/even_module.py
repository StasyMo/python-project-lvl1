from random import randint


rules_of_the_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def task_of_the_game():
    number_up_range = 1000000
    question_number = randint(1, number_up_range)
    print('Question: {}'.format(question_number), '\nYour answer: ', end='')
    user_answer = input()
    if question_number % 2:
        return user_answer, 'no'
    return user_answer, 'yes'
