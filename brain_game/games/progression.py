from random import randint


rules = 'What number is missing in the progression?'


def play():
    PROGRESSION_LENGTH = 10
    UP_RANGE = 10
    progression = product_progression(PROGRESSION_LENGTH, UP_RANGE)
    missed_elem = randint(0, PROGRESSION_LENGTH - 1)
    question = derivate(progression, missed_elem)
    return question, str(progression[missed_elem])


def product_progression(PROGRESSION_LENGTH: int, UP_RANGE: int):
    progression = [0] * PROGRESSION_LENGTH
    progression[0] = randint(0, UP_RANGE)
    common_difference = randint(1, UP_RANGE)
    number_of_member = 1
    while number_of_member < PROGRESSION_LENGTH:
        progression[number_of_member] = progression[number_of_member - 1] \
                                        + common_difference
        number_of_member += 1
    return progression


def derivate(progression: list, missed_elem: int):
    question = ''
    for i in range(len(progression)):
        if i == missed_elem:
            question += '..'
        else:
            question += str(progression[i])
        if i < len(progression) - 1:
            question += ' '
    return question
