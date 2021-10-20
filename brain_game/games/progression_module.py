from random import randint


rules_of_the_game = 'What number is missing in the progression?'


def task_of_the_game():
    PROGRESSION_LENGTH = 10
    UP_RANGE = 10
    progression = [0] * PROGRESSION_LENGTH
    progression[0] = randint(0, UP_RANGE)
    progression_step = randint(1, UP_RANGE)
    missed_elem = randint(0, UP_RANGE - 1)
    i = 1
    print('Question: ', end='')
    while i < 10:
        progression[i] = progression[i - 1] + progression_step
        i += 1
    for i in range(PROGRESSION_LENGTH):
        if i == missed_elem:
            print('.. ', end='')
        else:
            print(progression[i], end=' ')
    print('Your answer: ', end='')
    user_answer = input()
    try:
        user_answer = int(user_answer)
    except ValueError:
        return print('The answer might be a number')
    correct_answer = progression[missed_elem]
    return user_answer, correct_answer
