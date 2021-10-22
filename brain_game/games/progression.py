from random import randint


rules = 'What number is missing in the progression?'


def task():
    PROGRESSION_LENGTH = 10
    UP_RANGE = 10
    progression = product_progression(PROGRESSION_LENGTH, UP_RANGE)
    missed_elem = derivation(progression)
    return str(progression[missed_elem])


def product_progression(PROGRESSION_LENGTH: int, UP_RANGE: int):
    progression = [0] * PROGRESSION_LENGTH
    progression[0] = randint(0, UP_RANGE)
    progression_divide = randint(1, UP_RANGE)
    i = 1
    print('Question: ', end='')
    while i < 10:
        progression[i] = progression[i - 1] + progression_divide
        i += 1
    return progression


def derivation(progression: list):
    missed_elem = randint(0, len(progression) - 1)
    for i in range(len(progression)):
        if i == missed_elem:
            print('.. ', end='')
        else:
            print(progression[i], end=' ')
    print('')
    return missed_elem
