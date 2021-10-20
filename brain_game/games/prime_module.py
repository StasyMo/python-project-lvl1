from random import randint


rules_of_the_game = 'Answer "yes" if given number is prime. ' \
                    'Otherwise answer "no".'


def task_of_the_game(user_name: str):
    UP_RANGE = 1000
    question_number = randint(1, UP_RANGE)
    print('Question: {}'.format(question_number), '\nYour answer: ', end='')
    user_answer = input()
    prime_answer = 1
    step_prime = 1
    while step_prime <= question_number / 2:
        if question_number % step_prime == 0:
            prime_answer = step_prime
        step_prime += 1
    if prime_answer == 1:
        return user_answer, 'yes'
    return user_answer, 'no'
